import socket
server_host = 'data.pr4e.org'
page_file   = 'intro-short.txt'
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((server_host, 80))
cmd = 'GET http://' + server_host + '/' + page_file + ' HTTP/1.0\r\n\r\n'
print(cmd)
cmd = cmd.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

'''
HTTP/1.1 200 OK
Date: Thu, 26 Oct 2023 09:20:19 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "1d3-54f6609240717"
Accept-Ranges: bytes
Content-Length: 467
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain
'''