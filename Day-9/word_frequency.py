# Day - 9 -> Word Frequency Analyser

def analyze_text(text):

    text = text.lower()

    # Remove common punctuation
    for char in ".,!?;:":
        text = text.replace(char, "")

    words = text.split()
    frequency = {}

    # Count each word
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Display total and unique words
    print("\n========== Word Analysis ==========")
    print("Total Words  :", len(words))
    print("Unique Words :", len(frequency))
    print("\nWord Frequency:")

    for word in frequency:
        print(f"{word} : {frequency[word]}")

    # Find the most frequent word
    most_frequent_word = ""
    highest_count = 0

    for word in frequency:
        if frequency[word] > highest_count:
            highest_count = frequency[word]
            most_frequent_word = word

    print("\nMost Frequent Word:", most_frequent_word)
    print("Frequency:", highest_count)
    print("===================================")

while True:

    text = input("\nEnter a paragraph: ")

    analyze_text(text)

    choice = input("\nAnalyze another paragraph? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you!")
        break