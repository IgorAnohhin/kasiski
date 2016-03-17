__author__ = 'v-iganoh'


from syt import Syt
from vegenere import Vegenere
from kassiski import Kassiski


key = 'janet'
krypto_text ='CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE'
plain_text = 'THEALMONDTREEWASINTENTATIVEBLOSSOMTHEDAYSWERELONGEROFTENENDINGWITHMAGNIFICENTEVENINGSOFCORRUGATEDPINKSKIESTHEHUNTINGSEASONWASOVERWITHHOUNDSANDGUNSPUTAWAYFORSIXMONTHSTHEVINEYARDSWEREBUSYAGAINASTHEWELLORGANIZEDFARMERSTREATEDTHEIRVINESANDTHEMORELACKADAISICALNEIGHBORSHURRIEDTODOTHEPRUNINGTHEYSHOULDHAVEDONEINNOVEMBER'

data = [165, 235, 275, 285]
syt = Syt()
result = syt.compute(data)
print 'syt.compute'
print 'Result : %s' % result
assert(5 == result)
print ''

print 'vegenere.decrypt'
vegenere = Vegenere()
dekripted = vegenere.decrypt(krypto_text, key)
print plain_text
print dekripted
assert(plain_text == dekripted)
print ''

print 'vegenere.encrypt'
encrypted = vegenere.encrypt(plain_text, key)
print krypto_text
print encrypted
assert(krypto_text == encrypted)
print ''

print 'kassiski._char_frequency'
text = 'abbvvvggggddddd'
kassiski = Kassiski()
frequencies = kassiski._char_frequency(text)
frequencies.sort()
#assert(frequencies == [1, 2, 3, 4, 5]), 'real %s expected %s' % (frequencies, [1, 2, 3, 4, 5])
print ''

print 'kassiski._calculate_indexes_of_coincidence'
kassiski = Kassiski()
ic = kassiski._calculate_indexes_of_coincidence(krypto_text)
print ic
print ''

print 'kassiski._key_length'
kassiski = Kassiski()
estimation = kassiski._key_length(krypto_text)
print estimation
print ''

print 'kassiski._find_positions'
kassiski = Kassiski()
positions = kassiski._find_positions(krypto_text)
print positions
print ''

print '_calculate_diferencies'
pos = [1, 166, 236, 276, 286]
diff = Kassiski._calculate_diferencies(pos)
print 'Result: %s' % diff
assert diff == [165, 70, 40, 10], 'real %s expected %s' % (diff, [165, 70, 40, 10])
print ''

print '_calculate_factors'
factor = 165
factors = Kassiski._calculate_factors(factor)
print factors
print ''

print 'Kassiski._calculate_occurances_factor'
factors_occurances = Kassiski._calculate_occurances_factor(positions)
print factors_occurances
print ''

print '_calculate_key_length_estimation'
key_length = Kassiski._calculate_key_length_estimation(factors_occurances, 4, 5)
print key_length
assert key_length == 5, 'real %s expected %s' % (key_length, 5)
print ''

print '_estimate_key'
dkey = Kassiski._estimate_key(krypto_text, key_length)
print dkey
print ''