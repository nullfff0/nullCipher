from os.path import exists
from pprint import pprint
from Crypto.Cipher import AES
import hashlib


class nullCipher:
    def __init__(self, imgfile=""):
        self.imgfile = imgfile
        self.fileex = False
        if exists(self.imgfile):
            self.fileex = True
        else:
            print("File do not exist")


    def encryptTojpeg(self, secretstring: str, key: str):
        if self.fileex:
            with open(self.imgfile, "ab") as img:
                if type(secretstring) is bytes:
                    data = secretstring
                else:
                    data = bytes(secretstring, encoding="utf-8")
                key = hashlib.sha256(bytes(key, encoding="utf-8")).digest()
                cipher = AES.new(key, AES.MODE_EAX)
                ciphertext, tag = cipher.encrypt_and_digest(data)
                [img.write(x) for x in (cipher.nonce, tag, ciphertext)]
                img.write(b"\xff\xf0\xff\xd9")


    def decryptdata(self, encryptdata: str, key: str):
        try:
            key = hashlib.sha256(bytes(str(key), encoding="utf8")).digest()
            nonce, tag, ciphertext = encryptdata[:16], encryptdata[16:32], encryptdata[32:]
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            return data.decode("utf-8")
        except Exception as ex:
            return f"Wrong key: {ex}"


    def getencryptdata(self):
        if self.fileex:
            with open(self.imgfile, "rb") as img:
                data = img.read().split(b"\xff\xd9", maxsplit=1)[1].split(b"\xff\xf0\xff\xd9")[0:-1]
                return data
    

    def clearfile(self):
        if self.fileex:
            with open(self.imgfile, "rb") as img:
                filedata = img.read().split(b"\xff\xd9", maxsplit=1)[0] + b"\xff\xd9"
            with open(self.imgfile, "wb") as img:
                img.write(filedata)
        

