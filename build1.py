#!usr/bin/python3

import time
import os
os.system('docker-compose -f docker-compose-base.yml up -d')
time.sleep(5)



import os
os.system('docker exec -it mesaforte-be /bin/bash')

