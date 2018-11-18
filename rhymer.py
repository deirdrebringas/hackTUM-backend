import markovify
import pronouncing
from pymongo import MongoClient
import random

class Rhymer():
    def __init__(self, collection):
        self.collection = collection
        self.markov = ""

    def reverse_sentence(self, str):
        return " ".join(str.split()[::-1])
        
    def reverse_lines(self, str_arr):
        return "\n".join(map(lambda x: self.reverse_sentence(x), str_arr))
    
    def create_backwards_corpus(self):
        corpus = []
        lines = self.collection.find({}, { "line": 1,  "_id": 0 })
        for line in lines:
            corpus.append(line["line"])
        return self.reverse_lines(corpus)
    
    def create_markov(self):
        self.markov = markovify.NewlineText(self.create_backwards_corpus())

    def choose_random_indices(self, all_lines_len, num_ind_wanted):
        return random.sample(list(range(0,all_lines_len)), num_ind_wanted)

    def generate_lines(self, num_lines, baseWord):
        all_lines = []
        rap_lines = []
        rhymes = pronouncing.rhymes(baseWord)
        for rhyme in rhymes:
            _line = self.markov.make_sentence_with_start(rhyme, strict=False, tries=10)
            if _line is not None:
                all_lines.append(_line)
        if len(all_lines) < num_lines:
            random_indices = self.choose_random_indices(len(all_lines), len(all_lines))
        else: 
            random_indices = self.choose_random_indices(len(all_lines), num_lines)
        for ind in random_indices:
            rap_lines.append(all_lines[ind])
        return self.reverse_lines(rap_lines).split("\n")