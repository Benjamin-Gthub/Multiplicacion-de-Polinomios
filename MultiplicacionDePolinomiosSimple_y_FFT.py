import time
import numpy as np
from math import*
from tabulate import tabulate
import matplotlib.pyplot as plt


#Multiplicacion de polinomios(metodo simple):
def MultPol1(A,B):
    gradoA=int(len(A))
    gradoB=int(len(B))
    
    
    #Inicializar Lista
    C=[0]*(gradoA+gradoB-1)
    
    #Coeficientes del primer polinomio
    for i in range(gradoA):
        #Coeficiente del segundo polinomio
        for j in range(gradoB
                       ):
            C[j+i]=C[j+i]+(A[i]*B[j])
    return C




#Modulo para mostrar un polinomio
def Mostrar(A):
    res=""
    for x in range(len(A)):
        if(x!=len(A)-1):
            if(x==len(A)-2):
                res=res+(str(A[len(A)-x-1]))+" X"+" + "
            else:
                res=res+(str(A[len(A)-x-1])+" X^"+str(len(A)-x-1))+" + "
        else:
            res=res+(str(A[len(A)-x-1]))
    return res

#Modulo para generar Polinomio aleatorio
def GenerarPolinomio(grado):
    return np.random.randint(-11,11,size=(1,grado+1))[0]


#Modulo para hallar la Transformada Rapida de Furier(FFT) y su inversa(donde p=1 o p=-1)

def FFT(x,p):
    N = len(x)
    
    if N == 1:
        return x
    else:
        X_pares = FFT(x[::2],p)
        X_impares = FFT(x[1::2],p)
        factor =np.exp(2j*p*np.pi*np.arange(N)/ N)
        
        X = np.concatenate([X_pares+factor[:int(N/2)]*X_impares,X_pares+factor[int(N/2):]*X_impares])
        return X

#Genrar polinomio para FFT
def GenerarPolinomioFFT(grado):
    #Generar arreglo aleatorio
    aux=np.random.randint(-11,11,size=(1,grado+1))[0]
    #Agregar Ceros
    tamaototal=2**(int(log(grado+1,2))+1)
    cantidadceros=tamaototal-(grado+1)
    ceros=np.zeros(cantidadceros)
    aux=np.append(aux,ceros)
    #Retornar Arreglo
    return aux

def MultPol2(A,B):
    gradoA=int(len(A)/2)
    gradoB=int(len(B)/2)
    
    
    #Inicializar Lista
    C=[0]*(gradoA+gradoB)
    
    #Coeficientes del primer polinomio
    for i in range(gradoA):
        #Coeficiente del segundo polinomio
        for j in range(gradoB
                       ):
            C[j+i]=C[j+i]+(A[i]*B[j])
    return C
#Modulo para mostrar Menu
def Menu():
    print("|============== Menu =============|")
    print("| 1.-Multiplicacion Simple        |")
    print("| 2.-Multiplicacion FFT           |")
    print("| 3.-Comparacion de Tiempos       |")
    print("| 4.-Salir                        |")
    print("|=================================|")

def SubMenu(tab):
    print(tab+"|============== Submenu ================|")
    print(tab+"| 1.-Ingresar Polinomios                |")
    print(tab+"| 2.-Generar Polinomios Aleatorios      |")
    print(tab+"| 3.-Salir                              |")
    print(tab+"|=======================================|")

def SubMenu2(tab):
    print(2*tab+"|============== Submenu ================|")
    print(2*tab+"| 1.-Generar Polinomios Aleatorios      |")
    print(2*tab+"| 2.-Generar Tabla de Comparacion       |")
    print(2*tab+"| 3.-Salir                              |")
    print(2*tab+"|=======================================|")
#Opcion 1:
def Opcion1(tab):
    subopcion=0
    while(subopcion<3):
        SubMenu(tab)
        subopcion=int(input(tab+"Digite una opcion:"))
        if(subopcion==1):
            Opcion1_1(tab)
        elif(subopcion==2):
            Opcion1_2(tab)
        else:
            print()
