import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print(" ", "robot", "human")
for i in range(len(lst)):
    if lst[i] == 'robot':
        print(f"{i+1}   {1}   {0}")
    else:
        print(f"{i+1}   {0}   {1}")
