# Set variables

adj_description = "Adjectives are words that describe the qualities or states of being of nouns: enormous, doglike, silly, yellow, fun, fast. They can also describe the quantity of nouns: many, few, millions, eleven"
noun_description = "A noun is a word that refers to a thing (book), a person (Betty Crocker), an animal (cat), a place (Omaha), a quality (softness), an idea (justice), or an action (yodeling)."

# Give description of what everything is

grammar = input("Before we begin, do you need a refresher with your English grammar? ").lower()

if grammar == "yes":
    print("\n")
    print(adj_description)
    print("\n")
    print(noun_description)
    print("\n")
else:

    # Set input variables
    adj1 = input("Give me an adjective: ")
    noun1 = input("Give me a noun: ")
    pluralNoun = input("Give me a plural noun: ")
    personInRoom = input("Give the name of someone in the room: ")
    adj2 = input("Give me an adjective: ")


    # Print out madlib story

    print(f'There are many {adj1} ways to choose a/an {noun1} to read.')
    print(f'First, you could ask for recommendations from friends and {pluralNoun} .')
