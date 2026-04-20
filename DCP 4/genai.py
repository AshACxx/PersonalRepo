# Read a sentence from the user
sentence = input("Enter a sentence: ")

# Convert to lowercase to make counting case-insensitive
sentence = sentence.lower()

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary
word_count = {}

# Count word frequency
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the dictionary
print("Word frequency:")
print(word_count)