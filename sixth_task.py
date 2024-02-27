import sys


def task(num_first, num_two, operator):
  if operator == '+':
    return num_first + num_two
  elif operator == '-':
    return num_first - num_two
  elif operator == '/':
    if num_two == 0:
      return "Ділення на 0 неможливе!"
    else:
      return num_first / num_two
  elif operator == '*':
    return num_first * num_two
  else:
    return "Недійсний оператор"


num_first = float(sys.argv[1])
operator = sys.argv[2]
num_two = float(sys.argv[3])

result = task(num_first, num_two, operator)
print("Результат", result)