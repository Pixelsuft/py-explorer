use_7_theme=True
filter_folders_from_files=True


from sys import argv as start_args
from os import listdir as scan_dir
from os import chdir as change_dir
from os import getcwd as get_dir
from os import environ as env
from eel import init as eel_init
from eel import start as eel_start
from eel import expose as eel_expose
from os.path import isdir as is_dir

def get_type(path):
    return path.split('.')[-1]


@eel_expose
def py_change_dir(path):
    for i in env:
        path=path.replace('%'+i+'%',env[i])
        path=path.replace('%'+i.upper()+'%',env[i])
        path=path.replace('%'+i.lower()+'%',env[i])
    if is_dir(path):
        change_dir(path)
        return True
    else:
        return False


@eel_expose
def py_list_dir():
    scanned=scan_dir(get_dir())
    result=[get_dir()]
    result.append(['..', True, '..'])
    if filter_folders_from_files==False:
        for i in scanned:
            result.append([i,is_dir(i),get_type(i)])
    else:
        for i in scanned:
            if is_dir(i)==True:
                result.append([i,True,get_type(i)])
        for i in scanned:
            if is_dir(i)==False:
                result.append([i,False,get_type(i)])
    return result


eel_init('web')


if __name__=='__main__':
    if use_7_theme==True:
        env['__COMPAT_LAYER']='WinXPSp3'
    eel_start('index.html', size=(800, 600), mode='chrome', port=1337, cmdline_args=['--incognito'])