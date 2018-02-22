mikra_grammata = [chr(x) for x in range(97, 123)];
megala_grammata = [chr(x) for x in range(65, 91)];

def encrypt(char, letterList):
    originalIndex = letterList.index(char)
    newIndex = originalIndex + 13
    return letterList[newIndex % len(letterList)]

sourceString = input("Grapse to keimeno:");
resultString = "";
for char in sourceString:
    if char.isupper():
            resultString += encrypt(char, megala_grammata);
    elif char.islower():
            resultString += encrypt(char, mikra_grammata);
    else:
            resultString += char;
print("H kwdikopoihsh rot 13 einai:%s" % (resultString));
            

    
    
