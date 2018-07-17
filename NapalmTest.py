import re
from datetime import datetime
from napalm import get_network_driver

driver = get_network_driver('junos')

device = driver('lax01-pcijfw01.pci.insnw.net', 'spagan', 'p0Ag6@ul920l%2$gFC')
device.open()

cmd=['show security pki local-certificate']
cert_info = device.cli(commands=cmd)

for line in cert_info["show security pki local-certificate"].split('\n'):
    if "Not after" in line:
        match = re.search(r'\d{2}-\d{2}-\d{4}', line)
        expiration_date = datetime.strptime(match.group(), '%m-%d-%Y').date()
        current_date = datetime.now().date()

        delta = expiration_date - current_date

        if delta.days > 30:
            print str(delta.days), "days until IPSEC Certificate expiration"
        elif delta.days < 30:
            print str(delta.days), "days until IPSEC Certificate expiration"
        else:
            print str(delta.days), "days until IPSEC Certificate expiration"
