n=""
while (not n):
    theInput=int(raw_input("Enter an integer for testing:"))
    if theInput%2==0:
        print "%d is even"%theInput
    else:
        print "%d is odd"%theInput
    n=raw_input("Wanna go on testing?(y,n):")
    if n=="n":
        n=1
    else:
        n=0
print "--------------------------------"
pSchoolAge=4
votingAge=18
presidentAge=40
retireAge=60
yourAge=int(raw_input("How old are you?:"))
if(yourAge<pSchoolAge):
    print "Too young"
elif(yourAge>=18):
    print "Remember to vote "
    if(yourAge>=presidentAge):
        print "and vote for me."
    elif(yourAge<presidentAge):
        print " but unfortunately you can't be president"
    if(yourAge>=retireAge):
        print "Too old though!!"
print "--------------------------------";
out=""
for i in range(41,-1,-1):
    if i%3==0:
        ##print i
        out+=","+str(i)
print out
print "--------------------------------";
for i in range(6,30,1):
    if not ((not i%2) or (not i%3) or (not i%5)):
        print i
       
print "--------------------------------";
n=0
while True:
    n+=1
    if(79*n)%97==1:
       print n
       break
print "--------------------------------";


