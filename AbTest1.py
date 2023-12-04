import pynmea2
import matplotlib.pyplot as plt
import osmnx as ox
import matplotlib.image as mpimg
import numpy as np

# Get the street network for Blacksburg, VA
graph = ox.graph_from_address('495 Old Turner St, Blacksburg, VA 24060', dist=500, dist_type='bbox')

# Create a figure and axis
plt.ion()
fig, ax = ox.plot_graph(graph, show=False, close=False)

# Load the icon image
icon = mpimg.imread('icon.png')

# Display the icon at a specific location on the map
icon_extent = 0.0003  # Adjust icon size
lat, lon = 37.139, -80.256  # Initial position (replace with your desired coordinates)
icon_plot = ax.imshow(icon, extent=[lon - icon_extent, lon + icon_extent, lat - icon_extent, lat + icon_extent], zorder=10)

for x in range(1, 100):
    # Simulate GPS data
    ser = "$GPGGA,202659.149,3713.789,N,08025.260,W,1,12,1.0,0.0,M,0.0,M,,*71"
    line = ser
    msg = pynmea2.parse(line)
    lat, lon = msg.latitude, msg.longitude

    # Simulate heading data
    heading_degrees = 290.85  # Replace this with your actual heading data

    # Update icon position and rotation
    icon_plot.set_extent([lon - icon_extent, lon + icon_extent, lat - icon_extent, lat + icon_extent])  # Adjust position

    # Rotate the icon
    rotated_icon = np.rot90(icon, k=int(heading_degrees / 90))

    # Display the rotated icon
    icon_plot.set_data(rotated_icon)

    plt.draw()
    plt.pause(0.5)
