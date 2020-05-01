import zlib, base64

def compresser():
    file1=open('input_file.txt','r')
    text=file1.read()
    file1.close()

    code=base64.b64encode(zlib.compress(text.encode('utf-8'),9))
    code=code.decode('utf-8')

    f=open('compressed_output.txt','w')
    f.write(code)
    f.close()

compresser()
