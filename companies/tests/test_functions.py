# Python
import csv

# Django
from django.test import TestCase

# Models
from companies.models import Company

class CompanyTestFunction(Test):
    def setUp(self):
        self.createCSV = "./files/createCompanies.csv"
        self.updateCSV = "./files/updateCompanies.csv"
        self.createUpdateCSV = "./files/createUpdateCompanies.csv"

    def test_create_by_cv(self):

        #Load File
        with open(self.creatCompanies) as csvfile:
            csvReader = csv.reader(csvfile, delimiter = ',')      

        #Execute Function
        Compnay.loadCSV(self.createCSV)

        #Validate Data
        csvReader
        line_count = 0
        for row in spamreader:
            if line_count == 0:
                line_count += 1
            else:
                companyData = Company.objects.get(id=row[0])
                self.assertEqual(companyData.name, row[1])
                line_count += 1
    
    def test_update_companies(self):

        #Load File
        with open(self.creatCompanies) as csvfile:
            csvReader = csv.reader(csvfile, delimiter = ',')  

        #Execute Function
        Compnay.loadCSV(self.updateCSV)

        #Validate Data
        csvReader
        line_count = 0
        for row in spamreader:
            if line_count == 0:
                line_count += 1
            else:
                companyData = Company.objects.get(id=row[0])
                self.assertEqual(companyData.name, row[1])
                line_count += 1

    def test_create_update_companies(self):

        #Load File
        with open(self.creatCompanies) as csvfile:
            csvReader = csv.reader(csvfile, delimiter = ',')  

        #Execute Function
        Compnay.loadCSV(self.updateCSV)

        #Validate Data
        csvReader
        line_count = 0
        for row in spamreader:
            if line_count == 0:
                line_count += 1
            else:
                companyData = Company.objects.get(id=row[0])
                self.assertEqual(companyData.name, row[1])
                line_count += 1
