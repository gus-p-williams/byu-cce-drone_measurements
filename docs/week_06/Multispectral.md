# Week 6 — Multispectral Imaging Overview

This page introduces multispectral sensors on drones, the meaning of spectral bands, common indices (e.g., NDVI), and flight and calibration considerations for quantitative remote sensing.

## What is multispectral imaging?
Multispectral sensors capture image data at discrete spectral bands (e.g., red, green, blue, near-infrared, red-edge). By combining bands, we can compute spectral indices that relate to vegetation health, water content, and more.

## Common bands & indices
- RGB + NIR (near-infrared) is the common configuration for vegetation analysis.
- NDVI (Normalized Difference Vegetation Index) = (NIR - Red) / (NIR + Red)
- Other indices: NDRE (red-edge), SAVI, EVI, etc.

## Data products
- Reflectance-corrected orthomosaics for each band
- Vegetation index maps (NDVI, NDRE)
- Classified maps (crop vigor, stress zones)

## Flight planning & calibration
- Radiometric calibration: use reflectance panels or radiometric calibration workflows to convert DN to reflectance.
- Overlap & altitude: ensure sufficient overlap (forward & side) to allow mosaicking; plan altitude for desired GSD.
- Sun angle & time-of-day: consistent lighting reduces variation; avoid flights near sunrise/sunset when shadows dominate.

## Use cases
- Precision agriculture (crop vigor, prescription maps)
- Ecological monitoring and restoration
- Water resource monitoring and wetland studies

## Tools & file formats
- Common formats: GeoTIFFs per band, multispectral mosaics. Tools: QGIS, Pix4D, Agisoft Metashape, specialized multispectral software.

## Further reading & resources
- Placeholder for curated links to manufacturer guides and multispectral tutorials.

<!-- End Multispectral.md -->
