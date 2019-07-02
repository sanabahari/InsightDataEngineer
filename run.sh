#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
#python ./src/purchase_analytics.py ./input/order_products.csv ./input/products.csv ./output/report.csv

# run the main code
python3 ./src/Sana_Instacart_Analytics.py

# run the testunit for method hashJoin
python3 ./src/test_hashJoin.py

# run the testunit for method orderedDict
python3 ./src/test_orderedDict.py
