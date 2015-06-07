__author__ = 'Jed'

x=500
while x<501:
    if x%5==0 and x%2!=0:
        print ("cool")
    elif x%5==0 and x%2==0:
        print ("dude")
    else:
        print (x)
    x=x-1

    if x==0:
        break



