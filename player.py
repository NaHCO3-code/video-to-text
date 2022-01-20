import os,time

vt = 'vedio.vt'

with open(vt, 'r', encoding='utf8') as f:
    time.sleep(3)
    res = f.readline()
    os.system(f'mode con cols={res.split("|")[0]} lines={res.split("|")[1]}')
    delay = int(res.split("|")[2])*(1/float(res.split("|")[3][0:-2]))

    while res:
        res = f.readline()
        print('\n'.join(res.split('\\n')))
        time.sleep(delay)