#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # [derive mapper output key values]
    line = line.strip()
    vin, make_yr = line.split(" ",1)
    print (make_yr + '\t' + str(1))