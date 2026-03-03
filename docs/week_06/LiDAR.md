# Week 6 — LiDAR Overview

This page introduces LiDAR sensors on drones: how they work, the primary data products, common use cases, and practical guidance for planning LiDAR flights.

## What is LiDAR?
LiDAR (Light Detection and Ranging) uses rapid pulses of laser light to measure distances to surfaces. A LiDAR sensor records time-of-flight measurements and returns a dense set of 3D points (a point cloud) representing the scanned surfaces.

## How LiDAR works (short)
- The sensor emits laser pulses and measures the time until reflected light returns.
- Each return is georeferenced using GNSS/IMU data; multiple returns per pulse can capture vegetation structure.
- Post-processing filters, classifies, and creates products such as classified point clouds, digital surface models (DSM), digital terrain models (DTM), and intensity rasters.

### Direct example airborne/jungle mapping videos (Wikimedia file pages)
Below are direct links to the Wikimedia/Wikipedia file pages for several LiDAR video examples; these link to the original pages where the media is hosted and where license/attribution details are shown. Open each link to view the video on Wikimedia Commons/Wikipedia.

- 50 Kilometers of Brazilian Forest Canopy — https://en.wikipedia.org/wiki/File:50_Kilometers_of_Brazilian_Forest_Canopy.webm
  - Description: Airborne LiDAR survey across dense Brazilian forest canopy showing the scanning swath and canopy penetration. See the file page for licensing and attribution details.

- Flying Through LIDAR Canopy Data — https://en.wikipedia.org/wiki/File:Flying_Through_LIDAR_Canopy_Data.webm
  - Description: A fly-through of processed LiDAR point cloud data illustrating canopy and ground structure in 3D. See the file page for licensing and attribution details.

- Amazon Canopy Comes to Life through Laser Data — https://en.wikipedia.org/wiki/File:Amazon_Canopy_Comes_to_Life_through_Laser_Data.webm
  - Description: Visualization of LiDAR data over Amazon canopy; useful for seeing canopy-penetration and revealed ground features. See the file page for licensing and attribution details.

- Collecting LIDAR data over the Ganges and Brahmaputra River Basin — https://en.wikipedia.org/wiki/File:Collecting_LIDAR_data_over_the_Ganges_and_Brahmaputra_River_Basin.ogv
  - Description: Field and airborne footage illustrating data collection operations for large-area airborne LiDAR surveys. See the file page for licensing and attribution details.

What to look for in these videos:
- Platform motion and scanning swath alignment with flight lines.
- Visual differences between canopy (higher returns) and ground (lower returns).
- Transitions from raw point cloud to derived products (hillshades, DTMs, CHMs) in some clips.

## Common data products
- Raw/processed point cloud (LAS/LAZ)
- Classified returns (ground, vegetation, buildings)
- Digital Surface Model (DSM)
- Digital Terrain Model (DTM)
- Intensity imagery (reflectance-like raster)

## Typical sensors & platforms
- Lightweight scanning LiDAR units suited for small UAVs (Velodyne Puck, RIEGL miniVUX, Livox, etc.)
- Commonly paired with RTK/PPK GNSS and high-rate IMUs for better absolute accuracy

## Use cases
- High-precision topography and elevation mapping
- Vegetation structure and biomass estimation
- Corridor mapping (powerlines, roads)
- Forestry, archaeology, and floodplain modeling

## Flight planning considerations
- Altitude & resolution: lower altitude increases point density but reduces coverage and increases flight time.
- Overlap & swath: LiDAR sensors have swath widths and scan patterns; ensure flight lines provide sufficient overlap for full coverage.
- Sensor settings: scan rate, pulse repetition frequency (PRF), and scan angle affect density and penetration through vegetation.
- Georeferencing: use RTK/PPK or ground control to improve absolute accuracy.

## File formats & tools
- LAS/LAZ for point clouds; many GIS tools (PDAL, LAStools, QGIS) and commercial packages support LiDAR workflows.

## Example: LiDAR point cloud and derived terrain
Below is an illustrative figure that shows a stylized LiDAR point cloud (colored dots) over a terrain profile. The figure highlights how LiDAR returns include ground returns (used to build a Digital Terrain Model, DTM) and higher returns from vegetation or structures (which contribute to the Digital Surface Model, DSM).

![Stylized LiDAR point cloud and terrain model](images/lidar_pointcloud.svg)

Figure interpretation and tips:
- Ground returns (last returns) form the basis of a DTM — these are typically filtered from the full point cloud.
- First or highest returns (or a statistical summary) are used to build the DSM, which includes vegetation and structures.
- Classifying returns (ground, vegetation, building) is an important early processing step to derive useful elevation products.
- Pay attention to point density (points/m^2): higher density improves the ability to resolve small terrain features but increases data size and flight time.

## Further reading & resources
- [Lidar — Wikipedia](https://en.wikipedia.org/wiki/Lidar) — A comprehensive encyclopedia entry covering LiDAR's principles (time-of-flight, scanning methods), history, sensor types (airborne, terrestrial, bathymetric), common applications (topographic mapping, forestry, archaeology, autonomous systems), data formats, and processing concepts. The article includes diagrams, references, and links to related topics and standards.
  - Why visit: good quick primer for students who want a broad, well-referenced overview; useful for finding further reading, citations, and links to more specific topics (e.g., LAS format, bathymetric LiDAR, LiDAR processing techniques).

### Tools & sensors (selected links)
- PDAL (Point Data Abstraction Library) — https://pdal.io/ — Open-source library for translating and processing point cloud data; great for scripting LiDAR workflows.
- CloudCompare — https://www.cloudcompare.org/ — Open-source 3D point cloud processing and visualization tool (manual analysis, comparisons, segmentation).
- LAStools — https://rapidlasso.com/lastools/ — Fast tools for LiDAR processing (note licensing for some components).
- Potree — https://potree.org/ — Web-based point cloud viewer for publishing large point clouds in the browser.

Selected UAV LiDAR sensors / vendors (examples)
- RIEGL miniVUX series — https://www.riegl.com/products/airborne-laser-scanners/miniature-scanners/miniVUX-1-series/ — Proven small-form-factor LiDAR for UAVs.
- Velodyne Puck series (and Velodyne sensors) — https://velodynelidar.com/ — Lightweight scanning LiDAR sensors used on many platforms.
- Livox (Horizon / Avia) — https://www.livoxtech.com/ — Low-cost, high-performance solid-state LiDAR sensors now used in some UAV payloads.
- YellowScan — https://www.yellowscan-lidar.com/ — UAV-dedicated LiDAR systems and integrated platforms for surveying.
- DJI Zenmuse L1 — https://www.dji.com/zenmuse-l1 — Integrated LiDAR + RGB sensor for DJI platforms (example of an off-the-shelf UAV LiDAR payload).

<!-- End LiDAR.md -->
