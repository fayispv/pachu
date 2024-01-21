def factorial(number):
  result = number
  for i in range (1,number):
    result *= i
  return result

print(factorial(5))
