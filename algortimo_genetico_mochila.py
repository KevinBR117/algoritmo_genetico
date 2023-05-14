import random
# leer archivo txt
archivo = open('./productos.txt', 'r')

# crear lista de productos
lista_productos = []
for linea in archivo:
    lista_productos.append(linea.replace('\n', '').split(' '))
print(f'lista de productos: {lista_productos}\n')

# generar poblacion
poblacion = []
nueva_poblacion = []
numero_mochilas = 100
mejor_mochila = []
mutacion = 0.5
max_gen = 20
calorias_min = 800
peso_max = 1.5


def crear_poblacion_inicial(numero_mochilas):
    for i in range(numero_mochilas):
        mochila = [0] * len(lista_productos)
        puntuacion = [0] * 3
        for j in range(len(mochila)):
            # generar seleccion de productos aleatoria
            cargo_producto = random.randint(0, 1)
            if(cargo_producto == 1):
                mochila[j] = 1
                # peso
                puntuacion[0] += float(lista_productos[j][1])
                # caloria
                puntuacion[1] += int(lista_productos[j][2])

        puntuacion[2] = float(puntuacion[1]/puntuacion[0])
        # añadir puntuacion
        mochila.extend(puntuacion)
        # añadir a la poblacion
        poblacion.append(mochila)

    print(f'poblacion inicial: {poblacion}')


def mostrar_mejor_mochila():
    mejor_mochila = poblacion[0]
    for i in range(len(poblacion)):
        individuo = poblacion[i]
        # print(len(individuo), len(mejor_mochila))
        if(individuo[-1] >= mejor_mochila[-1]):
            if (individuo[len(individuo)-3] <= peso_max) and (individuo[len(individuo)-2] >= calorias_min):
                mejor_mochila = individuo
    print(f'mejor mochila: {mejor_mochila}')


def cruzar_inidividuos(poblacion):
    nueva_poblacion = []
    for i in range(0, len(poblacion), 2):
        # obtener individuo
        # print(i)
        individuo1 = poblacion[i][:len(lista_productos)]
        individuo2 = poblacion[i+1][:len(lista_productos)]

        # cruzar individuos
        corte = random.randint(1, len(lista_productos)-1)
        # corte = int(len(individuo1)/2)
        # print("corte", corte)
        mochila = individuo1[0:corte]
        mochila.extend(individuo2[corte:len(individuo2)])
        puntuacion = [0] * 3
        # generar puntuacion
        for j in range(len(mochila)):
            # print(j)
            if(mochila[j] == 1):
                # peso
                puntuacion[0] += float(lista_productos[j][1])
                # caloria
                puntuacion[1] += int(lista_productos[j][2])
        puntuacion[2] = float(puntuacion[1]/puntuacion[0])
        # añadir puntuacion
        mochila.extend(puntuacion)
        # añadir a la poblacion
        nueva_poblacion.append(mochila)

        # cruzar partes restantes
        mochila1 = individuo2[0:corte]
        mochila1.extend(individuo1[corte:len(individuo1)])
        puntuacion1 = [0] * 3
        # generar puntuacion
        for j in range(len(mochila1)):
            # print(j)
            if(mochila1[j] == 1):
                # peso
                puntuacion1[0] += float(lista_productos[j][1])
                # caloria
                puntuacion1[1] += int(lista_productos[j][2])
        puntuacion1[2] = float(puntuacion1[1]/puntuacion1[0])
        # añadir puntuacion
        mochila1.extend(puntuacion1)
        # añadir a la poblacion
        nueva_poblacion.append(mochila1)
    poblacion = nueva_poblacion
    print(f'nueva poblacion: {nueva_poblacion}\n')


def mutar_individuo(mutacion, poblacion):
    numero_mutaciones = int(mutacion * len(poblacion))

    while(numero_mutaciones >= 1):
        individuo = (random.randint(0, len(poblacion)-1))
        mochila = poblacion[individuo]
        producto_mutado = random.randint(0, len(lista_productos))
        
        for ind in poblacion:
            if(ind == mochila):
                # print(mochila)
                if(ind[producto_mutado] == 1):
                    ind[producto_mutado] = 0
                else:
                    ind[producto_mutado] = 1

                puntuacion = [0] * 3
                # print(poblacion[individuo])
                # print(len(poblacion[individuo])-3)
                for i in range(len(ind)-3):
                    if(ind[i] == 1):
                        # print('true')
                        # peso
                        puntuacion[0] += float(lista_productos[i][1])
                        # caloria
                        puntuacion[1] += int(lista_productos[i][2])
                puntuacion[2] = float(puntuacion[1]/puntuacion[0])
                # print(puntuacion)
                # print(puntuacion[2])
                # añadir puntuacion
                ind[len(ind)-3] = puntuacion[0]
                ind[len(ind)-2] = puntuacion[1]
                ind[len(ind)-1] = puntuacion[2]
                # poblacion[individuo] = ind
        numero_mutaciones -= 1


def main():
    for gen in range(max_gen):
        if (gen == 0):
            crear_poblacion_inicial(numero_mochilas)
            mostrar_mejor_mochila()
        else:
            cruzar_inidividuos(poblacion)
            mutar_individuo(mutacion, poblacion)
            mostrar_mejor_mochila()


if __name__ == '__main__':
    main()
