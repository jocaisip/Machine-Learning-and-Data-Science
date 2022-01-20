# Shopify Technical Challenge Submission

## Q1: 

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis.

Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. What metric would you report for this dataset? What is its value?

### Read dataset
![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/1.png)


<br/>

### Check if the dataset contains null values
![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/2.png)

No null values are present in the dataset, so we can proceed.

<br/>

### Calculating the AOV and count of values for Total Items
![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/3.png)

### Analyzing the AOV
By simply calculating the mean of order_amount, the AOV returned is 3,145, which is very high.

For the price of regular sneakers, having an AOV of $3,145 across all shops is peculiar unless they are sold in bulk. But this is not the case since most of the orders only have 1 or 2 items. Let's look deeper into the numbers of each shop.

<br/>


![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/4.png)

### Analyzing performance by shop
We calculate the order_amount by shop and sort them by the highest amount, and add the amount per item by dividing total items by order amount. Here we see that two shops, shop 42 and 78, have significantly higher order amounts than the rest. Shop 42 also seems to be selling exceedingly well, with 34,063 total items sold. Must be a very popular model.

On the other hand, shop 78 sold fewer items than the other shops but the order_amount of all the items is much higher. We can see this is due to them having the highest amount per item, at $25,725 each.

With these extraordinary figures, the order amounts from shop 42 and 78 skewed the value of AOV and should be removed from the calculation of AOV as they are significant outliers.

<br/>

### Metric: AOV by Segment
Not all sneaker shops are made equal, and since each shop sells only one model, they certainly aren't. A better way of generating AOV in this case is to look at the AOV by segment. Here we will look at the AOV by shop and the AOV by user.

![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/5.png)
![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/Shop_AOV.png)

We grouped by shop and calculated the average values for each. As expected, 42 and 78 have the highest AOV, contributing to the overall AOV of all shops. From the 10 top sneaker shops, only shop 42 has average items above 2 and actually has 667 average items, so it most likely sells sneakers in bulk instead of individually.

<br/>


![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/6.png)
![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/User_AOV.png)

Grouping by users, we see some interesting observations. User 607 have both the highest AOV and average items, with an average order of 2000 items and AOV of $704,000. With this kind of order volume, this customer is likely a reseller who buys in bulk and is not a typical customer.

The next users seem to be a high-end customers who purchase expensive sneakers, given an AOV of thousands of dollars for an average of 2 items. From these figures we can look at AOV from the customer perspective and identify different groups from high end customers, enterprise, and regular customers and further cluster them for analysis.

<br/>

![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/7.png)
![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/CumPerc_AOV.png)

Going back to AOV by shops segment, we calculate the cumulative percentage of each shop's AOV to the overall AOV in this pareto chart. From the chart we see that shop 42 and 78 together contribute over 90% of the AOV. With these values in the calculation, the original AOV does not accurately represent majority of the shops.
<br/>

### Conclusion
A good overall AOV metric would look at excluding the shops 78, 42, and user 607 as outliers, however, I propose a better metric would be AOV by segment. In AOV by segment, we have a clearer picture of the performance of the shops and type of sneaker models that are high performing and those that are not performing as well. Additionally, average order items give an indication of performance by volume, which will be more suited for shops that have volume targets where average order items. Moving forward, further analysis can be conducted on shops that sell sneakers in certain price ranges and the type of customers it attracts to determine other key metrics that correspond to them.

<br/>


## Q2: 

### 1. How many orders were shipped by Speedy Express in total?
<br/>
SELECT Count(OrderID) as Speedy_Express_Shipments<br/>
FROM Orders<br/>
JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID<br/>
WHERE ShipperName = 'Speedy Express';<br/>
<br/>

![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/SQL%20Q1.png)

### Speedy Express shipped 54 total orders.
<br/>

### 2. What is the last name of the employee with the most orders?
<br/>
SELECT Count(OrderID) as Order_Count, LastName as Employee_LastName<br/>
FROM Orders<br/>
JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID<br/>
GROUP BY LastName<br/>
ORDER BY Order_Count DESC;<br/>
<br/>

![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/SQL%20Q2.png)

### Peacock is the last name of the employee with the most orders.
<br/>

### 3. What product was ordered the most by customers in Germany?
<br/>
SELECT Count(Products.ProductID) as Product_Count, ProductName<br/>
FROM Products<br/>
JOIN OrderDetails ON OrderDetails.ProductID = Products.ProductID<br/>
JOIN Orders ON Orders.OrderID = OrderDetails.OrderID<br/>
JOIN Customers ON Customers.CustomerID = Orders.CustomerID<br/>
WHERE Country = 'Germany'<br/>
GROUP BY ProductName<br/>
ORDER BY Product_Count DESC;<br/>
<br/>

![Capture](https://raw.githubusercontent.com/jocaisip/Machine-Learning-and-Data-Science/main/Shopify%20Technical%20Challenge/Images/SQL%20Q3.png)

### Gorgonzola Telino is the product that customers in Germany ordered most.
