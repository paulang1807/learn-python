class ConfigSingleton:
    def __new__(cls):
        """creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, "instance"):
            cls.instance = super(ConfigSingleton, cls).__new__(cls)
        return cls.instance
    
    config1="config_val1"
    config2="config_val2" 