#!/usr/bin/env python3

import sys, time

class MaxMatch:
    def __init__(self, wordlist):
        self.d = []
        start = time.time()
        with open(wordlist, 'r', encoding = "UTF-8") as dictionary: 
            for word in dictionary.readlines():
                d.append(word)
        print("Initialized MaxMatch object in " + str(time.time() - start) + \
         " Seconds")

    def tokenize(self, line):
        start = time.time()
        #pord = Possible Word
        pord = line
        product = ''
        while line != '':
            if pord in self.d

        print("Tokenized Line in " + str(time.time() - start) + " Seconds")

    def process(self, input, output):
        start = time.time()
        with open(in_file, 'r', encoding = "UTF-8") as open_in:
            with open(out_file, 'w', encoding = "UTF-8") as open_out:
                for line in open_in.readlines():
                    spaced_line = maxmatch(line)
                    open_out.write(spaced_line)
        print("Tokenized " str(input) + "to" str(output) + "in" + \
         str(time.time() - start) + " Seconds")

# Default Script
if __name__ == '__main__':
    MaxMatch("./japanese_wordlist.txt").process(sys.argv[1], sys.argv[2])

