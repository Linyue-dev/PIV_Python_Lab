

# Generating Text

This lab is a modification from the book "The Practice of Programming" by Brian W. Kernighan and Rob Pike.


## Word counting

Code a function `word_count` that takes in file(s) and returns a dictionary containing the count of each word in the file. Each word should be converted to lowercase and punctuation removed.

**Hint:** to remove leading and tailing punctuation, you can use this:

    word = word.strip('"!“”#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ')


### Testing

Test your code with the file `pg1497.txt`. How many times does the word "philosophy" occur?


## Word following word pairs

Code a function `word_pairs` that takes in file(s) and returns a dictionary containing: for each two words in the text, the next word in the text. For example:

    and now for something completely different

would create this map:

    {
        ("and", "now"): "for",
        ("now", "for"): "something",
        ("for", "something"): "completely",
        ("something", "completely"): "different"
    }

For duplicate pairs, it doesn't really matter if you keep the first word or last word of the text.


## Generating text

Using the dictionary you create from a test file, create text in the following way:

1.  Read two words from the user `w1` and `w2`.
2.  Lookup the word pair `(w1, w2)` in the dictionary and retrieve `w3`.
3.  Collect the words in a list and repeat the steps with `w1 <- w2` and `w2 <- w3`.
4.  Print the generated text!


## Optional: Improve text generation by counting the words

Instead of taking the first/last word in the triple, for each pair in the text, count the occurrences of following words. When generating the text, you should take the word with the highest frequency.

**Hint**: you will need a dictionary with this type:

    word_counts: dict[tuple[str, str], dict[str, int]] = {}


## Optional: Improve text generation with 3 words

Instead of a pair of words, use each 3 words!

    word_counts3: dict[tuple[str, str, str], dict[str, int]] = {}

**Hint**: when generating text you might need to fall back to the `word_counts` (from the previous section), since there is less likelihood of your chosen words being `word_counts3`.


## Advice: Training data

The text in this starter is from Project Gutenberg <https://www.gutenberg.org/>. Grab more texts and add more to the dictionary!

