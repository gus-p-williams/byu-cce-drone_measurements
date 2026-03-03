# Week 6 — Multispectral Imaging Overview

This page introduces multispectral sensors on drones, explains common spectral bands and indices, and provides practical guidance for planning flights and producing quantitative products.

## Key Takeaways
- **Beyond visible:** Multispectral sensors capture light outside the visible range (Near-Infrared, Red-edge).
- **Plant health:** Healthy plants reflect Near-Infrared (NIR) light strongly, which is a key signal for vigor.
- **Indices:** Mathematical formulas like NDVI combine spectral bands to quantify plant stress and biomass.
- **Calibration:** Using reflectance panels is essential for comparing data over time or between sensors.

---

## What is multispectral imaging?
The term "multispectral imagery" refers to images captured across multiple bands of light. Whereas traditional RGB imagery records three primary bands (red, green, and blue), multispectral sensors also record light outside the visible range — for example near-infrared (NIR) and "red-edge" bands. More bands means more information about the scene, enabling enhanced analysis of natural resources and built environments.

What the human eye can see is only a small portion of the electromagnetic spectrum. Capturing reflected light beyond visible wavelengths reveals information about plant health, moisture, soil properties, and material composition that we cannot perceive with RGB alone.

### How does multispectral imaging work?
Multispectral sensors mount multiple detectors (or use filter arrays) that each record radiance in a narrow band of wavelengths. By measuring the relative reflectance in several bands, we can compute indices and extract features that map to physical properties — for example, chlorophyll content, water stress, or soil brightness.

### What do the common bands do?
- **Blue (visible):** Useful for detecting water, haze, and some soil/leaf properties.
- **Green (visible):** Correlated with green vegetation; useful for true-color rendering.
- **Red (visible):** Absorbed strongly by chlorophyll; key for many vegetation indices.
- **Near-Infrared (NIR):** Plants reflect strongly in the NIR when healthy; critical for NDVI.
- **Red-edge:** Transition zone between red and NIR; sensitive to canopy structure and stress.

When chlorophyll-rich leaves are illuminated, they absorb much of the blue and red light for photosynthesis and reflect green. They also reflect a large amount of NIR — a region invisible to humans — which is a powerful signal for assessing plant health.

## Common data products
- **Multispectral orthomosaics:** Per-band or multi-band GeoTIFFs.
- **Vegetation index maps:** NDVI (vigor), NDRE (dense canopy stress).
- **Classified maps:** Vigor classes, stressed areas, or material types.
- **Time-series change maps:** Monitoring growth or stress over a season.

## Key bands & indices
- **NDVI (Normalized Difference Vegetation Index)** = (NIR - Red) / (NIR + Red)
  - Commonly used to estimate vegetation vigor and relative chlorophyll.
- **NDRE (Normalized Difference Red Edge):** Better for dense canopies where NIR might saturate.

## Use cases & applications
- **Precision agriculture:** Map crop vigor and identify zones for targeted interventions (fertilizer, irrigation).
- **Forestry:** Monitor canopy health, detect dieback or pest outbreaks.
- **Ecology & restoration:** Monitor plant establishment, wetland vegetation, or invasive species.
- **Water resources:** Map algal blooms, shoreline vegetation, or wetland extent.

## Flight planning & best practices
- **Overlap:** Use high overlap (~75% forward / 70% side) to support radiometric consistency and mosaicking in complex vegetation.
- **Altitude & GSD:** Flying lower gives finer ground sample distance (GSD) but increases flight time.
- **Flight Timing:** Fly near solar noon (high sun angle) for consistent illumination and to reduce long shadows.
- **Environmental Conditions:** Aim for uniform sky conditions (either clear or completely overcast) to avoid changing shadows.

## Radiometric calibration
- **Reflectance panels:** Capture images of a calibrated panel before and after the flight to convert digital numbers to reflectance.
- **Downwelling Light Sensors (DLS):** Records illumination for per-image correction.
- **Why calibrate:** Without it, index values can vary between flights and are not comparable over time.

## Processing workflow
1. **Ingest images and metadata:** GPS tags, camera model, band wavelengths.
2. **Apply radiometric calibration:** Using panel or DLS readings.
3. **Align and stitch:** Create per-band orthomosaics via bundle adjustment.
4. **Generate indices:** Compute NDVI, NDRE, etc., from the stitched bands.

## Tools & software
- **Commercial:** Pix4D, Agisoft Metashape, DJI Terra.
- **Open Source:** OpenDroneMap, QGIS.
- **Manufacturer Resources:** [MicaSense (AgEagle)](https://micasense.com/){target='_blank'} - useful for sensor-specific guides.

## Example outputs & images

### 1) Electromagnetic spectrum (visual + NIR)
<img src="../images/electromagnetic-spectrum-jpg-1536x655.webp" alt="Electromagnetic spectrum" width="600" />

*Description: Illustration of where multispectral bands sit relative to human vision (visible spectrum).*

---

### 2) Leaf reflectance & spectral bands
<img src="../images/mulitspectral-leaf-jpg-1536x847.webp" alt="Leaf reflectance" width="600" />

*Description: Shows how healthy leaves reflect very little red light but a huge amount of Near-Infrared light.*

---

### 3) NDVI / crop health map
<img src="../images/Screenshot-2019-04-09-14.04.41.webp" alt="NDVI map example" width="600" />

*Description: An NDVI map showing variation in plant vigor across a field. Greener areas typically indicate higher vigor.*

---

### 4) Orchard disease detection
<img src="../images/1_AQtOQh_X4O0JKZg9tGzOmA.webp" alt="Orchard disease multispectral" width="600" />

*Description: Highlights low-health trees in an orchard that might be invisible in standard RGB photos.*

---

## Further reading & resources
- [Wikipedia — Vegetation Index](https://en.wikipedia.org/wiki/Vegetation_index){target='_blank'}
- [NASA — Measuring Vegetation (NDVI)](https://earthobservatory.nasa.gov/features/MeasuringVegetation){target='_blank'}

<!-- End Multispectral.md -->
