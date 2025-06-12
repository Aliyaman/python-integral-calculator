x = []
def trapezoidal(a,b,fx,n=100_000):
    sum = 0
    d_x = (b-a)/n
    for i in range(n+1):
        x.append(a+d_x*i)
    #print(x)
    for i in x:
        if i == x[0] or i == x[len(x)-1]:
            sum += fx(i)
            #pass
        else:
            #pass
            sum += 2*fx(i)
    sum *= d_x/2 
    print(sum)
    return sum