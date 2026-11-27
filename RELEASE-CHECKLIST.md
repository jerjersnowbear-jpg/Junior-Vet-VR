# Junior Vet VR 6.0 | Release acceptance checklist

This is a beta for supervised family testing, not a fully validated release. Record the phone, OS, browser, viewer model and date with each result. Never continue a headset test when uncomfortable. Test as an adult before involving a child.

| Gate | Pass criterion | Status |
|---|---|---|
| Case logic | 44 cases complete; ordered clues and incorrect answers work | Passed, mock GL |
| Mid-case resume | Restore exact clue or quiz state after leaving and reopening | Partial: same-session simulated-storage restore passed; actual device restart pending |
| Academy | 44 cases, 16 lessons and parent summary complete | Passed, browser DOM / simulated storage |
| Anatomy lab | 8 body systems, selectable structures, quizzes | Passed, browser DOM / simulated storage |
| Skills arena | Four scenarios, twelve decisions, corrective feedback, completion record | Passed, mock GL; physical gaze pending |
| Specialty navigation | All thirteen reception destinations reachable in logic | Passed, mock GL; physical gaze pending |
| Academy catalog | Filter by department and search patients | Passed, browser DOM |
| Viewer readiness | Report, generic stereo pattern and manual checks | Browser interface tested; physical validation pending |
| Safety preflight | Adult confirmation required before starting VR | Passed, browser DOM |
| Rest screen | Opens on 5-minute VR session; return disabled for first 30 seconds | Partial: screen invocation and initial disabled state tested, actual elapsed session pending |
| 3D rendering | All rooms render with no clipping or missing assets | Partial: independent Mesa renders of wildlife, marine, shelter and skills arena; earlier v5 renders of examination, heart and lung exhibits; live browser and phone testing pending |
| Immersive anatomy | Eight models, correct answers, shared progress | Passed mock-GL logic and same-session progress; physical gaze and backup round-trip pending |
| Motion tracking | Slow yaw/pitch/roll in both landscape orientations; no inversion, drift or sudden movement | Pending physical phone |
| Stereo optics | Images fuse comfortably; reticle and labels align; viewer-specific lens correction validated | Pending; generic stereo only, official Cardboard SDK not integrated |
| Gaze | Select targets consistently without accidental activation; recenter and exit work | Pending physical phone |
| Performance | Sustained smooth rendering; no overheating or severe battery drain | Pending physical phone; aim for stable 60 FPS if device permits |
| HTTPS | Public or private hosted deployment reachable on phone | Pending deployment |
| Offline | Load hosted app, confirm cache, disconnect, reopen 3D and academy | Pending actual HTTP/browser test |
| Backup | Export JSON; import on a separate device; verify exact progress | Pending end-to-end download/import |
| Accessibility | Screen mode usable with touch and keyboard; screen reader review; no unreadable text | Partial: mouse-driven DOM flow tested |
| Veterinary review | Qualified veterinarian reviews all 44 cases, 16 lessons, visuals, terminology and safety | Pending professional review |
| Child usability | Supervised child navigates without prompts, can exit, and explains what they learned | Pending family testing |
| Visual polish | Consistent model proportions, lighting, signs, species animation, realistic instrument feedback | Partial; stylized models, independent renders of four new scenes; live device verification pending |

## Test procedure
1. Host all files together on an HTTPS static host. Open in the phone's normal browser, not an embedded chat preview.
2. Complete one case in screen mode. Start a second, collect one clue, exit, close browser, reopen and resume. Check notebook.
3. Open Academy. Confirm shared progress, complete a science lesson, export backup, import on another browser only if desired. No accounts or names are required.
4. Adult tests Cardboard mode while seated. Check viewer fits device, rotate landscape, confirm setup, center view before wearing. Verify both eyes, motion directions, target alignment, no double images, readability and exit. Stop if uncomfortable. No official viewer QR calibration is implemented.
5. Verify five-minute rest screen; remove viewer and take a meaningful break, longer if needed. The 30-second timer is an interface reminder, not a medical recommendation or enforced daily limit. Restarting or reloading can reset it.
6. On HTTPS, after offline cache is ready, reopen both pages with network disconnected. Confirm no lost progress.
7. A veterinarian and parent review content and child suitability before routine independent use.

## Release decision
Do not label as fully ready until all required gates pass on the intended device and the curriculum is reviewed. If optics are not comfortable, use the academy or touchscreen mode instead. Native Cardboard SDK integration is a separate engineering milestone, not part of this build.
