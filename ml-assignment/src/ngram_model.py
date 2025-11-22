import random
import string
class TrigramModel:
    def __init__(self):
        """
        Initializes the TrigramModel.
        """
        # TODO: Initialize any data structures you need to store the n-gram counts.
        self.trigramCount = {}
        

    def fit(self, text):
        """
        Trains the trigram model on the given text.

        Args:
            text (str): The text to train the model on.
        """
        # TODO: Implement the training logic.
        # This will involve:
        # 1. Cleaning the text (e.g., converting to lowercase, removing punctuation).
        # 2. Tokenizing the text into words.
        # 3. Padding the text with start and end tokens.
        # 4. Counting the trigrams.
        text = text.lower()
        translator= str.maketrans('', '', string.punctuation)
        text= text.translate(translator)
        tokens = text.split()
        tokens = ['<s>', '<s>'] + tokens + ['</s>']
        for i in range(len(tokens) - 2):
            w1, w2, w3 = tokens[i], tokens[i+1], tokens[i+2]
            trigram = (w1, w2, w3)
            if trigram in self.trigramCount:
              self.trigramCount[trigram] += 1
            else:
              self.trigramCount[trigram] = 1
    def generate(self, max_length=50):
        """
        Generates new text using the trained trigram model.

        Args:
            max_length (int): The maximum length of the generated text.

        Returns:
            str: The generated text.
        """
        # TODO: Implement the generation logic.
        # This will involve:
        # 1. Starting with the start tokens.
        # 2. Probabilistically choosing the next word based on the current context.
        # 3. Repeating until the end token is generated or the maximum length is reached.
        current_words = ['<s>', '<s>']
        generated_words = []
        for _ in range(max_length):
            context = (current_words[-2], current_words[-1])
            candidates = [(trigram[2], count) for trigram, count in self.trigramCount.items() if trigram[0] == context[0] and trigram[1] == context[1]]
            if not candidates:
                break
            total_count = sum(count for _, count in candidates)
            r = random.randint(1, total_count)
            total_count = sum(count for _, count in candidates)
            r = random.randint(1, total_count)
            cumulative = 0
            next_word = None   
            for word, count in candidates:
                cumulative += count
                if r <= cumulative:
                    next_word = word
                    break
            if next_word is None:
                break
            if next_word == '</s>':
                            break
            generated_words.append(next_word)
            current_words.append(next_word)
        return " ".join(generated_words)


