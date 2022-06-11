import math
import os
import random
import re
import sys

i=1

if __name__ == '__main__':
    N = int(input().strip())
    if N%2 != 0:
        print('Weird')
    elif (N>=2 and N<=5) and N%2 == 0:
        print('Not Weird') 
    elif (N>=6 and N<=20) and N%2 == 0:
        print('Weird')
    elif N>20 and N%2 == 0:
        print('Not Weird') 