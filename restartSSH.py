# /usr/bin/python3
# -*- coding: utf-8 -*-
# from https://github.com/JJandke
#
# The script tries to reach the own device via SSH every 60 seconds.
# If this is not possible, the service will be restarted.
# Note: The script must be executed with root privileges.
#       The best way to do this would be to use a chronjob, which runs it at every boot.
# Furthermore: The script is only a workaround, and he error for the misbehavior of SSH should still be searched.
# If port 22 is refused, SSH must be uninstalled and then reinstalled again.
# It may be that paramiko must first be installed using "sudo pip3 install paramiko".

from os import system
import paramiko
import time

ssh = paramiko.SSHClient()
user = "pi"
hostname = "localhost"
pwd = "1234abcd"

while True:
    try:
        ssh.load_system_host_keys()
        ssh.connect(hostname=hostname, username=user, password=pwd)
        ssh.close()
        print("Successfully logged in, SSH is running.")

    except Exception as e:
        print(e)
        print("Unable to reach the PI via SSH, script will be restarted. ")
        system("sudo /etc/init.d/ssh restart")

    time.sleep(60)