def Opcion1_1(tab):
    #Primer Polinomio
    A=[]
    print(tab*2+"PRIMER POLINOMIO")
    print(tab*2+"================")
    n1=int(input(tab*2+"Digite el grado del primer polinomio:"))
    print()
    for x in range(n1+1):
        a=float(input(tab*3+"Digite el coeficiente "+str(x)+" del primer polinomio:"))
        A.append(a)
    print(tab*2+"================")
    #Segundo Polinomio
    print()
    print(tab*2+"SEGUNDO POLINOMIO")
    print(tab*2+"=================")
    B=[]
    n2=int(input(tab*2+"Digite el grado del segundo polinomio:"))

    for x in range(n2+1):
        a=float(input(tab*3+"Digite el coeficiente "+str(x)+" del segundo polinomio:"))
        B.append(a)

    #Mostramos los polinomios ingresados:
    print(tab*2+"P(X)=",Mostrar(A))
    print(tab*2+"Q(X)=",Mostrar(B))

    #Resultado de multiplicar ambas matrices:
    print(tab*2+"El resultado,es:")
    print(tab*2+"R(X)=",Mostrar(MultPol1(A,B)))
    print()
def Opcion1_2(tab):
    print(tab*2+"GENERAR PRIMER POLINOMIO")
    print(tab*2+"========================")
    n1=int(input(tab*2+"Digite el grado del primer polinomio:"))
    A=GenerarPolinomio(n1)
    print(tab*2+"Se genero con éxito el primer polinomio....")

    print(tab*2+"GENERAR SEGUNDO POLINOMIO")
    print(tab*2+"========================")
    n2=int(input(tab*2+"Digite el grado del Segundo polinomio:"))
    B=GenerarPolinomio(n2)
    print(tab*2+"Se generó tambien con éxito el segundo polinomio....")

    #Mostramos los polinomios Generados Aleatorios:
    print(tab*2+"Los Polinomios Aleatorios son: ")
    print(tab*2+"P(X)=",Mostrar(A))
    print(tab*2+"Q(X)=",Mostrar(B))
    print(tab*2+"________________________________")
    print()
    
    #Resultado de multiplicar ambas matrices:
    print(tab*2+"=============================================")
    print(tab*2+"El resultado,es:")
    print(tab*2+"R(X)=",Mostrar(MultPol1(A,B)))
    print(tab*2+"=============================================")
    print()


#Opcion 2:
def Opcion2(tab):
    subopcion=0
    while(subopcion<3):
        SubMenu(tab)
        subopcion=int(input(tab+"Digite una opcion:"))
        if(subopcion==1):
            Opcion2_1(tab)
        elif(subopcion==2):
            Opcion2_2(tab)
        else:
            print()

def Opcion2_1(tab):
    #Primer Polinomio
    A=[]
    print(tab*2+"PRIMER POLINOMIO")
    print(tab*2+"================")
    n1=int(input(tab*2+"Digite el grado del primer polinomio:"))
    print()
    for x in range(n1+1):
        a=float(input(tab*3+"Digite el coeficiente "+str(x)+" del primer polinomio:"))
        A.append(a)
    print(tab*2+"================")
    #Segundo Polinomio
    print()
    print(tab*2+"SEGUNDO POLINOMIO")
    print(tab*2+"=================")
    B=[]
    n2=int(input(tab*2+"Digite el grado del segundo polinomio:"))

    for x in range(n2+1):
        a=float(input(tab*3+"Digite el coeficiente "+str(x)+" del segundo polinomio:"))
        B.append(a)

    #Mostramos los polinomios ingresados:
    print(tab*2+"P(X)=",Mostrar(A))
    print(tab*2+"Q(X)=",Mostrar(B))

    #Resultado de multiplicar ambos polinomios:
    print(tab*2+"El resultado,es:")
    print(tab*2+"R(X)=",Mostrar(MultPol(A,B)))#FFT debe ser
    print()

