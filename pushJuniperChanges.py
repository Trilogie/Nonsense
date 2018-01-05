import sys
import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config


def getdevice(user, password, dev):

    device = dev.rstrip()
    device_split = device.split(',')
    site = device_split[0].split('-')
    subnet = device_split[1]
    dev = Device(host=device_split[0], user=user, password=password)
    return dev


def connectionhandler(dev):

    try:
        dev.open()
        dev.timeout = 300
        return dev
    except Exception:
        dev = "Could not connect"
        return dev


def pushconfig(user, password, dev):

    device = getdevice(user, password, dev)
    netdevice = connectionhandler(device)

    if netdevice != "Could not connect":

        print "Executing commands on", netdevice

        config_set = "  "
        print config_set

        with Config(netdevice, mode='private') as cu:
            cu.load(config_set, format='set')
            diff = cu.diff()
            print diff
            print "Committing Configuration"
            cu.commit(timeout=360)

        netdevice.close()
    else:
        print "Could not connect to %s, moving to next device" % device


if __name__ == "__main__":

    devicelist = open(sys.argv[1])
    user = getpass.getuser()
    password = getpass.getpass('LDAP Password: ')

    for dev in devicelist:
        pushconfig(user, password, dev)
