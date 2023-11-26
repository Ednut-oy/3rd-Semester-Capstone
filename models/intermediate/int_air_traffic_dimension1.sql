WITH Facts AS (
    SELECT 
        activity_period
    FROM {{ ref("stg_air_traffic_facts") }}
)

SELECT 
    -- Table ID
    Dim_Table1.operating_airline,
    Dim_Table1.operating_airline_iata_code,
    Dim_Table1.published_airline,
    Dim_Table1.published_airline_iata_code,
    Dim_Table1.geo_summary,
    Dim_Table1.geo_region,
    Dim_Table1.activity_type_code,
    Dim_Table1.price_category_code,
    Dim_Table1.terminal,
    Dim_Table1.boarding_area,
    Facts.activity_period
FROM {{ ref("stg_air_traffic_dimensions1") }} AS Dim_Table1
LEFT JOIN Facts
ON Dim_Table1.activity_period = Facts.activity_period  
