a = int(input())
a %= 86400
h = a // 3600
m = a // 60 % 60
s = a % 60

print(f'{h}:{m:02}:{s:02}')