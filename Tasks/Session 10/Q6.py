
# Create a class MobilePhone with attributes: brand, model, battery_percentage.
class MobilePhone:

    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    # Increase battery
    def charge(self, percent):
        self.battery_percentage += percent

        if self.battery_percentage > 100:
            self.battery_percentage = 100

        print("Battery Percentage:", self.battery_percentage, "%")

    # Reduce battery by 1% per 10 minutes
    def use_phone(self, minutes):
        battery_used = minutes // 10
        self.battery_percentage -= battery_used

        if self.battery_percentage < 0:
            self.battery_percentage = 0

        print("Battery after usage:", self.battery_percentage, "%")

    # Show phone status
    def show_status(self):
        print("\nBrand:", self.brand)
        print("Model:", self.model)
        print("Battery:", self.battery_percentage, "%")


# Create object
phone = MobilePhone("Samsung", "Galaxy S24", 80)

# Simulate usage
phone.show_status()

phone.use_phone(30)     # Battery decreases by 3%

phone.charge(10)        # Battery increases by 10%

phone.show_status()