# Sebastian Melendez Del Toro
# CIS129
class Pet:
    # Constructor
    def __init__(self):
        self.name = ""
        self.type = ""
        self.age = 0

    # Mutators
    def set_name(self, name):
        self.name = name

    def set_type(self, type):
        self.type = type

    def set_age(self, age):
        self.age = age

    # Accessors
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_age(self):
        return self.age

# Main module
def main():
    # Create a Pet object
    animal = Pet()

    # Get values for a pet
    input_name = input("Enter a pet name: ")
    animal.set_name(input_name)

    input_type = input("Enter a pet type: ")
    animal.set_type(input_type)

    input_age = int(input("Enter a pet age: "))
    animal.set_age(input_age)

    # Show values for this pet
    print("The pet name is", animal.get_name())
    print("The pet type is", animal.get_type())
    print("The pet age is", animal.get_age())


if __name__ == "__main__":
    main()

