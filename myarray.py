# TAD Array. Functions search, insert, delete and lenght

#I: Array and element
#Search for first instance of an element
#O: returns the position of the element
def search(Array, element):
  n=len(Array)
  for i in range(0,n):
    if Array[i]==element:
      return i
  return None    


#I: Array, element and position
#Place the element in the position input
#O: returns the modified Array
def insert(Array,element,position):
  n=len(Array)
  if position<0 or position>=n:
    return None
  else:
    for i in range(n-1,position,-1):
      Array[i]=Array[i-1]
    Array[position]=element
  return position  


#I: Array and element
#Search and delete the first instance of element
#O: returns the position of the element
def delete(Array,element):
  n=len(Array)
  existe=False

  for i in range(0,n):
    if Array[i]==element:
      if existe==False:
        position=i
      existe=True

  if existe==True:
    for i in range(position,n-1):
      Array[i]=Array[i+1]
    Array[n-1]=None
    return position
  return None    

#I: Array
#Counts not empty elements
#O: return the amount of not empty elements
def length(Array):
  n=len(Array)
  full=0
  for i in range(0,n):
    if Array[i]!=None:
      full+=1
  return full     
