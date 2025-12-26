n = int(input().strip())  

run_rate = 95.0
increment = 20.5

series = []

for _ in range(n):
    series.append(f"{run_rate:.1f}")
    run_rate += increment

print(" ".join(series))