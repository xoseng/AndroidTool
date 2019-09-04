# coding=utf8
adb_state='adb devices'
adb_restart='adb kill-server && adb start-server'
adb_root='adb root'
adb_get_imei='adb shell dumpsys iphonesubinfo'
adb_stop='adb kill-server'
adb_start='adb start-server'
adb_fastboot='adb reboot fastboot'
adb_root='adb root'
adb_factory_reset='adb shell "am broadcast -a android.intent.action.MASTER_CLEAR"'
adb_bluetooh_on='adb shell "su -c service call bluetooth_manager 6"'
adb_bluetooh_off='adb shell "su -c service call bluetooth_manager 8"'
adb_bluetooh_check='adb shell "dumpsys bluetooth_manager"'
adb_bluetooh_settings='adb shell "am start -a android.settings.BLUETOOTH_SETTINGS"'
adb_list_packages='adb shell "pm list packages -f"'
adb_storage_off='adb shell "am start -n com.android.systemui/.usb.UsbStorageActivity"'
factory_test='adb shell "am start -a android.intent.action.DIAL -d tel:*%23*%232580%23*%23*'
card_storage_test='adb shell echo $EXTERNAL_STORAGE'
card_read_test='adb shell "ls /storage/sdcard0"'
#should be set variable for number phone
call_test='adb shell "am start -a android.intent.action.CALL -d tel:690103101"'
test_radio='adb shell "monkey -p com.mediatek.FMRadio -c android.intent.category.LAUNCHER 1"'
adb_storage_disabled='adb shell "setprop persist.sys.usb.config adb"'
###########################
adb_get_brightness='adb shell "settings get system screen_brightness"'
#scale: 0 - 255
adb_set_brightness_full='adb shell "settings put system screen_brightness 255"'
adb_set_brightness_middle='adb shell "settings put system screen_brightness 127"'
test_audio_file='adb shell "am start -a android.intent.action.VIEW -d file:///storage/sdcard0/SpeechAudio.mp3 -t audio/mp3"'
adb_sound_recorder_open='adb shell "am start -a android.intent.action.MAIN -n com.android.soundrecorder/com.android.soundrecorder.SoundRecorder"'
adb_id_device='adb shell "getprop | grep display.id"'
#test_audio_record='adb shell "screenrecord storage/sdcard0/demo.mp3 --time-limit 3"'
#test_audio_record_open='adb shell "am start -a android.intent.action.VIEW -d file:///storage/sdcard0/demo.mp3 -t audio/mp3""'

#https://stackoverflow.com/questions/7789826/adb-shell-input-events
adb_headsethook='adb shell "input keyevent 79"'
adb_key_ok='adb shell "input keyevent 23"'
adb_key_up='adb shell "input keyevent 19"'
adb_key_down='adb shell "input keyevent 20"'
adb_key_left='adb shell "input keyevent 21"'
adb_key_right='adb shell "input keyevent 22"'
adb_key_volumeup='adb shell "input keyevent 24"'
adb_key_volumedown='adb shell "input keyevent 25"'
adb_key_endcall='adb shell "input keyevent 6"'
adb_onscreen_time='adb shell "settings put system screen_off_timeout 60000"'
clear_screen='cls'
def call_test_number(phone_number):
    call_adb_command='adb shell "am start -a android.intent.action.CALL -d tel:{}"'.format(phone_number)
    return call_adb_command
