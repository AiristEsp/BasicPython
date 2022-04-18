programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again.",
"Loop": "The action of doing somthing over and over again"
}

programming_dictionary["Greeting"] = "Hello , How re you today?"


# Create Empty Dictionary
programming_dictionary["Bug"] = "A moth in yout computer"
print(programming_dictionary["Bug"])

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
