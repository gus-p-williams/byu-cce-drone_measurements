# Week 6 — Thermal Imaging Overview

**Key resource:** [DJI — Thermal Drone Basics](https://enterprise-insights.dji.com/blog/thermal-drone-basics) — A concise, practical overview of thermal sensor types, common payloads, basic flight-planning tips, calibration and emissivity considerations, and typical operational use-cases. Read this to get a manufacturer perspective on common workflows and sensor capabilities.

- Radiometric JPEG/TIFF, FLIR-specific formats. Software: FLIR Tools, QGIS (with plugins), Agisoft/Metashape (some support), and UAV-specific inspection tools.
<!-- End Thermal.md -->

- Placeholder for curated links to manufacturer guides and tutorials.
## Further reading & resources
## Tools & formats

- Overlap: ensure sufficient overlap for mosaicking (forward & side overlap recommendations depend on sensor and altitude).
- Altitude & resolution: thermal sensors often have coarser spatial resolution than RGB—lower altitude increases ground sampling distance (GSD) resolution but reduces coverage.
- Emissivity and calibration: surfaces have different emissivities—knowing or estimating emissivity improves temperature accuracy.
- Time of day: early morning or late evening often yields better thermal contrast for many inspection tasks.
## Flight planning & best practices

- Vegetation stress and irrigation monitoring (qualitative)
- Search & rescue and first responder support
- Electrical inspections (hotspots on panels, equipment)
- Building inspections (heat loss, insulation defects)
## Use cases

- Time-series thermal datasets for monitoring changes
- Thermal mosaics (stitched orthomosaics showing temperature distribution)
- Radiometric TIFFs (temperature-stamped images)

- Building inspections / HVAC / insulation
  - Why this matters: Thermal images reveal heat loss, missing insulation, HVAC leaks, and rooftop issues. They are useful for teaching emissivity, and for comparing qualitative visual patterns to calibrated temperature data.
  - Examples students may examine: roof heat loss, window/door thermal leaks, HVAC duct defects.

- Electrical & powerline inspection
  - Why this matters: Thermal hotspots on panels, transformers, circuit breakers or line hardware can indicate failing components, overloads, or poor connections and are commonly used for condition-based maintenance.
  - Examples students may examine: transformer hotspots, solar panel cell anomalies, switchgear inspections.

- Search & rescue / first responders
  - Why this matters: Thermal imagery helps detect humans or warm objects in low-light or obscured conditions where visible imagery may fail; it illustrates operational constraints and detection limits.
  - Examples students may examine: drone-assisted searches, night-time perimeter sweeps, locating warm bodies in collapsed structures.

- Agriculture / vegetation stress
  - Why this matters: Thermal contrasts can indicate irrigation stress, soil moisture differences, or animal presence and serve as qualitative indicators to complement multispectral indices.
  - Examples students may examine: irrigation effectiveness, livestock detection, early-season crop stress.
## Data products

- Some cameras provide relative thermal imagery (for visual inspection), while higher-end units provide radiometrically calibrated images for quantitative temperature analysis.
- Sensors detect emitted infrared radiation and convert it to temperature values, either as scaled pixel values or calibrated temperature measurements.
## How thermal sensors work

Thermal sensors measure long-wave infrared radiation emitted by objects, producing images that represent surface temperature differences rather than visible light reflectance.
## What is thermal imaging?

This page outlines thermal (infrared) sensors on drones: how they capture thermal information, typical data products, use cases, and practical flight considerations.

## Example images and suggested activities

Below are three representative thermal images included in the course `docs/week_06/images/` directory. Each figure links to the original Wikimedia Commons file page (see the file page for license and author information). Use the examples below for the suggested student activities.

### 1) Lakeshore Geyser — thermal image

<a href="https://commons.wikimedia.org/wiki/File:Thermal_image_of_Lakeshore_Geyser_(early_evening,_1_August_2016).jpg" target="_blank">
  <img src="/en/latest/week_06/images/lakeshore_geyser_thermal.jpg" alt="Thermal image of Lakeshore Geyser" width="720">
</a>

Figure: Thermal image of Lakeshore Geyser — see the linked file page for full attribution and license details.

Description: This thermal image captures geothermal heat expression and temperature contrasts between hot water/steam and surrounding cooler ground in the early evening. Notice the strong temperature gradients and how emissive surfaces (wet ground, steam) appear compared to dry terrain.

Suggested student activities:
- Compare thermal contrast at different times of day and explain when thermal surveys are most informative.
- Discuss how surface state (wet vs dry) and emissivity affect apparent temperatures.
- Practice qualitative interpretation: identify regions of interest and explain likely causes of observed thermal patterns.

---

### 2) Coronation Reserve — paired visual + thermal

<a href="https://commons.wikimedia.org/wiki/File:Thermal_image_and_visual_image_of_Coronation_Reserve.png" target="_blank">
  <img src="/en/latest/week_06/images/coronation_reserve_thermal_rgb.png" alt="Thermal and visual image of Coronation Reserve" width="960">
</a>

Figure: Side-by-side thermal and visual images — see the linked file page for full attribution and license details.

Description: This file contains a thermal image alongside the corresponding visual (RGB) image. Side-by-side comparisons help correlate thermal anomalies with visible features (e.g., buildings, water bodies, vegetation patches).

Suggested student activities:
- Co-registration exercise: mark features on the RGB image and locate corresponding thermal signatures.
- Overlay/mosaicking discussion: describe how to align thermal orthomosaics with RGB basemaps.
- Annotate anomalies and propose hypotheses for observed thermal differences.

---

### 3) Large temperature-differential example (29 °C)

<a href="https://commons.wikimedia.org/wiki/File:Thermal_and_visual_image_showing_29_degree_C._temperature_differential.png" target="_blank">
  <img src="/en/latest/week_06/images/temp_29deg_differential_thermal.png" alt="Thermal and visual image showing 29°C differential" width="1280">
</a>

Figure: Thermal + visual image showing a ~29 °C differential — see the linked file page for full attribution and license details.

Description: This example highlights a large measured temperature differential between two adjacent surfaces. It demonstrates the dynamic range of thermal data and the importance of calibration when extracting absolute temperatures.

Suggested student activities:
- If radiometric TIFFs are available, practice extracting temperature values and compare sensor limitations.
- Discuss how color maps influence interpretation and document the units and calibration metadata required for quantitative analysis.
- Compare relative contrasts across scenes and consider factors that may produce apparent differences (emissivity, viewing angle, atmospheric effects).

---

Each figure links to the original Wikimedia Commons file page; review the file page for author and license information if you plan to reuse the images beyond course materials.
