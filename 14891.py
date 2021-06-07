def rotate(d, a):
  if d == 1:
    right = a[0:7]
    left = a[7]
    a = left + right
  if d == -1:
    right = a[0]
    left = a[1:8]
    a = left + right
  
  return a

a = [input() for _ in range(4)]
t= int(input())

for _ in range(t):
  n, d = map(int, input().split())
  dir = [0]*4
  n -= 1
  temp = n
  dir[temp] = d
  while temp < 3:
    if a[temp][2] != a[temp+1][6]:
      dir[temp+1] = -(dir[temp])
    temp += 1
  temp = n
  while temp > 0:
    if a[temp][6] != a[temp-1][2]:
      dir[temp-1] = -(dir[temp])
    temp -= 1
  for i in range(4):
    a[i] = rotate(dir[i], a[i])

print(int(a[0][0]) + int(a[1][0])*2 + int(a[2][0])*4 + int(a[3][0])*8)

