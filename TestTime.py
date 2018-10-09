'''import time
inicio = time.time()

for i in range(1,n):
	j = i+j 
fin = time.time()

tiempoTranscurrido = (fin-inicio) * 1000 # para expresarlo en milisegundos

print("Tiempo: " + str(tiempoTranscurrido))'''

import time
import sys
import random
from Sorts import MergeSort
from Busquedas import InsertionSort


MetodoDeOrdenamiento = str(sys.argv[1])
NumeroDeElementos = int(sys.argv[2])
TiempoInicial = 0
TiempoFinal = 0
TiempoParaOrdenar = 0	
Lista=[random.randint(0,10000) for i in range(NumeroDeElementos)]

if MetodoDeOrdenamiento == "MergeSort":
	
	TiempoInicial = time.time()
	
	ListaOrdenada = MergeSort (Lista, 0, NumeroDeElementos)

	TiempoFinal = time.time()

elif MetodoDeOrdenamiento == "InsertionSort": 

	TiempoInicial = time.time() 

	ListaOrdenada = InsertionSort(Lista, 0, NumeroDeElementos) 	

	TiempoFinal = time.time() 

TiempoParaOrdenar = (TiempoFinal - TiempoInicial)*1000

print(MetodoDeOrdenamiento, NumeroDeElementos, TiempoParaOrdenar)
