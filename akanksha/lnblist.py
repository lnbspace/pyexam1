l1=input("enter the elements:")
l2=input("enter the elements:")
odd_i=[]
even_i=[]
for i in range (0,len(l1)):
  if i%2:
    even_i.append(l2[i])
  else:
    odd_i.append(l1[i])
l3=odd_i+even_i
print(l3)

