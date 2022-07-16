from nullCipher import nullCipher

def decryptData(imgname: str, key: str):
    cipher = nullCipher(imgname)
    data = cipher.getencryptdata() # We get an list of encrypted items (you can add multiple items within an image)
    result = cipher.decryptdata(data[0], key) #  our list consists of one item, but it's stil an list, so data[0] - first and only item
    return result

if __name__ == "__main__":
    print(decryptData("test.jpeg", "somekey"))