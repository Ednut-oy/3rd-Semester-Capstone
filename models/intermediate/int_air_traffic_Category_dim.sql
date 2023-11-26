WITH Category_Data AS (
    SELECT 
        activity_type_code,
        price_category_code,
        terminal
    FROM {{ ref("stg_air_traffic") }}
)
