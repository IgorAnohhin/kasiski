__author__ = 'v-iganoh'

from helper import Helper


class Vegenere:

    def __init__(self):
        self.helper = Helper()

    def encrypt(self, plaintext, key):
        plaintext = self.helper.format(plaintext)
        key = self.helper.format(key)
        print ''

    def decrypt(self, kryptotext, key):
        kryptotext = self.helper.format(kryptotext)
        key = self.helper.format(key)
        plaintext = ''

        for index, char in enumerate(kryptotext):
            krypto_char = ord(char) - 65
            key_char = ord(key[index % len(key)]) - 65
            plain_char = ((krypto_char - key_char) % 26)

            if plain_char < 0:
                plain_char += 26

            plain_char += 65
            plaintext += unichr(plain_char)

        return plaintext