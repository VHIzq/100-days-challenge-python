
def add(n1, n2):
    return n1 + n2


def divide(n1, n2):
    return n1 / n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


operations = {
  '+': add, 
  '/': divide, 
  '-': substract, 
  '*': multiply
  }

def calculator():
  num1 = float(input('Whats the first number?: '))
  again = True

  for op in operations:
    print(op)

  while again:
    op_symbol = input('Pick an operation: ')
    num2 = float(input('Whats the next number?: '))
    calculation_fn = operations[op_symbol]
    result = calculation_fn(num1, num2)
    print(f'{num1} {op_symbol} {num2} = {result}')
    
    calc_again = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation.: ")

    if calc_again == 'y':
      num1 = result
    else:
      again = False
      calculator()

calculator()