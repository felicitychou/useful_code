# python 2/3
'''
print(str2base64(b"Hello World"))
print(base642str(str2base64(b"Hello World")))
print(file2base64("test"))
print(base642file(file2base64("test"),'test3'))

python 2 output
SGVsbG8gV29ybGQ=
Hello World
SGVsbG8gV29ybGQ=
Hello World

python 3 output
b'SGVsbG8gV29ybGQ='
b'Hello World'
b'SGVsbG8gV29ybGQ='
b'Hello World'
'''
import base64

def str2base64(str):
    return base64.b64encode(str)

def base642str(base64_str):
    return base64.b64decode(base64_str)

def file2base64(filepath):
    with open(filepath,'rb') as file:
        return base64.b64encode(file.read())

def base642file(base64_str,filepath):
    with open(filepath,'wb') as file:
        data = base64.b64decode(base64_str)
        file.write(data)
        return data


