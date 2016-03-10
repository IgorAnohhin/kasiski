__author__ = 'v-iganoh'


from syt import Syt
from vegenere import Vegenere


key = 'janet'
krypto_text = 'CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE'
plain_text = 'THEALMONDTREEWASINTENTATIVEBLOSSOMTHEDAYSWERELONGEROFTENENDINGWITHMAGNIFICENTEVENINGSOFCORRUGATEDPINKSKIESTHEHUNTINGSEASONWASOVERWITHHOUNDSANDGUNSPUTAWAYFORSIXMONTHSTHEVINEYARDSWEREBUSYAGAINASTHEWELLORGANIZEDFARMERSTREATEDTHEIRVINESANDTHEMORELACKADAISICALNEIGHBORSHURRIEDTODOTHEPRUNINGTHEYSHOULDHAVEDONEINNOVEMBER'

data = [165, 235, 275, 285]
syt = Syt()
result = syt.compute(data)
assert(5, result)
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