__author__ = 'v-iganoh'

import math
from helper import Helper


class Kassiski:

    def __init__(self):
        print '__init__'

    @staticmethod
    def _char_frequency(text):
        frequencies = [0 for i in range(26)]
        text = Helper.format(text)

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
        krypto_text = Helper.format(krypto_text)
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

    @staticmethod
    def _calculate_factors(number):
        factors = []
        i = 1
        while i <= int(math.sqrt(number)):
            if number % i == 0:
                factors.append(i)
            i += 1

        ln = len(factors)
        i = ln -1
        while i >= 0:
            factors.append(number / factors[i])
            i -= 1

        return factors

    @staticmethod
    def _calculate_occurances_factor(positions):
        occurances_factors = {}
        for value in positions:
            differencies = Kassiski._calculate_diferencies(value[[i for i in value][0]])
            for diff in differencies:
                factors = Kassiski._calculate_factors(diff)
                for factor in factors:
                    if factor in occurances_factors:
                        tfactor = occurances_factors[factor]
                        occurances_factors[factor] = tfactor + 1
                    else:
                        occurances_factors[factor] = 1

        return occurances_factors

    @staticmethod
    def _calculate_key_length_estimation(occurances_factors, min_key_length, max_key_length):
        keys = occurances_factors.keys()
        max_key = 0
        max_freq = 0

        for key in keys:
            if key < min_key_length or key > max_key_length:
                continue

            freq = occurances_factors.get(key)
            if freq >= max_freq and min_key_length <= key <= max_key_length:
                max_freq = freq
                max_key = key

        if max_key < min_key_length:
            return min_key_length
        elif max_key > max_key_length:
            return max_key_length
        else:
            return max_key

    @staticmethod
    def _array_max_position(arr):
        max_position = 0

        for index, value in enumerate(arr):
            if value > arr[max_position]:
                max_position = index

        return max_position

    @staticmethod
    def _estimate_key(krypto_text, key_length):
        cip = [0 for i in range(key_length)]
        key = ''

        i = 0
        while i < key_length:
            cip[i] = ''
            i += 1

        i = 0
        while i < len(krypto_text):
            cip[i % key_length] += krypto_text[i]
            i += 1

        i = 0
        while i < key_length:
            freq = Kassiski._char_frequency(cip[i])
            key += unichr((Kassiski._array_max_position(freq) - 4) + 65)
            i += 1

        return key

    def compute(self, krypto_text, min_key_length, max_key_length):
        positions = self._find_positions(krypto_text)
        occurances_factors = Kassiski._calculate_occurances_factor(positions)

        key_lehgth_estimation = Kassiski._calculate_key_length_estimation(occurances_factors, min_key_length, max_key_length)

        return key_lehgth_estimation