import os
import pandas as pd
import PyPDF2
from PyPDF2 import PdfReader

# csv_settings = pd.read_csv(r"C:\Users\dapache\python_scripts\myvenv\scripts_python\password_settings.csv", sep=";")
# for row in csv_settings.itertuples():
#     print("Protegiendo PDF en ruta\n {Ruta} \ncon la contraseña {Clave}"
#           .format (Ruta=row[1], Clave=row[2])
#    ) 

path_csv = pd.read_csv(r'C:\Users\dapache\python_scripts\myvenv\scripts_python\certificados.txt', sep=';')
df = pd.DataFrame(path_csv)



reader = PdfReader (r'C:\Users\dapache\python_scripts\myvenv\scripts_python\VO-GA-DGO-2480330-23.pdf')
number_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(df)