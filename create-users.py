#!/usr/bin/python3

# Imports required for system and string operations
import os
import re
import sys

def main():
    for line in sys.stdin:

        # Check if line is a comment (starts with '#')
        match = re.match("^#", line)

        # Split the line into fields by colon delimiter
        fields = line.strip().split(':')

        # Skip lines that are comments or incorrectly formatted (not 5 fields)
        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        # Print message and create user account
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        # Uncomment this line to execute the command
        # os.system(cmd)

        # Print message and set user password
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        # Uncomment this line to execute the command
        # os.system(cmd)

        # Add user to each group
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # Uncomment this line to execute the command
                # os.system(cmd)

if __name__ == '__main__':
    main()
