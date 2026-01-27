# Using QGIS for Drone Measurement Analysis

**QGIS** is a free and open-source Geographic Information System (GIS). We use it to load the maps (orthomosaics) we created and take precise measurements.

## 1. Installing QGIS
1.  Go to the [QGIS Download Page](https://qgis.org/en/site/forusers/download.html).
2.  Download the **Long Term Release (LTR)** version (most stable).
3.  Install it on your computer.

## 2. Loading Your Orthomosaic
1.  Open QGIS Desktop.
2.  Start a **New Empty Project**.
3.  Locate your orthomosaic file (usually a `.tif` file created in Bentley iTwin or other software).
4.  Drag and drop the `.tif` file into the main QGIS window.
5.  You should see your map appear. if asked about Coordinate Reference Systems (CRS), click "OK" to use the image's default system.

## 3. Performing Measurements

### Measure Line (Distance)
1.  Look for the icon that looks like a ruler 📏 in the top toolbar (or press `Ctrl+Shift+M`).
2.  A window called "Measure" will pop up.
3.  Click on your map to start a line.
4.  Click again to add a segment.
5.  **Right-click** to finish the measurement.
6.  Read the "Total" length in the window (ensure units are set to meters or feet as needed).

### Measure Area
1.  In the "Measure" window, click the drop-down arrow next to the title (or the specific Area icon in the toolbar).
2.  Select **Measure Area**.
3.  Click around the perimeter of the object you want to measure (e.g., a building roof or a parking lot).
4.  **Right-click** to close the polygon.
5.  Read the area in square meters or square feet.
