import querygs 
import gspread
import pandas as pd
import numpy as np

#Application_Pandas
print()

certificados_1427 = pd.read_csv(r'C:\Users\dapache\python_scripts\myvenv\scripts_python\Script_1427\certificados.txt',
                                 sep=' ',
                                 index_col=0, 
                                 header=0
                                 )

valores = pd.DataFrame(certificados_1427)

print(valores)



