-- Creating a cleaned view with numeric score and patient volume
CREATE OR REPLACE VIEW readmissions_clean AS
SELECT
    "Facility ID",
    "Facility Name",
    "State",
    "Measure Name",
    "Compared to National",
    "Start Date",
    "End Date",
    CASE
        WHEN "Score" ~ '^[-]?[0-9]+\.?[0-9]*$' THEN "Score"::float
        ELSE NULL
    END AS score_numeric,
    CASE
        WHEN "Denominator" ~ '^[0-9]+$' THEN "Denominator"::integer
        ELSE NULL
    END AS volume_numeric,
    "Number of Patients Returned"
FROM unplanned_visits;

-- Creating dashboard view
DROP VIEW IF EXISTS dashboard_data;

CREATE VIEW dashboard_data AS
WITH latest AS (
    SELECT DISTINCT ON ("Facility ID", "Measure Name")
        "Facility ID",
        "Facility Name",
        "State",
        "Measure Name",
        "Compared to National",
        "Start Date",
        "End Date",
        score_numeric,
        volume_numeric,
        "Number of Patients Returned"
    FROM readmissions_clean
    WHERE "Measure Name" IN (
        'Heart failure (HF) 30-Day Readmission Rate',
        'Hybrid Hospital-Wide All-Cause Readmission Measure (HWR)',
        'Pneumonia (PN) 30-Day Readmission Rate'
    )
    AND score_numeric IS NOT NULL
    ORDER BY "Facility ID", "Measure Name", "End Date" DESC
)
SELECT * FROM latest;