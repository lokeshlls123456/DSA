import math

value = float(input())

truncated = int(value)
rounded_up = math.ceil(value)
rounded_down = math.floor(value)

print(truncated)
print(rounded_up)
print(rounded_down)