def Opcion2_2(tab):
    print(tab*2+"GENERAR PRIMER POLINOMIO")
    print(tab*2+"========================")
    n1=int(input(tab*2+"Digite el grado del primer polinomio:"))
    A=GenerarPolinomioFFT(n1)
    print(tab*2+"Se genero con éxito el primer polinomio....")

    print(tab*2+"GENERAR SEGUNDO POLINOMIO")
    print(tab*2+"========================")
    n2=int(input(tab*2+"Digite el grado del Segundo polinomio:"))
    B=GenerarPolinomioFFT(n2)
    print(tab*2+"Se generó tambien con éxito el segundo polinomio....")

    #Mostramos los polinomios Generados Aleatorios:
    print(tab*2+"Los Polinomios Aleatorios son: ")
    print(tab*2+"P(X)=",Mostrar(A))
    print(tab*2+"Q(X)=",Mostrar(B))
    print(tab*2+"________________________________")
    print()
    
    #Resultado de multiplicar ambos Polinomios:
    print(tab*2+"=============================================")
    print(tab*2+"El resultado,es:")
    
    YK=FFT(A,1)*FFT(B,1)
    C3=FFT(YK,-1)
    print(tab*2,C3)
    print(tab*2+"=============================================")
    print()
    
#Opcion 3:
def Opcion3(tab):
    subopcion=0
    while(subopcion<3):
        SubMenu2(tab)
        subopcion=int(input(2*tab+"Digite una opcion:"))
        if(subopcion==1):
            Opcion3_1(2*tab)
        elif(subopcion==2):
            Opcion3_2(2*tab)
        else:
            print()
def Opcion3_1(tab):
    n=int(input(tab+"Digite el grado de los polinomios a generar: "))
    A=GenerarPolinomioFFT(n)
    B=GenerarPolinomioFFT(n)

    #Resolver por forma estandar
    i1=time.time()
    C1=MultPol2(A,B)
    f1=time.time()
    #Resolver por forma FFT
    i2=time.time()
    YK=FFT(A,1)*FFT(B,1)
    C2=FFT(YK,-1)
    C2=C2/len(A)
    f2=time.time()
    #Mostrar los tiempos de ejecucion:
    print("El tiempo que se demoro mediante el algoritmo estandar, fue:", f1-i1)
    print("El tiempo que se demoro mediante el algoritmo de FFT, fue:", f2-i2)

    #Mostrar los resultados:
    opcion=str(input(tab+"Desea ver los resultados ? S/N :"))
    if(opcion.lower()=="s"):
        print(tab+"El polinomio A, fue:")
        print(tab,A)
        print()
        print(tab+"El polinomio B fue:")
        print(tab,B)
        print()
        print(tab+"El resultado de multiplicar ambos polinomios:")
        print(tab+"-> Con el Algoritmo Estandar :")
        print()
        print(tab,C1)
        print()
        print(tab+"-> Con el Algoritmo FFT :")
        print()
        print(tab,C2)
        print()

def Opcion3_2(tab):
    n=int(input(tab+"Digite la cantidad de comparaciones: "))
    grado=1
    Tabla=[]
    while(grado<n):
        print()
        #Generamos los polinomios
        A=GenerarPolinomioFFT(2**grado-1)
        B=GenerarPolinomioFFT(2**grado-1)

        #Medir el tiempo de ejecucion mediante la multiplicacion Normal
        i1=time.perf_counter()
        C1=MultPol1(A,B)
        f1=time.perf_counter()

        #Medir el tiempo de ejecucion mediante la multiplicacion con FFT
        
        i2=time.perf_counter()
        YK=FFT(A,1)*FFT(B,1)
        C3=FFT(YK,-1)
        C3=C3/len(A)
        
        f2=time.perf_counter()

        #Agregar los resultados a la tabla
        Tabla.append([2**grado-1,f1-i1,f2-i2])
        #Mostrar el proceso de la ejecucion
        print(tab+"proceso: ",round(((grado+1)/n)*100,2),"%           Completado                                           ")
        grado=grado+1

    #Mostramos la tabla
    #Mostrar el proceso de la ejecucion
    #print("proceso: ",round(((grado+1)/n)*100,2),"%           Completado                                           ")

    #Mostrar la tabla de los resultados
    print(tabulate(Tabla,headers=['Grado', 'T. Multiplicacion Normal(seg.)', 'T. Multiplicacion FFT(seg.)'],tablefmt='fancy_grid'))
    print("-----------------------------")


    #Graficar resultados
    x = [colum1[0] for colum1 in Tabla]
    y1 = [colum2[1] for colum2 in Tabla]
    y2= [colum3[2] for colum3 in Tabla]

    fig, ax = plt.subplots()
    ax.plot(x,y1,label="Algoritmo Normal")
    ax.plot(x,y2,label="Algoritmo FFT")
    ax.set_ylabel('Tiempo de  Ejecucion (seg,)')
    ax.set_xlabel('Grado de los Polinomios(n)')
    ax.set_title('Grafico De Comparacion')
    ax.legend(loc = 'upper left')
    plt.show()


    
