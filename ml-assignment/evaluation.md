# Evaluation

Please provide a 1-page summary of your design choices for the Trigram Language Model.

This should include:

- How you chose to store the n-gram counts.
- How you handled text cleaning, padding, and unknown words.
- How you implemented the `generate` function and the probabilistic sampling.
- Any other design decisions you made and why you made them.

1. after searching a bit i came to know that n-gram count is key value pair , it says how many n gram appears (3 for trigram model ) in each line , so went for dictinary data structure
2. cleaning is dont by using inbuilt string functions to lower the cases , removing punctuations etc

