#!/usr/bin/env python

import sys
import socket

port = 79

if __name__ == "__main__":

    users = sys.argv[1:]

    for user in users:
        if '@' in user:
            parts = user.split('@')
            user = parts[0]
            ip = socket.gethostbyname(parts[1])
            host = socket.gethostbyaddr(ip)[0]
        else:
            host = 'localhost'

        print "[%s]" % (host)

        s = socket.socket()

        s.connect((ip, port))
        s.send("%s\n" % user)

        output = 'x'
        while output != '':
            output = s.recv(512)
            print output.replace('\r\n', '\n'),
        s.close
