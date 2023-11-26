with source as (

    select * from {{ source('3rd_semester_project', 'Air_Traffic_Data') }}

)
    select
        -- dimension table 1
        operating_airline,
        operating_airline_iata_code,
        published_airline,
        published_airline_iata_code,
        geo_summary,
        geo_region,
        activity_type_code,
        price_category_code,
        terminal,
        boarding_area
    from source