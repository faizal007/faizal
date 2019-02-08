str=str(input(''))
try:
    i = float(str)
    print("Yes")
except (ValueError, TypeError):
    print('No')
print()
