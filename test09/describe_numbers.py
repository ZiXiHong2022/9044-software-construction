#!/usr/bin/env python3

import sys
import statistics
import math


arg = list(map(int, sys.argv[1:]))


count = len(arg)
unique = len(set(arg))
minimum = min(arg)
maximum = max(arg)
mean = statistics.mean(arg)
median = statistics.median(arg)
mode = statistics.multimode(arg)[0] 
total_sum = sum(arg)
product = math.prod(arg)  


print(f"count={count}")
print(f"unique={unique}")
print(f"minimum={minimum}")
print(f"maximum={maximum}")
print(f"mean={mean}")
print(f"median={median}")
print(f"mode={mode}")
print(f"sum={total_sum}")
print(f"product={product}")





    






