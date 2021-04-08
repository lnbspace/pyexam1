
lst = []
print('Enter 5 integers:')

for i in range(0, 5):
    ele = int(input())
    lst.append(ele) 
    if ele<9:
        lst.remove(ele)

print(lst)
        
Sum = sum(lst)
print(Sum)