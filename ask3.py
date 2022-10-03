lst = [1,2,3,4,5,6,7] 
list =[]
n=[1,2,3,4,5,6,7] 
print(n)

def Josephus(n, k):
    
    index = k - 1
    list.append(n[index])
    k -= 1
    
    print('Dead people:')
    while (len(n) > 1):
        print(n.pop(index))
        index = (k + index) % len(n)
        list.append(n[index])
    print("Last to die:", n.pop(index))
    print('Josephus ', list)
   
Josephus(n, 3)

