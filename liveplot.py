#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial,datetime

ser = serial.Serial('/dev/ttyUSB0',9600)

x = []
temparr = []
presarr = []
altarr  = []
axarr   = []
ayarr   = []
azarr   = []
gxarr   = []
gyarr   = []
gzarr   = []

s = ser.readline()

def animate(i):

    s     = ser.readline()
    line  = s.decode(encoding='ascii',errors='ignore').replace('\r\n','')
    data = line.split(',')
    print(data)

    dp   = int(data[0])
    temp = float(data[4])
    pres = float(data[5])/100.0
    alt  = float(data[6])
    ax   = float(data[7])
    ay   = float(data[8])
    az   = float(data[9])
    gx   = float(data[10])
    gy   = float(data[11])
    gz   = float(data[12])

    x.append(dp)
    temparr.append(temp)
    presarr.append(pres)
    altarr.append(alt)
    axarr.append(ax)
    ayarr.append(ay)
    azarr.append(az)
    gxarr.append(gx)
    gyarr.append(gy)
    gzarr.append(gz)

    if len(x)>100:
        x.pop(0)
        temparr.pop(0)
        presarr.pop(0)
        altarr.pop(0)
        axarr.pop(0)
        ayarr.pop(0)
        azarr.pop(0)
        gxarr.pop(0)
        gyarr.pop(0)
        gzarr.pop(0)

    plt.subplot(331)
    plt.cla()
    plt.plot(x, temparr)
    plt.ylabel('Temperature / [$^\circ$C]')
    plt.grid(True)

    plt.subplot(332)
    plt.cla()
    plt.plot(x, presarr)
    plt.ylabel('Pressure / [hPa]')
    plt.grid(True)

    plt.subplot(333)
    plt.cla()
    plt.plot(x, altarr)
    plt.ylabel('Altitude / [m]')
    plt.grid(True)

    plt.subplot(334)
    plt.cla()
    plt.plot(x, axarr)
    plt.ylabel('$a_x$ / [G]')
    plt.grid(True)

    plt.subplot(335)
    plt.cla()
    plt.plot(x, ayarr)
    plt.ylabel('$a_y$ / [G]')
    plt.grid(True)

    plt.subplot(336)
    plt.cla()
    plt.plot(x, azarr)
    plt.ylabel('$a_z$ / [G]')
    plt.grid(True)

    plt.subplot(337)
    plt.cla()
    plt.plot(x, gxarr)
    plt.xlabel('MSGNUM')
    plt.ylabel('$g_x$ / [$^\circ$/s]')
    plt.grid(True)

    plt.subplot(338)
    plt.cla()
    plt.plot(x, gyarr)
    plt.xlabel('MSGNUM')
    plt.ylabel('$g_y$ / [$^\circ$/s]')
    plt.grid(True)

    plt.subplot(339)
    plt.cla()
    plt.plot(x, gzarr)
    plt.xlabel('MSGNUM')
    plt.ylabel('$g_z$ / [$^\circ$/s]')
    plt.grid(True)

ani = FuncAnimation(plt.gcf(), animate, interval=1)

plt.show()
