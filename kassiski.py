__author__ = 'v-iganoh'

from helper import Helper


class Kassiski:

    def __init__(self):
        self.helper = Helper()

    def _char_frequency(self, text):
        frequencies = [0 for i in range(26)]
        text = self.helper.format(text)

        for index, char in enumerate(text):
            frequencies[ord(char) - 65] += 1

        frequencies = [n for n in frequencies if n != 0]
        return frequencies

    def _calculate_indexes_of_coincidence(self, text):
        return self._calculate_indexes_of_coincidence_arr(self._char_frequency(text))

    @staticmethod
    def _calculate_indexes_of_coincidence_arr(frequencies):
        ind_c = 0
        summ = 0
        for f in frequencies:
            summ += f

        for f in frequencies:
            top = f * (f - 1)
            bottom = summ * (summ - 1)
            ind_c += top / bottom

        return ind_c

    def _key_length(self, krypto_text):
        ic = self._calculate_indexes_of_coincidence(krypto_text)
        top = 0.027 * len(krypto_text)
        bottom = (len(krypto_text) - 1) * ic - 0.038 * len(krypto_text) + 0.065
        estimation = top / bottom

        return estimation

    def _find_positions(self, krypto_text):
        krypto_text = self.helper.format(krypto_text)
        positions = {}

        for i in range(len(krypto_text)-2):
            sub = krypto_text[i:i+3]
            if sub in positions:
                positions[sub].append(i+1)
            else:
                positions[sub] = [i+1]

        return self._remove_zero_or_one_occurancies(positions)

    @staticmethod
    def _calculate_diferencies(positions):
        diferencies = []
        if len(positions) > 1:
            for index in range(len(positions)-1):
                diferencies.append(positions[index + 1] - positions[index])
        else:
            diferencies.append(0)
        return diferencies

    @staticmethod
    def _remove_zero_or_one_occurancies(positions):
        combination = [{value: positions[value]} for value in positions if len(positions[value]) > 1]
        return combination

    def _calculate_occurances_factor(self, positions):
        for value in positions:
            print value

            differencies = self._calculate_diferencies(value[[i for i in value][0]])
            for diff in differencies:
                factors = self._calculate_factors(diff)

            print differencies

    def compute(self, krypto_text, min_key_length, max_key_length):
        str = []
        combinations = self._find_positions(krypto_text)


        print ''