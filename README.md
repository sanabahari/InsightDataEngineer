# InsightDataEngineer: Purchase-Analytics code challenge

## Table of Contents
1. [Problem](README.md#problem)
1. [Running the code](README.md#running-the-code)
1. [Code verification I](README.md#Code-verification:-test-files)
1. [Code verification II](README.md#Code-verification:-unit-test)
1. [Programming practices](README.md#Programming-practices)
1. [Algorithm](README.md#algorithm)

## Problem

For this problem, we solved the challenge based on Instacart [dataset](https://www.instacart.com/datasets/grocery-shopping-2017) containing 3 million Instacart orders using Python3.
 

The task was to determine, for each department, the number of time a product was purchased, and the number of times a product was requested for the first time and a ratio of those two numbers.

To show the scalability of the code we ran the code on a desktop computer based on the train data (more than 3M data points), which was completed less than few minutes. 

This code does not use any external libraries such as pandas or numpy. The standard libraries used are `collections` and `csv`.

## Running the code

1. copy the input files as products.csv and order_products.csv. Please note, the structure should be as the format exlpained in the `Code verification: test files` section. If the dataset is altered slightly, e.g. only few colomns are added removed, please update the constants exlpained in `Programming practices` section

2. The input files are located in `/input/products.csv` and `/input/order_products.csv`. The former is products order table and the latter is the product table.

3. Once the inpute files are located, one should run the bash file as `.\run_sh`, which reades the driver code in the `/src/` directory.

4. The generated output is now located in `/output/report.csv`  and has the following form (this example is only for test data)

```
department_id,number_of_orders,number_of_first_orders,percentage
3,2,1,0.50
4,2,0,0.00
12,1,0,0.00
13,2,1,0.50
16,2,0,0.00
```
for the given input provided by Insight. Our code writes the data as csv in the requested format: the first column is sorted in an ascending fashion, the code would not `department_id` if `number_of_orders` is `0`, and the `percentage` is rounded to the second decimal.

Consistent with Instacart and Insight request, statistics are defined as:
`number_of_orders`. How many times was a product requested from this department? (If the same product was ordered multiple times, we count it as multiple requests)

`number_of_first_orders`. How many of those requests contain products ordered for the first time?

`percentage`. What is the percentage of requests containing products ordered for the first time compared with the total number of requests for products from that department? (e.g., `number_of_first_orders` divided by `number_of_orders`)

## Code verification: test files

To test the code, we generated synthesized data, which are located in `/insight_testsuite/tests/`. The data itself is generated by a code that takes the large dataset, selects given number of rows randomly from order_prouct table, locates the corresponding department IDs in the products table, and finally generates the products table based on the given number of rows (which is not necessarily equal to that of the order_prouct table). This simple method ensures the test data has non-zero number of products for the selected departments; although the set of products may not necessarily span over all departments. 

Two test files are generated:

`test1`. This is the original test provided by Insight. We did not change the data; however, the contents of report.csv is included only to verify

```
department_id,number_of_orders,number_of_first_orders,percentage
3,2,1,0.50
4,2,0,0.00
12,1,0,0.00
13,2,1,0.50
16,2,0,0.00
```

`Sana_test` is manually generated test file. The input has 10 rows for both orders and products.
products.csv structure:

```
product_id,product_name,aisle_id,department_id
10060,Original BBQ Sauce,72,13
11930,Sea Salt Baked Lentil Chips,107,19
19366,Sprouted Organic Cinnamon Raisin English Muffins,93,3
20588,Vegan Buttery Sticks,91,16
24852,Banana,24,4
32989,Mighty 4 Purple Carrot Blackberry Quinoa & Greek Yogurt Tots Snack,92,18
38747,Kettle Cooked Sea Salt & Vinegar Potato Chips,107,19
38996,Grape Tomatoes,83,4
40825,Havarti Cheese Slices,21,16
46667,Organic Ginger Root,83,4
```
and order_products.csv :

```
order_id,product_id,add_to_cart_order,reordered
461376,10060,13,0
2480413,38747,4,1
2496644,20588,2,1
1480122,24852,1,0
205775,19366,1,1
2465982,40825,7,0
1881132,46667,2,1
147534,32989,4,1
3127765,11930,6,1
2265390,38996,5,0
```

and the output, therefore, is given by

```
department_id,number_of_orders,number_of_first_orders2,percentage
3,1,0,0.00
4,3,2,0.67
13,1,1,1.00
16,2,1,0.50
18,1,0,0.00
19,2,0,0.00
```



## Code verification: unit test

We generated two unit tests code to verify the main functions used in the code. Two main functions that are tested are test_hashJoin.py, which tests the function hashJoin and test_orderedDict.py, which tests the function orderedDict. The details of the hashJoin function is given below.

##  Programming practices

* We used numerous comments in the source file, xxx, to explain each part of the code. 
* We did our best to name the variables in a meaningful manner.
* We did not hardwire the code using the numbers. Instead we defined constant variables, defined below, to streamline the process of transferring the code to another potentially similar data with comparable schema/structure

 list of constants:
 
 * rProdID1: productID colomn in products.csv
 * rProdID2: productID colomn in order_products.csv
 * rReOrderedJoin: reordred colomn in the joined table
 * rDeptIDJoin: department ID colomn in the joined table


## Algorithm

The steps to solve the problem can be seen in the form of the following algorithm:

1. Extract the data from csv files. As the files would be in string, we convert the appropriate colomns into integer before analysis. Table 1 is for products.csv and Table 2 is for products_order.csv.
2. The common column between Table 1 and Table 2 is used, employing hash function `hashJoin`, to generate a joined table called results.
3. We then calculate the number of times an item of a certain department is purchased. Care is taken to not include the departments that have no items for a given input. Needless to say, for the full data, there is no empty department.
4. We then use the function `orderedDict` to sort thedata in terms of department ID. This is done because we later need to write the output in ascending fashion. The outcome is an ordered dictionary called NoOrders, which contains the number of purchases for non-empty departments.
5. We then construct the dictionary firstTimeNumber to contain the departments and the number of items purchased for the first time based on the column reordered in order_products.csv. 
6. Since we need to write 0 if a department contains non-zero number of purchases but has no first-time one, we exploit again the key/value structure to assign 0 to those departments appear in dictionary NoOrders but not firstTimeNumber. We finally order the latter dictionary under the name firstOrders. 
7. Finally, we write the outcome in the required format csv.

Also, a quick note, in a form of a psuedo code for hash joint function:

`let table 1 = the larger input table (order_products.csv in our project) )`

`let table 2 = the smaller input table (products.csv in our project)`

`let rProdID1 = the join column ID of table 1`

`let rProdID2 = the join column ID of table 2`

`let h = a multimap for mapping from single values to multiple rows of table 2 (constructed as an empty one)`

`let results = the output table (starts out empty)`

for each row `b` in table 2:

   place `b` in multimap h under key b(rProdID2)

for each row `a` in table 1:

   for each row `b` in multimap h under key a(rProdID1):
   
      let c = the concatenation of row a and row `b`
      
      place row c in table results


