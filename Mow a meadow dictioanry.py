with open("mow.txt", "r") as my_file:
    text = str(my_file.read())
    
key = ""
my_dict = {}
for char in text:
    if char != " " and char != "," and char != "." and char != "\n":
        key = key + char
    else:
        if key not in my_dict:
            my_dict[key] = 1
        else:
            my_dict[key] += 1
        #endif
        key = ""
    #endif
#next char
print(my_dict)
