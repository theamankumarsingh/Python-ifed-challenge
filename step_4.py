import time, pandas as pd, numpy as np  #importing necessary libraries
timestamp,subset_elements, all_elements=[],[],[] #global variables
def readNumList():
    '''Reads the files subset_elements.txt and all_elements.txt, which contains the subset elements and all elements respectively
    
    Parameters:
        None
    
    Returns:
        None'''
    global subset_elements,all_elements #making sure the vars are global here
    with open('subset_elemets.txt') as f:
        subset_elements = f.read().split('\n') #reading subset elements from file and storing in form of a list
    with open('all_elements.txt') as f:
        all_elements = f.read().split('\n') #reading all elements from file and storing in form of a list
def stopwatch():
    '''Captures the current time (a time stamp)
    
    Parameters:
        None
        
    Returns:
        None'''
    timestamp.append(time.time()) #append current time (in seconds) and appends it to timestamp which as all captured time (from unix epoch)
def getCommonNum(a,b):
    '''Returns the number of common elements between list a and b
    
    Paramters:
        a (list): First list of elements
        b (list): Second list of elements
        
    Returns:
        int: number of elements common to a and b'''
    return len(set(a) & set(b))  #uses & operator on sets to get a new set containing common element
if __name__ == "__main__":
    #main
    readNumList() #reading elements from the files
    stopwatch() #capturing first timestamp
    verified_elements=getCommonNum(subset_elements,all_elements) #getting number of common elements
    stopwatch() #capturing second timestamp
    print(verified_elements,'Duration: {} seconds'.format(timestamp[-1]-timestamp[-2]),sep='\n') #printing number of common elements, along with time taken to compute common elements