from zipfile import ZipFile
file="FileCompress.zip"
with ZipFile(file,'r') as zip:
    zip.printdir()
    print("Extracting ,...")
    zip.extractall()
    print("Done !")