x = []
def riemann_sum(a,b,fx,n=100_000):
    sum = 0
    d_x = (b-a)/n
    for i in range(n+1):
        x.append(a+d_x*i)
    
    for i in x:
        sum = sum + fx(i)*d_x
    print(sum)
    return sum 
