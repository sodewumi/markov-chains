from sys import argv

script, corpus = argv

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    corpus_txt = open(corpus)
    for line in corpus_txt:
        line = line.rstrip()
        print line
    # return {}


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = "Some text"

# Get a Markov chain
chain_dict = make_chains(corpus)

# Produce random text
random_text = make_text(chain_dict)

print random_text
