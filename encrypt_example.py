from nullCipher import nullCipher


def addFileToimg(filename: str, imgname: str, key: str):
    cipher = nullCipher(imgname) 
    with open(filename, "rb") as textfile:
        filedata = textfile.read() # Getting a binary string of the file
        cipher.encryptTojpeg(filedata, key=key)


if __name__ == "__main__":
    addFileToimg("secrets.txt", "test.jpeg", "somekey")