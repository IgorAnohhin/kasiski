__author__ = 'v-iganoh'

from helper import Helper


class Kassiski:

    def __init__(self):
        self.helper = Helper()

    def _char_frequency(self, text):
        frequencies = [i for i in range(26)]
        text = self.helper.format(text)

        for index, char in enumerate(text):
            frequencies[ord(char) - 65] += 1

        return frequencies

    def compute(self):
        print ''