import requests as rq, sys
pokemon='golduck'
def check():
    try:
        res.raise_for_status()
    except Exception as exc:
        print('Error: '+exc)
        sys.exit(1)
#code
res=rq.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
check()
print(res.json()['types'][0]['type']['name'])

res=rq.get(res.json()['types'][0]['type']['url'])
check()
lst=res.json()['damage_relations']
for x in ['double_damage_from','half_damage_from']:
    for y in range(len(lst[x])):
        print(lst[x][y]['name'])

for x in ['double_damage_from']:
    for y in range(len(lst[x])):
        print('Type:'+lst[x][y]['name'])
        r=rq.get('https://pokeapi.co/api/v2/type/'+lst[x][y]['name']).json()['pokemon']
        check()
        for z in range(5):
            print(r[z]['pokemon']['name'])           
        print()
