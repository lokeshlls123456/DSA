N = input().strip() 
K = int(input().strip()) 

if 1 <= K <= len(N):
    print(int(N[K-1])) 
else:
    print(-1)