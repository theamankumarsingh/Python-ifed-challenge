def nearest_square(num):
    '''Returns a perfect square less than or equal to n.
    If n is negative, returns 0
    
    Parameters:
        num (int): Upper limit of perfect square (inclusive)
        
    Returns:
        int: Perfect number less than or equal to num'''
    if num<0:
        return 0 #returns 0 if n is negative
    return int(num**0.5)**2  #First rooting the number, then removing fractional part, and then squaring the number