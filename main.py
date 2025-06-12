from riemann import riemann_sum


def f(x):
    return x**2

riemann_sum(0,5,f)