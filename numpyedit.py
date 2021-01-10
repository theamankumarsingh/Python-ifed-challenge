import time
import pandas as pd
import numpy as np
with open('subset_elemets.txt') as f:
    subset_elements = f.read().split('\n')
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')
start = time.time()
verified_elements=np.nonzero(np.isin(subset_elements, all_elements))
print(len(verified_elements[0]))
print('Duration: {} seconds'.format(time.time() - start))