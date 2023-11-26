WITH Other_Data AS (
    SELECT 
        boarding_area,
        passenger_count
    FROM {{ ref("stg_air_traffic")}}
)
