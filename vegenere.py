__author__ = 'v-iganoh'

from helper import Helper


class Vegenere:

    def __init__(self):
        self.helper = Helper()

    def encrypt(self, plaintext, key):
        plaintext = self.helper.format(plaintext)
        key = self.helper.format(key)
        kryptotext = ''

        for index, char in enumerate(plaintext):
            plain_char = ord(char) - 65
            key_char = ord(key[index % len(key)]) - 65
            krypto_char = ((plain_char + key_char) % 26) + 65
            kryptotext += unichr(krypto_char)

        return kryptotext

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