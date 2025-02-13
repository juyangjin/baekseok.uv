from hashlib import sha256 as SHA
import codecs

SIZE = 1024*256

def getFileHash(filename):
    sha = SHA()
    h = open(filename,'rb')
    content = h.read(SIZE)
    while content:
        sha.update(content)
        content=h.read(SIZE)
    h.close()

    hashval = sha.digest()
    return hashval

def hashCheck(file1,file2):
    hashval1 = getFileHash(file1)
    hashval2 = getFileHash(file2)

   # if hashval1 == hashval2:
   #     print('Two File are Same')
   # else:
   #     print('Two File are Different')


def main():
    file1 = 'A.txt'
    file2 = 'B.txt'

    
   # print(codecs.encode(hashval,'hex_codec'))
    hashval = getFileHash(file1)
    hashval1 = codecs.encode(hashval,'hex_codec')

    hashCheck(file1,file2)

    
main()

        
