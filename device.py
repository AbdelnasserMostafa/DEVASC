from toolbox import generate_device_name, is_ipv4_address

class Device:
    def __init__(self, hostname): 
        self.hostname = hostname 
        self.motd = None
    
    def show(self, p = None):
        if not p:
           return str(vars(self))
        elif hasattr(self, p):
           return (getattr(self, p))
        else:
           return f">> no attribute '{p}'"


class Interface:
    def __init__(self, name, address):
        self.name = name
        self._address = address
        self.state = "Down"
        
    @property
    def address(self):
        return self._address  # Using properties in Python you can define input and output restrictions (getters and setters)
    
    @address.setter
    def address(self, value):
        if not is_ipv4_address(value):
            raise ValueError(f">> {value} is not a valid ipv4 address")
        self._address = value
        
    def __repr__(self):  # __repr__ is Python magic method for defining behavior of object print outs.
        return str(vars(self))
 
