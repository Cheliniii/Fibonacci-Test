
def phibonash(num):
    
    fibonacci = []
    if num >= 0:
        fibonacci.append(0)
    if num > 0:
        fibonacci.append(1)
    
    next_term = 0

    while (next_term + fibonacci[-2]) <= num:
    
        next_term = fibonacci[-1] + fibonacci[-2]
        #if next_term > num:
         #   break
  
        fibonacci.append(next_term)
    
    return fibonacci


num = int(input("Input Number: "))
result = phibonash(num)
print(result)

