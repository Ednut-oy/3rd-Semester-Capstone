with source as (

    select * from {{ source('3rd_semester_project', 'Air_Traffic_Data') }}

)
    select
        -- dim airline details
        operating_airline,
        operating_airline_iata_code,
        published_airline,
        published_airline_iata_code,

        -- dim location
        geo_summary,
        geo_region,

        -- dim category
        activity_type_code,
        price_category_code,
        terminal,
        
        -- dim date
        activity_period_start_date,
        activity_period, 
        data_as_of,
        data_loaded_at,

        -- other columns
        boarding_area,
        passenger_count
    from source