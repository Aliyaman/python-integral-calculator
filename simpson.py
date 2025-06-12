x = []

def simpson_rule(a,b,fx,n=100_000):
    sum = 0
    d_x = (b-a)/n

    for i in range(n+1):
        x.append(a+d_x*i)

    for index,i in enumerate(x):
        if i == x[0] or i == x[len(x)-1]:
            sum += fx(i)
        elif index % 2 == 0:
            sum += 2*fx(i)
        elif index % 2 != 0:
            sum += 4*fx(i)
    sum *= d_x/3
    print(sum)
    return sum
        

