def donothing():
    return

def decrypt(sentence, shift):
    letters = list(sentence)
    code = 0
    for j in range(len(letters)):
        if ord(letters[j]) == 32:
            donothing()
        else:
            code = ord(letters[j]) - shift
            letters[j] = chr(code)
    result = "".join(letters)
    return result