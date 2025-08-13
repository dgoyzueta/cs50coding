SELECT p.description as property_name,
       strftime('%Y', r.paymentDate) as year,
       sum(r.amount) as total_amount
FROM property p
JOIN contract c ON p.id = c.propertyId
JOIN rent r ON c.id = r.contractId
GROUP BY property_name, year
ORDER BY property_name, year DESC;

SELECT p.description as property_name,
       strftime('%Y', m.serviceDate) as service_year,
       sum(m.cost) as total_cost
FROM property p
JOIN contract c ON p.id = c.propertyId
JOIN maintenance m ON c.id = m.contractId
WHERE c.status = 'ACTIVE'
GROUP BY property_name, service_year
ORDER BY property_name, service_year DESC;
