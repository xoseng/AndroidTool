# coding=utf8
from subprocess import check_output

def adb_start():
    val= str(check_output("adb kill-server && adb start-server", shell=False))
    return val

def adb_devices():
    val= str(check_output("adb devices", shell=False))
    return val

def device_status():
    try:
        val=adb_devices()
        val=val.replace('\\r','')
        val=val.replace('\\t','')
        val=val.replace('\\n','\n')
        val=val.replace("b'","")
        val=val.replace("'","")
        val=val.split('\n')[1]
        val=val.split('device')[0]
        status = 'CONNECTED'
        if val == '':
            status='DISCONNECTED'
        return status
    except:
        status = 'DISCONNECTED'
        return status

def make_call(number):
    #notice! conver special chars to ussd codes!
    number = str(number)
    conversion_num = ''
    for digit in number:
        if digit == '#':
            digit = '%23'
        conversion_num = conversion_num + digit
    command='adb shell "am start -a android.intent.action.CALL -d tel:{}"'.format(conversion_num)
    val = str(check_output(command, shell=False))
    return val

def end_call():
    val= str(check_output('adb shell "input keyevent 6"', shell=False))
    return val

def get_info():
    val= str(check_output('adb shell "getprop"', shell=False))
    val=val.replace("b'","")
    val=val.replace("'","")
    val=val.replace("\\r","")
    val=val.replace("\\n","\n")
    return val

def get_imei():
    command='adb shell "service call iphonesubinfo 1"'
    val = str(check_output(command, shell=False))
    val=val.replace('\\r','')
    val=val.replace('\\t','')
    val=val.replace('\\n','')
    val=val.replace('b"','')
    val=val.replace('"','')
    val1=val.split("'")[1].replace('.','')
    val2=val.split("'")[3].replace('.','')
    val3=val.split("'")[5].replace('.','')
    val=val1+val2+val3
    val=val.strip()
    return val

def get_serial():
    val= str(check_output('adb shell "getprop"', shell=False))
    val=val.replace("\\n","\n")
    val=val.split('[ro.serialno]:')[1]
    val=val.split(']')[0]
    val=val.replace('[','').strip()
    return val

def get_version():
    val= str(check_output('adb shell "getprop"', shell=False))
    val=val.replace("\\n","\n")
    val=val.split('[ro.fota.version.display]:')[1]
    val=val.split(']')[0]
    val=val.replace('[','').strip()
    return val

def get_model():
    val= str(check_output('adb shell "getprop"', shell=False))
    val=val.replace("\\n","\n")
    val=val.split('[ro.product.model]:')[1]
    val=val.split(']')[0]
    val=val.replace('[','').strip()
    return val

def get_androidversion():
    val= str(check_output('adb shell "getprop"', shell=False))
    val=val.replace("\\n","\n")
    val=val.split('[ro.build.version.release]:')[1]
    val=val.split(']')[0]
    val=val.replace('[','').strip()
    return val

def get_manufacturer():
    val= str(check_output('adb shell "getprop"', shell=False))
    val=val.replace("\\n","\n")
    val=val.split('[ro.product.manufacturer]:')[1]
    val=val.split(']')[0]
    val=val.replace('[','').strip()
    return val

def get_macwiffi():
    val= str(check_output('adb shell "cat /sys/class/net/wlan0/address"', shell=False))
    val=val.replace("b'","")
    val=val.replace("'","")
    val=val.replace("\\r\\r\\n","")
    val=val.strip()
    return val

def get_macbt():
    #######
    #val= str(check_output('adb shell "settings get secure bluetooth_address"', shell=False))
    #val=val.replace("b'","")
    #val=val.replace("'","")
    #val=val.replace("\\r\\r\\n","")
    #val=val.strip()
    #######
    val= str(check_output('adb shell "getprop"', shell=False))
    val=val.replace("\\n","\n")
    val=val.split('[persist.service.bdroid.bdaddr]:')[1]
    val=val.split(']')[0]
    val=val.replace('[','').strip()
    return val

def factory_reset():
    val=str(check_output('adb shell "am broadcast -a android.intent.action.MASTER_CLEAR"', shell=False))
    return val
