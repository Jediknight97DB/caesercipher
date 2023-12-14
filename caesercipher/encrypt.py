def donothing():
    return

def encrypt(sentence, shift = 4 ):
    letters = list(sentence)
    code = 0
    for i in range(len(letters)):
        if ord(letters[i]) == 32:
            donothing()
        else:
            code = ord(letters[i]) + shift
            letters[i] = chr(code)
    result = "".join(letters)
    return result