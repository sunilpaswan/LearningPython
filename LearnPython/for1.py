words = ['hello','how','welcome','excellent','qwertw']

for s in words[:]:
    if len(s) < 4:
        words.remove(s) #It will remove the words that less than 3 letters.
        print(words)

    elif len(s) > 5:
        words.insert(0 , s)
        print (words) #It will insert the word that are greater than 5 letters