-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

--It represents the properties that a person can have for administrative purposes.
CREATE TABLE property (
    "id" integer,
    "description" text NOT NULL,
    "address" text NOT NULL,
    "zipcode" text NOT NULL,
    "state" text NOT NULL,
    "bookValue" numeric NOT NULL,
    "marketValue" numeric NOT NULL,
    PRIMARY KEY("id")
);

--It represents the contracts that a property can have with tenants if the property is rented.
--The status of the contract can be ACTIVE(signed), or CLOSED(the contract ended).
CREATE TABLE contract (
    "id" integer,
    "propertyId" integer,
    "startDate" numeric NOT NULL,
    "endDate" numeric NULL,
    "rentAmount" numeric NOT NULL,
    "status" text NOT NULL CHECK("status" IN ("ACTIVE", "CLOSED")),
    PRIMARY KEY("id"),
    FOREIGN KEY("propertyId") REFERENCES "property"("id")
);

--It represents the list of tenants that are part of the contract when they rent a property I administer.
CREATE TABLE tenant (
    "id" integer,
    "contractId" integer,
    "firstName" text NOT NULL,
    "middleName" text,
    "lastName" text NOT NULL,
    "driverLicense" text NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("contractId") REFERENCES "contract"("id")
);

--It represents the payments for rent for a particular contract.
CREATE TABLE rent (
    "id" integer,
    "contractId" integer,
    "paymentDate" numeric NOT NULL,
    "amount" numeric NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("contractId") REFERENCES "contract"("id")
);

--It represents the services for maintenance I hired for a given property and tenant.
CREATE TABLE maintenance (
    "id" integer,
    "propertyId" integer,
    "contractId" integer,
    "serviceDate" numeric NOT NULL,
    "cost" numeric NOT NULL,
    "serviceDescription" text NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("propertyId") REFERENCES "property"("id"),
    FOREIGN KEY("contractId") REFERENCES "contract"("id")
);


-- Create indexes to speed common searches
CREATE INDEX "property_search_1" ON "property" ("description");
CREATE INDEX "property_search_2" ON "property" ("address");
CREATE INDEX "tenant_search" ON "tenant" ("lastName");
CREATE INDEX "maintenance_search" ON "maintenance" ("serviceDescription");


--Create view to get the sum of payments for rent for each property across the years:
CREATE VIEW rent_collected AS
SELECT p.description as property_name,
       strftime('%Y', r.paymentDate) as year,
       sum(r.amount) as total_amount
FROM property p
JOIN contract c ON p.id = c.propertyId
JOIN rent r ON c.id = r.contractId
GROUP BY property_name, year
ORDER BY property_name, year DESC;

--Create view to get the total cost per service year of maintenance for active contracts:
CREATE VIEW services AS
SELECT p.description as property_name,
       strftime('%Y', m.serviceDate) as service_year,
       sum(m.cost) as total_cost
FROM property p
JOIN contract c ON p.id = c.propertyId
JOIN maintenance m ON c.id = m.contractId
WHERE c.status = 'ACTIVE'
GROUP BY property_name, service_year
ORDER BY property_name, service_year DESC;
