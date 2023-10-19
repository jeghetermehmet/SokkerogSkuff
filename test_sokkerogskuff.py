from skuff import Skuff
from sokk import Sokk
def hovedprogram():
    sokkV = Sokk("V")
    sokkH = Sokk("H")
    
    skuff1 = Skuff()
    skuff1.sett_inn_sokk(sokkV)
    skuff1.sett_inn_sokk(sokkH)
    skuff1.sett_inn_sokk(sokkV)
    skuff1.sett_inn_sokk(sokkH)
    skuff1.sjekk_status()
    
    skuff1.sett_inn_sokk(sokkH)
    skuff1.sett_inn_sokk(sokkH)
    skuff1.sjekk_status()

hovedprogram()