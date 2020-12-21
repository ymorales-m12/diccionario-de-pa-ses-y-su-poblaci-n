Paises = {"Nicaragua":["Managua",'40m','750M'],"Mexico":["Mexico",'36m','800M'],"Brasil":["Brasilia",'50m','615M'],"Haiti":["Puerto Principe",'25m','900M']}

llaves = Paises.keys()
for a in llaves:
  print('La Capital de ' + a + ' es ' + Paises[a][0] + ' y tiene una poblacion de ' + Paises[a][1]+ ' de Habitantes '+'y con una PIB de ' + Paises[a][2])

