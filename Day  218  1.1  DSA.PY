X = float(input())  
R = float(input())  
Y = float(input())  

interest = (X * R * Y) / 100
total_amount = X + interest
discount = 0.02 * interest
final_amount = total_amount - discount
print(f"Interest: {interest:.2f}")
print(f"Total Amount: {total_amount:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Settlement Amount: {final_amount:.2f}")