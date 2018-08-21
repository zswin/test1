#coding=utf-8
__author__ = 'zs'
#test qingguo camera stream video download

import threading
import time
import requests

global _REFRESH_INTERVAL
global _COOKIE
global _DEVICE_IDS
_COOKIE = ['_ntes_nnid=d091984d2150ff942bdc3cea9ccca6e3,1533625884581; _ntes_nuid=d091984d2150ff942bdc3cea9ccca6e3; usertrack=ezq0pFtqhJWUa/FoBM8AAg==; Province=0571; City=09491; _ga=GA1.2.1660653292.1533707420; __utmc=56135659; __utmz=56135659.1534760248.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); QINGGUO_ACCESS_SOURCE=noSource; P_INFO=lag_zs@163.com|1534469276|2|partner|00&99|zhj&1534435110&partner#zhj&330300#10#0#0|&0|partner&note_client|lag_zs@163.com; __utma=56135659.1660653292.1533707420.1534760248.1534762175.2',]
_REFRESH_INTERVAL = 30
_DEVICE_IDS = ['189021806601340',]
def f_refresh():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

    paths = ['https://qlive.163.com/live/square/camera/play','https://qlive.163.com/live/square/camera/heart']
    headers = {'Content-Type':'application/json', 'Cookie': _COOKIE[0]}
    post_data = {"deviceId": _DEVICE_IDS[0]}
    resp_play = requests.post(paths[0], data = post_data, headers = headers, verify = False)
    print('POST TO play:', resp_play.status_code)
    resp_heart = requests.post(paths[1], data = post_data, headers = headers, verify = False)
    print('POST TO heart:', resp_heart.status_code)

    global timer1
    timer1 = threading.Timer(_REFRESH_INTERVAL, f_refresh)
    timer1.start()

if __name__ == '__main__':
    timer2 = threading.Timer(1, f_refresh)
    print('-- Begin -- ')
    timer2.start()

'''--address
https://qlive.163.com/live/pc/index.html#/m/channel?id=189021806601340

--cookie
_ntes_nnid=d091984d2150ff942bdc3cea9ccca6e3,1533625884581; _ntes_nuid=d091984d2150ff942bdc3cea9ccca6e3; usertrack=ezq0pFtqhJWUa/FoBM8AAg==; Province=0571; City=09491; _ga=GA1.2.1660653292.1533707420; S_INFO=1534469276|0|2&70##|lag_zs; P_INFO=lag_zs@163.com|1534469276|0|partner|00&99|zhj&1534435110&partner#zhj&330300#10#0#0|&0|partner&note_client|lag_zs@163.com; __utma=56135659.1660653292.1533707420.1534760248.1534760248.1; __utmc=56135659; __utmz=56135659.1534760248.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); QINGGUO_ACCESS_SOURCE=noSource; __utmb=56135659.16.9.1534760432113


-- 需要设置csrfToken

--response
{
    "playUrl": "rtmp://v128b0486.live.126.net/live/56782738826a4606a7ad57b443457e59",
    "append": "N",
    "audioSwitch": 0,
    "code": 200,
    "hlsUrl": "http://pullhls128b0486.live.126.net/live/56782738826a4606a7ad57b443457e59/playlist.m3u8",
    "rtmpUrl": "rtmp://v128b0486.live.126.net/live/56782738826a4606a7ad57b443457e59"
}


--下载

ffmpeg -i "rtmp://v128b0486.live.126.net/live/56782738826a4606a7ad57b443457e59" -c copy -f mp4 output.mp4'''
