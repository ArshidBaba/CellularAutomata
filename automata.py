# import numpy as np
# a = np.arange(15).reshape(3, 5)
import time
cells = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
# newcells = cells.copy()
generation = int(input("Enter the number of generations: "))
ruleset = [0,1,0,1,1,0,1,0]

def rules(a, b, c):
    if a == 1 and b == 1 and c == 1: return ruleset[0]
    elif a == 1 and b == 1 and c == 0: return ruleset[1]
    elif a == 1 and b == 0 and c == 1: return ruleset[2]
    elif a == 1 and b == 0 and c == 0: return ruleset[3]
    elif a == 0 and b == 1 and c == 1: return ruleset[4]
    elif a == 0 and b == 1 and c == 0: return ruleset[5]
    elif a == 0 and b == 0 and c == 1: return ruleset[6]
    elif a == 0 and b == 0 and c == 0: return ruleset[7]
    return 0

for g in range(generation):
    newcells = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(cells)
    time.sleep(2)    
    for i in range(1,len(cells)-1):
        left = cells[i-1]
        middle = cells[i]
        right = cells[i+1]
        newcells[i] = rules(left,middle,right)
    cells = newcells
    
    
    
# generation += 1

  
