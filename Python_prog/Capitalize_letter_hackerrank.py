#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    #return print(list(s))
    for i in s[:].split():
        s = s.replace(i,i.capitalize())

    return s

if __name__ == '__main__':


    s = input()

    result = solve(s)
    print(result)


