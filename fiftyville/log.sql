-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get the data of crimes scenes for the specific date and location
select * from crime_scene_reports
where year = 2023 and month = 7 and day = 28
and street = 'Humphrey Street'
limit 5;

-- Get the data of crimes scenes for the specific date and location and only select the theft crime
select * from crime_scene_reports
where year = 2023 and month = 7 and day = 28
and street = 'Humphrey Street' and description like '%CS50%';

-- Review interviews of witnesses from the day when the theft happened
select * from interviews
where year = 2023 and month = 7 and day = 28
-- Gotten a record for a flight to be bought on July 29

-- Try to see records of phone calls from the day of the theft
select * from phone_calls
where duration < 60
and year = 2023 and month = 7 and day = 28;

-- A look into the license plates leaving the bakery on that day from the security log of the bakery
select * from bakery_security_logs
where year = 2023 and month = 7 and day = 28;

-- Get people's names that withdrew money from the ATM on the day of the theft. The location of the ATM
-- was reported by a witness.
select * from people where id in (
    select person_id from bank_accounts
    where account_number in (
        select account_number from atm_transactions
        where year = 2023 and month = 7 and day = 28
        and atm_location = 'Leggett Street' and transaction_type = 'withdraw'
    )
);

-- Get flights from Fiftyville city on July 29
select * from flights where origin_airport_id in (
    select id from airports where city = 'Fiftyville'
);

-- Get passports from passengers with a flight on July 29 from Fiftyville as the origin city
select * from passengers where flight_id in (
    select id from flights where origin_airport_id in (
        select id from airports where city = 'Fiftyville'
    )
);

-- Got 2 suspects from the people table
-- ids: 514354 and 686048
select * from people
where passport_number in (
    select passport_number from passengers where flight_id in (
        select id from flights
            where year = 2023 and month = 7 and day = 29
            and origin_airport_id in (
            select id from airports where city = 'Fiftyville'
        )
    )
and passport_number in (
        select passport_number from people where id in (
            select person_id from bank_accounts
            where account_number in (
                select account_number from atm_transactions
                where year = 2023 and month = 7 and day = 28
                and atm_location = 'Leggett Street' and transaction_type = 'withdraw'
            )
        )
    )
and license_plate in (
    select license_plate from bakery_security_logs
    where year = 2023 and month = 7 and day = 28
    and activity = 'exit' and hour = 10 and minute between 16 and 26
    )
and phone_number in (
    select caller from phone_calls
    where duration <= 60 and year = 2023 and month = 7 and day = 28
    )
);

--Bank transactions from the 2 suspects from the day when the theft happened.
--If you escape you need money so the person id with the highest amount withdrew from the ATM is the id 686048
select b.person_id, t.*
from atm_transactions t join bank_accounts b on t.account_number = b.account_number
where year=2023 and month=7 and day=28
and transaction_type='withdraw' and atm_location='Leggett Street'
and b.person_id in (514354, 686048)
order by amount desc limit 1;

--Select name of the person where id is 686048
--Name: Bruce
select name from people where id = 686048;

--Select name of the person who received the call from Bruce (accomplice) on the day of the theft
--Name: Robin
select name from people where phone_number in (
    select receiver from phone_calls
    where duration <= 60 and year = 2023 and month = 7 and day = 28
    and caller in (
        select phone_number from people where id = 686048
    )
);

--Get the destination city where the thief is going to
--City: New York City
select city from airports where id in (
    select destination_airport_id from flights where id in (
        select flight_id from passengers where passport_number in (
            select passport_number from people where id = 686048
        )
    )
);
