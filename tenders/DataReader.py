class ContractorData:
    pass


class ProcurerData:
    def __init__(self):
        self.company_name = ''
        self.city = ''


class DataReader:
    def __init__(self):
        self.procurers = []
        self.contractors = []

    def load(self, fileName):
        self.contractors.append(ContractorData())

        procurer = ProcurerData()
        procurer.company_name = 'Oddział Specjalny Żandarmerii Wojskowej'
        procurer.city = 'Mińsk Mazowiecki'
        second = ProcurerData()
        second.company_name = 'Centrum Onkologii Instytut im. Marii Skłodowskiej-Curie'
        second.city = 'Warszawa'
        self.procurers.append(procurer)
        self.procurers.append(second)

    def getContractors(self):
        return self.contractors

    def getProcurers(self):
        return self.procurers
