import pandas as pd
import re
iphone=0
windows=0
tablet=0
bot=0
mac=0
android=0
uniqueip=0
logsum=0
y2019_=0
y2018_=0
y2017_=0
y2016_=0
yandex=0
y2020=0

google=0
bing=0

mozilla=0
chrome=0
opera=0
safari=0
for i in range(1,6):
    logs=pd.read_csv('2019/disk'+str(i)+'.csv')
    #
    print(logs.head())
    logs=logs.loc[logs['datetime'].str.contains('2020')==True]
    logs=logs.loc[logs['request_method'].str.contains('hotel')==True]
    logsum+=logs['browser'].count()
    a=logs['receiving_ip'].nunique()
    uniqueip+=a
    #b=logs['browser']
    mozilla_=logs.loc[logs['browser'].str.contains('Mozilla')==True]
    chrome_=logs.loc[logs['browser'].str.contains('Chrome')==True]
    safari_=logs.loc[logs['browser'].str.contains('Safari')==True]
    opera_=logs.loc[logs['browser'].str.contains('opera')==True]

    google_=logs.loc[logs['browser'].str.contains('google')==True]
    bing_=logs.loc[logs['browser'].str.contains('bingbot')==True]

    iphone_=logs.loc[logs['browser'].str.contains('iPhone')==True]
    windows_=logs.loc[logs['browser'].str.contains('Windows')==True]
    android_=logs.loc[logs['browser'].str.contains('Android')==True]
    tablet_=logs.loc[logs['browser'].str.contains('TABLET')==True]
    bot_=logs.loc[logs['browser'].str.contains('bot')==True]
    mac_=logs.loc[logs['browser'].str.contains('Macintosh')==True]
    iphone+=iphone_['browser'].count()
    windows+=windows_['browser'].count()
    tablet+=tablet_['browser'].count()
    bot+=bot_['browser'].count()
    mac+=mac_['browser'].count()
    android=android_['browser'].count()

    google+=google_['browser'].count()
    bing+=bing_['browser'].count()

    mozilla+=mozilla_['browser'].count()
    chrome+=chrome_['browser'].count()
    safari+=safari_['browser'].count()
    opera+=opera_['browser'].count()

    y2019=logs.loc[logs['datetime'].str.contains('2019')==True]
    y2018=logs.loc[logs['datetime'].str.contains('2018')==True]
    y2017=logs.loc[logs['datetime'].str.contains('2017')==True]
    y2016=logs.loc[logs['datetime'].str.contains('2016')==True]
    y2020_=logs.loc[logs['datetime'].str.contains('2020')==True]
    y2020+=y2020_['datetime'].count()
    y2019_+=y2019['datetime'].count()
    y2018_+=y2018['datetime'].count()
    y2017_+=y2017['datetime'].count()
    y2016_+=y2016['datetime'].count()
    yandex_=logs.loc[logs['browser'].str.contains('yandex')==True]
    yandex+=yandex_['browser'].count()
#b=logs['browser'].unique()
#print(b)

print('yandex',yandex)
print(logsum)
print(uniqueip)
print(y2020,y2019_,y2018_,y2017_,y2016_)
print("iphone count:  ",iphone)
print("windows count: ",windows)
print("android count: ",android)
print("TABLET count: ",tablet)
print("bot count: ",bot)
print("mac count: ",mac)

print("mozzila count: ",mozilla)
print("chrome count: ",chrome)
print("safari count: ",safari)
print("opera count: ",opera)

print("google count: ",google)
print("bing count: ",bing)
"""
yandex 0
3560
143
3582 0 0 0 0
iphone count:   256
windows count:  1861
android count:  813
TABLET count:  0
bot count:  23
mac count:  389
mozzila count:  3560
chrome count:  1541
safari count:  2410
opera count:  0
google count:  71
bing count:  0
"""
