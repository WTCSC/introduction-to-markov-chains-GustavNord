# Imports the random module
import random

# Asks for user input for a starting word and how many words to be created
word_input = input("Starting Word: ")
number_input = int(input("Number of Words: "))

# Defines what the source should be
text = "It is always a pleasure to a man in public life to meet the real governing classes. I wish to bid you welcome to Washington this evening, and to say but one word of greeting to you, and that word shall take the form of a warning. I did not speak in jest when I alluded to you as representatives of the governing classes. I think that we of the United States can not keep too fresh in our minds the fact that the men ultimately responsible for the Government are not the representatives of the people, but the people themselves, and that therefore heavy is the responsibility that lies upon the people and above all upon those who do the most toward shaping the thought of the people. In the days of my youth I was a literary man myself. In reading a book recently, a series of essays, I was immensely struck by one thought developed in it. The writer, one of our greatest scholars, was speaking of the fact that freedom could not exist unless there went with it a thorough appreciation of responsibility,[6] and he used a phrase somewhat like this—that among all peoples there must be restraint; if there is no restraint the result is inevitably anarchy. That means the negation of all government, and the negation of all government of course means the negation of popular government; and that therefore there must be restraint, and that therefore a free people had merely substituted self-restraint for external restraint; and the permanence of our freedom as a people, the permanence of our liberties, depends upon the way in which we show and exercise that self-restraint"

# Replaces the periods from the taken sources with nothing
new_text = text.replace(".", "")

# Creates a dictonary
transitions = {}

# Separating the text into words
words = new_text.split()
# Loops through the words except the last one
for i in range(len(words) - 1):
    # The current word
    current_word = words[i]
    # Word after the current word
    next_word = words[i + 1]
    # if statement that if the current word isn't in the dictionary it should create a new list for this word
    if current_word not in transitions:
        transitions[current_word] = []
        # Add the new word to the list for the current word
    transitions[current_word].append(next_word)
# Defines a function with the starting word and number of words
def generate_text(start_word, num_words):
    # Start with the start_word from user input and make a list with the words and start a counter for how many words
    current_word = start_word
    result = [current_word]
    counter = 0
    # Generate the amount of words that user input
    for _ in range(num_words - 1):
        # Checks if the current word has a list of next words
        if current_word in transitions:
            # Chooses a random word to be used next and adds the chosen word to the results and also add one to the counter
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            counter = counter + 1
            # After at least 5 words, there is a ten percent chance of a period after the last word, if so, reset the counter
            if random.random() < 0.1 and counter >= 5:
                result[-1] += '.'
                counter = 0
            # Update the current word and stop if there are no next words for the current word
            current_word = next_word
        else:
            break
            # Combine the words into a string
    return " ".join(result)
# Generates the text before capitalizing 
b4caps = generate_text(word_input, number_input)
# Splits the text to sentences and capitalizing and adding periods to them and later joining them together
sentences = b4caps.split('.')
sentences = [sentence.strip().capitalize() + '.' for sentence in sentences if sentence.strip()]
real_text = ' '.join(sentences)
# If an 'i' occurs, switch it to a 'I'
real_text = real_text.replace(" i ", " I ")
# print the final 'real' text
print(real_text)
