class My_String():
    def __init__(self, string):
        self.string = string
    #end func

    def uppercase(self):
        new = []
        for i in self.string:
            if 65 <= ord(i) <= 90:
                new.append(i)
            else:
                u = chr(ord(i) - 32)
                new.append(str(u))
            #endif
        #next i
        return new
    #end func
                 
    def lowercase(self):
        new = []
        for i in self.string:
            if 97 <= ord(i) <= 122:
                new.append(i)
            else:
                u = chr(ord(i) + 32)
                new.append(str(u))
            #endif
        #next i
        return new
    #end func
        
    
    def set_char(self, char, pos):
        new = []
        for i in self.string:
            new.append(i)
        #next i
        for k in range(0, len(new)):
            if k == pos:
                new[k] = char
            #endif
        #next k
        self.string = new
    #end func       
        
    def get_string(self):
        return self.string
    #end func
#end class


name = My_String("Carroll")
print(name.lowercase())
print(name.uppercase())
name.set_char("z", 2)
print(name.get_string())




