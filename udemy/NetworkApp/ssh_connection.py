import paramiko
import os.path
import time
import sys
import re

user_file = input("\n Enter user file path and name: ")

if os.path.isfile(user_file):
    print("\n* Username/password file is valid\n")
else:
    print("\n* File {} does not exist.\n".format(user_file))
    sys.exit()

cmd_file = input("\n Enter commands file path and name: ")

if os.path.isfile(cmd_file):
    print("\n* Command file is valid\n")
else:
    print("\n* File {} does not exist.\n".format(cmd_file))
    sys.exit()


def ssh_connection(ip_list):
    global user_file
    global cmd_file

    try:
        selected_user_file = open(user_file, 'r')
        selected_user_file.seek(0)
        username = selected_user_file.readlines()[0].rsplit(',')[0].rstrip("\n")
        selected_user_file.seek(0)
        password = selected_user_file.readlines()[0].rsplit(',')[1].rstrip("\n")

        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip_list.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()

        connection.send("\n")
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        connection.send("\n")
        connection.send("config t\n")
        time.sleep(1)

        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)

        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + "\n")
            time.sleep(2)

        selected_user_file.close()
        selected_cmd_file.close()

        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {} :".format(ip_list))
        else:
            print("\n DONE for device {} \n".format(ip_list))

        #router_output_decode = router_output.decode("utf-8")
        #print(re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", router_output_decode)[1])

        session.close()

    except paramiko.AuthenticationException:
        print("* Invalid username or password \n")
        print("* Closing program")
