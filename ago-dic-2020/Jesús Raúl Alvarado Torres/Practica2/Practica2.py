lista_numeros = input().split()
n=lista_numeros[0]  #Numero de problemas = n
m=int(lista_numeros[1])  #Minutos para hacer la tarea = m
i = 0
np = 0 #np = numero de problemas
lista_minutos = input().split()

problemas = sorted(lista_minutos) #Ordena de menor a mayor

while i < m:
        i = i + int(problemas[i])
        np = np + 1

if m < int(problemas[0]):
    print("0")
else:
    print(np)