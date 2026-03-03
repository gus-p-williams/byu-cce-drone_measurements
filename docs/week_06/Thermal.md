# Week 6 — Thermal Imaging Overview

This page outlines thermal (infrared) sensors on drones: how they capture thermal information, typical data products, use cases, and practical flight considerations.

## Key Takeaways
- **Heat, not light:** Thermal sensors measure emitted infrared radiation (heat), not reflected visible light.
- **Surface variation:** Different materials emit heat differently (emissivity), which affects temperature readings.
- **Timing matters:** Early morning or late evening often provides the best thermal contrast for inspections.
- **Applications:** Used widely in building inspections, search and rescue, and precision agriculture.

---

**Key resource:** [DJI — Thermal Drone Basics](https://enterprise-insights.dji.com/blog/thermal-drone-basics){target='_blank'} — A concise, practical overview of thermal sensor types, common payloads, basic flight-planning tips, calibration and emissivity considerations, and typical operational use-cases.

---

## What is thermal imaging?
Thermal sensors measure long-wave infrared radiation emitted by objects, producing images that represent surface temperature differences rather than visible light reflectance.

## How thermal sensors work
- **Infrared Detection:** Sensors detect emitted infrared radiation and convert it to temperature values, either as scaled pixel values or calibrated temperature measurements.
- **Radiometric vs. Non-radiometric:** Some cameras provide relative thermal imagery (for visual inspection), while higher-end units provide radiometrically calibrated images for quantitative temperature analysis.
- **Emissivity:** Surfaces have different emissivities—knowing or estimating emissivity improves temperature accuracy.

## Common data products
- **Radiometric TIFFs:** Temperature-stamped images where each pixel contains a temperature value.
- **Thermal Mosaics:** Stitched orthomosaics showing temperature distribution over a large area.
- **Time-series datasets:** Comparisons of thermal maps over time to monitor changes.
- **File Formats:** Radiometric JPEG/TIFF, FLIR-specific formats.

## Use cases & applications

### 1) Building & Infrastructure Inspection
Thermal images reveal heat loss, missing insulation, HVAC leaks, and rooftop issues.
- **Examples:** Roof heat loss, window/door thermal leaks, HVAC duct defects.

### 2) Electrical & Powerline Inspection
Thermal hotspots on panels, transformers, or circuit breakers can indicate failing components or overloads.
- **Examples:** Transformer hotspots, solar panel cell anomalies, switchgear inspections.

### 3) Search & Rescue / First Responders
Thermal imagery helps detect humans or warm objects in low-light or obscured conditions.
- **Examples:** Drone-assisted searches, night-time perimeter sweeps.

### 4) Agriculture / Vegetation Stress
Thermal contrasts can indicate irrigation stress, soil moisture differences, or animal presence.
- **Examples:** Irrigation effectiveness, livestock detection.

## Flight planning & best practices
- **Overlap:** Ensure high overlap (~80% forward and side) for successful mosaicking, as thermal images often lack distinct features.
- **Altitude & Resolution:** Thermal sensors often have coarser spatial resolution than RGB; flying lower increases ground sampling distance (GSD) but reduces coverage.
- **Time of Day:** Early morning or late evening often yields better thermal contrast for many inspection tasks.
- **Environmental Conditions:** Avoid high winds or recent rain, which can "wash out" thermal signatures.

## Tools & software
- **Processing:** FLIR Tools, QGIS (with plugins), Agisoft Metashape, Pix4D, and UAV-specific inspection tools.

## Example images & student activities

Below are representative thermal images. Use these examples for the suggested activities.

### 1) Lakeshore Geyser — thermal image
<a href="https://commons.wikimedia.org/wiki/File:Thermal_image_of_Lakeshore_Geyser_(early_evening,_1_August_2016).jpg" target="_blank">
  <img src="../images/lakeshore_geyser_thermal.jpg" alt="Thermal image of Lakeshore Geyser" width="720">
</a>

*Description: Notice the strong temperature gradients between hot water/steam and the cooler surrounding ground. This highlights how geothermal heat is expressed.*

**Activity:**
- Discuss how surface state (wet vs dry) and emissivity affect apparent temperatures.

---

### 2) Coronation Reserve — paired visual + thermal
<a href="https://commons.wikimedia.org/wiki/File:Thermal_image_and_visual_image_of_Coronation_Reserve.png" target="_blank">
  <img src="../images/coronation_reserve_thermal_rgb.png" alt="Thermal and visual image of Coronation Reserve" width="960">
</a>

*Description: Side-by-side comparison helps correlate thermal anomalies with visible features like buildings or vegetation patches.*

**Activity:**
- **Co-registration:** Identify a feature in the RGB image and locate its corresponding thermal signature.

---

### 3) Large temperature-differential example
<a href="https://commons.wikimedia.org/wiki/File:Thermal_and_visual_image_showing_29_degree_C._temperature_differential.png" target="_blank">
  <img src="../images/temp_29deg_differential_thermal.png" alt="Thermal and visual image showing 29°C differential" width="1280">
</a>

*Description: This example shows a ~29°C differential, demonstrating the dynamic range of thermal sensors.*

**Activity:**
- Discuss how color maps (palettes) influence interpretation and what metadata is needed for absolute temperature extraction.

---

## Further reading & resources
- [FLIR — How Do Thermal Cameras Work?](https://www.flir.com/discover/otm-ii/how-do-thermal-cameras-work/){target='_blank'}
- [NASA — Infrared Waves](https://science.nasa.gov/ems/07_infraredwaves){target='_blank'}

<!-- End Thermal.md -->
