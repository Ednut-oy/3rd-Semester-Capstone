with source as (

    select * from {{ source('3rd_semester_project', 'Air_Traffic_Data') }}

)
    select
        -- dimensions table 2
        activity_period_start_date,
        data_as_of,
        data_loaded_at
    from source