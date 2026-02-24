# Structure-from-Motion (SfM) — Workflow Overview

This note explains the core steps in a typical Structure-from-Motion (SfM) photogrammetry pipeline, from feature detection and matching through sparse and dense reconstruction to mesh and orthophoto generation. The images included are schematic and intended to illustrate concepts rather than precise algorithmic detail.

## High-level pipeline
1. Image acquisition: capture overlapping images with known approximate camera poses (from drone GPS/IMU).
2. Feature detection & matching: detect keypoints (SIFT, ORB, AKAZE, etc.) in images and match descriptors between image pairs.
3. Initial pose estimation & sparse reconstruction: use pairwise matches to estimate relative camera poses (essential/fundamental matrix, RANSAC) and triangulate a sparse set of 3D points (tie points).
4. Bundle adjustment: jointly refine camera poses and 3D point positions to minimize reprojection error across all observations.
5. Dense reconstruction: generate a dense point cloud by stereo-matching (multi-view stereo) across images using the refined poses.
6. Mesh & texturing: build a surface mesh (polygons) from the dense cloud, then project images onto the mesh to create a textured model and orthophotos.
7. Georeferencing & export: if GCPs or RTK/PPK data are available, align and scale the model to real-world coordinates and export orthophotos, DSM/DTM, and 3D models.

---

## Feature detection and matching

![](images/sfm_camera_matches.svg)

Feature detectors find distinctive keypoints in each image and compute descriptors. Matching algorithms pair keypoints across images to form correspondences; these correspondences are the basis for estimating relative camera geometry and triangulating 3D points.

Why matches matter
- A single 3D point must be observed in at least two images to be triangulated.
- Robust matching (with RANSAC) rejects outliers and inconsistent matches, improving the stability of pose estimation.

---

## Sparse (coarse) reconstruction and bundle adjustment

- From initial matched image pairs, SfM estimates relative rotations and translations between cameras (up to scale unless absolute information exists) using the essential or fundamental matrix and RANSAC to remove false matches.
- Triangulation of correspondences yields a sparse (coarse) point cloud of tie points and initial camera positions.
- Bundle adjustment refines all camera poses and 3D points by minimizing reprojection error — this step greatly improves internal consistency and is computationally expensive but crucial for accuracy.

---

## Dense reconstruction and mesh generation

![](images/sfm_pointcloud_pipeline.svg)

- Using the refined camera poses, multi-view stereo algorithms compute dense depth estimates for pixels and generate a dense point cloud.
- The dense cloud is then meshed into polygons (e.g., via Poisson surface reconstruction or Delaunay triangulation) and textured using the original photos to create realistic 3D models.
- Orthophotos and digital surface models (DSMs) are created by projecting/orthorectifying the imagery onto the mesh or rasterizing the dense point cloud.

---

## Common algorithmic building blocks
- Keypoint detectors and descriptors: SIFT, SURF (patented historically), ORB, AKAZE, BRISK.
- Robust estimation: RANSAC for essential/fundamental matrix fitting and outlier rejection.
- Bundle adjustment solvers: Ceres Solver, g2o, SBA.
- Multi-view stereo: Patch-based MVS (PMVS), dense image matching implementations in commercial and open-source tools.
- Surface reconstruction: Poisson reconstruction, Delaunay triangulation, and mesh simplification techniques.

## Practical tips
- Image quality and overlap drive SfM success — low-texture surfaces or repetitive patterns cause matching failures.
- Varying perspectives and oblique imagery help reconstruct vertical surfaces and reduce occlusions.
- Use GCPs or RTK/PPK for absolute positioning and scale when survey-grade accuracy is required.
- Start processing with a small subset to validate camera models and matching quality before scaling to the full dataset.

