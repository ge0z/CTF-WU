#!/usr/bin/python3
#MCTF23
#geoz

from cryptography.fernet import Fernet

f = Fernet("zddKGBJzBhqAhqsLaU3raQQJ2NXN6t2sMqaI5-EbXBU=".encode())
print (f.decrypt("gAAAAABkOYHFTseEbHr5WLoOhNGBAVy9Cp4fSRBFi5rgtvGKQQqBByAqDoI2F19awweUdAlvdHUh8eYojpAQC-tZPc6xyr_Vkm0ZU0uahaXHTxfdULzBngI=".encode()).decode())
