a=input("enter any string")
n=int(input("enter total number of pelindrom"))
s=a
c=0
while(a>0):
  dig=a%10
c=c*10+dig
a=a/10
if(s==c):
    print("the sentence is not pelindrom ")
else:
    print("the sentence is pelindrom")
