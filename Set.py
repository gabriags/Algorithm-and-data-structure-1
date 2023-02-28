# TAD Set. Functions Create, check duplicates, union, intersection and Defference
from algo1 import *

#I: Set
#Delete repeat elements from set
#O: An array from TAD set
def Create_Set(Arreglo):
  
  dup=check_duplicates(Arreglo)
  if dup==True:

    n=len(Arreglo)

    #Search and empty repeat elements
    for i in range(0,n):
      contador1=0
      for j in range(0,n):
        if Arreglo[i]==Arreglo[j]:
          contador1=contador1+1
          if contador1>1:
            Arreglo[j]=None

    #Counts empty elements
    contador2=0 
    for i in range(0,n):
      if Arreglo[i]==None:
        contador2=contador2+1               
  
    #Generate a new array
    if contador2!=0:
      m=n-contador2
      ArregloNew=Array(m,0)
      
      posicion=0
      
      for i in range(0,n):
        if Arreglo[i]!=None:
          ArregloNew[posicion]=Arreglo[i]
          posicion=posicion+1
      return ArregloNew
  else:
    return Arreglo          

#I: Array  
#Sarch for repeat elements
#O: returns true if there is and returns false if not
def check_duplicates(Arreglo):
  n=len(Arreglo)
  verifica=False
  for i in range(0,n):
    repetidos=0
    for j in range(0,n):
      if Arreglo[i]==Arreglo[j]:
        repetidos=repetidos+1
        if repetidos>1:
          verifica=True
  if verifica==True:
    print("ERROR: duplicate elements exist")
  return verifica            

#I: two vectors S and T
#performs the union of vectors without repeating elements
#O: return the new vector
def Union(S,T):

  S=Create_Set(S)
  T=Create_Set(T)
  n=len(S)
  m=len(T)
  U=Array(m+n,0)
  j=0

  for i in range(0,m+n):
    if i<n:
      U[i]=S[i]
    else:
      U[i]=T[j]
      j=j+1

  vectorU=Create_Set(U)
  return (vectorU)    

#I: two vectors S and T
#perform the intesection within the two vectors
#O: return the new set
def Intersection(S,T):

  S=Create_Set(S)
  T=Create_Set(T)
  n=len(S)
  m=len(T)
  U=Array(m+n,0)
  k=0

  for i in range(0,n):
    for j in range(0,m):
      if S[i]==T[j]:
        U[k]=S[i]
        k=k+1
  if k!=0:
    vectorI=Create_Set(U)
    return(vectorI)
  else:
    print("Los vectores 1 y 2 no tienen elementos en común")
    return[None]        

#
#Lee los conjuntos, los vuelve tipo Set y busca la diferencia entre ellos
def Difference(S,T):
  
  S=Create_Set(S)
  T=Create_Set(T)
  n=len(S)
  m=len(T)
  U=Array(n,0)
  k=0
  #Cuenta la cantidad de elementos que se encuentran en el primer conjunto y no en el segundo
  for i in range(0,n):
    contador1=0
    for j in range(0,m):
      if S[i]==T[j]:
        contador1=contador1+1
    #llena un vector con dichos elementos    
    if contador1==0:
      U[k]=S[i]
      k=k+1


  #Elimina las posiciones vacias del nuevo vector
  if k!=0:
    contador2=0 
    for i in range(0,n):
      if U[i]==None:
        contador2=contador2+1

    largo=n-contador2
    T=Array(largo,0)
    j=0

    for i in range(0,n):
      if U[i]!=None:
        T[j]=U[i]
        j=j+1   
    return(T)        

  else:
    print("No existe un conjunto diferencia")
    return[None]      
