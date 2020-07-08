list1=[]
n=int(input("enter no of elements you want to enter in list1:"))
for a in range(0,n):
    num=int(input("enter number :"))
    list1.append(num)
for b in list1:
    if b>0:
        print(b)
print("These are output for list1")        
    
print("\n \n \n")
list2=[]
x=int(input("enter no of elements you want to enter in list2:"))
for i in range(0,x):
    y=int(input("enter number :"))
    list2.append(y)
for j in list2:
    if j>0:
        print(j)
print("These are output for list2")    
