import sys
import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config


def pushconfig(user, password, dev):

    device = dev.rstrip()
    device_split = device.split(',')
    site = device_split[0].split('-')
    subnet = device_split[1]
    firewall = Device(host=device_split[0], user=user, password=password)

    print "Executing commands on", firewall

    connected = False

    for i in range(0, 100):
        while True:
            try:
                firewall.open()
                firewall.timeout = 300
            except Exception as err:
                print "Cannot connect to device:", err
                continue
            connected = True
            break
        if connected:
            break

    config_set = """  """
    print config_set

    with Config(firewall, mode='private') as cu:
        cu.load(config_set, format='set')
        diff = cu.diff()
        print diff
        print "Committing Configuration"
        cu.commit(timeout=360)

    firewall.close()


if __name__ == "__main__":

    devicelist = open(sys.argv[1])
    user = getpass.getuser()
    password = getpass.getpass('LDAP Password: ')

    for dev in devicelist:
        pushconfig(user, password, dev)
