-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

--Creating sample data for the property table:
INSERT INTO property (id, description, address, zipcode, state, bookValue, marketValue)
VALUES
(1, "The Commons", "1010 Ambergate Place Apt 5", "22102", "VA", 250000, 350000),
(2, "The Kings", "1010 Fisher Drive Apt 2", "22180", "VA", 350000, 450000);

--Creating sample data for the contract table:
INSERT INTO contract (id, propertyId, startDate, endDate, rentAmount, status)
VALUES
(1, 1, "2021-01-01","2021-12-31", 1800, "CLOSED"),
(2, 1, "2025-01-01",NULL, 1900, "ACTIVE"),
(3, 2, "2025-02-01",NULL, 2000, "ACTIVE");

--Creating sample data for the tenant table:
INSERT INTO tenant (id, contractId, firstName, middleName, lastName, driverLicense)
VALUES
(1,1, "PETER", "ANDREW", "SMITH", "C1234567"),
(2,2, "SAM", "ELIZABETH", "HOPKINS", "X1234567"),
(3,2, "JOHN", "DOE", "HOPKINS", "Y1234567"),
(4,3, "DANIEL", "JOHN", "HARVARD", "Z1234567");

--Creating sample data for the rent table:
INSERT INTO rent (id, contractId, paymentDate, amount)
VALUES
(1, 1, "2021-01-01", 1800),
(2, 1, "2021-02-01", 1800),
(3, 1, "2021-03-01", 1800),
(4, 1, "2021-04-01", 1800),
(5, 1, "2021-05-01", 1800),
(6, 1, "2021-06-01", 1800),
(7, 1, "2021-07-01", 1800),
(8, 1, "2021-08-01", 1800),
(9, 1, "2021-09-01", 1800),
(10, 1, "2021-10-01", 1800),
(11, 1, "2021-11-01", 1800),
(12, 1, "2021-12-01", 1800),
(13, 2, "2025-01-01", 1900),
(14, 2, "2025-02-01", 1900),
(15, 2, "2025-03-01", 1900),
(16, 2, "2025-04-01", 1900),
(17, 3, "2025-02-01", 2000),
(18, 3, "2025-03-01", 2000),
(19, 3, "2025-04-01", 2000);

--Creating sample data for the maintenance table:
INSERT INTO maintenance (id, propertyId, contractId, serviceDate, cost, serviceDescription)
VALUES
(1, 1, 1, "2021-10-10", 150.5, "Work on bathtub and sink because they were clogged."),
(2, 1, 1, "2021-11-22", 35.5, "Replacement of smoke-detector battery."),
(3, 2, 3, "2025-03-13", 50.5, "Replacement of lightbulbs for the kitchen and living room.");

--Query the views about rents collected so far and services done to the properties so far:
SELECT * FROM rent_collected;

SELECT * FROM services;
