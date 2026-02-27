class Person:
    def __init__(self):
        line = input("Enter the venue details").strip()
        if ',' in line:
            parts = line.rsplit(',', 1)
            self.name = parts[0].strip()
            self.age = parts[1].strip()

p1 = Person()
print("\nVenue Details")
print("Venue Name : " + p1.name)
print("City Name : " + p1.age)