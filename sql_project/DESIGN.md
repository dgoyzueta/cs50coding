# Design Document

By Daniel Goyzueta Saenz

Video overview: <(https://youtu.be/sJeq-E7WY2Y)>

## Scope

The purpose of my database is to facilitate the administration of properties as a landowner. This database
can be used to track properties that a person can get during his or her life. This properties may be put
to rent in order to get income. This is a simple model that makes it easy to track not only properties
but also the amount of income collected and the expenses you may have when doing fixes or maintenance to
the properties.

Within the scope of the database are the following entities:
    - Property: This entity tracks the properties you own.
    - Contract: This entity tracks the contracts signed by the renters for renting a property.
    - Rent: This entity tracks the rents that were paid by the renters.
    - Tenant: This entity tracks the list of persons that signed the contract and therefore are considered
              tenants. This entity can include one or more tenants who are part of the contract.
    - Maintenance: This entity tracks the list of services that were performed to maintain or repair the
              properties.

What is outside of the scope of this database are detailed addresses in the Property table and also foreign
addresses. The Contract table does not support saving entire documents such as PDF or WORD files. The Rent
table only records the payments done so this means that it does not include an scheduled payment. The Tenant
table contains only basic information to identify people so it does not include PII information such Social
Security Numbers, gender, and DOB. The Maintenance table includes basic information to register services
performed to the properties so it does not include detailed description of the services, just a basic
description of what was done.

## Functional Requirements

You can perform CRUD operationes in the database but they will be done by running SQL stataments directly on
the tables.

Beyond the scope of what a user should be able to do:
You can't scheduled payments in the future for renters so you won't be able to identify if a payments was done
late, you can only identify when the payments were done. To identify if payments were late, you should run
SELECT statement on the Rent table and compare the payment date with a particular date considered for payments
and that was part of the contract.

## Representation

Entities are captured in SQLite tables with the following schema:

### Entities

The database has the following tables and columns:

Property: This table has the following columns:
* `id` as an `integer` column containing the id of the property. This column is the primary Key.
* `description` as a `text` column with no NULL values having a description to the property such as the name of
   the condo, for example.
* `address` as a `text` column with no NULL values having the address of the property including
   number of street, street name and unit or apartment number if that is the case.
* `zipcode` as a `text` column with no NULL values. This only applies to US addresses.
* `state` as a `text` column with no NULL values. This only applies to US addresses.
* `bookValue` as a `numeric` column with no NULL values. This is the value used to calculate property taxes.
* `marketValue` as a `numeric` column with no NULL values. This is the current market value of the property.

Contract: This table has the following columns:
* `id` as an `integer` column having the id of the contract. This column is the primary key.
* `propertyId` as an `integer` column having the id of the property related to the contract. This is a foreign
   key.
* `startDate` as a `numeric` column with no NULL values. This is the beginning of the contract.
* `endDate` as a `numeric` column with accepted NULL values. This date is the end of the contract. This column
   can be NULL if the contract is still in place or active.
* `rentAmount` as a `numeric` column with no NULL values. The is the stipulated rent amount to be paid monthly.
* `status` as a `text` column with no NULL values. It accepts only the values "ACTIVE" (if the contract is
   still in use) or "CLOSED" (if the contract ended).

Tenant: This table has the following columns:
* `id` as an `integer` column. This is the id of the tenant. This column is the primary key.
* `contractId` as an `integer` column. This is the contract id and it is a foreign key.
* `firstName` as a `text` column with no NULL values. This has the first name of the tenant.
* `middleName` as a `text` column with NULLs accepted. This may have the middle name of the tenant.
* `lastName` as a `text` column with no NULL values. This has the last name of the tenant.
* `driverLicense` as a `text` column with no NULL values having the driver's license id, number or code of the
   tenant.

Rent: This table has the following columns:
* `id` as an `integer` column. This has the id of the rent that was paid. This is the primary key.
* `contractId` as an `integer` column having the id of the contract. This is a foreign key.
* `paymentDate` as a `numeric` column with no NULL values having the payment date of the rent.
* `amount` as a `numeric` column with no NULL values having the amount paid.

Maintenance: This table has the following columns:
* `id` as an `integer` column having the id of the service for maintenance requested. This is the primary key.
* `propertyId` as an `integer` column having the id of the property. This is a foreign key.
* `contractId` as an `integer` column having the id of the related contract. This is a foreign key.
* `serviceDate` as a `numeric` column with no NULL values having the service date.
* `cost` as a `numeric` column with no NULL values having the cost of the service for maintenance done.
* `serviceDescription` as a `text` column with no NULL values having the description of the service for
   maintenance that was performed.

### Relationships

Entity relationship diagram:

![ER Diagram](Properties_ERD.png)

As shown in the ER diagram, a property can have 0 or more contracts signed for its use as a rented property.
The contract can have 0 or more records for rent that were paid. Also, the contract can have 1 or more tenants
who are part of the contract. Finally, the contract can have 0 or more records for maintenance during its use.

## Optimizations

The database has indexes that were created to speed up searches on the database. The indexes are created for
the columns `description` and `address` in the `property` table, `lastName` in the `tenant` table, and
`serviceDescription` in the `maintenance` table. The idea is that you usually don't remember codes for records
and that is why columns that contain `TEXT` values can be used to locate the records of interest.

The database also has 2 views: One view, called `rent_collected`, can be used to list all the rents collected for
properties broken down by year of payment in descending order and showing the sum of rents per property and year of payment. The second view, called `services`, can be used to list all the maintenances done to the properties broken down by year of service in descending order showing the sum of cost of services done per property and
year of service.

## Limitations

This design does not allow to plan ahead rents to be collected for a given contract because it only records
payments done. Also, the database does not save entire contract documents such as PDF or WORD documents. Another
limitation of the database, is the granularity of information for addresses, tenants and services where the idea
is to get sufficient information to track what is going on with the property without getting lost in too many
details. A benefit of the database is the capacity to record what is relevant to manage the properties in an agile way without relying on spreadsheets.
