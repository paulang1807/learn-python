import os
from abc import ABC, abstractmethod

class ParentClass():
    # class level object attribute
    classAttr1 = 'same irrespective of instance'

    # Constructor method
    # This method is called when an object of the class is created
    # It initializes the instance variables and can take parameters
    # **kwargs allows passing a variable number of keyword arguments
    def __init__(self, var1="Val1", var2=True, **kwargs):
        for key, value in kwargs.items():
            # set self.key = value
            setattr(self,key,value)
        
        self.var1 = var1
        self.var2 = var2

        # Private variable, CANNOT be accessed outside the class
        # This variable is name-mangled to make accidental access harder (e.g., accessible as _ParentClass__varP1)
        # Trying to access this variable using just the name (__varP1) from outside the class will raise an AttributeError
        # However, it can still be accessed using the name-mangled version (_ParentClass__varP1)
        self.__varP1 = "private variable" 
        
        # Protected variable
        # It is accessible in derived class or subclasses and also from outside the class if you know the name
        self._varP2 = "protected variable"  
        # Note: Python does not have true private and protected variables, but this is a convention to indicate that the variable is intended for internal use only
        # It is not enforced by the language, but it is a good practice to follow this convention

        # Get the current directory path (similar to os.getcwd())
        # Using __file__ may raise a NameError if the code is run in an interactive environment where __file__ is not defined
        # Use __file__ if available, otherwise fallback to current working directory
        self.dir_name = os.path.dirname(__file__) if '__file__' in globals() else os.getcwd()

    # General class method
    @classmethod
    def class_meth1(cls):
        return f"class meth1 ret val: {cls.classAttr1}"

    # General static method
    @staticmethod
    def static_meth1():
        """Return a static method example string."""
        return "static meth1 ret val: static"
    
    # Method for polymorphism
    # This method can be overridden in subclasses to provide a specific implementation
    def subclass_meth(self):
        print("This method will be overridden in subclasses")

    # Getter method for a private attribute
    def get_varP1(self):
        """
        Sample function to get a private variable
        """
        return self.__varP1

    # Setter method for a private attribute
    def get_varP1(self, newValue):
        """
        Sample function to set a private variable
        """
        self.__varP1 = newValue
    
    def __str__(self):
        # Print user friendly message when the class name is being printed
        return f"Class name is {self.__class__.__name__}"

class InheritedClass(ParentClass):
    def __init__(self, valX, valY, localvalX):
        data = {
            "myName":valX,
            "varY":valY
        }
        self.localvalX = localvalX
        # Initialize parent class
        super().__init__(**data)
    
    def __del__(self):
        # Opp of __init__. Cleanup / destroy object
        # Automatically called at the end of the program
        print(f"{self.myName} destroyed!")

    # Polymorphism 
    # This method has the same name as a method in the parent class, but provides a different implementation
    def subclass_meth(self):
        print("A method with same name exists in the second inherited class as well")

    def get_class_attr_dyn(self, attrSuffix):
        """
        Sample function to get a class attribute based on a dynamically defined attr name
        """
        # Get attr name dynamically (assume parameter attrSuffix can have value 1 or 2)
        attrName = f"var{attrSuffix}"

        # Returns value for self.var1 if attrSuffix=1, self.var2 if attrSuffix = 2
        attrVal = getattr(self, attrName)
        return attrVal

class AnotherInheritedClass(ParentClass):
    def __init__(self, valX, valZ):
        data = {
            "myName":valX,
            "varZ":valZ
        }
        super().__init__(**data)

    # Polymorphism  
    # This method has the same name as a method in the parent class, but provides a different implementation
    def subclass_meth(self):
        print("A method with same name exists in the first inherited class as well")


# Multiple inheritance example
# Note: Multiple inheritance can lead to the diamond problem, where a method is inherited from multiple parent classes
# Python uses the C3 linearization algorithm to resolve this issue, ensuring a consistent method resolution order (MRO)
  
# Second parent class
# Notice that this includes ABC (Abstract Base Class) to define an abstract class
class ParentClass2(ABC):
    def __init__(self, var1="Val1"):
        
        self.varX2 = var1

    def class_meth2(self):
        return f"class meth2 ret val: {self.varX2}"
    
    # Abstract method
    # Usually does not have an implementation in the parent class
    # Subclasses must implement this method to provide a specific implementation
    # This is a way to enforce that subclasses must implement this method
    # If a subclass does not implement this method, it will raise a NotImplementedError when instantiated
    # This is useful for defining a common interface for subclasses, ensuring that they provide specific
    # implementations for certain methods while still allowing for flexibility in how those methods are implemented
    @abstractmethod
    def abs_meth(self):
        pass
    

# Class inheriting from multiple parent classes
# Note: The order of inheritance matters, as it determines the method resolution order (MRO)
# In this case, ParentClass will be checked first for methods and attributes before ParentClass2
# If a method or attribute is found in both classes, the one from ParentClass will be used
# This is known as the C3 linearization algorithm in Python
# The __init__ method of both parent classes is called, and the instance variables are initialized
class MultInheritedClass(ParentClass, ParentClass2):
    def __init__(self, valX, valY, valX2, localvalX):
        self.localvalX = localvalX
        # Initialize parent classes
        ParentClass.__init__(self, var1=valX, var2=valY)
        ParentClass2.__init__(self, var1=valX2)

        def __str__(self):
            return f"Class name is MultInheritedClass with local value {self.localvalX}"
        
        # Override the abstract method from the parent class
        # Note: Abstract methods are not enforced in Python, but it is a good practice to implement them in subclasses
        # to ensure that the subclass provides a specific implementation for the method
        # This is an example of polymorphism, where a method in the subclass has the same name as a method in the parent class
        # but provides a different implementation
        # In this case, the subclass provides a specific implementation for the abstract method abs_meth
        # defined in the parent class
        # This allows the subclass to provide its own implementation of the method, while still adhering to
        # the contract defined by the parent class
        # This method must be implemented in the subclass, otherwise it will raise a NotImplementedError
        def abs_meth(self):
            print("Implementing abstract class")
        
# Example usage of the classes defined above
tstClass1Data = {
    "valX":"Class1",
    "valY":3,
    "localvalX": "test1"
}
tstClass1 = InheritedClass(**tstClass1Data)


tstClass2Data = {
    "valX":"Class2",
    "valY":9,
    "localvalX": "test2"
}
tstClass2 = InheritedClass(**tstClass2Data)

tstClass3Data = {
    "valX":"Class3",
    "valZ":True
}
tstClass3 = AnotherInheritedClass(**tstClass3Data)

print(dir(ParentClass))
print(f"Parent object class attribute from inherited class: {tstClass1.classAttr1}")
print(f"Inherited class variables: Class1 variable - {tstClass1.myName} , Class2 variable - {tstClass2.myName} , Class3 variable - {tstClass3.varZ}")
print(f"Parent class method from inherited class: {tstClass1.class_meth1()}")
print(f"Polymorphism example: Class1 -  {tstClass2.subclass_meth()}, Class3 -  {tstClass3.subclass_meth()}")
print(tstClass1)
# del tstClass1