# This code tests the orderedDict method used in the code
# Based on the given dictionary (dict1 in esting::test_dict) one may construct the
# ordered dictionary (b in Testing::test_dict) or finds it using orderedDict function (a in Testing::test_dict)
# we compare the two to ensure orderedDict works as it should be 
# the dictionary has pairs that could resemble key = departmentID and value = number of purchases

import collections
def orderedDict(dict1):
    #ordered dictionary based on keys
    od = collections.OrderedDict(sorted(dict1.items()))
    return od
    
import unittest
import collections

class Testing(unittest.TestCase):
    
    def test_dict(self):
        dict1 = {13: 1, 3: 1, 4: 0, 12: 0, 16: 0}
        
        # ordered dictionary based on dict1
        a = orderedDict(dict1)
            
        # known ordered dictionary based on Dict1 (manually constructed)
        b = {3: 1, 4: 0, 12: 0, 13: 1, 16: 0}
        
        self.assertEqual(a, b)
              
    

if __name__ == '__main__':
    unittest.main()  
