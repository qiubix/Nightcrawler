from xml.dom.minidom import parse
import html
from bs4 import BeautifulSoup


class ContractorData:
    def __init__(self):
        self.company_name = ''
        self.city = ''
        self.full_address = ''


class ProcurerData:
    def __init__(self):
        self.company_name = ''
        self.city = ''
        self.full_address = ''


class DataReader:
    def __init__(self):
        self.procurers = []
        self.contractors = []
        self.document = None

    def load(self, fileName):

        with open(fileName, 'r') as file:
            self.document = parse(file)

        publications = self.document.getElementsByTagName('ogloszenie')
        for publication in publications:
            procurer = ProcurerData()
            contractor = ContractorData()
            childNodes = publication.childNodes
            for childNode in childNodes:
                if childNode.nodeName == 'nazwa':
                    companyName = childNode.firstChild.nodeValue.rstrip()
                    procurer.company_name = companyName
                if childNode.nodeName == 'miejscowosc':
                    city = childNode.firstChild.nodeValue.rstrip()
                    procurer.city = city
                if childNode.nodeName == 'tekst':
                    tenderText = childNode.firstChild.nodeValue
                    fullAddress = self.extractProcurersAddress(tenderText)
                    procurer.full_address = fullAddress

                    contractorName = self.extractContractorName(tenderText)
                    contractor.company_name = contractorName

            self.procurers.append(procurer)
            if contractor.company_name != '':
                self.contractors.append(contractor)

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
                fullAddressData = p.contents[1]

                street = fullAddressData.split(',')[1]
                street = self.trimSideWhitespace(street)

                postal = fullAddressData.split(',')[2]
                postal = self.trimSideWhitespace(postal)

                fullAddress = street + ', ' + postal
                nextContainsAddress = False
                # print(fullAddress)
                return fullAddress

        # print(soup.prettify())
        # print(unescapedText)

    def trimSideWhitespace(self, text):
        trimmed = text.lstrip()
        trimmed = trimmed.rstrip()
        return trimmed

    def extractContractorName(self, text):
        unescapedText = html.unescape(text)
        contractorSection = self.extractContractorSection(unescapedText)
        if contractorSection != '':
            soup = BeautifulSoup(contractorSection, 'html.parser')
            addressData = soup.ul.li.string
            name = addressData.split(',')[0]
        else:
            name = ''
        return name

    def extractContractorSection(self, unescapedText):
        splitted = unescapedText.split('\n')
        mark = 'SEKCJA V: UDZIELENIE ZAMÓWIENIA'
        contractorSection = ''
        isContractorSection = False
        for line in splitted:
            if mark in line:
                isContractorSection = True
            if '</body>' in line:
                isContractorSection = False
            if isContractorSection:
                contractorSection += line
                contractorSection += '\n'
        return contractorSection

    def extractContractorCity(self, text):
        unescapedText = html.unescape(text)
        contractorSection = self.extractContractorSection(unescapedText)
        if contractorSection != '':
            soup = BeautifulSoup(contractorSection, 'html.parser')
            addressData = soup.ul.li.string
            postal = addressData.split(',')[2]
            city = postal.rsplit()[1]
        else:
            city = ''
        return city
