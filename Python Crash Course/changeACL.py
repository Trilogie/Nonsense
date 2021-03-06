#!/usr/bin/env python

import ConfigParser
import argparse
import time
from netmiko import ConnectHandler


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="Configuration file to log into devices")
    parser.add_argument("routers", help="File containing routers", type=argparse.FileType('r'))
    args = parser.parse_args()

    return args


def connect(username, password, host):
    conn = ConnectHandler(ip=host, username=username, password=password, device_type='cisco_ios')
    conn.find_prompt()
    return conn


def check_acl(conn):
    # Enter send command here
    conn.send_command("show ntp ass")
    time.sleep(2)

    # Enter config commands in here(list)
    config_commands = [" "]
    output = conn.send_config_set(config_commands)

    return output


def main():
    args = get_args()

    config = ConfigParser.ConfigParser()
    config.readfp(open(args.config))
    dev = args.routers
    router = []

    for line in dev:
        router.append(line.rstrip())

    for host in router:
        try:
            username = config.get("router-man", "username")
            password = config.get("router-man", "password")
        except ConfigParser.NoOptionError:
            username = args.username
            password = config.get("router-man", "password")

        conn = connect(username=username, password=password, host=host)
        output = check_acl(conn)

        print output


if __name__ == '__main__':
    main()
