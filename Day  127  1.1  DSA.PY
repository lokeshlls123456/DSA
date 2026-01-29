def detectPerfectNumber(n):
    if n <= 1:
        return 0
    
    sum_div = 1  # 1 is always a proper divisor for n > 1
    sqrt_n = int(n**0.5)
    
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            sum_div += i
            counterpart = n // i
            if counterpart != i:
                sum_div += counterpart
    
    return 1 if sum_div == n else sum_div