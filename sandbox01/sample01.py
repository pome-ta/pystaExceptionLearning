num_str = '-1.0'
try:
  num_int = int(num_str)
except Exception as e:
  print(e)
  num_float = float(num_str)
