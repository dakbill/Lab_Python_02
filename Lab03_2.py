import math
number=float(raw_input("Enter the number:"))
temp=0
tnum=number
A=""
for i in range(int((math.log10(number)+1)-1),-1,-1):
        temp+=(tnum%10)*(10**i)
        tnum=int(tnum/10)
print "The low level encryption",int(temp)
for i in range(int((math.log10(number)+1)-1),-1,-1):
        temp+=(((tnum%10)+7)%10)*(10**i)
        tnum=int(tnum/10)
print "The higher level encryption",int(temp)
