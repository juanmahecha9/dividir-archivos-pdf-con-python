import PyPDF2
import os
import time
import datetime

def data(ruta):
    ruta_division= "/Users/juanmaheha/workspace/py/split"
    with os.scandir(ruta) as ficheros:
        for fichero in ficheros:
        
            if(".pdf" in fichero.name):
                print(fichero.name)
                split(ruta+"/"+fichero.name,ruta_division,fichero.name.replace(".pdf","") )
        

def split(document,out_path,name):
    today = str(datetime.datetime.now().strftime('%Y-%m_%d %H:%M:%S.%f'))
    print (today)
    pdf = PyPDF2.PdfFileReader(open(document, "rb"))
    
    if os.path.exists(out_path):
        print("Exist path")
    else:
        os.mkdir(out_path)

    container = {}
    for i in (range(pdf.getNumPages())):
        i = int(i)
        container[f"pdf_writer{i}"] = PyPDF2.PdfFileWriter()
        container[f"pdf_writer{i}"].addPage(pdf.getPage(i))
        with open(f"{out_path}/{name}-{i}.pdf","wb") as doc_file:
            container[f"pdf_writer{i}"].write(doc_file)
        time.sleep(1)

data("/Users/juanmaheha/workspace/py/pdf")

