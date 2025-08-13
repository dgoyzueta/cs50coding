
-- *** The Lost Letter ***
-- Find the id for the address 900 Somerville Avenue
select * from addresses where address = '900 Somerville Avenue' limit 5;
-- Find the package id for the congratulatory letter
select * from packages where contents like '%congrat%' limit 5;
-- Get the package_id from scans. It returns 384
select * from scans
where package_id in (select id from packages where contents like '%congrat%')
and address_id in (select id from addresses where address = '900 Somerville Avenue');
-- Get the address id where it was sent. It returns 854
select address_id from scans where package_id = 384 and action = 'Drop'
-- Get address and type from Addresses.
select address, type from addresses
where id = (select address_id from scans where package_id = 384 and action = 'Drop');

-- *** The Devious Delivery ***
--Get data from packages where the origin address is NULL. It returns package id 5098
select id from packages where from_address_id is null;

--Get data from scans where the action = 'Drop' and package id is 5098. It returns address id 348
select address_id from scans where action = 'Drop' and package_id in (select id from packages where from_address_id is null);

--Get content of the package. Result: Duck debugger
select contents from packages where id = (select id from packages where from_address_id is null);

--Get address type where address id is 348. Result: Police Station
select type from addresses where id in (select address_id from scans where action = 'Drop' and package_id in (select id from packages where from_address_id is null));

-- *** The Forgotten Gift ***
--Get Address id for address 109 Tileston Street and 728 Maple Place
select id from addresses where address = '109 Tileston Street'; -- 9873
select id from addresses where address = '728 Maple Place'; -- 4983
--Get data from packages where address ids correspond to the addresses above. The pagage id is 9523
select id from packages where from_address_id = 9873 and to_address_id = 4983;
--Get scans for the package above
select * from scans where package_id in (select id from packages where from_address_id = 9873 and to_address_id = 4983);
--> The driver 11 dropped the package at address 7432 and the driver 17 picked it up again from this address
--> and the package is still on its way
select name from drivers where id = 17;
--> The name of the driver is Mikel
