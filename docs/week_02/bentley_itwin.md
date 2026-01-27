# Bentley iTwin Capture Modeler

**Bentley iTwin Capture Modeler** (formerly ContextCapture) is a powerful photogrammetry software used to turn 2D drone photos into 3D models and 2D maps.

## 1. Accessing the Software
*   **Lab Computers:** The software is installed on the lab computers. Search for "iTwin Capture Modeler" in the start menu.
*   **Student License:** If you have a student license code, you can download the software from the Bentley Education portal.

## 2. Standard Workflow

The process of creating a model generally follows these steps:

### Step 1: Create a New Project
1.  Open iTwin Capture Modeler.
2.  Click **New Project**.
3.  Name your project (e.g., `Lab_02_Campus_Map`) and choose a save location.

### Step 2: Import Photos
1.  Select the **Photos** tab or block.
2.  Click **Add Photos** -> **Add entire directory** if your drone photos are in one folder.
3.  The software will read the metadata (GPS locations) automatically.

### Step 3: Aerotriangulation (AT)
This step figures out exactly where each camera was in 3D space when it took the picture.
1.  Click **Submit Aerotriangulation**.
2.  Use the default settings for now.
3.  Click **Submit**.
4.  Wait for the process to finish. When complete, you will see a sparse point cloud of your site.

### Step 4: Reconstruction & Production
Once the AT is done, you can build your outputs.
1.  Click **New Reconstruction**.
2.  Select the area you want to process (usually the whole box).
3.  Click **Submit Production**.
4.  Choose your desired output format:
    *   **Orthophoto/DSM:** For 2D maps and elevation models (Format: `TIFF` or `KML`).
    *   **3D Mesh:** For a realistic 3D model (Format: `3MX` or `OBJ`).
    *   **Point Cloud:** For raw 3D points (Format: `LAS`).
5.  Click **Submit**.

When the production is finished, you can view the results in the integrated viewer or export the files to use in other software like QGIS.
