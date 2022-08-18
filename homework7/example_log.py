import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']