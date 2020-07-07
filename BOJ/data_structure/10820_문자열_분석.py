'''
# 예제 입력 1
This is String
SPACE    1    SPACE
 S a M p L e I n P u T
0L1A2S3T4L5I6N7E8
'''
from sys import stdin
input = stdin.readline

while True:
  try:
    string = input()
  except:
    break
  if len(string) == 0:
    break
  count = [0] * 4
  for c in string:
    if 'a' <= c <= 'z':
      count[0] += 1
    elif 'A' <= c <= 'Z':
      count[1] += 1
    elif '0' <= c <= '9':
      count[2] += 1
    elif c == ' ':
      count[3] += 1
  print(*count)