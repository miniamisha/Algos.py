#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findOdd' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY series as parameter.
#

def findOdd(series):
    print(series)

if __name__ == '__main__':
  
  

    series_count = int(input().strip())

    series = []

    for _ in range(series_count):
        series_item = input()
        series.append(series_item)

    result = findOdd(series)
    print(result)

 
