import english as eng
import brl2unicode
import nemethSystem as nm

def text2nemeth(checkStr):
    brl=[]
    index = 0
    numericIndicator = False

    while(index<len(checkStr)):

        #Accommodating for white space
        if(checkStr[index]==' '):
            brl.append('000000')
            index += 1
            continue

        # if(checkStr[index]=='"' or checkStr[index]=="'"):

        # Checking for ^, indicative of need to use superscript indicator
        if(checkStr[index] == '^'):
            brl.append(eng.punctuations['%superscript'])
            index += 1
            numericIndicator = True     # Setting NumericIndicator to True prevents it being appended
                                        # before number in the power
            continue

        #Checking if the character is a decimal point (Page 11)
        if(checkStr[index]=='.'):
            if(index<len(checkStr)-1 and checkStr[index+1].isdigit()):
                if(index==0 or (index>0 and not checkStr[index-1].isdigit())):
                    brl.append(nm.numericIndicator)
                    numericIndicator = True
                brl.append(nm.decimalPoint)
                index += 1
                continue
            else:
                brl.append(eng.specialCharacters['.'])
                numericIndicator = False
                index += 1
                continue

        #Checking if the comma is a mathematics comma or not
        if(checkStr[index]==','):
            if(index < len(checkStr) - 1 and checkStr[index + 1].isdigit() and checkStr[index-1].isdigit()):
                brl.append(nm.mathComma)
                index += 1
                continue

        # Checking if the character is a digit (Page 12)
        print(checkStr[index])
        if(checkStr[index].isdigit()):
            if(not numericIndicator):
                brl.append(nm.numericIndicator)
            numericIndicator = True
            brl.append(nm.digits[checkStr[index]])
            index += 1
            continue

        #Checking if the character is a mathematical symbol (Page 12)
        if(checkStr[index] in nm.mathsym.keys()):
            data = nm.mathsym[checkStr[index]]
            print(len(data),checkStr[index])
            if(len(data)>6):
                data = map(''.join, zip(*[iter(data)] * 6))
                brl += list(data)
            else:
                brl.append(data)
            print(brl)
            index += 1
            continue

        #Checking if the character is an alphabet (Page 12)
        if(checkStr[index].isalpha()):
            if(checkStr[index].isupper()):
                brl.append(eng.specialCharacters['%capital'])
            brl.append(eng.alphabet[checkStr[index].lower()])
            numericIndicator = False        #Setting numericIndicator to False allows for the numeric indicator to be added later on
            index += 1
            continue

        #Checking for English Punctuations
        if(checkStr[index] in eng.punctuations.keys()):
            brl.append(eng.punctuations[checkStr[index]])
            index += 1
            continue

        if(checkStr[index] in eng.specialCharacters.keys()):
            brl.append(eng.specialCharacters[checkStr[index]])
            index += 1
            continue
    return(brl2unicode.toUnicodeSymbols([brl], flatten=True))
