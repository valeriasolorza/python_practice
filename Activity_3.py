def flat_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

nested_array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
result = flat_sort(nested_array)
print(result) 

# Data immutability is ensured by using pure functions that return new arrays without modifying the original input.
# This solution is a pure function because it returns a deterministic output without any side effects.
# The solution uses higher-order functions like reduce(), which takes another function as an argument.
# An imperative style might seem easier for mutability, but the functional approach offers conciseness and predictability.
# Functional programming helps solve this problem by promoting immutability, making the code easier to debug and maintain.


# Define the general Podracer class
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"


# Define AnakinsPod class that inherits from Podracer
class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2


# Define SebulbasPod class that inherits from Podracer
class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"


# Example usage:
pod1 = Podracer(500, "perfect", 10000)
pod2 = AnakinsPod(700, "repaired", 12000)
pod3 = SebulbasPod(600, "trashed", 11000)

# Repairing a podracer
pod1.repair()

# Boosting Anakin's Pod speed
pod2.boost()

# Using flame_jet to trash another podracer
pod3.flame_jet(pod1)

print(pod1.condition)  # Output: trashed
print(pod2.max_speed)  # Output: 1400

# Encapsulation bundles attributes and methods inside objects, keeping them managed and hidden.
# Abstraction hides the complexity of methods like repair, boost, and flame_jet, exposing only the necessary interface.
# Inheritance allows AnakinsPod and SebulbasPod to reuse attributes and methods from the Podracer class.
# Polymorphism allows different subclasses to use shared methods like repair, while adding their own unique methods.
