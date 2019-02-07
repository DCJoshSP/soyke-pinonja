class My_String():
    def __init__(self, string):
        self.string = string

    def uppercase(self):
        new = ""
        for i in self.string:
            if 65 <= ord(i) <= 90:
                new = new + i
            else:
                u = chr(ord(i) - 32)
                new = new + str(u)
        return new
                 
    def lowercase(self):
        new = ""
        for i in self.string:
            if 97 <= ord(i) <= 122:
                new = new + i
            else:
                u = chr(ord(i) + 32)
                new = new + str(u)
        return new
    
    def set_string(self, new_string):
        self.string = new_string
        
    def get_string(self):
        return self.string
#end class


name = My_String("Carroll")
print(name.lowercase())
print(name.uppercase())
name.set_string("Cartwright")
print(name.get_string())




