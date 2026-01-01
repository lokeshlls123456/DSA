n = int(input().strip())

term = 0.5
series = []

for _ in range(n):
    series.append(f"{term:.1f}")
    term *= 3
print(" ".join(series))