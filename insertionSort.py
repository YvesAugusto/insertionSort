from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
 
def geraLista(size):
    vector = []
    while size > 0:
        vector.append(size)
        size-=1
    return vector
  
def geraInversa(size):
  lista=list(range(size,1,-1))
  return lista

def geraOrdenado(size):
	return list(range(size))


def desenhaGrafico(x,y,y2,xl = "Entradas", yl = "Saídas", name='fig'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo Aleatório")
    ax.plot(x,y2, label = "Melhor Tempo Decrescente")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name+'.png')

operacoes=[]
def insertionSort(vector): 
  
    count=0
    for i in range(1, len(vector)): 
        key = vector[i] 
        j = i-1
        while j >=0 and key < vector[j] : 
		vector[j+1] = vector[j] 
		j -= 1
		count+=1

        vector[j+1] = key

    operacoes.append(count)
    return vector
listas=[]
listaInversa=[]
listaOrdenada=[]
x2 = [10000,20000,50000,100000]
y = []
y2=[]
y3=[]

for i in range(4):
  listas.append(geraLista(x2[i]))
  listaInversa.append(geraInversa(x2[i]))
  listaOrdenada.append(geraOrdenado(x2[i]))


for i in range(4):
  y.append(timeit.timeit("insertionSort({})".format(listas[i]),setup="from __main__ import insertionSort",number=1))
  print("Terminou de ordenar um vetor de tamanho " + str(x2[i]) + "...")
  
for i in range(4):
  y2.append(timeit.timeit("insertionSort({})".format(listaInversa[i]),setup="from __main__ import insertionSort",number=1))
  print("Terminou de ordenar um vetor de tamanho " + str(x2[i]) + "...")

for i in range(4):
  y3.append(timeit.timeit("insertionSort({})".format(listaOrdenada[i]),setup="from __main__ import insertionSort",number=1))
  print("Terminou de ordenar um vetor de tamanho " + str(x2[i]) + "...")


print(operacoes[:])

desenhaGrafico(x2,y,y2,'Quantidade','Tempo', 'insertionWorstCase')
desenhaGrafico(x2,operacoes[0:4],operacoes[4:8],'Quantidade','Swaps', 'insertionWorstCaseSwap')

desenhaGrafico(x2,y,y3,'Quantidade','Tempo', 'insertionBestCase')
desenhaGrafico(x2,operacoes[0:4],operacoes[8:12],'Quantidade','Swaps', 'insertionBestCaseSwap')
