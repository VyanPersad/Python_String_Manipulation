def stringLength():
    s=input("Type string here --> ")
    print("The string length is "+str(len(s))+".")

#stringLength()    

def printChar():
    s=input("Type string here --> ")
    if len(string) == 0:
        print("String is Empty")
    elif i<len(s):
        print(string(i))
    else:
        print("Out of Range")    

def reverseString():
    s=input("Type string here --> ")
    #This is a specific syntax
    #[start:stop:step]
    #By leaving the params blank the default values 
    #This is the simplest and quickest way
    print(s[::-1])
    #Reversed is a built in function that returns 
    #the sequence as a list
    reversed_list = "".join(reversed(s))
    print(reversed_list)

def firstANDlast():
    #Prints the first and last n characters of a string
    s=input("Type string here --> ")
    numChars=input("Type number to chars to print --> ")
    if len(s)>numChars*2:
        #[:n] will slice from 1 to 3 but not the 3rd char.
        #[len()-n] will slice from the (end-n) char to the end.
        firstandlast = s[:numChars] + s[len(s)-numChars:]
        print(firstandlast)
    else:
        print("Word too short")    

def removeChar():
    edited_str=""
    s=input("Type string here --> ")
    #You can also use the range(a,b,c)
    #Where a = start, b = length of seq, c = increment
    #In this case you won't need the if statement
    for i in range(len(s)):
        if i % 2 != 0:
            edited_str=edited_str+s[i]

    print(edited_str)  

def removeNums():
    showNum=""
    s=input("Type string here --> ")
    for i in s:
        if i.isdecimal():
            showNum=showNum+s[i]

    print(showNum)


def removespecChar():
    #Removes a specific character from the string
    s=input("Type string here --> ")
    chartoRem = 3

    if (len(s)==0)or(chartoRem>=len(s)):
        print(s)
    else:
        removeStr = ""
        for i in range(len(s)):
            if i!=chartoRem:
                removeStr=removeStr+s[i]    
        print(removeStr)

def replaceChar():
    s=input("Type string here --> ")
    replacedStr=""
    curr_char = "a"
    new_Char = "!"

    for char in s:
        #Within the loop you can use a built in function
        #replace(char_to_replace,char_to replace_with)
        #
        #s.replace("a","!")
        #That should work
        #print(s.replace("a","!"))
        #This will output it as well
        if char == curr_char:
            replacedStr=replacedStr+new_Char
        else:
            replacedStr=replacedStr+char    

    print(replacedStr)

  



        
