# hash table function: colomn index1 of table1 and colomn index2 of table2 point to
# an identical value and can be inner-joined. 
# this is based on hash join. To see the details and psuedo code please refer to ReadME
from collections import defaultdict
 
def hashJoin(table1, index1, table2, index2):
    h = defaultdict(list)
    # hash phase
    for s in table1:
        h[s[index1]].append(s)
    # join phase
    return [s+r[1:] for r in table2 for s in h[r[index2]]]

# a function to order dictionary dict1 based on key
# this is to facilitate writing in ascending order; for other types of sorting, the arguments should be adjusted
import collections
def orderedDict(dict1):
    #ordered dictionary based on keys
    od = collections.OrderedDict(sorted(dict1.items()))
    return od


  #read csv files and convert to desired data type (list of list)
import csv
with open('./input/products.csv') as prod_test:
    table1 = list(csv.reader(prod_test,delimiter=','))
    # get rid of header
    del table1[0]
    # convert strings (as output of csvread) to integer
    for row in table1:
        row[0] = int(row[0])
        row[2] = int(row[2])
        row[3] = int(row[3]) 

        

with open('./input/order_products.csv') as order_test:
    table2 = list(csv.reader(order_test,delimiter=','))
    # get rid of header
    del table2[0]
    # convert strings (as output of csvread) to integer
    for row in table2:
        row[0] = int(row[0])
        row[1] = int(row[1])
        row[2] = int(row[2])
        row[3] = int(row[3]) 
        


# inner-join the two tables; results is a list
# the order is such that the first argument is that of the orders and the second argument is for the products
# the 2nd and fourth arguments are, respectively, the number of colomn for which the common value for inner join
# exists
# in this challenge rProdID1 = 0: i.e. the first colomn of products is productID (common colomn)
# in this challenge rProdID2 = 0: i.e. the first colomn of products is productID (common colomn)
rProdID1=0;rProdID2=1
results = hashJoin(table1, rProdID1, table2, rProdID2)



# deptNoNumber is the number of products ordered at each department
# colomn rDeptIDJoin=3 corresponds to the department ID in the joined table
# CAUTION: if the format of the data is altered the number of colomn should be adjusted
deptNoNumber = {}
rDeptIDJoin=3
for res in results:
    # the following ensures if no item is purchased, the department is not in deptNoNumber
    if res[rDeptIDJoin] not in deptNoNumber:
        deptNoNumber[res[rDeptIDJoin]] = 1
    else:
        deptNoNumber[res[rDeptIDJoin]] += 1
        
        


# an ordered dictionary showing the No. of purchaes for each depatment
NoOrders = orderedDict(deptNoNumber)


# firstTimeNumber is the number of times an item is purchased for each department based on reordered label
# i.e. colomn reorered of joined table here rReOrderedJoin=6
# rDeptIDJoin is defined above
# CAUTION: if the format of the data is altered, r1 and r2 below should be adjusted
firstTimeNumber = {}
rReOrderedJoin = 6
for res in results:
    # if reordered or res[6] is not 0 (1) it has been purchased before so we don't count the productID
    if res[rReOrderedJoin] != 0:
        continue
    # the following ensures if no item is purchased, the department is not in firstTimeNumber
    if res[rDeptIDJoin] not in firstTimeNumber:
        firstTimeNumber[res[rDeptIDJoin]] = 1
    else:
        firstTimeNumber[res[rDeptIDJoin]] += 1
        
        

# to ensure an 0 is assigned to all departments that has no member in firstTimeNumber dictionary
# such that firstOrders and NoOrders have the same number of key.value pairs
firstOrders=firstTimeNumber
for r in NoOrders.keys():
    if r not in firstTimeNumber.keys():
        firstOrders[r]=0
firstOrders = orderedDict(firstOrders)



# write the results in csv format based on given headers in ascending order based on deptID
# the result is saved as report.csv
# the first colomn is deptID as the key for NoOrders (ascending order)
# the second colomn is the value i.e. number of orders, for deptID
# the third colomn is the value i.e. i.e. number of times ordered for the first time for deptID
# the fourth colomn is the percentage of the thirs to the second colomn written in two decimal points
with open('./output/report.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["department_id", "number_of_orders","number_of_first_orders","percentage"])
    for key in NoOrders.keys():
        f.write("%d,%d,%d,%0.2f\n"%(key,NoOrders[key],firstOrders[key],float(firstOrders[key]/NoOrders[key])))
