from xml.dom.minidom import parse
import html
from bs4 import BeautifulSoup


class ContractorData:
    pass


class ProcurerData:
    def __init__(self):
        self.company_name = ''
        self.city = ''
        self.full_address = 'ul. Warszawska, 05-300 Mińsk Mazowiecki'


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

    def extractProcurersAddress(self, text):
        unescapedText = html.unescape(text)
        soup = BeautifulSoup(unescapedText, 'html.parser')
        all_p = soup.find_all('p')
        nextContainsAddress = False
        for p in all_p:
            if p.string == 'SEKCJA I: ZAMAWIAJĄCY':
                # print(p)
                # print(p.string)
                nextContainsAddress = True
            elif nextContainsAddress:
                fullAddress = p.contents[1]
                fullAddress = fullAddress.split(',', 1)[-1]
                street = fullAddress.split(',', 1)[0]
                fullAddress = fullAddress.split(',', 1)[-1]
                postal = fullAddress.split(',', 1)[0]
                street = street.lstrip()
                street = street.rstrip()
                postal = postal.lstrip()
                postal = postal.rstrip()
                fullAddress = street + ', ' + postal
                nextContainsAddress = False
                # print(fullAddress)
                return fullAddress
        # print(soup.prettify())
        # print(unescapedText)
