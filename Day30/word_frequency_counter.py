from collections import Counter
import string

class WordFrequencyCounter:
    def __init__(self):
        self.word_count = Counter()

    def process_text(self, text):
        # Remove punctuation and convert text to lowercase
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator).lower()

        # Split text into words
        words = cleaned_text.split()

        # Update word count
        self.word_count.update(words)

    def display_frequencies(self):
        if not self.word_count:
            print("No words found.")
        else:
            print("Word Frequencies:")
            for word, count in self.word_count.items():
                print(f"'{word}': {count} times")


def main():
    word_counter = WordFrequencyCounter()

    # Ask the user for text input
    print("Enter text (type 'STOP' to finish):")
    while True:
        user_input = input()
        if user_input.strip().upper() == 'STOP':
            break
        word_counter.process_text(user_input)

    # Display word frequencies
    word_counter.display_frequencies()


if __name__ == "__main__":
    main()
