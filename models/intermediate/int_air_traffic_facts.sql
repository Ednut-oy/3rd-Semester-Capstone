WITH Facts AS (
    SELECT 
        activity_period,
        passenger_count
    FROM {{ ref("stg_air_traffic_facts") }}
)