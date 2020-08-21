import math   #외부의 파일을 이 파일안으로 들고들어와라

print(math.pow(2, 10))
print(math.pi)


"""
모듈이 파일 하나인경우도 있지만 
여러개의 파일인 경우도 있다 
"""

#ftp 클라이언트 모듈
from ftplib import FTP

ftp = FTP("ftp1.at.proftpd.org")
print(ftp.login()) 
print(ftp.retrlines('LIST'))
print(ftp.quit())
