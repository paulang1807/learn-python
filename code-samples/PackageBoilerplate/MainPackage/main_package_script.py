# The following is executed as soon the file is imported or invoked directly
print( "Main Package Script called")

# This will print "__main__" when the .py is invoked directly
# Prints the current package name when invoked after being imported in another module
print(f"Current package name is {__name__}")

# The following functions will be executed only when called explcitly after importing
def main_package_func():
    print("In Main Package")

def print_package_name():
    """Prints the current package name when invoked after being imported in another module
    """
    print(f"Current package name is {__name__}")