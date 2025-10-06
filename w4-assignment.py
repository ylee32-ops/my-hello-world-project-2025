# import required modules
from tkinter import *
from PIL import Image, ImageDraw, ImageTk
import math
import seaborn as sns

width, height = 800, 400
scaleFactor = 4 
img = Image.new("RGBA", (width * scaleFactor, height * scaleFactor), (10, 10, 30, 255))
draw = ImageDraw.Draw(img)

palette = list(sns.color_palette("cool", 12).as_hex())
get_rgb = lambda x: tuple(int(x[i:i+2], 16) for i in (0, 2, 4))
rgb_palette = [get_rgb(c.replace("#", "")) for c in palette]

rows = 8
cols = 25
circle_radius = 80 * scaleFactor
spacing_x = width * scaleFactor / cols
spacing_y = height * scaleFactor / rows

for i in range(rows):
    for j in range(cols):
        wave_offset = math.sin(j * 0.5 + i * 0.4) * 40 * scaleFactor
        x = int(j * spacing_x + spacing_x / 2)
        y = int(i * spacing_y + spacing_y / 2 + wave_offset)

        color_index = int((j / cols) * (len(rgb_palette) - 1))
        color = (*rgb_palette[color_index], 100 + int(80 * abs(math.sin(i + j * 0.3))))

        draw.ellipse(
            (x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius),
            fill=color,
            outline=None
        )

img = img.resize((width, height), resample=Image.LANCZOS)

app = Tk()
app.title("Wave Flow Pattern 🌊")
canvas = Canvas(app, width=width, height=height, bg="black")
canvas.pack()

tk_img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, anchor="nw", image=tk_img)

img.save("wave_flow_pattern.png", "PNG")

app.mainloop()

