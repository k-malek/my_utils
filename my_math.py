def nww(a, b): return a*b//nwd(a, b)
def nwd(a, b): return nwd(b, a%b) if b else a

def two_points_dist(a,b):
    return sum([(a_val - b_val)**2 for a_val,b_val in zip(a,b)])**0.5
    
def line_function(p1,p2):
    a=0 if p1[0]==p2[0] else (p1[1]-p2[1])/(p2[0]-p1[0])
    b=p1[1]-p1[0]*a
    result='y='
    if a!=0:
        result+=f'{a}x'
        if b>0:
            result+='+'
    if b!=0:
        result+=f'{b}'
    return a,b,result
    
def divisors_generator(a):
    for i in range(1,a+1):
        if a%i==0: yield i

def all_divisors(a):
    divisors=[]
    for i in range(1,int(a**0.5)+1):
        if a%i==0:
            divisors.append(i)
            if a//i!=i:
                divisors.append(a//i)
    return sorted(divisors)
        
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_nums_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def factorial(n,start=2):
    result=1
    for i in range(start,n+1):
        result*=i
    return result
    
def fibo_generator():
    fibo=0
    next_fibo=1
    while True:
        yield(fibo)
        fibo,next_fibo = next_fibo,next_fibo+fibo
    
def is_fibo(n):
    fibo_gen=fibo_generator()
    fibo=next(fibo_gen)
    while fibo<=n:
        if n==fibo:
            return True
        fibo=next(fibo_gen)
    return False