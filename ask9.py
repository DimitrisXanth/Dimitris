#π21231
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list =[]

def pair(lst, t):
    sum = 0
    x=0
    for x in lst:
        x=0
        print("x=",x)
        y=x+1
        while sum !=t :
            print(y)
            sum = lst[x]+lst[y]
            if sum == t: 
                list.append(lst[x])
                list.append(lst[y])
                item1= lst[x]
                item2= lst[y]
                lst.remove(item1)
                lst.remove(item2)
                print(list,lst)
                pair(lst,t)
              
            y=y+1    
                
                
pair(lst,10)

      


