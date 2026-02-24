# Week 4 — Mission Planning for Structure-from-Motion (SfM) Mapping

## Overview
This note covers practical mission planning for drone photogrammetry using Structure-from-Motion (SfM) reconstruction workflows. It focuses on image-collection strategy, camera and gimbal settings, flight altitude and resolution tradeoffs, overlap and flight-line patterns, and practical tips for getting clean, well-joined datasets ready for processing.

## What is Structure-from-Motion (SfM)?
- SfM is a photogrammetric method that reconstructs camera positions and a 3D point cloud from overlapping images by finding matching keypoints across photos.
- Success depends on image redundancy, varied perspectives, and consistent exposure/appearance across the dataset.

## Key concepts
- Tie points: features that appear in multiple images which the SfM algorithm matches to estimate camera poses.
- Overlap / redundancy: multiple views of the same area increase tie-point matches and robustness.
- GSD (Ground Sample Distance): the ground distance represented by one image pixel — a measure of spatial resolution.

## Mission-planning software and provided parameters
- Commercial mission-planning apps are normally used to generate automated flight lines and image triggers. Common tools include Pix4Dcapture, DJI GS Pro, UgCS, QGroundControl, DroneDeploy, and others.
- In this course we provide the specific mission parameters (polygon or center/extent, altitude, overlap percentages, gimbal angles, speed, and capture interval) that students should enter into their chosen planning app. Providing parameters ensures consistent data collection across teams and makes processing and grading reproducible.

What instructors provide
- Area definition: polygon KML/GeoJSON or center coordinates and extents to import into the planner.
- Altitude (AGL): the planned flight height above ground.
- Overlap: forward (along-track) and side (sidelap) percentages.
- Gimbal angles: nadir and any oblique pass angles needed for structures.
- Capture method: time-based interval or distance-trigger (or camera trigger event); suggested interval or distance between photos.
- Flight speed: recommended cruise speed for the selected capture interval to meet the overlap target.
- Camera settings: RAW vs JPEG, shutter speed, ISO, white balance, and any image stabilization recommendations.
- Pass plan: number of flight lines, cross-hatch or perpendicular passes, and any orbit/oblique passes.
- Ground control: number and approximate positions of required GCPs (coordinates provided separately when survey-quality georeferencing is needed).
- Safety settings: return-to-home altitude, geofence limits, maximum ascent/descent rates, and battery/segment breaks.
- Export requirements: mission file format, log submission, and photo naming conventions if required.

Sample parameter template (example students will receive)
- Area: KML polygon (attached)
- Altitude: 100 m AGL
- Forward overlap: 80%
- Side overlap: 70%
- Flight direction: east-west with alternating line directions
- Gimbal: 0° for nadir pass; additional 25° oblique pass (single altitude)
- Speed: 5 m/s
- Capture: trigger every 2 seconds (or distance ~10 m depending on speed)
- Camera: RAW, shutter 1/125, ISO 100, manual white balance
- GCPs: 4 markers around the perimeter (coordinates supplied)
- Safety: RTL altitude 120 m, mission split for battery swaps, geofence as provided

Guidance for students
- Import the provided area/missions into your planner and verify the flight-line spacing and estimated image count before flying.
- Check that the planner's estimate for capture spacing matches the overlap targets (speed and interval together determine along-track overlap).
- Always perform a short test flight to confirm image spacing, exposure, and battery estimates before committing to the full mission.

## Image-collection best practices
- Overlap (forward/along-track): 75–85% recommended for detailed mapping and complex structures.
- Sidelap (between adjacent flight lines): 60–75% is common; increase toward 80% for difficult surfaces or tall vegetation.
- Nadir (straight down) vs oblique images:
  - Nadir images provide uniform top-down coverage and are essential for planar surfaces.
  - Oblique images (15°–45° off-nadir) help capture vertical faces, building facades, and reduce reconstruction gaps for structures.
  - For structures or facades, combine a nadir survey with one or more oblique passes or orbit shots.
- Gimbal angle:
  - Use 0° (nadir) for orthomosaic-focused surveys.
  - Use 15°–35° for mixed nadir/oblique surveys; 45° or higher for targeted facades (but be careful of extreme foreshortening).
- Camera overlap strategy:
  - For urban/structural surveys: 80% forward, 70% side is a good starting point.
  - For open/flat terrain: 70% forward, 60% side may be sufficient.
- Flight-line spacing and cross-hatch:
  - Use a cross-hatch (orthogonal) set of flights or extra perpendicular passes over complex sites to improve tie points and reduce systematic errors.

## Camera settings and image quality
- Use manual exposure to avoid changes between images; lock shutter speed and ISO where lighting is consistent.
- Keep ISO low to minimize noise; increase shutter speed to avoid motion blur (higher speed for windy conditions or fast rotorcraft).
- Disable aperture/ISO auto modes, HDR, and other in-camera processing that changes image appearance between frames.
- Use consistent white balance (manual) if possible.

