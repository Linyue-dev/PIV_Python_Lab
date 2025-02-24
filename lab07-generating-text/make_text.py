import sys
from traceback import print_tb

def word_count(texts: list[str]) -> dict:
    # TODO modify as needed
    # create a dict and initialize it
    words: dict ={}
    # count of split word
    total: int = 0
    for text in texts:
        fh = open(text)
        for line in map(str.strip, fh):
            for word in line.lower().split():
                word = word.strip('"!“”#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ')
                # "philosophy,--he" still cannot strip(), so use replace()
                word = word.replace(',--', ' ').replace('--', ' ')
                for w in word.split():
                    # total += 1 # 220044 words
                    # print(w)
                    # create variable count
                    count: int = 0
                    for char in w:
                        count += 1
                    words[w] = count
        fh.close()
    # print(f"total word: {total}")
    return words
def make_word_pairs(texts: list[str]) -> dict:
    # create a dict and initialize it
    # word_pairs: dict[tuple, list] = {} why value is list??
    word_pairs: dict [tuple,list]= {}
    # count of split word
    total: int = 0
    for text in texts:
        w2 = None
        w3 = None
        with open(text) as fh:
            for line in map(str.strip,fh):
                for word in line.lower().split():
                    word = word.strip('"!“”#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ')
                    # total += 1 # 219259 words
                    # print(word)
                    w1,w2,w3 = w2,w3,word
                    pairs = (w1,w2)
                    if pairs not in word_pairs:
                        word_pairs[pairs] = []
                    word_pairs[pairs].append(w3)
    # print(f"total word: {total}")
    return word_pairs

def generating_text(texts: list[str]) -> list[str]:
    # create a list and initialize it
    generate_text: list[str] = []
    # user input two string words
    w1:str = input("enter a word: ")
    w2:str = input("enter a word again: ")

    word_pairs: dict[tuple,list] = make_word_pairs(texts)
    first_pair: tuple =(w1, w2)
    if first_pair in word_pairs:
        # Add w1 and w2 in the list
        generate_text.append(w1)
        generate_text.append(w2)
        while first_pair in word_pairs:
            w3_list:list = word_pairs[first_pair]
            w3 = w3_list[0]
            generate_text.append(w3)
            w1 = w2
            w2 = w3
            first_pair = (w1,w2)
    return generate_text


def main(texts: list[str]):
    # TODO Word counting
    words: dict = word_count(texts)
    # count:int = 0
    # for key in words:
    #     if key == 'philosophy':
    #         count += 1
    #     print(key)
    # if count == 0:
    #     print(f"philosophy doesn't in words")
    # else:
    #     print(f"philosophy occur {count} times")

    # TODO Word Pairs
    # word_pairs: dict = make_word_pairs(texts)
    # for key, value in word_pairs.items():
    #     print(f"{key}: {value}")



    # TODO generated text
    # generate_text:list = generating_text(texts)
    print(generating_text(texts))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main(["pg1497.txt"])
