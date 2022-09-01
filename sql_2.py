from sql import create_connection, select_query


connection = create_connection('northwind.db')

# Вибрати усіх клієнтів
customers = """
select * from Customers
"""
# for item in select_query(connection, customers):
#     print(item)

# Вибрати усіх клієнтів, але тільки ім'я та місто
customers_name_city = """
select ContactName, City from Customers
"""
# for item in select_query(connection, customers_name_city):
#     print(item)

# Вибрати усі міста звідки клієнти але без повтореннь
customers_unique_cities = """
select distinct City from Customers;
"""
# for item in select_query(connection, customers_unique_cities):
#     print(item)

# Вибрати усі міста та країни звідки клієнти але без повтореннь
customers_unique_cities_countries = """
select distinct City, Country from Customers;
"""
# for item in select_query(connection, customers_unique_cities_countries):
#     print(item)

# Порахувати кількість замовників
customers_count = """
select count(*) from Customers;
"""
# for item in select_query(connection, customers_count):
#     print(item)

# Порахувати кількість унікальних країн з яких наші клієнти
customer_countries_count = """
select count(distinct Country) from Customers;
"""
# for item in select_query(connection, customer_countries_count):
#     print(item)

###############################################################################
# Вибрати усі замовлення з країн Франція, Австрія, Іспанія
orders_from_countries = """
select * from Orders where ShipCountry in ('France', 'Austria', 'Spain');
"""
# for item in select_query(connection, orders_from_countries):
#     print(item)

# Вибрати усі замовлення та відсортувати по даті замовлення по зменшенню та по
# даті відгрузки по зростанню
orders_sorted = """
select * from Orders order by OrderDate desc , ShippedDate asc;
"""
# for item in select_query(connection, orders_sorted):
#     print(item)

# Вибрати мінімальну ціну серед продуктів яких не менше 30 одиниць у продажу
min_product_price = """
select min(UnitPrice) from Products where Products.UnitsInStock > 30;
"""
# for item in select_query(connection, min_product_price):
#     print(item)

# Знайти середню кількість днів, що йде на формування замовлень з США
average_usa_order_days = """
select avg(JULIANDAY(Orders.ShippedDate) - JULIANDAY(Orders.OrderDate)) 
from Orders where ShipCountry = 'USA';
"""
# for item in select_query(connection, average_usa_order_days):
#     print(item)

# Порахувати загальну суму на яку маємо товарів
products_sum = """
select round(sum(UnitPrice * UnitsInStock), 2) from Products;
"""
# for item in select_query(connection, products_sum):
#     print(item)

# Вибрати всі замовлення у яких країна починається з U
orders_from_U = """
select * from Orders where ShipCountry like 'U%';
"""
# for item in select_query(connection, orders_from_U):
#     print(item)

# Вибрати замовлення, що мають бути відвантажені в країну, що починається з N
# відсортувати по вазі по зменшенню та вивести тільки перші 10 результатів
orders_from_N = """
select OrderID, Freight, ShipCountry from Orders 
where ShipCountry like 'N%' order by Freight desc limit 10;
"""
# for item in select_query(connection, orders_from_N):
#     print(item)

# Знайти замовників у яких ми не маємо телефонів
customers_no_phone = """
select CustomerID, ContactTitle, CompanyName, ContactName from Customers 
where Phone is null;
"""
# for item in select_query(connection, customers_no_phone):
#     print(item)

# Порахувати клієнтів, що мають телефон
customers_with_phone_count = """
select count(*) from Customers where Phone is not null;
"""
# for item in select_query(connection, customers_with_phone_count):
#     print(item)

# Порахувати постачальників з кожної країни, відсортувати по кількості
# по зменшенню
suppliers_from_country_count = """
select Country,  count(*) from Suppliers 
GROUP BY Country order by count(*) desc ;
"""
# for item in select_query(connection, suppliers_from_country_count):
#     print(item)

# Порахувати сумарну вагу замовлень в яких відомий регіон
# потім відфільтрувати тільки ті в яких вага більше 2750 та відсортувати
# по зменшенню
orders_sum_freight = """
select ShipCountry, sum(Freight) from Orders
where ShipRegion is not null 
group by ShipCountry
having sum(Freight) > 2750
order by sum(Freight) desc;
"""
# for item in select_query(connection, orders_sum_freight):
#     print(item)

# Вибрати унікальні країни замовників та постачальників та відсортувати
# по збільшенню
unique_suppliers_customers_countries = """
select Country from Customers
UNION
select Country from Suppliers
order by Country;
"""
# Показати різницю з UNION ALL
# for item in select_query(connection, unique_suppliers_customers_countries):
#     print(item)

# Вибрати країни з яких замовники, постачальники та робітники
countries_employees_suppliers_customers = """
select Country from Customers
INTERSECT 
select Country from Suppliers
INTERSECT 
select Country from Employees
order by Country;
"""
# for item in select_query(connection, countries_employees_suppliers_customers):
#     print(item)

# Вибрати країни з яких замовники, постачальники але не робітники
countries_not_employees_suppliers_customers = """
select Country from Customers
INTERSECT 
select Country from Suppliers
EXCEPT 
select Country from Employees
order by Country;
"""
# for item in select_query(connection, countries_not_employees_suppliers_customers):
#     print(item)

###############################################################################
# Знайти замовників та співробітників, що обслуговують їх замовлення
# вони мають бути з Лондона і ті і ті, а доставка має йти компанією
# доставки Speedy Express
# вивести ім'я прізвище робітника та компанії замовника
customer_company_employee = """
select Customers.CompanyName, 
Employees.FirstName || ' ' || Employees.LastName 
from Orders
join Customers using (CustomerID)
join Employees using (EmployeeID)
join Shippers on Orders.ShipVia = Shippers.ShipperID
where Customers.City = 'London' 
      and Employees.City = 'London'
      and Shippers.CompanyName = 'Speedy Express';
"""
# for item in select_query(connection, customer_company_employee):
#     print(item)

# Знайти замовників, що не зробили жодного замовлення
customers_with_no_orders = """
select ContactName, OrderID from Customers
LEFT JOIN Orders using (CustomerID)
where OrderID is null
order by ContactName
"""
# Показати що буде просто з JOIN
# for item in select_query(connection, customers_with_no_orders):
#     print(item)

###############################################################################
# Subqueries
# Вивести усі унікальні товари яких замовлено рівно 10 одиниць
products_ordered_ten = """
select ProductName from Products
where ProductID in (
    select ProductID from "Order Details" where Quantity = 10
) 
"""
# for item in select_query(connection, products_ordered_ten):
#     print(item)

products_ordered_ten_join = """
select distinct ProductName, Quantity
from Products
join "Order Details" "O D" on Products.ProductID = "O D".ProductID
where Quantity = 10;
"""
for item in select_query(connection, products_ordered_ten_join):
    print(item)
