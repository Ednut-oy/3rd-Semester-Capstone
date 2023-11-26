WITH Airline_Data AS (
    SELECT 
        operating_airline,
        operating_airline_iata_code,
        published_airline,
        published_airline_iata_code,
    FROM {{ ref("stg_air_traffic")}}
)
