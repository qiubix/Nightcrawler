class Contractor:
    pass


class Procurer:
    def __init__(self):
        self.company_name = 'Oddział Specjalny Żandarmerii Wojskowej'


class DataReader:
    def __init__(self):
        self.procurers = []
        self.contractors = []

    def load(self, fileName):
        self.contractors.append(Contractor())
        self.procurers.append(Procurer())

    def getContractors(self):
        return self.contractors

    def getProcurers(self):
        return self.procurers
