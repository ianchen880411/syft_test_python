# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 13:47:44 2025

@author: ian.chen
"""

import colour
import numpy as np
from PIL import Image
import requests
import matplotlib.pyplot as plt

def show_colour_info():
    # 1) 使用 colour-science
    cmfs = colour.MSDS_CMFS["CIE 1931 2 Degree Standard Observer"]
    print("Showing color matching functions shape:")
    print(cmfs.shape)

    # 2) Numpy array 操作
    a = np.array([[1, 2], [3, 4]])
    print("Numpy array:\n", a)

    # 3) Pillow 建立一張純色影像
    img = Image.new("RGB", (100, 100), color="blue")
    img.save("test_blue.png")
    print("Created a 100x100 blue image using Pillow.")

    # 4) requests 做 HTTP GET
    r = requests.get("https://httpbin.org/get")
    print(f"HTTP GET status code: {r.status_code}")
    print(f"Response JSON: {r.json()}")

    # 5) matplotlib 繪圖
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title("Sine wave")
    plt.savefig("sine_wave.png")
    print("Saved plot sine_wave.png using matplotlib.")

if __name__ == "__main__":
    show_colour_info()
