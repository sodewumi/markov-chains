from sys import argv

script, corpus_path = argv

def make_chains(corpus_path):
    """Takes input text as string; returns dictionary of markov chains."""
    corpus_txt = open(corpus_path)
    bi_grams = {}
    
    text = corpus_txt.read().split()

    for wrd in range(len(text)-2):
        key = (text[wrd], text[wrd +1])
        nxt_wrd = text[wrd + 2]

        if key not in bi_grams.keys():
            bi_grams[key] = [nxt_wrd]
        else:
            bi_grams[key].append(nxt_wrd)

        # Another way to preform the if else statement above
        # bi_grams[key] = bigrams.get(key, []).append(nxt_wrd)

    # return {}
    return bi_grams


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = "Some text"

# Get a Markov chain
chain_dict = make_chains(corpus_path)
print(chain_dict)

# Produce random text
random_text = make_text(chain_dict)

print random_text
