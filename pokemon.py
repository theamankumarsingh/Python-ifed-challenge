import requests as rq, sys #imports
def check(res): #check for errors
    try:
        res.raise_for_status()
    except Exception as exc:
        print('Error: '+exc)
        sys.exit(1)
def checkPokemon(pokemon):
    '''Checks if the pokemon exists
    
    Parameters:
        pokemon (str): Name of pokemon
        
    Returns:
        bool: True if exists, else False'''
    res=rq.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
    try:
        res.raise_for_status()
    except:
        return False
    return True
def pokemonType(pokemon):
    '''Returns the type of the pokemon
    
    Parameters:
        pokemon (str): Name of pokemon
        
    Returns:
        str: Type of pokemon'''
    res=rq.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
    check(res)
    return res.json()['types'][0]['type']['name']
def pokemonAbilities(pokemon):
    '''Returns all abilities of the pokemon
    
    Parameters:
        pokemon (str): Name of pokemon
        
    Returns:
        list: A list of all abilities of the pokemon'''
    res=rq.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
    check(res)
    lst=res.json()['abilities']
    return [lst[i]['ability']['name'] for i in range(len(lst))]
def doubleDamageFrom(pokemon,count=5,random=True):
    '''Returns list of pokemons which can do double damage to the pokemon
    
    Parameters:
        pokemon (str): Name of pokemon
    
    Keyword Arguments:
        count (int): number of entries to return (default=5)
        random (bool): If the selection of entries would be random instead of linear (default=True)
        
    Returns:
        list: A list of all pokemons which can do double damage'''
    lst=doubleDamageType(pokemon)
    l=[]
    if random:
        i=0
        while True:
            for pos in range(len(lst)):
                r=rq.get('https://pokeapi.co/api/v2/type/'+lst[pos]).json()['pokemon']
                if i>=len(r):
                    continue
                if not count:
                    return l
                l.append(r[i]['pokemon']['name'])
                count-=1
            i+=1                           
    else:
        for pos in range(len(lst)):
            r=rq.get('https://pokeapi.co/api/v2/type/'+lst[pos]).json()['pokemon']
            for i in range(len(r)):
                if not count:
                    return l
                l.append(r[i]['pokemon']['name'])
                count-=1
def doubleDamageType(pokemon):
    '''Returns type of pokemons the pokemon is weak to
    
    Parameters:
        pokemon (str): Name of pokemon
        
    Returns:
        list: A list of types to which the pokemon is at a disadvantage'''
    res=rq.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
    check(res)
    res=rq.get(res.json()['types'][0]['type']['url'])
    check(res)
    lst=res.json()['damage_relations']['double_damage_from']
    l=[]
    for pos in range(len(lst)):
        l.append(lst[pos]['name'])
    return l