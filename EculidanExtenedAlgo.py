import math



def fillEculidanTable (a,b ) :

        flag = True
        table = []

        a = a
        b = b
        r = a % b
        q = math.floor(a / b)
        templist = [a, b, r, q]
        table.append(templist)
        i = 0

        u=[1,0]
        v=[0,1]

        while (flag == True) :
            if (r==0) :
                flag =False
            else:
                v.append(v[i] - (v[i + 1] * q))
                u.append(u[i] - (u[i + 1] * q))
                i+=1
                a=b
                b=r
                r=a%b
                q = math.floor(a / b)
                templist = [a, b, r, q]
                table.append(templist)

        return v[len(v)-1]




print("We know that extend eculidan algorthim can find inverse "
      "\nof certin number b in mod of n ...."
      "\nIn Order to calculate inverse plese enter following "
      "\n(Note that n is mod and b is the number that u want to find inverse) ")
a = int (input("Enter n = "))
b = int (input("Enter b = "))
result = fillEculidanTable (a,b)

if result < 0 :
    result = result%a

if (math.gcd(a, b) == 1):
    print( "The inverse of " + str(b) + " in mod of " + str(a) + " is = " + str(result))
else:
    print( "Inverse not applicable ")

