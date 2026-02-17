# Hospital Readmissions Performance Dashboard

This dashboard was built to analyze hospital readmission rates using publicly available data from the Centers for Medicare & Medicaid Services (CMS), primarily to identify performance patterns across U.S. hospitals for three key measures: heart failure readmissions, pneumonia readmissions, and all-cause readmissions. The interactive dashboard allows healthcare stakeholders such as quality improvement teams, hospital administrators, and policy makers to explore geographic trends, compare hospital performance, and understand the relationship between patient volume and readmission outcomes.

---

## Business Problem

Hospitals with higher than expected readmission rates face financial penalties. This dashboard helps answer questions like:

- Which states have the highest/lowest readmission rates?
- Which hospitals are the best and worst performers?
- Is there a relationship between patient volume and readmission outcomes?
- How do different conditions (heart failure, pneumonia, all-cause) compare?

---

## Data Source

- **Dataset:** [CMS Unplanned Hospital Visits – Hospital](https://data.cms.gov/provider-data/dataset/632h-zaca)
- **Time Period:** July 2023 – November 26, 2025
- **Measures Used:**
  - Heart failure (HF) 30-Day Readmission Rate
  - Pneumonia (PN) 30-Day Readmission Rate
  - Hybrid Hospital-Wide All-Cause Readmission Measure (HWR)
- **Hospitals:** 67,1301 facilities across the U.S.

---

## Tools Used

- **PostgreSQL** – Data cleaning, transformation, and creation of analysis-ready views
- **Python (pandas, sqlalchemy, psycopg2)** – Importing raw CSV data into PostgreSQL
- **Tableau Public** – Building the interactive dashboard

---

## Methodology

1. **Data Acquisition:** Downloaded the CMS Unplanned Hospital Visits – Provider CSV.
2. **Data Import:** Used a Python script to load the CSV into a PostgreSQL database, handling missing values and data type issues.
3. **Data Cleaning & Transformation:** Created SQL views to:
   - Convert text scores to numeric values.
   - Extract patient volume from the `Denominator` column (since `Number of Patients` contained "Not Applicable" for readmission rates).
   - Filter to the three measures of interest and keep only the most recent data per hospital and measure.
4. **Export for Tableau:** Exported the final view to a CSV file.
5. **Dashboard Design:** Built an interactive dashboard in Tableau Public with:
   - A map showing average readmission scores by state.
   - Bar charts for top 10 best and worst performing hospitals.
   - A scatter plot exploring patient volume vs. readmission scores.
   - Interactive filters for measure, state, and comparison category.

---

## Key Insights

- **Wide performance range:** The best hospitals have readmission scores as low as **0–13**, while the worst exceed **58–69**.
- **Specialty hospitals dominate the top 10 best list** – facilities focused on orthopedics and elective procedures have exceptionally low readmission rates.
- **Patient volume does not strongly correlate with readmission performance** – high‑volume hospitals are found across the entire performance spectrum.
- **For all three measures, the majority of hospitals perform “No Different Than the National Rate”**, but a significant minority are outliers on either side.

---

## Dashboard Preview

### Full Dashboard
![Full Dashboard](https://github.com/jahanara-m/hospital-readmissions-dashboard/blob/main/images/dashboard-full.png)

### Map View (Average Score by State)
![Map View](https://github.com/jahanara-m/hospital-readmissions-dashboard/blob/main/images/map-view.png?raw=true)

### Scatter Plot: Patient Volume vs. Readmission Score
![Scatter Plot](https://github.com/jahanara-m/hospital-readmissions-dashboard/blob/main/images/scatter-plot.png?raw=true)

---

## Live Dashboard

[Click here to view the interactive dashboard on Tableau Public](https://public.tableau.com/app/profile/jahanara.mohamed/viz/HospitalReadmissionsPerformanceDashboard/ReadmissionsOverview)

---
