a=25
b=4
c=a+b
d=3.14
Version_year=("latest")
print(c) #donne 29 
c=a*b
print(c) #donne 100 car c prends la nouvelle valeur suite à nouvelle assignation
c=a%b  # on cherche le modulo 4 de 25 (reste entier de la division)
print( c ) # au passage Python se fout complétement des espaces :-)
### type de variables
#ceci est une liste
O_liste=["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi","gromanche"]
print(O_liste)
#On peut modifier une liste 
O_liste=["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi","dimanche"]
print(O_liste)
# ceci est un tuple
O_tuple=("janvier", "mars", "février", )
print(O_tuple)
# les tuples ne sont pas modifiables (mutables)
O_tuple=("janvier", "fevrier","mars" )
print(O_tuple) #mais apparement ont peut les réassigner !!!?
#### on joue avec les sets
O_set= ["pomme","poire", "pomme"]
print(O_set)
O_set=set(O_set)
print(O_set) #et hop on vire les doublons (les sets n'acceptent pas les doublons !!!)
print(O_set)