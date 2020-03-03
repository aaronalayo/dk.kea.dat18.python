def recursive_fibo(num_elements):
   if num_elements == 1:
       return 0
   elif num_elements == 2:
       return 1 
   else:
       return recursive_fibo(num_elements-2) + recursive_fibo(num_elements-1)

def gen_fibo():
    a,b = 0,1
    while True:
        yield a
        a, b = a, a+b

if __name__=='__main__':
    # print(recursive_fibo(12))  
    gf = gen_fibo()
    for i in range(12):
        print(next(gf))

   




