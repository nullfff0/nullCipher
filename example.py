from nullCipher import nullCipher
from pprint import pprint

def addFileToimg(filename: str, imgname: str):
    cipher = nullCipher(imgname)
    with open(filename, "rb") as textfile:
        filedata = textfile.read()
        cipher.encryptTojpeg(filedata, key="somekey")

if __name__ == "__main__":
    cipher = nullCipher("2345.jpeg")
    # addFileToimg("passwords.txt", "2345.jpeg")
    data = cipher.getencryptdata()
    string = cipher.decryptdata(data[0], key="somekeyd")
    print(string)
