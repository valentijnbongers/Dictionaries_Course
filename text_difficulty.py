import string
with open("romeojuliet.txt", "r") as textfile:
    text = textfile.read()

#make the whole text lowercase
text = text.lower()

#replace every punctuation in the text with ''
text = text.translate(str.maketrans('', '', string.punctuation))

#turns the list of words into a 1D table, each cell contains 1 word
words = text.split()

#creates dictionary with word as key and count as value
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Number of different words:", len(word_count))
print("List of words and count:", word_count)
