# dictionary = A changeable, unordered collection of unique key

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'Brazil':'Brasilia',
            'Russia':'Moscow'}

#print(capitals['USA'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key, value)

capitals.update({'Germany':'Berlim'})
capitals.update({'USA':'Las Vegas'})

for key,value in capitals.items():
    print(key, value)

capitals.pop('USA')
#capitals.clear()

for key,value in capitals.items():
    print(key, value)