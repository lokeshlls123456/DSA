n = int(input().strip()) 

series = [str(i**2) for i in range(1, n+1)]  
print(" ".join(series))