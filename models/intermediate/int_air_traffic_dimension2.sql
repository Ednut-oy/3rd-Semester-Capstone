WITH Facts AS (
    SELECT 
        activity_period
    FROM {{ ref("stg_air_traffic_facts") }}
)

SELECT 
    -- Table ID
    Dim_Table2.boarding_area,
    Dim_Table2.passenger_count
FROM {{ ref("stg_air_traffic_dimensions2") }} AS Dim_Table2
LEFT JOIN Facts
ON Dim_Table2.activity_period = Facts.activity_period  
