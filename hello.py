def factorial(number):
  result = number
  for i in range (1,number):
    result *= i
  return result

print(factorial(5))

def factorial_rec(number):
  if number >1 :
    res = number * factorial_rec(number-1)
    return res
  return 1
  
print(factorial_rec(6))
