#interactive input
sentence = input("Enter the sentence to be reversed")

#split the sentence to extract individual words
words = sentence.split()

#Reverse the Order of Words in the Sentence
reversed_words = words[::-1]
reversed_sentence = " ".join(reversed_words)

print(reversed_sentence)