## Flight altitude, GSD, and tradeoffs
- GSD formula (conceptual): GSD ∝ (flight height × sensor size) / (focal length × image pixels). Use your camera/drone data to calculate exact GSD.
- Practical rule-of-thumb example: with a small-sensor camera (sensor width ≈ 6.17 mm, focal length ≈ 4.5 mm, image width 4000 px), at 100 m AGL you might expect ~3–4 cm/pixel GSD.
- Tradeoffs:
  - Lower altitude → better resolution (smaller GSD) but more images to cover the same area (higher data volume and longer processing times).
  - Higher altitude → less data and faster processing but reduced ability to resolve small features.
  - Choose altitude based on the smallest feature you need to resolve and allowable processing time/storage.

## Estimating image count and coverage
- Compute approximate footprint per image using camera FOV at planned altitude; then estimate number of flight lines and passes using overlap and area size.
- Many mission-planning apps provide image-count estimates and battery/flight-time planning; always build margin for extra images and safety.

## Special considerations for structures and vertical surfaces
- Orbit or multi-altitude passes capture different perspectives for tall structures.
- Add oblique passes at multiple elevations when mapping towers, silos, or building facades.
- Mark GCPs (ground control points) and survey them if you need accurate georeferencing beyond the onboard GNSS accuracy.

## Data management and processing tips
- Plan for storage: raw images can be large. For a mid-sized survey, expect hundreds to thousands of images and tens to hundreds of GB.
- Split large projects into blocks if necessary and stitch in processing software with shared GCPs or tie images between blocks.
- Create an acquisition log with GPS time, battery, weather, camera settings, and notable events to aid troubleshooting.

## Preflight checklist for SfM mapping
- Confirm batteries charged and spares available.
- Card space sufficient; label media and backup after each flight.
- Camera settings: RAW, manual exposure, fixed white balance, image stabilization off (if recommended by manufacturer), disable HDR.
- Flight plan set with desired overlap/altitude and failsafes (return-to-home, geofence).
- Check lighting: avoid low sun angle causing long shadows across the target; mid-day or overcast conditions often work best for even lighting.
- Safety: verify airspace, NOTAMs, permissions, and on-site hazards.

## Processing recommendations
- Start with a small subset to validate camera calibration and tie-point density before processing full dataset.
- Use masks for areas you don’t want to match (e.g., moving water or people) where supported.
- If you have GCPs, import surveyed coordinates and use them to align and scale the model.
- Run a dense reconstruction and mesh with conservative settings for initial QA, then increase quality for final products.

## Further reading and tools
- Mission planners: Pix4Dcapture, DJI GS Pro, UgCS, QGroundControl, and many other apps provide flight automation and overlap controls.
- SfM/processing software: Agisoft Metashape, Pix4Dmapper, OpenDroneMap, RealityCapture, and cloud services.

---

### Quick reference: recommended starting settings
- Overlap: 80% forward / 70% side
- Nadir + oblique mix for structures (0° + 15°–35° oblique)
- Camera: RAW, manual exposure, low ISO, shutter speed to avoid motion blur
- GCPs: optional for visual models, required for survey-grade outputs
- Cross-hatch passes for complex or tall sites


---

## Example mission diagrams

Below are two schematic example mission diagrams to illustrate common acquisition patterns used in SfM mapping. These are simplified diagrams to show concepts — use your mission-planning app to generate exact flight lines for your drone and site.

![](images/flight_grid.svg)

*Figure 1 — Grid flight plan with alternating flight-line directions. Blue solid lines show planned nadir flight lines; green dashed lines show optional cross-hatch/perpendicular passes to improve tie points and reduce systematic errors.*

Use this pattern when you need consistent nadir coverage over a large area (fields, parking lots, rooftops). Add cross-hatch passes when the surface is complex, has tall vegetation, or when you want improved vertical accuracy.

![](images/orbit_oblique.svg)

*Figure 2 — Orbit and oblique passes around a structure. Orange dashed path shows an oblique orbit with sample camera positions and pointing directions toward the structure.*

This pattern is useful for structures, towers, and vertical facades. Combine oblique/orbit passes with nadir coverage so roof geometry and top surfaces are captured as well.

Practical tips when using these patterns:
- Export the flight plan from your planner and review estimated image count and battery requirements before flying.
- Maintain consistent camera settings between nadir and oblique passes where possible to improve matching (same exposure and white balance).
- For oblique/orbit passes, stagger altitudes if the structure is tall to capture more vertical detail.
- Consider additional ground control or checkpoints around complex sites for improved absolute accuracy.

---

If you want, I can also add a small calculation tool or example spreadsheet to estimate GSD and image count using your drone/camera parameters — tell me the drone/camera model and image size and I’ll add it.
