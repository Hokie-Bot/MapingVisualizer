#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pynmea2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import osmnx as ox

# Get the street network for Blacksburg, VA
graph = ox.graph_from_address('495 Old Turner St, Blacksburg, VA 24060',dist=500,dist_type='bbox')
#area = ox.graph_from_place('Blacksburg, Virginia, USA')
#buildings = ox.features_from_place(query='Blacksburg, Virginia, USA', tags={'building':True})
#north, east, south, west = buildings.total_bounds

#print(buildings.total_bounds)

icon = mpimg.imread('icon.png')

ser = "$GPGGA,202659.149,3713.668,N,08025.329,W,1,12,1.0,0.0,M,0.0,M,,*73"
line = ser
msg = pynmea2.parse(line)

#plt.xlim(east, west)
#plt.ylim(north, south)
lat, lon = msg.latitude, msg.longitude
print(lon,lat)
#plt.plot(lat, lon,'ro')
# Redraw the map
#plt.draw()
plt.ion()
fig, ax = ox.plot_graph(graph,show=False,close=False)

me=ax.scatter(lon,lat,c='red')
plt.draw()
plt.pause(1)
for x in range(1,100):
    ser = "$GPGGA,202659.149,3713.789,N,08025.260,W,1,12,1.0,0.0,M,0.0,M,,*71"
    line = ser #add to be readline if needed and add if(starts with $GPGGA) before next 2 lines
    msg = pynmea2.parse(line)
    lat, lon = msg.latitude, msg.longitude
    me.set_color('blue')
    plt.draw()
    plt.pause(5)
    me.set_offsets([lon,lat])
    plt.draw()
    plt.pause(5)
    
# Set the x and y limits of the map




# In[ ]:




