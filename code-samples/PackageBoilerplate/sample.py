from MainPackage import main_package_script
from MainPackage.SubPackage import sub_package_script

# The following is executed only if the .py file is called directly
# It does not get executed if the file is imported
if __name__ == "__main__":
    # Execute functions from main package
    main_package_script.print_package_name()
    main_package_script.main_package_func()

    # Execute function from sub package
    sub_package_script.sub_package_func()