import random
import math

f = open("read.txt", 'r')

n = int(f.readline())

interval = f.readline()
intv = interval.split()
inter = list(map(int, intv))

par = f.readline()
param = par.split()
parametri = list(map(int, param))

precizie = int(f.readline())

probabilitate_recombinare = float(f.readline())

probabilitate_mutatie = float(f.readline())

nr_etape = int(f.readline())

desecretizare = (inter[1] - inter[0]) * pow(10, precizie)
lungime = round(math.log(desecretizare, 2))

def rand_chrom(p):
    x = ""
    for i in range(p):
        y = str(random.randint(0, 1))
        x += y
    return x

########## Populatia initiala ##########
lista_fitness = [0]
lista_x = [0]
cromozomi = [0]
print("Populatia initiala: ")
for i in range(1, n + 1):
    x = round(random.uniform(inter[0], inter[1]), precizie)
    y = rand_chrom(lungime)
    f = parametri[0] * x * x + parametri[1] * x + parametri[2]
    cromozomi.append(y)
    lista_x.append(x)
    lista_fitness.append(f)
    print(i , ": ", y, "x= ", x, "f= ", f)

########## Probabilitati selectie #########
print("\n")
print("Probabilitati selectie: ")
suma_fitness = 0.0
suma_fitness_list = [0]
for i in range(1, len(lista_fitness)):
    suma_fitness += lista_fitness[i]

for i in range(1, len(lista_fitness)):
    print("cromozom ", i, "probabilitate ", lista_fitness[i]/suma_fitness)
    suma_fitness_list.append(lista_fitness[i]/suma_fitness)

######## Intervale probabilitatile selectie ######
print("\n")
print("Intervale probabilitati selectie: ")
intervale = []
s = 0.0
for i in range(1, len(suma_fitness_list)):
    intervale.append(s)
    s += suma_fitness_list[i]
intervale.append(1.0)
print(intervale)

####### Procesul de selectie #######
def cautare_binara(array, x):
    st = 0
    dr = len(array)
    mid = 0
    while st <= dr:
        mid = (st + dr) // 2
        if array[mid] < x:
            st = mid + 1
        elif array[mid] > x:
            dr = mid - 1

    return mid + 1

cromozomi_selectati = []
print("\n")
print("Selectie cromozomi")
for i in range(1, n + 1):
    u = random.uniform(0, 1)
    q = cautare_binara(intervale, u)
    if q == n + 1:
        q -= 1
    cromozomi_selectati.append(q)
    print("u= ", u, "selectam cromozomul", q)


####### Dupa selectie ######
print("\n")
print("Dupa selectie: ")
populatie1_cromozomi = [0]
populatie1_x = [0]
populatie1_fitness = [0]
for i in range(0, n):
    populatie1_cromozomi.append(cromozomi[cromozomi_selectati[i]])
    populatie1_x.append(lista_x[cromozomi_selectati[i]])
    populatie1_fitness.append(lista_fitness[cromozomi_selectati[i]])
    print(i + 1, ": ", cromozomi[cromozomi_selectati[i]], " ", "x= ", lista_x[cromozomi_selectati[i]], " f= ", lista_fitness[cromozomi_selectati[i]])

###### Probabilitatea de recombinare 0.25 ######
print('\n')
print("Probabilitatea de incrucisare 0.25")
cromozomi_recombinare = []
for i in range(1, n + 1):
    u = random.uniform(0, 1)
    if u < probabilitate_recombinare:
        cromozomi_recombinare.append(i)
        print(i, ": ", populatie1_cromozomi[i], "u= ", u, "<", 0.25)
    else:
        print(i, ": ", populatie1_cromozomi[i], "u= ", u)


if len(cromozomi_recombinare) % 2 == 1:
    del cromozomi_recombinare[-1]

random.shuffle(cromozomi_recombinare)

def crossover(x1, x2):
    x1 = list(x1)
    x2 = list(x2)

    k = random.randint(0,lungime)
    print("punct ", k)
    for i in range(0, k):
        x1[i], x2[i] = x2[i], x1[i]

    x1 = ''.join(x1)
    x2 = ''.join(x2)

    return x1, x2

for i in range(0, len(cromozomi_recombinare), 2):
    print("Recombinare dintre cromozomul", cromozomi_recombinare[i], "cu cromozomul", cromozomi_recombinare[i + 1], ": ")

    a = populatie1_cromozomi[cromozomi_recombinare[i]]
    b = populatie1_cromozomi[cromozomi_recombinare[i + 1]]
    print(a, b, end=" ")
    a, b = crossover(a, b)
    print("Rezultat", a, b)
    print("\n")
    populatie1_cromozomi[cromozomi_recombinare[i]] = a
    populatie1_cromozomi[cromozomi_recombinare[i + 1]] = b

    populatie1_fitness[cromozomi_recombinare[i]], populatie1_fitness[cromozomi_recombinare[i + 1]] = populatie1_fitness[cromozomi_recombinare[i + 1]], populatie1_fitness[cromozomi_recombinare[i]]

    populatie1_x[cromozomi_recombinare[i]], populatie1_x[cromozomi_recombinare[i + 1]] = populatie1_x[cromozomi_recombinare[i + 1]], populatie1_x[cromozomi_recombinare[i]]

###### Dupa recombinare ######
print("Dupa recombinare")
for i in range(1, n + 1):
    print(i, ":", populatie1_cromozomi[i], " ", "x= ", populatie1_x[i], " ", "f= ",populatie1_fitness[i])

###### Mutatia - v2###### pentru v1 aparea o mutatie la aproximativ 20 rulari
print("Probabilitate de mutatie pentru fiecare gena", probabilitate_mutatie)
print("Au fost modificati cromozomii: ")
for i in range(1, n + 1):
    for j in range(1, lungime + 1):
        u = random.uniform(0, 1)
        if u < probabilitate_mutatie:
            p = round(random.uniform(0, lungime - 1))
            copie = list(populatie1_cromozomi[i])
            if copie[p] == 0:
                copie[p] = 1
            else:
                copie[p] = 0
            listToStr = ''.join([str(elem) for elem in copie])
            populatie1_cromozomi[i] = listToStr
            print(i)

print("\n")
print("Dupa mutatie")
for i in range(1, n + 1):
    print(i, ":", populatie1_cromozomi[i], " ", "x= ", populatie1_x[i], " ", "f= ", populatie1_fitness[i])

###### Evolutia maximului ###### TODO: pentru urmatoarele generatii
print("\n")
print("Evolutia maximului: ")
while(nr_etape):
    print(max(populatie1_fitness))
    nr_etape -= 1



    






