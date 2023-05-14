import random
individuo1 = [0,1,0,1,0,1,0,1]
individuo2 = [1,0,1,0,1,0,1,0]

cruce = random.randint(1,len(individuo1)-1)
print(cruce)

mochila1 = individuo1[0:cruce]
print(mochila1)
mochila2 = individuo2[cruce:len(individuo2)-1]
print(mochila2)

print(random.randint(0, 9))