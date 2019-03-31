import struct
def pcsize():# to calculate pc is executing in 32 or 6 bits
    print(struct.calcsize('p')*8)
def stringlenght(str):
    count=0
    for char in str:
        count+=1
    print(count)
def extension(file):
    return file.split('.')
    # that is if the file name is kjb.jjb it will split into kjb and jjb and put
    #it into a list
def personaldetail():
    name=input('enter your name')
    age=input('enter your age')
    address=input('enter address')
    #print name age and and address in different lines
    print(' name:{}\nAge:{}\nAddress:{}'.format(name,age,address))
print('***************************************************')
print('1 get file extension name')
print('2 age calculator anfd check u are teenager or not')
print('3 display ur personal details in deffernt line')
print('4 check wheather the pyhton is executing in wheather 32 or 64 bits')
print('5 check tkhe lenght of th string')
print('****************************************************')
choice =input('enter ur choice 1|2|3|4|5')4
if choice=='1':
    filename=input('enter the filename ')
    ext=extension(filename)
    print(ext[-1])
if choice=="2":
   age=int(input("Enter your year of birth for example~1998 :"))
   age=2019-age
   if age >18:
       print("Your age is :",2019-age,"(You are Adult)")
   else:
       print("Your age is :",2019-age,"You are teenager")
if choice=="3":
    personal_detail()
if choice=="4":
    pcsize()
if choice=="5":
    Sl=input("Enter the sentence")
    Stringl=stringlength(Sl)

