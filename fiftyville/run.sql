select city from airports where id in (
    select destination_airport_id from flights where id in (
        select flight_id from passengers where passport_number in (
            select passport_number from people where id = 686048
        )
    )
);
