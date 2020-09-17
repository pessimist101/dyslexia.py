import random
import string

def shuffle_word(word):
    lastCount = -1
    while word[lastCount] in string.punctuation:
        lastCount -= 1
    firstCount = 0
    while word[firstCount] in string.punctuation:
        firstCount += 1
    firstCount += 1
    if len(word[firstCount:lastCount]) <= 1:
        return word
    l = [i for i in word[firstCount:lastCount]]
    random.shuffle(l)
    return word[:firstCount] + ''.join(l) + word[lastCount:]

def dyslexia():
    sentence = input('Enter a sentence: ')
    newSentence = ' '.join([shuffle_word(word) for word in sentence.split(' ')])
    print(newSentence)

dyslexia()
