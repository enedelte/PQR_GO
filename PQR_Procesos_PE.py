#Librerias

from operator import index
import gspread 
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

from requests import head

#Application_GSpread Google Api's

scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("credenciales.json", scopes)

client = gspread.authorize(credentials)

#Query "Certificados 1427"

sheet = client.open("Seguimiento PQR Procesos PE").worksheet("Certificado_decreto_1427")

datasheet = sheet.get_all_records()

#Application_Pandas

dataframe = pd.DataFrame(sheet.get_all_records(head))

#col = sheet.col_values(1)
#row = sheet.row_values(1)
#cell = sheet.cell(1,1)

#col1 = sheet.col_values(3)
#row1 = sheet.row_values(1)
#cell1 = sheet.cell(1,1)

#col2 = sheet.col_values(13)
#row2 = sheet.row_values(1)
#cell2 = sheet.cell(1,1)

print(dataframe)


