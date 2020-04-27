import sys
import subprocess


def ip_reach(ip_list):

    for ip in ip_list:
        ip = ip.rstrip("\n")

        ping_reply = subprocess.call('ping %s /n 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if ping_reply == 0:
            print("\n* {} is reachable\n".format(ip))
            continue
        else:
            print("\n* {} not reachable. Check connectivity and try again.".format(ip))
            sys.exit()
