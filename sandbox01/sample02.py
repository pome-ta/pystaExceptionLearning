HEX_LETTERS = '0123456789abcdef'

i = HEX_LETTERS.find('g')

'''
i = None
try:
  i = HEX_LETTERS.index('g')
except ValueError:
  pass
'''

print(i)
