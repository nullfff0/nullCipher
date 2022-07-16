# About The Project
nullCipher - pretty simple pyhon library for encoding data inside a existing .jpeg image. The operating principle is based on the SHA256 data hashing algorithm using an AES encrypted key.
# Getting Started

 ## Installation
 1. Clone the repo
 ```
 git clone https://github.com/nullfff0/nullCipher.git
 ```
 2. Install the requirements
 ```
 pip install -r requirements.txt
 ```
 ## Usage
 ```python
 from nullCipher import nullCipher
 

 cipher = nullCipher("test.jpeg") 
 ```
## Examples
1. Simple function to encrypt "secrets.txt" inside the "test.jpeg" image
 ```python
from nullCipher import nullCipher


def addFileToimg(filename: str, imgname: str, key: str):
    cipher = nullCipher(imgname) 
    with open(filename, "rb") as textfile:
        filedata = textfile.read() # Getting a binary string of the file
        cipher.encryptTojpeg(filedata, key=key)


if __name__ == "__main__":
    addFileToimg("secrets.txt", "test.jpeg", "somekey")

 ```
 But it is not necessary to encrypt the binary string of the file, you can also pass a regular string to the function:
```python
cipher = nullCipher("test.jpeg")
somestring = "Some secret data"
cipher.encryptTojpeg(somestring, key="somekey")
```

 2. And lets decrypt them
 ```python
from nullCipher import nullCipher

def decryptData(imgname: str, key: str):
    cipher = nullCipher(imgname)
    data = cipher.getencryptdata() # We get an list of encrypted items (you can add multiple items within an image)
    result = cipher.decryptdata(data[0], key) #  our list consists of one item, but it's stil an list, so data[0] - first and only item
    return result

if __name__ == "__main__":
    print(decryptData("test.jpeg", "somekey"))
 ```
 Result:
 ```
some secret string [1]
some secret string [2]
some secret string [3]
 ```
3. Clear file
```python
nullCipher("test.jpeg").clearfile()
```

# Enjoy!