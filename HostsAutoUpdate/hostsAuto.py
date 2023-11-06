import requests
from datetime import datetime
import time

beginTag = '# ######### Hosts Auto Update (begin) #########\n'
endTag = '# ######### Hosts Auto Update (end) #########\n'


def update():
    print(f'Update at {datetime.now()}')
    try:
        newHosts = requests.get(
            'https://gitlab.com/ineo6/hosts/-/raw/master/next-hosts').content.decode('UTF-8')

        with open('/auto/hosts', 'r') as file:
            oldHosts = file.readlines()

        if (beginTag in oldHosts) and (endTag in oldHosts):
            beginIndex = oldHosts.index(beginTag)
            endIndex = oldHosts.index(endTag)
            oldHosts = oldHosts[:beginIndex] + oldHosts[endIndex + 1:]

        oldHosts += ['' if oldHosts[-1] == '\n' else '\n', beginTag, '\n', newHosts, '\n', endTag]

        with open('/auto/hosts', 'w') as file:
            for line in oldHosts:
                file.write(line)

        print('Done!')
        return True
    except BaseException as e:
        print(e)
        return False

if __name__ == '__main__':
    while True:
        success = update()
        time.sleep((6 * 3600 if success else 60))
