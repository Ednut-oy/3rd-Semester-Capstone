with source as (

    select * from {{ source('3rd_semester_project', 'Air_Traffic_Data') }}

)
    select
        -- datetime
        activity_period,
        passenger_count
    from source