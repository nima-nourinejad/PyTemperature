class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __repr__(self):
        return "Temperature in Celsius is %s" % self.celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def is_colder(self, other):
        return self.celsius < other.celsius

    def is_hotter(self, other):
        return self.celsius > other.celsius

# Example usage:
temp1 = Temperature(10)
temp2 = Temperature(20)

print(temp1)  # Output: Temperature in Celsius is 10
print(temp1.celsius)  # Output: 10
print(temp1.to_fahrenheit())  # Output: 50.0
print(temp1.to_kelvin())  # Output: 283.15
print(temp1.is_colder(temp2))  # Output: True
print(temp1.is_hotter(temp2))  # Output: False