#===============================================================================================
#                                       Programa principal
#===============================================================================================
tab="     "
opcion=0
while(opcion<4):
    Menu()
    opcion=int(input("Digite una Opcion:"))
    if(opcion==1):
        Opcion1(tab)
    elif(opcion==2):
        Opcion2(tab)
    elif(opcion==3):
        Opcion3(tab)
    else:
        tab=input("Digite cualquier tecla para salir...")



#Programa Principal(solo funciona para arreglos del tamaño 2**x)
##grado=1
##Tabla=[]
##while(grado<10):
##    print()
###print(GenerarPolinomioFFT(4))
##    print("============= Ejemplo grado"+str(2**grado-1)+"===================")
##    A=GenerarPolinomioFFT(2**grado-1)
###A=np.append(A,[0,0])
##    print(A)
##    B=GenerarPolinomioFFT(2**grado-1)
###B=np.append(B,[0,0])
##    print(B)
###Multiplicacion normal:
##    i1=time.perf_counter()#time.time()
##    C1=MultPol(A,B)
##    f1=time.perf_counter()#time.time()
##    print("El tiempo que se demoro el algoritmo, es:", f1-i1)
##    
###MULTIPLICACION FFT
##    i2=time.perf_counter()#time.time()
##    
##    YK=FFT(A,1)*FFT(B,1)
##    C3=FFT(YK,-1)
##    C3=C3/len(A)
##    
##    f2=time.perf_counter()#time.time()
##    print("El tiempo que se demoro el algoritmo por FFT, es:", f2-i2)
##    #Mostrar resultados:
##    print("RESPUESTA MULTI. NORMAL")
##    print(C1)
##    #print("RESPUESTA MULTI. FFT")
##    #print(C2)
##    print("RESPUESTA IFFT")
##    print(C3)
##    Tabla.append([2**grado-1,f1-i1,f2-i2])
##    grado=grado+1
##
###Mostramos la tabla
###Mostrar el proceso de la ejecucion
##        #print("proceso: ",round(((x+1)/nPrimeros)*100,2),"%           Completado                                           ")
##
##        #Mostrar la tabla de los resultados
##print(tabulate(Tabla,headers=['Grado', 'T. Multiplicacion Normal(seg.)', 'T. Multiplicacion FFT(seg.)'],tablefmt='fancy_grid'))
##print("-----------------------------")
##
##
###Graficar resultados
##x = [colum1[0] for colum1 in Tabla]
##y1 = [colum2[1] for colum2 in Tabla]
##y2= [colum3[2] for colum3 in Tabla]
##
##fig, ax = plt.subplots()
##ax.plot(x,y1,label="Algoritmo Normal")
##ax.plot(x,y2,label="Algoritmo FFT")
##ax.set_ylabel('Tiempo de  Ejecucion (seg,)')
##ax.set_xlabel('Grado de los Polinomios(n)')
##ax.set_title('Grafico De Comparacion')
##ax.legend(loc = 'upper left')
##plt.show()

