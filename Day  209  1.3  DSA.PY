age = int(input().strip())
show_time = float(input().strip())

if show_time == 13.30:
    price = 2.00
else:
    if age > 13:
        price = 5.00 
    else:
        price = 2.00   
print(f"${price:.2f}")