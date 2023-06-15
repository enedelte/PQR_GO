#Query de Google sheet
import gspread
import csv
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from requests import head

#Scopes 
scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credenciales.json', scopes)
client = gspread.authorize(credentials)
worksheet = client.open("Seguimiento PQR Procesos PE").worksheet("Certificado_decreto_1427")

plano = pd.DataFrame(worksheet.get_values())
#Exporta a txt en la carpeta de Scripts con nombre en ".txt"
plano.to_csv("certificados.txt", 
             sep=" ",
             header=0, 
             quotechar='"', 
             index=0, 
             quoting=csv.QUOTE_MINIMAL, 
             escapechar=";")

print("\nSe ha actualizado el documento\n    certificados.txt\n Ya puedes verificarlo.")