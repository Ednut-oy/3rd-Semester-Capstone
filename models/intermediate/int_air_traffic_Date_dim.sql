WITH Date_Data AS (
    SELECT 
        activity_period_start_date,
        activity_period, 
        data_as_of,
        data_loaded_at
    FROM {{ ref("stg_air_traffic")}}
)
