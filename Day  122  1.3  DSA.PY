n = int(input().strip())

series = []

for i in range(n):
    if i == 0:
        series.append(6)  # 1st term
    elif i == 1:
        series.append(11)  # 2nd term
    else:
    
        next_term = series[-1] + 5 * i
        series.append(next_term)

print(" ".join(map(str, series)))