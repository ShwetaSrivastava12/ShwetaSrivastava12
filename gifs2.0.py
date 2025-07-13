#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import imageio
import tkinter as tk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk, ImageSequence

image_paths = [
    r"C:\Users\minis\OneDrive\Desktop\My_Images\BTS.jpg.jpg",
    r"C:\Users\minis\OneDrive\Desktop\My_Images\BTS-PNG-Picture.png",
    r"C:\Users\minis\OneDrive\Desktop\My_Images\Bts.gif",
]

target_size = (300, 200)
images = []

for path in image_paths:
    if not os.path.exists(path):
        print(f"Warning: Image not found at '{path}'. Skipping.")
        continue
    try:
        img = Image.open(path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize(target_size)
        images.append(np.array(img))
    except Exception as e:
        print(f"Error processing '{path}': {e}")

if images:
    try:
        gif_path = r"C:\Users\minis\OneDrive\Desktop\my_animation.gif"
        imageio.mimsave(gif_path, images, duration=0.10)
        print(f"GIF saved to: {gif_path}")
    except Exception as e:
        print(f"Error saving GIF: {e}")
else:
    print("No valid images found. GIF not created.")

os.makedirs("frames", exist_ok=True)

for i in range(10):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x + i * 0.3)
    plt.figure()
    plt.plot(x, y)
    plt.title(f"Frame {i}")
    plt.savefig(f"frames/frame_{i}.png")
    plt.close()

sine_images = [imageio.imread(f"frames/frame_{i}.png") for i in range(10)]
imageio.mimsave('sine_wave.gif', sine_images, duration=0.10)

def run_gif_viewer(gif_file):
    if not os.path.exists(gif_file):
        print(f"Error: GIF not found at '{gif_file}'")
        return

    gif = Image.open(gif_file)
    frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]

    root = tk.Tk()
    root.title("GIF Viewer")

    label = tk.Label(root, image=frames[0])
    label.pack()
    label.image = frames[0]

    def update_frame(index=0):
        frame = frames[index % len(frames)]
        label.config(image=frame)
        label.image = frame
        root.after(100, update_frame, index + 1)

    root.after(0, update_frame)
    root.mainloop()

def run_image_switcher():
    paths = image_paths[:2]  # Just use first two images
    valid_imgs = []
    for path in paths:
        if os.path.exists(path):
            img = Image.open(path)
            valid_imgs.append(ImageTk.PhotoImage(img))
        else:
            print(f"Missing: {path}")
            valid_imgs.append(None)

    root = tk.Tk()
    root.title("Image Switcher")

    index = [0]
    label = tk.Label(root)
    label.pack()

    def update_image():
        idx = index[0]
        img = valid_imgs[idx]
        if img:
            label.config(image=img)
            label.image = img
        index[0] = (idx + 1) % len(valid_imgs)

    update_image()
    btn = tk.Button(root, text="Next Image", command=update_image)
    btn.pack()

    root.mainloop()


# In[2]:


def run_gif_viewer(gif_file):
    if not os.path.exists(gif_file):
        print(f"Error: GIF not found at '{gif_file}'")
        return

    root = tk.Tk()
    root.title("GIF Viewer")

    try:
        gif = Image.open(gif_file)
        frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
        tk_frames = [ImageTk.PhotoImage(frame) for frame in frames]
    except Exception as e:
        print(f"Error loading frames: {e}")
        root.destroy()
        return

    label = tk.Label(root, image=tk_frames[0])
    label.pack()
    label.image = tk_frames[0]

    current_frame_index = [0]

    def update_frame():
        index = current_frame_index[0]
        frame = tk_frames[index]
        label.config(image=frame)
        label.image = frame
        current_frame_index[0] = (index + 1) % len(tk_frames)
        root.after(100, update_frame)

    root.after(0, update_frame)
    root.mainloop()


# In[3]:


run_gif_viewer(r"C:\Users\minis\OneDrive\Desktop\my_animation.gif")


# In[ ]:




