# Week 6 — Thermal Imaging Overview
- Radiometric JPEG/TIFF, FLIR-specific formats. Software: FLIR Tools, QGIS (with plugins), Agisoft/Metashape (some support), and UAV-specific inspection tools.
<!-- End Thermal.md -->

- Placeholder for curated links to manufacturer guides and tutorials.
## Further reading & resources
## Tools & formats

- Overlap: ensure sufficient overlap for mosaicking (forward & side overlap recommendations depend on sensor and altitude).
- Altitude & resolution: thermal sensors often have coarser spatial resolution than RGB—lower altitude increases ground sampling distance (GSD) resolution but reduces coverage.
- Emissivity and calibration: surfaces have different emissivities—knowing or estimating emissivity improves temperature accuracy.
- Time of day: early morning or late evening often yields better thermal contrast for some inspections.
## Flight planning & best practices

- Vegetation stress and irrigation monitoring (qualitative)
- Search & rescue and first responder support
- Electrical inspections (hotspots on panels, equipment)
- Building inspections (heat loss, insulation defects)
## Use cases

- Time-series thermal datasets for monitoring changes
- Thermal mosaics (stitched orthomosaics showing temperature distribution)
- Radiometric TIFFs (temperature-stamped images)
## Data products

- Some cameras provide relative thermal imagery (for visual inspection), while higher-end units provide radiometrically calibrated images for quantitative temperature analysis.
- Sensors detect emitted infrared radiation and convert it to temperature values, either as scaled pixel values or calibrated temperature measurements.
## How thermal sensors work

Thermal sensors measure long-wave infrared radiation emitted by objects, producing images that represent surface temperature differences rather than visible light reflectance.
## What is thermal imaging?

This page outlines thermal (infrared) sensors on drones: how they capture thermal information, typical data products, use cases, and practical flight considerations.

