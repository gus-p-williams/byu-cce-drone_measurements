# Week 6 — Multispectral Imaging Overview

This page introduces multispectral sensors on drones, explains common spectral bands and indices, and provides practical guidance for planning flights and producing quantitative products.

## What is multispectral imaging?
The term "multispectral imagery" refers to images captured across multiple bands of light. Whereas traditional RGB imagery records three primary bands (red, green, and blue), multispectral sensors also record light outside the visible range — for example near-infrared (NIR) and short-wave infrared (SWIR) or "red-edge" bands. More bands means more information about the scene, which enables enhanced analysis and more precise management of natural resources and built environments.

What the human eye can see is only a small portion of the electromagnetic spectrum. Capturing reflected light beyond visible wavelengths reveals information about plant health, moisture, soil properties, and material composition that we cannot perceive with RGB alone.

### How does multispectral imaging work?
Multispectral sensors mount multiple detectors (or use filter arrays) that each record radiance in a narrow band of wavelengths. By measuring the relative reflectance in several bands, we can compute indices and extract features that map to physical properties — for example, chlorophyll content, water stress, or soil brightness.

### What do the five bands do? (common 5-band setup)
- Blue (visible): useful for detecting water, haze, and some soil/leaf properties.
- Green (visible): correlated with green vegetation and useful for true-color rendering and vegetation assessment.
- Red (visible): absorbed strongly by chlorophyll; key for many vegetation indices.
- Near-Infrared (NIR): plants reflect strongly in the NIR when healthy; NIR is critical for vegetation vigor indices like NDVI.
- Red-edge / SWIR (transition zone between red and NIR): sensitive to canopy structure and stress, useful for dense vegetation and biochemical analysis.

When chlorophyll-rich leaves are illuminated, they absorb much of the blue and red light for photosynthesis and reflect green (which is why they look green to our eyes). They also reflect a large amount of NIR — a region invisible to humans — and it is this NIR reflectance that is a powerful signal for assessing plant health.

### Why this is useful
By combining band measurements (for example computing NDVI = (NIR - Red) / (NIR + Red)), we convert raw radiance measurements into indices that correlate with vegetation vigor, biomass, or stress. Multispectral data therefore enables large-scale, quantitative monitoring of crops, forests, wetlands, and urban vegetation.

## Illustrations & visual aids
Below are useful reference pages and illustrations you can use when studying multispectral concepts. Where possible we link to public-domain images and Wikipedia pages that explain the underlying concepts:

- Electromagnetic spectrum (overview): https://en.wikipedia.org/wiki/Electromagnetic_spectrum
- Visible light and the visible spectrum: https://en.wikipedia.org/wiki/Visible_spectrum
- Vegetation reflectance and spectral signatures (why plants reflect NIR): https://en.wikipedia.org/wiki/Vegetation_index

If you'd prefer embedded images rather than external links, place the image files into `docs/week_06/images/` (for example `electromagnetic_spectrum.svg` and `leaf_reflectance.png`) and I will update the page to display them with consistent widths and captions.

### Why this matters for you
- Multispectral imagery is used to detect crop stress, nutrient deficiencies, pests, and water stress earlier than RGB alone.
- It supports precision agriculture, ecological monitoring, forestry management, and research where spectral response is important.

## Key bands & indices (student summary)
- Typical band set: Blue, Green, Red (RGB) + Near-Infrared (NIR) ± Red-edge.
- NDVI (Normalized Difference Vegetation Index) = (NIR - Red) / (NIR + Red)
  - Commonly used to estimate vegetation vigor and relative chlorophyll.
- NDRE, OSAVI, SAVI, EVI and other indices are useful for crop-specific or canopy-density situations (red-edge bands are valuable for dense canopies).

## Common data products
- Multispectral orthomosaics (per-band GeoTIFFs)
- Vegetation index maps (NDVI, NDRE)
- Combined RGB + index overlays for visualization
- Classified maps (vigor classes, stressed areas)
- Time-series change maps for monitoring

## Capture & flight planning (practical guidance)
- Overlap: use high overlap to support mosaicking and radiometric consistency. A common starting point is ~75% forward (along-track) and 60% side (cross-track). For very dense vegetation or radiometric studies increase overlap (80%+).
- Altitude & GSD tradeoffs: flying lower gives finer ground sample distance (GSD) but increases the number of images and flight time. Choose altitude to balance desired resolution and data volume.
  - Example: halving flight altitude roughly halves GSD but quadruples number of images to cover the same area.
