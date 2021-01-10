import requests as rq, sys
def check(res): #check for errors
    try:
        res.raise_for_status()
    except Exception as exc:
        print('Error: '+exc)
        sys.exit(1)
def ability(pokemon):
    '''Returns all abilities of the pokemon
    
    Parameters:
        pokemon (str): Name of pokemon
        
    Returns:
        list: A list of all abilities of the pokemon'''
    res=rq.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
    check(res)
    lst=res.json()['abilities']
    return [lst[i]['ability']['name'] for i in range(len(lst))]