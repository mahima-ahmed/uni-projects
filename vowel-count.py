# Implement a recursive function that counts the number of vowels in a phrase or word.
def vocal_count (w):
    if (len(w) == 0):
        return 0
    else:
        if (w [0] in 'aeiouAEIOU'):
            return 1 + vocal_count(w[1:])
        else:
            return 0 + vocal_count(w[1:])

sentence = input('Enter a word or a sentence: ')
print ('The sentence or word has', vocal_count(sentence), 'vowels.')
