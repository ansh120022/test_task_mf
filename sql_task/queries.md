Navigate https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

### test 1
``` sql
SELECT CASE
           WHEN
                  (SELECT address
                   FROM customers
                   WHERE ContactName = 'Giovanni Rovelli') = 'Via Ludovico il Moro 22' THEN 'passed'
           ELSE 'failed'
       END AS test_giovanni_address;
```
### test 2
``` sql
SELECT CASE
           WHEN
                  (SELECT count(*)
                   FROM customers
                   WHERE city='London') = 6 THEN 'passed'
           ELSE 'failed'
       END AS test_customers_from_london;
``` 

### test 3
``` sql
INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Test Customer', 'Test city', 'Test country');

SELECT CASE
           WHEN
                  (SELECT count(*)
                   FROM Customers
                   WHERE CustomerName='Test Customer'
                     AND city='Test city'
                     AND country='Test country') > 0 THEN 'passed'
           ELSE 'failed'
       END AS test_add_customer;
``` 