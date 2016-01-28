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
        procurer = ProcurerData()
        procurer.company_name = 'Oddział Specjalny Żandarmerii Wojskowej'
        procurer.city = 'Mińsk Mazowiecki'
        self.contractors.append(ContractorData())
        self.procurers.append(procurer)

    def getContractors(self):
        return self.contractors

    def getProcurers(self):
        return self.procurers
