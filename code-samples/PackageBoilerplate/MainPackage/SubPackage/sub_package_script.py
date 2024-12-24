# The following is executed as soon the file is imported or invoked directly
print( "Sub Package Script called")

# The following functions will be executed only when called explcitly after importing
def sub_package_func():
    print("In Sub Package")