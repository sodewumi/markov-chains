from sys import argv
import random

script, corpus_path = argv

def make_chains(corpus_path):
    """Takes input text as string; returns dictionary of markov chains."""
    corpus_txt = open(corpus_path)
    bi_grams = {}
    
    text = corpus_txt.read().split()

    for wrd in range(len(text)-2):
        key = (text[wrd], text[wrd +1])
        nxt_tupple = text[wrd + 2]

        if key not in bi_grams.keys():
            bi_grams[key] = [nxt_tupple]
        else:
            bi_grams[key].append(nxt_tupple)

        # Another way to preform the if else statement above:
        # bi_grams[key] = bigrams.setDefault(key, []).append(nxt_tupple)
    return bi_grams


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # choose a random bi-gram then find the value of said bi-gram. 
    # Afterward choose a random value from the generated list
    rndm_bi_gram = random.choice(chains.keys())
    rndm_wrd = random.choice(chains[rndm_bi_gram])
    generated_txt = rndm_wrd

    # the last word from the previous bi-gram key along with the randomly
    # choosen word is saved for the next iteration of the while loop
    nxt_tupple = (rndm_bi_gram[1], rndm_wrd)
    bi_gram_value = chains.get(nxt_tupple)

    while bi_gram_value:
        # the random word is put in the first element of the nxt word tuple,
        # and the second element is the newly choosen random word.
        new_rndm_wrd = random.choice(bi_gram_value)
        generated_txt = generated_txt +" "+ new_rndm_wrd
        nxt_tupple = (nxt_tupple[1], new_rndm_wrd)

        # if the bi-gram from the previous while loop has a value, return it
        # If there is not a value, return None and close the loop
        bi_gram_value = chains.get(nxt_tupple)


    return generated_txt


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = "Some text"

# Get a Markov chain
chain_dict = make_chains(corpus_path)

# Produce random text
random_text = make_text(chain_dict)

print random_text
