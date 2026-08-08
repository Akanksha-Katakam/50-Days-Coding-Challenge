# Day - 6 -> Text Analyser

def analyze_text(text):
    characters = len(text)
    words = text.split()
    spaces = text.count(" ")
    
    vowels = 0
    consonants = 0
    digits = 0
    special_characters = 0

    for char in text:
        if char.lower() in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1
        elif char.isdigit():
            digits += 1
        elif char != " ":
            special_characters += 1

    print("\n========== Text Analysis ==========")
    print("Characters        :", characters)
    print("Words             :", len(words))
    print("Vowels            :", vowels)
    print("Consonants        :", consonants)
    print("Spaces            :", spaces)
    print("Digits            :", digits)
    print("Special Characters:", special_characters)
    print("===================================")


# Main program
while True:
    text = input("\nEnter a sentence or paragraph: ")

    analyze_text(text)

    choice = input("\nAnalyze another text? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you!")
        break