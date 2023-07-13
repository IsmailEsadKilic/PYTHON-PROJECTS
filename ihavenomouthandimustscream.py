class OBAMAAA():
    def __init__ (self,i="i",have="have",no="no",mouth="mouth"):
        self._and = i
        self.i = have
        self.must = no
        self.scream = mouth

    def doit(self):
        return f"{self._and} {self.i} {self.must} {self.scream} and i must scream"

    def __str__(self):
        return f"{self._and} {self.i} {self.must} {self.scream} and i must scream"

    def screamla(self):
        return(f"{self.doit()} AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!")

sussyyyy = OBAMAAA()

print(sussyyyy)
print(sussyyyy.screamla())

class AMOGUS(OBAMAAA):
    def grr(self):
        print(f"{self.doit()} grr!")

already_gave_up = AMOGUS()

already_gave_up.grr()
print(already_gave_up)

class icri(OBAMAAA):
    def cri(self):
        print(f"{self.doit()} 'tears'")

i_already_did = icri()
i_already_did.cri()