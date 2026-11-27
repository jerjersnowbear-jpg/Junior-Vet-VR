# Junior Vet VR 6.0 | Willow Veterinary World

Willow Animal Hospital is a self-contained procedural 3D educational clinic for smartphones, with a browser-based learning academy that does not require WebGL or motion sensors. No accounts, advertising, analytics, API keys, external assets, or AI services. Fictional cases and in-game achievements, not professional training or medical advice.

## Start

- Extract all files into one directory. Open `index.html` in a browser for 3D screen mode. Open `academy.html` for the regular screen-based learning academy. The academy needs `curriculum.js` in the same directory.
- For phone VR and offline installation, host the entire directory on HTTPS (for example, GitHub Pages). Create a repository, upload the extracted files to the root, select Settings > Pages > Deploy from a branch > main > root. Use the published URL. No hosting has been performed.
- On the phone, use a regular browser, rotate landscape, select Start Cardboard VR, review preflight and grant motion permission if requested. Remain seated and supervised. Look straight ahead at launch and hold your gaze on a target. Use the pause/menu target, or remove the viewer and double-tap the screen to exit. Follow the viewer's age guidance. Stop if uncomfortable; the screen-based mode remains available.
- After initial HTTPS loading and successful offline cache setup, browsers that support installation may offer Add to Home Screen or Install App. Browser-specific behavior and actual offline reopen have not been verified in this environment.
- Progress is stored locally on the same origin and shared between 3D and academy. Existing v2 progress uses the same key. Avoid simultaneous tabs; clearing site data loses local progress. Export JSON from the parent dashboard to preserve it.

## Version 6.0 changes

- Four additional 3D locations: woodland wildlife rescue, aquatic hospital, adoption center and skills arena. All thirteen non-reception destinations have reception targets and screen navigation buttons.
- Twelve additional fictional patient cases, bringing the total to 44 cases across eleven clinical departments, 132 ordered evidence interactions and 44 case quizzes. Eleven animal model categories, including four new procedural models (owl, turtle, fish, hedgehog). New environments have specialty props, observation tanks, perches and rest stations.
- Four decision-based skills scenarios, each with three ordered decisions, safe corrective feedback and completion records. No treatment procedures or real diagnostic recommendations. Skills progress is included in shared progress and academy backup sanitation; unfinished skills scenarios restart on room reentry.
- Academy case catalog now offers department filtering and patient/topic search. All prior cases, lessons and anatomy modes retained. Four new skills scenarios are in the 3D clinic only, playable in VR or screen mode.
- Updated service worker cache identifier; no external assets or APIs. No native Cardboard SDK, no viewer-specific calibration.
- Automated mock-GL and screen DOM tests passed for all 44 cases, all 16 lessons, both eight-challenge anatomy modes, four skills scenarios and navigation. Four independent scene renders used app geometry and actual GLSL under Mesa GLES2; not browser or headset screenshots. See `tests/latest-results.txt`.

## Retained version 5.0 changes

- Added a tenth 3D destination: the Willow Science Studio, accessible from reception or the screen-mode department buttons. Eight individually selectable, procedural teaching models and eight knowledge challenges work with gaze and touchscreen controls. These are schematic models, not species-accurate clinical anatomy.
- Select Heart to see a pulsing model and activate a synthesized heartbeat rhythm, or select Lungs to see gentle expansion. A visible stylized Dr. Willow provides context-sensitive hints in active cases and the anatomy studio.
- Dogs, cats and rabbits have independent blinking; dogs and cats have tail movement; several mammal species have varied coat colors. No claim of full skeletal rigging or realistic physiology.
- The 3D anatomy challenge record is stored in the existing shared progress object and is included in the academy backup format. Older backups without this field still load. Separate 2D atlas progress remains outside the backup.
- Added subtle contact shading and reduced repeated HUD updates. Actual phone FPS and thermal performance remain unmeasured.

## Retained v4 functionality

- Version 4 included 9 locations and expanded to 32 cases, 96 tool/clue interactions, 32 case quizzes and seven species.
- Added a non-WebGL academy with all 32 cases, 16 science lessons with quizzes, progress summary, printable training record and backup import/export. Uses the original case content and shared progress. Local storage failure is reported in academy.
- Mid-case checkpoint/resume, validated saved state, tighter gaze target angle, adult confirmation, automatic VR break screen after five minutes, 30-second rest reminder, exit on hidden browser tab.
- Additional original room props and specialty-specific decorations. Still stylized and procedural, not photorealistic or fully rigged animal animations.
- Install manifest, icons, versioned service worker cache, and automated smoke test workflow. Requires HTTP(S) for service workers (HTTPS in normal deployment). First visit requires connectivity.
- Generic stereoscopic optics with adjustable field of view and eye separation; no official Cardboard SDK, QR viewer profile, calibrated lens correction, or native APK.

- Added a screen-based interactive schematic canine anatomy lab with eight body systems, 22 selectable structures, and eight knowledge challenges. Atlas completion is stored separately on the same browser and is not part of academy JSON backup.
- Added graphics resolution settings, synthesized chimes, extra 3D room detail, four patients per clinical department, and exit on stale motion tracking.
- Added `device.html`, a local browser compatibility report, generic stereo reference pattern and manual adult test checklist. It is not optical calibration or safety certification.

## Verification

JavaScript syntax checks passed for all four pages, curriculum and service worker. Chromium DOM smoke tests with mocked WebGL and simulated local storage passed all 32 clinical flows, 32 academy cases, 16 science lessons, 8 screen atlas challenges, 8 new immersive anatomy challenges, and 10 destination visits. The updated geometry and GLSL shaders rendered independently using Mesa GLES2 for the examination room and heart and lung exhibits. The three new images in `previews/` are geometry-only renders (no live HUD or stereo tracking). The older academy and atlas previews are retained for reference. See `tests/latest-results.txt`. Live mobile WebGL, headset optics, actual gaze targeting, audio playback, offline reopening, backup import/export on physical devices, clinical review and child usability remain pending. No native Cardboard SDK or lens correction is included.

## References (APA 7)

Google. (n.d.). *Quickstart for Google Cardboard for Android NDK*. Google for Developers. https://developers.google.com/cardboard/develop/c/quickstart

Google. (n.d.). *Overview of generating a QR viewer profile*. Cardboard Manufacturer Help. https://support.google.com/cardboard/manufacturers/answer/6321873

MDN contributors. (n.d.). *Making PWAs installable*. MDN Web Docs. https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable

MDN contributors. (n.d.). *Using service workers*. MDN Web Docs. https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers

The cases are original fictional scenarios and have not been professionally verified. Review their content with a veterinarian before presenting them as medically accurate educational material.

Antinoff, N. (2025, May). *Description of dogs*. Merck Veterinary Manual. https://www.merckvetmanual.com/dog-owners/introduction-to-dogs/description-of-dogs

Moriello, K. A. (2024, September). *Structure of the skin in dogs*. Merck Veterinary Manual. https://www.merckvetmanual.com/dog-owners/skin-disorders-of-dogs/structure-of-the-skin-in-dogs
