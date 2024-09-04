# Function to print a greeting
def hello():
    print("Hello! Nice to see you.")

# Function to pack three arguments into a list
def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

# Function to print out what you are eating for lunch
def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {lunch_items[0]}")
        for item in lunch_items[1:]:
            print(f"Next I eat {item}")

# Test the functions
hello()
print(pack("sandwich", "chips", "apple"))
eat_lunch(["sandwich", "chips", "apple"])
eat_lunch([])
