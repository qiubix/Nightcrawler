from xml.dom.minidom import parse


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
        self.document = None

    def load(self, fileName):
        self.contractors.append(ContractorData())

        with open(fileName, 'r') as file:
            self.document = parse(file)

        ogloszenia = self.document.getElementsByTagName('ogloszenie')
        for ogloszenie in ogloszenia:
            procurer = ProcurerData()
            childNodes = ogloszenie.childNodes
            for childNode in childNodes:
                if childNode.nodeName == 'nazwa':
                    companyName = childNode.firstChild.nodeValue.rstrip()
                    procurer.company_name = companyName
                if childNode.nodeName == 'miejscowosc':
                    city = childNode.firstChild.nodeValue.rstrip()
                    procurer.city = city

            self.procurers.append(procurer)

    def getContractors(self):
        return self.contractors

    def getProcurers(self):
        return self.procurers
