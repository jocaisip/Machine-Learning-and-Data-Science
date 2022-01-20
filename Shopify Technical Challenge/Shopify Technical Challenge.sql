# 1. How many orders were shipped by Speedy Express in total?
SELECT Count(OrderID) as Speedy_Express_Shipments
FROM Orders
JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID
WHERE ShipperName = 'Speedy Express';
# A: Speedy Express shipped 54 total orders.


# 2. What is the last name of the employee with the most orders?
SELECT Count(OrderID) as Order_Count, LastName as Employee_LastName
FROM Orders
JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY LastName
ORDER BY Order_Count DESC;
# A: Peacock is the last name of the employee with the most orders.


# 3. What product was ordered the most by customers in Germany?
SELECT Count(Products.ProductID) as Product_Count, ProductName
FROM Products
JOIN OrderDetails ON OrderDetails.ProductID = Products.ProductID
JOIN Orders ON Orders.OrderID = OrderDetails.OrderID
JOIN Customers ON Customers.CustomerID = Orders.CustomerID
WHERE Country = 'Germany'
GROUP BY ProductName
ORDER BY Product_Count DESC;
# A: Gorgonzola Telino is the product that customers in Germany ordered most.

