#saraksts1 = [1, 2, 3, 4, 5, 6, 7, 8, 9] #izveidojat jaunu sarakstu 5 elementiem

#print(saraksts1[2]) #izvada konkrētu elementu noradot tā indeksu [2]

#for i in range(0, len(saraksts1)): # in range kura diapazona darbosies for len sasniedz pēdejo skaitli
 #   print("i =",i)
  #  print(saraksts1[i])
#print()
#for i in range( len(saraksts1)-1, -1, -1): 
#    print("i =",i)
 #   print(saraksts1[i])
    
"""
garums = int(input('garums: '))
augums = int(input('augstums: '))

for i in range(0,augums):
    for j in range(0,garums):
        print('#', end= " ")
    print()    
    
print()

for i in range(0,augums):
    for j in range(0,garums):
        print('#', end= " ")
    print()    
"""
garums = int(input('garums: '))
augums = int(input('augstums: '))

for i in range(0,augums):
    for j in range(0,garums):
        if i == j:
            print('o', end= " ")
        else:
            print(' ', end= " ")
    print()    
    
print()

for i in range(0,augums):
    for j in range(0,garums):
        print('#', end= " ")
    print()    
