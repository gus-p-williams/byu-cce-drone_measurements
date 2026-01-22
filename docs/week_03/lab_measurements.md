# Measurement Lab

---

## Background

In engineering and construction, accurate measurement of distance and area is essential for site planning, cost estimation, drainage design, and infrastructure layout. Traditional field techniques such as pacing and taping provide quick approximations but are limited in accuracy. Modern surveying increasingly relies on aerial imagery and Geographic Information Systems (GIS) to obtain precise measurements efficiently.

In this lab, you will compare multiple methods for estimating area:

- Human pacing
- Using Drone-collected imagery
- Google Maps measurement tools
- GIS-based measurements using QGIS

By comparing these approaches, you will evaluate accuracy, uncertainty, and practical trade-offs between field and remote measurement techniques, similar in spirit to how pacing, taping, and total station measurements are compared in the traditional surveying lab 

---

## Objectives

By completing this lab, students will:

1. Calibrate their walking pace (feet per step). 
2. Estimate the area of a single parking stall using pacing. 
3. Compare accuracy, uncertainty, and sources of error between methods. 
4. Understand the advantages of aerial and GIS-based surveying techniques.

---

## Required Materials

- Drone aerial image of assigned parking lot (provided)
- Google Maps (web browser)
- QGIS software
- Measuring tape or known-distance reference (provided)
- Calculator (Optional)
- Lab Worksheet

---

## Procedure

### Part 1 – Pace Calibration

For the first part of the lab you will be finding your pace length in feet per step. This will be used later to convert your pacing measurements into feet. If you have already completed a similar activity, you may use your previously calculated pace length, as long as it was done recently, and you are confident in its accuracy. Follow these steps to calibrate your pace length:

1. The TAs will already measure a straight 100‑ft distance on the ground using a tape or known reference.
2. Walk the distance at a normal pace and count your steps. Try to be as consistent as possible with your stride.
3. Repeat at least **three (3)** times and compute the average number of steps per 100 ft.
4. Compute your pace length using:

$$
\text{Feet per step} = \frac{100}{\text{average steps}}
$$

5. Record this value for use in later calculations.

---

For the rest of the activity you will be measuring the area of the asphalt for the following parking lot, just east of the Engineering Building.

![EB_Parking_Lot.png](images/EB_Parking_Lot.png)

---

### Part 2 – Finding the Area by Pacing

Sometimes measurement and estimations can very rough estimates. The particular parking lot we will be measuring is not a perfect rectangle. For the pacing activity, you will just pace out the top and left side of the lot, just like in the image below.

![EB_Parking_Lot_Pacing.png](images/EB_Parking_Lot_Pacing.png)

1. Using your calibrated pace length from Part 1, pace the **length** and **width** of the entire parking lot.
2. Convert your paced steps to feet using your pace length.
3. Estimate the parking lot area assuming a rectangular shape:

$$
A_{\text{lot,pacing}} = (\text{length in ft})\,(\text{width in ft})
$$

4. Record your answer and briefly explain your method and assumptions. Explain any sources of uncertainty and how they might affect your result.
5. Measure (by pacing) the length and width of a single parking stall, then calculate its area. 
6. Measure the width of the driving lane between rows of parking stalls. 
7. Use your stall dimensions and driving-lane width to determine how many stalls fit along the length and width of the parking lot. Estimate the total number of stalls, then calculate the total parking lot area by multiplying the number of stalls by the area of one stall and adding the area occupied by the driving lanes. (You can use the image below as a guide and to help count stalls.)

![EB_Parking_Lot.png](images/EB_Parking_Lot.png)

8. Record your answer and briefly explain your method and assumptions. Explain any sources of uncertainty and how they might affect your result.

---

### Part 3 – Google Maps Measurement 

Using Google Maps, you will measure the area of the parking lot and a single parking stall. Similar to the pacing method, you will trace the outline of the area you are measuring and let Google Maps compute the area for you.

1. Open **Google Maps**.
2. Navigate to the assigned parking lot. We are recommending you use satellite view for this part.
3. Right‑click on the map and select **Measure distance**.
4. Trace the outline of a single parking stall.
5. Record the area reported (ft²).
6. Briefly explain your measurement process.
7. Use the same measurement tool to trace the full parking lot boundary. When try tracing the parking lot, be sure to zoom in enough to accurately follow the edges. We are looking for the area of the asphalt only, not including any sidewalks or grassy areas.
8. Record the total area (ft²).
9. Explain any difficulties or uncertainties encountered.

---

### Part 4 – Orthomosaic Measurement (QGIS)

Using QGIS software, you will measure the area of the parking lot and a single parking stall from the provided drone imagery. This method is similar to the Google Maps method, but you will be using GIS software to perform the measurements. This allows for more precise tracing and area calculation since you can zoom in closely and use GIS tools to assist with the measurements.

1. Open QGIS and load the provided drone imagery of the parking lot.
2. Using the polygon drawing tool, trace the outline of a single parking stall.
3. Use the field calculator to compute the area of the polygon in square feet.
4. Record the area of the stall (ft²) and briefly explain your measurement process.
5. Next, trace the entire parking lot boundary using the polygon tool.
6. Use the field calculator to compute the area of the parking lot polygon in square feet.
7. Record the total area of the parking lot (ft²).
8. Explain any difficulties or uncertainties encountered during the measurement process.

---

## Discussion Questions (Optional)

- Which method produced the largest value? Why?
- Which method do you believe is most accurate?
- What are the largest sources of error for pacing?
- How does image resolution affect QGIS accuracy? Compare drone imagery to Google Maps.
- When is drone surveying preferable to field methods?