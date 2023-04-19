#!/usr/bin/python3

import cgi
import csv

# with open('..\db\contact.csv', 'r', newline='') as f:
#     spamreader = csv.reader(f)
#     for row in spamreader:
#         print(row)

args = cgi.FieldStorage()
values = [
    args.getfirst("name", ""),
    args.getfirst("email", ""),
    args.getfirst("subject", ""),
    args.getfirst("message", ""),
]

with open('../db/contact.csv', 'a', newline='') as f:
    spamwriter = csv.writer(f)
    spamwriter.writerow(values)

print("Content-Type: text/html\r\n")
print(open('../redirect.arghtml').read().format(f"/~zyh215/groupproject/message-received.html?name={values[0]}"))
