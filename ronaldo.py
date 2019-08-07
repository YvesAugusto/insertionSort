from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
 
def geraLista(size):
    array = []
    while size > 0:
        array.append(size)
        size-=1
    return array
  
def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", name='fig'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name+'.png')

operacoes = []
operacoes2 = []
def insertionSort(A):
    ans=0
    count = 0
    for j in range(1,len(A)):
        key = A[j] 
        i = j-1
        while (i > -1) and key < A[i]:
            A[i+1]=A[i] 
            i=i-1
            count+=1
        
        A[i+1] = key
        ans+=1
    operacoes.append(count)
    operacoes2.append(ans)
    return A


listas=[]
x2 = [10000,20000,50000,100000]
y = []

for i in range(4):
  listas.append(geraLista(x2[i]))

for i in range(4):
  y.append(timeit.timeit("insertionSort({})".format(listas[i]),setup="from __main__ import insertionSort",number=1))  
  print("Terminou de ordenar um vetor de tamanho " + str(x2[i]) + "...")

desenhaGrafico(x2,y,'Quantidade','Tempo', 'insertion')
desenhaGrafico(x2,operacoes,'Quantidade','Swaps', 'insertionSwap')
desenhaGrafico(x2, operacoes2, 'Quantidade', 'Swaps', 'insertionSwapp')