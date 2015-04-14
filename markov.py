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
        nxt_wrd = text[wrd + 2]

        if key not in bi_grams.keys():
            bi_grams[key] = [nxt_wrd]
        else:
            bi_grams[key].append(nxt_wrd)

        # Another way to preform the if else statement above:
        # bi_grams[key] = bigrams.get(key, []).append(nxt_wrd)
    return bi_grams


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    generated_txt = ""
    stopped = False
    nxt_wrd = None

    while not stopped:
        if nxt_wrd == None:
            # choose a random bi-gram
            rndm_bi_gram = random.choice(chains.keys())
            # print rndm_bi_gram, "randomly choosen bi-gram"
            rndm_bi_gram_value = chains[rndm_bi_gram]
            rndm_wrd = random.choice(rndm_bi_gram_value)
            # print rndm_wrd, "first rndm word"

            generated_txt = generated_txt +" "+ rndm_wrd
            nxt_wrd = (rndm_bi_gram[1], rndm_wrd)
            # print nxt_wrd, "first next word"
        else:
            bi_gram_value = chains.get(nxt_wrd, None)
            if bi_gram_value == None:
                stopped = True
            else:
                previous_rndm_wrd = rndm_wrd
                new_rndm_wrd = random.choice(bi_gram_value)
                # print new_rndm_wrd, "rnm word"
                generated_txt = generated_txt +" "+ new_rndm_wrd
                nxt_wrd = (previous_rndm_wrd, new_rndm_wrd)
                # print nxt_wrd, "next word"


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
