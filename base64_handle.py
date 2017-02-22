
import base64


def str2base64(buffer):
    return base64.b64encode(buffer)

def base642str(buffer):
    return base64.b64decode(buffer)


def file2base64(filepath):
    with open(filepath,'rb') as file:
        return base64.b64encode(file.read())

def base642file(base64,filepath);
    with open(filepath,'wb') as file:
        return base64.b64decode()
