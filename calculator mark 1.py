#this program is created by gurnish singh
def add(x,y):
    return print(x+y);
def subtract(x,y):
    return print((x-y))
def multiply(x,y):
    return print(x*y)
def divide(x,y):
    return print((x/y))
def modulous(x,y):
    return print(x%y)
def cel(fahr):
    return print((fahr-32)*5/9)
def fahr(cel):
    fahr=(cel*(9/5)+32)
    return print(fahr)
def square(x):
    return print( x**.5)
def prime(x):
    count =0
    if(x)>0:
        for i in range(2,x):
            if x%i == 0:
                count+=1
    if(count==0):
            print('prime number')
    else:
        print('not a prime')
print ('****************************************************')
print('CALCULATOR')
print('1 add')
print('2 subtract')
print('3 multiply')
print('4 divide')
print('5 modulus')
print('6 fahr to cel')
print('7 cel to fahr')
print('8 square root')
print('9 prime number or not')
print('******************************************************')
choice=input('enter your choice 1|2|3|4|5|6|7|8|9')
if choice == '1':
    x,y=map(int,input('type input with spaces ').split())
    add(x,y)
elif choice == '2':
    x,y=map(int,input('type input with spaces ').split())
    subtract(x,y)
elif choice == '3':
    x,y=map(int,input('type input with spaces ').split())
    multiply(x,y)
elif choice == '4':
    x,y=map(int,input('type input with spaces ').split())
    if y==0:
        print ('ERROR denominator cannot be zero')
    else:
        divide(x,y)
elif choice == '5':
    x,y=map(int,input('type input with spaces ').split())
    modulous(x,y)
elif choice == '6':
    x=int(input())
    cel(x)
elif choice == '7':
    x=int(input())
    fahr(x)
elif choice == '8':
    x=int(input())
    square(x)
elif choice == '9':
    x=int(input())   
    prime(x)











           
