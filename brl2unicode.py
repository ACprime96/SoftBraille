from six import unichr

def toUnicodeSymbols(brl, flatten=False):
    """
     Constructs the Unicode representation of a translated braille sentence.
     If flatten=False, a list is returned in the same format as the input.
     Otherwise, a string is returned with the translated Braille in Unicode.
    """
    retObj=[]

    for wrd in brl:
        print(wrd)
        retObj.append([])
        for ch in wrd:
            binary_repr = int(ch[::-1], 2)
            hex_val = hex(binary_repr)[2:]
            if len(hex_val) == 1: hex_val = "0" + hex_val

            uni_code = "28{}".format(hex_val)
            uni_code = unichr(int(uni_code, 16))
            retObj[-1].append(uni_code)

    if flatten:
        flattened_array = []
        for j in retObj:
            for i in j:
                flattened_array.append(i)

            flattened_array.append(" ") # Include a space between two words

        return "".join(flattened_array)

    return retObj
