WITH location_Data AS (
    SELECT 
        geo_summary,
        geo_region,
    FROM {{ ref("stg_air_traffic")}}
)
