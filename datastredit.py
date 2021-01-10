import time
import pandas as pd
import numpy as np
with open('subset_elemets.txt') as f:
    subset_elements = f.read().split('\n')
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')
start = time.time()

verified_elements=set(subset_elements) & set(all_elements)
#verified_elements = [element for element in subset_elements if element in all_elements]

print(len(verified_elements))
print('Duration: {} seconds'.format(time.time() - start))