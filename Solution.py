# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

for i in range(int(input())):
    ar =  input().strip().split()
    if(ar[0] == 'append'):
        d.append(ar[1])
    elif(ar[0] == 'pop'):
        d.pop()
    elif(ar[0] == 'popleft'):
        d.popleft()
    elif(ar[0] == 'appendleft'):
        d.appendleft(ar[1])
        
print(' '.join(d))
