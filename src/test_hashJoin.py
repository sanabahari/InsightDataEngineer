# This code tests the core funciton used in the code i.e. hashJoin
# Based on the products and order_products tables (table1 and table2 in Testing::test_table) 
# given as input for the test problem one may construct the join table (b in Testing::test_table)
# we compare the two to ensure hashJoin works as it should be 


from collections import defaultdict
def hashJoin(table1,index1, table2, index2):
        h = defaultdict(list)
        # hash phase
        for s in table1:
            h[s[index1]].append(s)
        # join phase
        return [s+r[1:] for r in table2 for s in h[r[index2]]]
 
 
import unittest
from collections import defaultdict    

class Testing(unittest.TestCase):
    
    def test_table(self):
        table1 = [[9327, 'Garlic Powder', 104, 13], 
                  [17461, 'Air Chilled Organic Boneless Skinless Chicken Breasts', 35, 12], 
                  [17668, 'Unsweetened Chocolate Almond Breeze Almond Milk', 91, 16], 
                  [28985, 'Michigan Organic Kale', 83, 4], 
                  [32665, 'Organic Ezekiel 49 Bread Cinnamon Raisin', 112, 3], 
                  [33120, 'Organic Egg Whites', 86, 16], 
                  [45918, 'Coconut Butter', 19, 13], 
                  [46667, 'Organic Ginger Root', 83, 4], 
                  [46842, 'Plain Pre-Sliced Bagels', 93, 3]]
    
        table2 = [[2, 33120, 1, 1], 
                  [2, 28985, 2, 1], 
                  [2, 9327, 3, 0], 
                  [2, 45918, 4, 1], 
                  [3, 17668, 1, 1], 
                  [3, 46667, 2, 1], 
                  [3, 17461, 4, 1], 
                  [3, 32665, 3, 1], 
                  [4, 46842, 1, 0]]
        
        # hash join table for the given input using the method hashJoin
        a = hashJoin(table1, 0, table2, 1)
            
        # known inner join table for the given input (manually constructed)
        b = [[33120, 'Organic Egg Whites', 86, 16, 33120, 1, 1], 
             [28985, 'Michigan Organic Kale', 83, 4, 28985, 2, 1], 
             [9327, 'Garlic Powder', 104, 13, 9327, 3, 0], 
             [45918, 'Coconut Butter', 19, 13, 45918, 4, 1], 
             [17668, 'Unsweetened Chocolate Almond Breeze Almond Milk', 91, 16, 17668, 1, 1], 
             [46667, 'Organic Ginger Root', 83, 4, 46667, 2, 1], 
             [17461, 'Air Chilled Organic Boneless Skinless Chicken Breasts', 35, 12, 17461, 4, 1], 
             [32665, 'Organic Ezekiel 49 Bread Cinnamon Raisin', 112, 3, 32665, 3, 1], 
             [46842, 'Plain Pre-Sliced Bagels', 93, 3, 46842, 1, 0]]
        
        self.assertEqual(a, b)
            
        
           

if __name__ == '__main__':
    unittest.main() 