- Gimbal angle: for orthomosaics, use nadir (straight down) imagery. For vegetation diagnostics and 3D structure, small oblique angles may be helpful but complicate mosaicking.
- Flight timing: fly near solar noon where possible for consistent illumination. Avoid low sun angles (early morning or late afternoon) to reduce long shadows.
- Radiometric considerations: cloud cover, changing sun, and BRDF (reflectance anisotropy) can all affect indices. Try to fly in uniform sky conditions.

## Radiometric calibration (to get quantitative results)
- Reflectance panels: capture images of a calibrated reflectance panel before/after the flight to convert digital numbers (DN) to reflectance.
- Downwelling light sensors (DLS): some sensors include a DLS that records illumination for per-image correction.
- Dark frame / sensor calibration: follow manufacturer guidance for sensor-specific corrections.
- Why calibrate: without radiometric correction, index values can vary between flights and are not directly comparable over time or between sensors.

## Processing workflow (simple contract)
Inputs: multispectral raw images + GPS/IMU, optional reflectance panel photos or DLS readings
Outputs: per-band orthomosaics, vegetation index rasters, classification maps
Errors / edge cases: inconsistent lighting, missing calibration images, low overlap, moving targets (wind), GNSS errors

Typical steps
1. Ingest images and metadata (camera model, band wavelengths, GPS tags).
2. Apply radiometric calibration (reflectance panel / DLS corrections).
3. Align and stitch images into per-band orthomosaics (bundle adjustment / tie points).
4. Generate vegetation indices (NDVI, NDRE) and perform classification/analysis.

## Flight planning recommendations (quick checklist)
- Set overlap: 75% forward / 60% side (increase for complex terrain or denser canopy).
- Use consistent altitude for the entire mission.
- Record reflectance panel photos at the start and end of mission.
- Avoid rapid changing illumination (moving clouds) when possible.
- Log metadata and note any anomalies (wind gusts, sensor issues).

## Use cases (student-facing examples)
- Precision agriculture: map crop vigor and identify zones for targeted interventions.
- Forestry: monitor canopy health, detect dieback or pest outbreaks.
- Ecology & restoration: monitor plant establishment, wetland vegetation, or invasive species.
- Water resources: map algal blooms, shoreline vegetation, or wetland extent.

## Tools, formats & common software
- File formats: GeoTIFF (per-band), multi-band GeoTIFFs, shapefiles or GeoPackage for vector outputs.
- Processing tools & links
  - Pix4D (commercial): https://www.pix4d.com
  - Agisoft Metashape (commercial): https://www.agisoft.com
  - OpenDroneMap (open source): https://www.opendronemap.org
  - QGIS (open source GIS): https://qgis.org
  - DJI Terra (commercial, multispectral support varies by hardware): https://www.dji.com/terra
  - MicaSense (manufacturer resources for multispectral sensors): https://www.micasense.com

## Further reading & resources
- Introductory overview: short explanations of multispectral concepts and NDVI calculations.
- Manufacturer & software guides: check your sensor and software vendor for calibration and processing workflows.

## Notes for this course
- In class labs we will provide example flights, reflectance panel data, and step-by-step processing instructions using open-source and commercial tools. When doing your own projects, maintain consistent calibration procedures to make your results comparable over time.

## Example outputs & images
Below are common multispectral outputs you will see in labs and projects. Each figure is followed by a short, student-facing note describing what the image shows and how it can be used.

### 1) Electromagnetic spectrum (visual + NIR)

<img src="../images/electromagnetic-spectrum-jpg-1536x655.webp" alt="Electromagnetic spectrum" width="600" />

*Illustration of the electromagnetic spectrum and the visible/NIR regions — useful to understand where multispectral bands sit relative to human vision.*

---

### 2) Leaf reflectance & spectral bands

<img src="../images/mulitspectral-leaf-jpg-1536x847.webp" alt="Leaf reflectance" width="600" />

*Leaf reflectance curve and band placement — shows visible and NIR reflectance differences.*

---

### 3) Water storage pond — DSM

<img src="../images/Tank-DSM-filled.webp" alt="Water storage pond DSM" width="600" />

*Digital surface model (DSM) of a water storage pond — useful for estimating fill depth and extent.*

---

### 4) NDVI / crop health map (example)

<img src="../images/Screenshot-2019-04-09-14.04.41.webp" alt="NDVI map example" width="600" />

*NDVI map showing variation in plant vigor across a field.*

---

### 5) Orchard disease detection (example)

<img src="../images/1_AQtOQh_X4O0JKZg9tGzOmA.webp" alt="Orchard disease multispectral" width="600" />

*Multispectral-derived map highlighting low-health trees in an orchard.*

---

These examples illustrate how multispectral outputs translate directly into practical decisions: precision management, irrigation control, field scouting, material classification, and disaster assessment.

<!-- End Multispectral.md -->
