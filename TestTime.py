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
	
	MergeSort (Lista, 0, NumeroDeElementos)

	TiempoFinal = time.time()

elif MetodoDeOrdenamiento == "InsertionSort": 

	TiempoInicial = time.time() 

	InsertionSort(Lista, 0, NumeroDeElementos) 	

	TiempoFinal = time.time() 

TiempoParaOrdenar = (TiempoFinal - TiempoInicial)*1000

print(MetodoDeOrdenamiento, NumeroDeElementos, TiempoParaOrdenar)
