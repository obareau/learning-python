import sys
import subprocess
 
def execute(option, *machines):
    for machine in machines:
        result = subprocess.call(['ping', option, machine])
        if not result:
            print("Address {} OK".format(machine))
        else:
            print("Address {} no response".format(machine))
 
OS = sys.platform
 
option = '-n' if OS != 'win32' else ''
 
execute(option, '192.168.0.1', '12.250.120.63')
# faudrait pouvoir switcher d'une ip à l'autre ...
execute(option, '192.168.0.2', '12.250.120.63')

