#1

import math

class Circle:
    def __init__(self, radii_list):
        self.radii = radii_list  # Store the list of radii

    def area(self, radius):
        """Calculates the area of a circle given its radius."""
        return math.pi * radius ** 2

    def circumference(self, radius):
        """Calculates the circumference of a circle given its radius."""
        return 2 * math.pi * radius

    def circle_properties(self):
        """Returns the area and circumference for each radius in the list."""
        properties = []
        for radius in self.radii:
            area = self.area(radius)
            circumference = self.circumference(radius)
            properties.append({
                'radius': radius,
                'area': area,
                'circumference': circumference
            })
        return properties

# Example usage
radii_list = [10, 501, 22, 100, 999, 87, 351]
circle = Circle(radii_list)

# Get the properties (area and circumference) of all circles
circle_info = circle.circle_properties()

# Print the results
for info in circle_info:
    print(f"Radius: {info['radius']} | Area: {info['area']:.2f} | Circumference: {info['circumference']:.2f}")

#2

class Circle:
    # Private variable
    __Ip = 3.141

    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        # Using the private variable __Ip to calculate the area of the circle
        area = Circle.__Ip * (self.radius ** 2)
        return area

    def get_ip_value(self):
        # Method to return the value of the private variable __Ip
        return Circle.__Ip


# Example usage
circle = Circle(5)
area = circle.calculate_area()
ip_value = circle.get_ip_value()

print(f"Area of the circle: {area}")
print(f"Value of Ip: {ip_value}")


#3

class ShapeCalculator:
    def __init__(self, sides):
        self.sides = sides  # List of side lengths
    
    def area(self):
        # Calculate area for each side assuming it's a square
        areas = [side ** 2 for side in self.sides]
        return areas
    
    def perimeter(self):
        # Calculate perimeter for each side assuming it's a square
        perimeters = [4 * side for side in self.sides]
        return perimeters


# Given list of numbers
side_lengths = [10, 501, 22, 37, 100, 999, 87, 351]

# Create an instance of ShapeCalculator
calculator = ShapeCalculator(side_lengths)

# Calculate the areas and perimeters
areas = calculator.area()
perimeters = calculator.perimeter()

# Print the results
print("Side lengths:", side_lengths)
print("Areas of squares:", areas)
print("Perimeters of squares:", perimeters)



#4

# Part A: Base TV Class
class TV:
    def __init__(self, brand, inches=None):
        self.brand = brand
        self.channel = 1  # Default channel
        self.volume = 50  # Default volume
        self.on = False  # TV is off by default
        self.inches = inches  # Optional size of the TV
        
    def increase_volume(self):
        """Increase volume, max 100"""
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume cannot be increased beyond 100.")
    
    def decrease_volume(self):
        """Decrease volume, min 0"""
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume cannot be decreased below 0.")
    
    def set_channel(self, channel):
        """Set the channel, max 50 channels"""
        if 1 <= channel <= 50:
            self.channel = channel
        else:
            print(f"Channel must be between 1 and 50. Staying at current channel {self.channel}.")
    
    def reset_tv(self):
        """Reset TV to channel 1 and volume 50"""
        self.channel = 1
        self.volume = 50
        print("TV has been reset.")
    
    def status(self):
        """Display current status of the TV"""
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

# Part B: LED TV Class
class LedTV(TV):
    def __init__(self, brand, inches=None, screen_thickness=None, energy_usage=None, lifespan=None, refresh_rate=None):
        super().__init__(brand, inches)
        # Additional properties for LedTV
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        
    def display_details(self):
        """Display detailed features of the LED TV"""
        details = (
            f"LED TV - Brand: {self.brand}\n"
            f"Screen Size: {self.inches} inches\n"
            f"Screen Thickness: {self.screen_thickness} cm\n"
            f"Energy Usage: {self.energy_usage} W\n"
            f"Lifespan: {self.lifespan} hours\n"
            f"Refresh Rate: {self.refresh_rate} Hz\n"
        )
        return details
    
    def viewing_angle(self):
        """Display the viewing angle of the LED TV"""
        print(f"Viewing angle: 178 degrees (LED TV standard)")

    def backlight(self):
        """Display backlight information"""
        print("Backlight: Adjustable, LED panel")

# Part B: Plasma TV Class
class PlasmaTV(TV):
    def __init__(self, brand, inches=None, screen_thickness=None, energy_usage=None, lifespan=None, refresh_rate=None):
        super().__init__(brand, inches)
        # Additional properties for PlasmaTV
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        
    def display_details(self):
        """Display detailed features of the Plasma TV"""
        details = (
            f"Plasma TV - Brand: {self.brand}\n"
            f"Screen Size: {self.inches} inches\n"
            f"Screen Thickness: {self.screen_thickness} cm\n"
            f"Energy Usage: {self.energy_usage} W\n"
            f"Lifespan: {self.lifespan} hours\n"
            f"Refresh Rate: {self.refresh_rate} Hz\n"
        )
        return details
    
    def viewing_angle(self):
        """Display the viewing angle of the Plasma TV"""
        print(f"Viewing angle: 160 degrees (Plasma TV standard)")

    def backlight(self):
        """Display backlight information"""
        print("Backlight: No adjustable backlight for Plasma panels.")

# Example Usage

# Create a TV object
tv = TV(brand="Panasonic", inches=42)
print(tv.status())  # Print status of TV
tv.increase_volume()
tv.set_channel(8)
print(tv.status())  # Check status after changes

# Reset the TV
tv.reset_tv()
print(tv.status())  # TV reset to defaults

# Create a LED TV object
led_tv = LedTV(brand="Samsung", inches=55, screen_thickness=5, energy_usage=100, lifespan=50000, refresh_rate=120)
print(led_tv.display_details())  # Print LED TV details
led_tv.viewing_angle()  # Display viewing angle
led_tv.backlight()  # Display backlight info

# Create a Plasma TV object
plasma_tv = PlasmaTV(brand="LG", inches=60, screen_thickness=10, energy_usage=200, lifespan=60000, refresh_rate=60)
print(plasma_tv.display_details())  # Print Plasma TV details
plasma_tv.viewing_angle()  # Display viewing angle
plasma_tv.backlight()  # Display backlight info
