import os
import pandas as pd
import PyPDF2


# def lock_pdf(pdf_dir, strPassword):
#     filename = os.path.basename(pdf_dir)
#     pdf = open(pdf_dir, "rb")
#     pdf_data = PyPDF2.PdfFileReader(pdf)
#     pages_no = pdf_data.numPages
#     output = PyPDF2.PdfFileWriter(pdf)

    # for i in range(pages_no)
    #     inputPdf = PyPDF2.PdfFileReader(pdf)
    #     output.addPage(inputPdf.getPage(i))
    #     output.encrypt(strPassword)
    #     save_dir = os.path.join(os.getcwd(), "protected_PDFs", filename)
    #     with open(save_dir, "wb") as outputSream:
    #         output.write(outputSream)
    #     pdf.close()


csv_settings = pd.read_csv(r"C:\Users\dapache\python_scripts\myvenv\password_settings.csv", sep=";")

for row in csv_settings.itertuples():
    print("Protegiendo PDF en \n"
          "{file} con la contraseña {password}"
          .format (file= row[1], password= row[2])
          )

   
