#5 -> Function  simpleGreetings to accept name as input and print simple greetings Namaskara name
def simpleGreetings():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print(f"Namaskara {name}")
    print(f"You are  {age} years old now")

#6-> Function to Print ASCII  values of string input

def printASCIIOfString(string):
    for character in string:
        ascii_value = ord(character)
        print(f"{character} -> {ascii_value}")


def invoke_printASCIIOfString():    
    printASCIIOfString("abc")
    printASCIIOfString("123")
    printASCIIOfString("ABC")


# 7-> Function to getStrlength to get string length

def getStrLength(string)->int:
    counter = 0
    
    if string != None:
        for character in string:
            counter = counter + 1

    return counter

def invoke_getStrLength():
    input1 = None # NULL 
    length = getStrLength(input1)
    print(f"String length of {input1} is {length}")

    input2 = "" # Empty string
    print(f"String length of {input2} is {getStrLength(input2)}")

    input3 = "m" # only one item is present
    print(f"String length of {input3} is {getStrLength(input3)}")

    input4 = "mahesh" # many items are present
    print(f"String length of {input4} is {getStrLength(input4)}")