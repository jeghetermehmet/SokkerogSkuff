class Skuff:
    def __init__(self):
        self._sokkeliste = []
    def sett_inn_sokk(self, sokken):
        self._sokkeliste.append(sokken)
    def sjekk_status(self):
        antH = 0
        antV = 0
        for sokker in self._sokkeliste:
            if sokker.hent_side() == "V":
                antV += 1
            else:
                antH += 1
        if antV == antH:
            print("Alt i orden")
        else:
            print("Ulikt antall høyre- og venstresokker")



