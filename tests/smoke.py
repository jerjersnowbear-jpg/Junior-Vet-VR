"""Logic smoke tests using Chromium with in-memory storage and mock GL. Not a VR hardware test."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import os,json
ROOT=Path(__file__).resolve().parents[1]
STORE='''<script>const _store={};Object.defineProperty(window,'localStorage',{value:{getItem:k=>_store[k]??null,setItem:(k,v)=>_store[k]=String(v)}});window.confirm=()=>true;</script>'''
MOCK='''<script>const _get=HTMLCanvasElement.prototype.getContext;let counter=0;const mockGL=new Proxy({getShaderParameter:()=>true,getProgramParameter:()=>true,getAttribLocation:()=>0,getUniformLocation:()=>({}),createBuffer:()=>({}),createShader:()=>({}),createProgram:()=>({}),createTexture:()=>({})},{get(t,k){if(k in t)return t[k];if(/^[A-Z0-9_]+$/.test(k))return ++counter;return ()=>{}}});HTMLCanvasElement.prototype.getContext=function(k,...a){return k==='webgl'?mockGL:_get.call(this,k,...a)};</script>'''
with sync_playwright() as p:
    opts={'headless':True,'args':['--no-sandbox']}
    if os.environ.get('CHROMIUM_BIN'):opts['executable_path']=os.environ['CHROMIUM_BIN']
    b=p.chromium.launch(**opts);page=b.new_page(viewport={'width':1100,'height':700});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    html=(ROOT/'index.html').read_text().replace('<script>\n\'use strict\';',STORE+MOCK+"<script>\n'use strict';",1).replace("if(new URLSearchParams(location.search).has('test'))window.__vet=","window.__vet=")
    page.set_content(html);assert page.evaluate('!!window.__vet'),errors
    result=page.evaluate('''async()=>{let v=__vet;await v.start(false);for(let c of v.cases){v.enter(c.room);v.startCase(c.id);v.chooseTool(1);if(v.state.step!==0)throw Error('out of order');v.chooseTool(0);if(!v.validResume())throw Error('resume');v.showMenu();await v.start(false,true);if(v.state.step!==1)throw Error('restore');v.chooseTool(1);v.chooseTool(2);v.answer((c.correct+1)%3);if(v.state.phase!=='quiz')throw Error('wrong answer');v.answer(c.correct);if(v.state.phase!=='done')throw Error('correct answer');}return v.state.progress}''');assert len(result['completed'])==44 and len(result['visits'])==12 and 'resume' not in result,result
    result=page.evaluate("""()=>{let v=__vet;v.enter('anatomy');if(v.state.targets.filter(t=>t.startsWith('system')).length!==8)throw Error('missing systems');for(let i=0;i<v.systems.length;i++){v.anatomySelect(i);if(v.anatomyState.selected!==i||!v.state.targets.includes('anQuiz'))throw Error('select');v.anatomyQuestion();v.anatomyAnswer((v.systems[i][4]+1)%3);if(v.anatomyState.mode!=='quiz')throw Error('wrong answer');v.anatomyAnswer(v.systems[i][4]);if(!v.anatomyState.done.includes(i))throw Error('no credit');}v.enter('exam');v.startCase(0);if(v.anatomyState.motion<3)throw Error('no dynamic geometry');v.enter('anatomy');if(v.anatomyState.done.length!==8)throw Error('lost science progress');return v.state.progress}""");assert result['anatomy3d']==list(range(8)) and len(result['visits'])==13,result
    print('PASS: 8 immersive anatomy exhibits, 8 challenge flows, persistence on room reentry, dynamic patient geometry, 13 visited rooms (mock GL)')
    result=page.evaluate("""()=>{let v=__vet;v.enter('hub');for(let r of v.rooms.slice(1))if(!v.state.targets.includes(r.id))throw Error('missing hub target '+r.id);v.enter('skills');for(let i=0;i<v.skillScenarios.length;i++){v.skillSelect(i);for(let q of v.skillScenarios[i].questions){let k=v.skillState.step;v.skillAnswer((q[2]+1)%3);if(v.skillState.step!==k)throw Error('wrong choice advanced');v.skillAnswer(q[2]);}if(v.skillState.mode!=='done')throw Error('scenario not completed');}v.enter('hub');v.enter('skills');return {done:v.skillState.done,visits:v.state.progress.visits,stored:JSON.parse(localStorage.getItem('jvet.progress')).skills}}""");assert result['done']==result['stored']==list(range(4)) and len(result['visits'])==14,result
    print('PASS: all 13 reception destinations, four skills scenarios, 12 ordered decisions, wrong answers, saved skill records, 14 rooms (mock GL)')
    page.evaluate('__vet.showMenu()');page.locator('#startVR').click();assert page.locator('#confirmVR').is_disabled();page.locator('#adultCheck').check();assert page.locator('#confirmVR').is_enabled();page.locator('#stereoPreview').click();assert page.evaluate('__vet.state.vr');assert page.locator('#overlay .eye').count()==2;assert page.locator('#vrExit').is_visible();assert page.locator('#toolbar').is_hidden();assert not page.evaluate('!!document.fullscreenElement');page.locator('#vrExit').click();assert page.locator('#menu').is_visible();page.set_viewport_size({'width':700,'height':1100});page.locator('#startVR').click();page.locator('#adultCheck').check();page.locator('#stereoPreview').click();assert page.locator('#preflight').is_visible() and 'sideways' in page.locator('#motionStatus').inner_text();page.locator('#preflightBack').click();page.set_viewport_size({'width':1100,'height':700});page.evaluate('__vet.takeBreak()');assert page.locator('#breakScreen').is_visible() and page.locator('#breakReturn').is_disabled();assert not errors,errors
    print('PASS: 44 VR cases, ordered clues, wrong answers, mid-case restore, 12 visited rooms, preflight and break UI (mock GL)')
    page2=b.new_page(viewport={'width':1100,'height':850});errors=[];page2.on('pageerror',lambda e:errors.append(str(e)));a=(ROOT/'academy.html').read_text().replace('<script src="curriculum.js"></script>',STORE+'<script>'+(ROOT/'curriculum.js').read_text()+'</script>');page2.set_content(a)
    data=page2.evaluate('CURRICULUM.cases');assert len(data)==44
    page2.get_by_label('Filter by department').select_option('marine');assert page2.locator('#cases .card:visible').count()==4
    page2.get_by_label('Find a patient or topic').fill('Coral');assert page2.locator('#cases .card:visible').count()==1
    page2.get_by_label('Find a patient or topic').fill('');page2.get_by_label('Filter by department').select_option('');assert page2.locator('#cases .card:visible').count()==44
    assert page2.evaluate("clean({skills:[0,3,3,7]}).skills")==[0,3]
    print('PASS: specialty filter, patient search, skills backup sanitation')
    for c in data:
        page2.locator('#cases .card').nth(c['id']).locator('button').click()
        for tool in c['tools']:page2.get_by_role('button',name='Use '+tool,exact=True).click()
        page2.get_by_role('button',name=c['answers'][(c['correct']+1)%3],exact=True).click();assert page2.locator('#case [role=status]').inner_text().startswith('Try again')
        page2.get_by_role('button',name=c['answers'][c['correct']],exact=True).click();page2.get_by_role('button',name='Choose another patient').click()
    page2.get_by_role('button',name='Science lessons').click()
    for i,j in enumerate([0,1,2,0,1,2,0,1]*2):page2.locator('#lessons .card').nth(i).locator('button').nth(j).click()
    page2.get_by_role('button',name='Parent dashboard').click();assert 'All training completed' in page2.locator('#parent').inner_text();assert not errors,errors
    if os.environ.get('PREVIEW'):page2.get_by_role('button',name='Patient cases').click();page2.evaluate('window.scrollTo(0,0)');page2.screenshot(path=os.environ['PREVIEW'])
    print('PASS: 44 academy cases, incorrect answer feedback, 16 lessons, parent dashboard')
    page3=b.new_page(viewport={'width':1100,'height':760});errors=[];page3.on('pageerror',lambda e:errors.append(str(e)));page3.set_content((ROOT/'atlas.html').read_text().replace('<script>',STORE+'<script>',1))
    for i,j in enumerate([0,1,1,2,0,1,2,0]):
        page3.locator('#tabs button').nth(i).click();page3.locator('#parts button').last.click();page3.locator('#answers button').nth((j+1)%3).click();assert 'Try again' in page3.locator('#feedback').inner_text();page3.locator('#answers button').nth(j).click();assert 'Correct!' in page3.locator('#feedback').inner_text()
    assert '8/8' in page3.locator('#counter').inner_text();assert not errors,errors
    page3.locator('#tabs button').nth(3).click()
    if os.environ.get('ATLAS_PREVIEW'):page3.evaluate('window.scrollTo(0,0)');page3.screenshot(path=os.environ['ATLAS_PREVIEW'],full_page=True)
    print('PASS: all 8 anatomy systems, organ selection, wrong answers and completion')
    page4=b.new_page(viewport={'width':1100,'height':750});errors=[];page4.on('pageerror',lambda e:errors.append(str(e)));page4.set_content((ROOT/'device.html').read_text());assert 'webgl:' in page4.locator('#results').inner_text();page4.locator('[data-check]').first.check();assert '1/6' in page4.locator('#manual').inner_text();page4.locator('#start').click();assert page4.locator('#stereo').is_visible();page4.keyboard.press('Escape');assert page4.locator('#stereo').is_hidden();assert not errors,errors
    print('PASS: device readiness interface, stereo pattern, exit and manual checklist')
    b.close()
