def store_water(R, H):
    pi = 3.14
    volume = pi * (R ** 2) * H
    return round(volume)

# Read inputs without extra text
R = int(input())
H = int(input())

print(store_water(R, H))