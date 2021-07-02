
from art import logo


def add(a,b):
  return int(a + b)

def sot(a,b):
  return int(a - b)

def mult(a,b):
  return int(a * b)

def div(a,b):
  return int(a / b)

a = int(input('insert 1st number: '))
b = int(input('insert 2nd number: '))

operations = {
'+': add(a,b),
'-': sot(a,b),
'*': mult(a,b),
'/': div(a,b)
}

operators_choiche = [key for key in operations]

operation_symbol = input(f'insert operator {operators_choiche}: ')

answer = calculation_function = operations[operation_symbol]

print(f"{a} {operation_symbol} {b} = {answer}")

