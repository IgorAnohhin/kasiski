__author__ = 'v-iganoh'


from syt import Syt
from vegenere import Vegenere
from kassiski import Kassiski


key = 'janet'
krypto_text = 'CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE'
plain_text = 'THEALMONDTREEWASINTENTATIVEBLOSSOMTHEDAYSWERELONGEROFTENENDINGWITHMAGNIFICENTEVENINGSOFCORRUGATEDPINKSKIESTHEHUNTINGSEASONWASOVERWITHHOUNDSANDGUNSPUTAWAYFORSIXMONTHSTHEVINEYARDSWEREBUSYAGAINASTHEWELLORGANIZEDFARMERSTREATEDTHEIRVINESANDTHEMORELACKADAISICALNEIGHBORSHURRIEDTODOTHEPRUNINGTHEYSHOULDHAVEDONEINNOVEMBER'

data = [165, 235, 275, 285]
syt = Syt()
result = syt.compute(data)
print 'Result : %s' % result
assert(5 == result)
print ''

vegenere = Vegenere()
dekripted = vegenere.decrypt(krypto_text, key)
print plain_text
print dekripted
assert(plain_text == dekripted)
print ''

encrypted = vegenere.encrypt(plain_text, key)
print krypto_text
print encrypted
assert(krypto_text == encrypted)
print ''

text = 'abbvvvggggddddd'
kassiski = Kassiski()
frequencies = kassiski._char_frequency(text)
frequencies.sort()
assert(frequencies == [1, 2, 3, 4, 5]), 'real %s expected %s' % (frequencies, [1, 2, 3, 4, 5])
print ''

kassiski = Kassiski()
ic = kassiski._calculate_indexes_of_coincidence(krypto_text)
print ic
print ''

kassiski = Kassiski()
estimation = kassiski._key_length(krypto_text)
print estimation
print ''

kassiski = Kassiski()
positions = kassiski._find_positions(krypto_text)
print positions[0]
print positions
print ''
factors = kassiski._calculate_occurances_factor(positions)
print factors
print ''