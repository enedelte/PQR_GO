#Librerias
from operator import index
import gspread 
import csv
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from requests import head

#Application_GSpread Google Api's

scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("credenciales.json", scopes)

client = gspread.authorize(credentials)

#Lista de llaves Application GSPread

sheet = client.open("Seguimiento PQR Procesos PE").worksheet("Certificado_decreto_1427")

#list_of_lists = sheet.get_all_values()
#list_of_dicts = sheet.get_all_records()
#cell = sheet.find("DAVID ALEJANDRO APACHE RODRIGUEZ")
#value = sheet.acell("C16")
#cell = sheet.findall("DAVID ALEJANDRO APACHE RODRIGUEZ")
#print(cell)

#col = sheet.col_values(1)
#row = sheet.row_values(2)

#este print sirve para buscar la fila y columna, en la que se ubica la incformación buscada con cell = sheet.find(" ")
#print("Se ha encontrado el registro en la fila %s y columna %s" % (cell.col, cell.row))
#print("El valor encontrado se encuentra en la %s" % (value))

#Application_Pandas

dataframe = pd.DataFrame(sheet.get_all_records())

df = dataframe.iloc[:10]

print(df)

#Exporta a txt en la carpeta de Scripts con nombre en ".txt"
df.to_csv("certificados.txt", sep=" ",
          quoting=csv.QUOTE_MINIMAL, escapechar=";")



#Application Numpy
#array = np.array(sheet.get_all_values)
#array = np.array([[1,2,3],[4,5,6]])
#print(array)

