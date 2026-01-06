#8-> Function to Count vowels  getCountOfOvewel for a given string

def count_vowels(string)-> int:
    counter = 0

    #This was to show another not so good way to write if statement
    # if (character == 'a' or character == 'e' or  character == 'i' or character == 'o' or character == 'u' or character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U'):

    if string is not None:  # if (string != NULL) this is how we write this in C
        for character in string:
            if (character == 'a' or
                character == 'e' or 
                character == 'i' or 
                character == 'o' or 
                character == 'u' or 
                character == 'A' or 
                character == 'E' or 
                character == 'I' or 
                character == 'O' or 
                character == 'U'):
                counter +=1  # counter = counter + 1
    
    return counter

def invoke_count_vowels():
    input = "mahesh"
    print(f"Number of vowels in {input} is = {count_vowels(input)}")

    input = None
    print(f"Number of vowels in {input} is = {count_vowels(input)}")

    input = ""
    print(f"Number of vowels in {input} is = {count_vowels(input)}")

    input = "a"
    print(f"Number of vowels in {input} is = {count_vowels(input)}")

    input = "123"
    print(f"Number of vowels in {input} is = {count_vowels(input)}")



#9 - Function to Reverse string reverseString 

def reverseString(string)->str:

    length = len(string)
    
    #for start, end in zip(range(0,length, 1), range(length-1, -1, -1)):
        #print(f"Start = {start} end = {end}")
        #string[start], string[end] = string[end], string[start]

    reversedString = ""
    for end in range(length-1, -1, -1):
        reversedString += string[end]
    
    return reversedString

def invoke_stringReverse():
    name = "abcde"
    name = reverseString(name)
    print(name)

# 10 - Function to get sum of all elements in the integer array getSum

def getSum(numbers)->int:

    sumOfElements = 0
    for number in numbers:
        sumOfElements = sumOfElements + number
    
    return sumOfElements

def getSumV2(numbers: list):

    sumOfElements = 0
    length = len(numbers)
    
    for index in range(0, length, 1):
        sumOfElements = sumOfElements + numbers[index]
    
    return sumOfElements


def invoke_getSum():
    numbers = [1,2,3]

    #numbers = [1.1,2.1,3.1]
    #sumOfNumbers = getSum(numbers)

    sumOfNumbers = getSumV2(numbers)
    print(f"Sum of numbers = {sumOfNumbers}")