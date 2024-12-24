import os

class ParentClass:
    # class level object attribute
    classAttr1 = 'same irrespective of instance'

    def __init__(self, var1="Val1", var2=True, **kwargs):
        for key, value in kwargs.items():
            # set self.key = value
            setattr(self,key,value)
        
        self.var1 = var1
        self.var2 = var2
        # Get the current directory path (similar to os.getcwd())
        self.dir_name = os.path.dirname(__file__)

    # General class method
    @classmethod
    def class_meth1(cls):
        return f"class meth1 ret val: {cls.var2}"

    # General static method
    @staticmethod
    def static_meth1():
        return f"static meth1 ret val: static"
    
    # Abstract method
    def abs_meth(self):
        raise NotImplementedError("Subclass must implement this method")
    
    def __str__(self):
        # Print user friendly message when the class name is being printed
        return f"Class name is ParentClass"

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

    def abs_meth(self):
        print("Implementing abstract class")

    # Polymorphism
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

class AnotherInheritedClass(ParentClass):
    def __init__(self, valX, valZ):
        data = {
            "myName":valX,
            "varZ":valZ
        }
        super().__init__(**data)

    # Polymorphism
    def subclass_meth(self):
        print("A method with same name exists in the first inherited class as well")

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

print(f"Parent object class attribute from inherited class: {tstClass1.classAttr1}")
print(f"Inherited class variables: Class1 variable - {tstClass1.myName} , Class2 variable - {tstClass2.myName} , Class3 variable - {tstClass3.varZ}")
print(f"Parent class method from inherited class: {tstClass1.class_meth1()}")
print(f"Polymorphism example: Class1 -  {tstClass2.subclass_meth()}, Class3 -  {tstClass3.subclass_meth()}")
print(tstClass1)
# del tstClass1
