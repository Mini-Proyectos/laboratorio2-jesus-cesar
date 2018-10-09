'''import time

n = 1000
j=0
inicio = time.time()

for i in range(1,n):
	j = i+j 
fin = time.time()

tiempoTranscurrido = (fin-inicio) * 1000 # para expresarlo en milisegundos

print("Tiempo: " + str(tiempoTranscurrido))'''

import time
import sys
from Sorts import MergeSort

MetodoDeOrdenamiento = str(sys.argv[1])
NumeroDeElementos = int(sys.argv[2])
TiempoInicial = 0
TiempoFinal = 0
TiempoParaOrdenar = 0

Lista=[3,1,4,5,1,3,4,2,0,13,4,1,3,6,8,2,5,25,14,1467,515,141]#Esta lista es para probar

if MetodoDeOrdenamiento == "MergeSort":
	
	TiempoInicial = time.time()
	
	ListaOrdenada = MergeSort (Lista, 0, NumeroDeElementos)

	TiempoFinal = time.time()

#Aqui iria el elif


TiempoParaOrdenar = (TiempoFinal - TiempoInicial)*1000

print(MetodoDeOrdenamiento, NumeroDeElementos, TiempoParaOrdenar)