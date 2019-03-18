#!/usr/bin/env python3

import sys, time

class MaxMatch:
    def __init__(self, wordlist):
        self.d = []
        start = time.time()
        with open(wordlist, 'r', encoding = "UTF-8") as dictionary: 
            for word in dictionary.readlines():
                if word[-1] == '\n':
                    word = word[:-1]
                self.d.append(word)
        print("Initialized MaxMatch object in " + str(round(time.time() - start, 2)) + \
         " Seconds")

    def tokenize(self, line):
        start = time.time()
        line = line.replace(' ','').replace('\n','')
        #pord means Possible Word
        pord = line
        product = ''
        while len(line) > 0:
            if pord in self.d:
                product += pord + ' '
                line = line[len(pord):]
                pord = line
            elif len(pord) == 1:
                product += pord + ' '
                line = line[len(pord):]
                pord = line
            else:
                pord = pord[:-1]
        product += '\n'
        print("Tokenized Line in " + str(round(time.time() - start, 2)) + " Seconds")
        return product

    def process(self, input, output):
        start = time.time()
        with open(input, 'r', encoding = "UTF-8") as open_in:
            with open(output, 'w', encoding = "UTF-8") as open_out:
                for line in open_in.readlines():
                    spaced_line = self.tokenize(line)
                    open_out.write(spaced_line)
        print("Tokenized " + input + " to " + output + " in " + \
         str(round(time.time() - start, 2)) + " Seconds")

#Actual Execution is Here
MaxMatch("./japanese_wordlist.txt").process(sys.argv[1], sys.argv[2])

