

xro = True

def TruOrFalse():
    if xro:
        return True or False

    else:
        print("nah, python is too slow, and I am too lazy, to let anyone tell me what I should code") 

TruOrFalse()

def spin_words(sentence):
    sentence = sentence[::-1]
    return sentence
print(spin_words(sentence="HELLO FAM"))


try:
    1 / 0
except ZeroDivisionError:
    print("hm")
finally:
    print("let's see")