def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

"""Each letter is shifted down the alphabet by a fixed amount.

text is the initial text
shift is the amount of places the letters will be shifted by 

encrypt example:

cipher('this is a test', 3, encrypt=True)

decrypt example: 

cipher('this is a test', 3, encrypt=False)
"""