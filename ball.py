import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Ball(ttk.Frame):
    def __init__(self, parent, height, width):
        super().__init__(parent)

        self.height = int(height)
        self.width = int(width)

        self["height"] = self.height
        self["width"] = self.width
        self["style"] = "BackgroundORANGE.TFrame"

        self.grid_propagate(0) #disables grid shrinking


        

        self.x = tk.StringVar(value="0")
        self.y = tk.StringVar(value="0")
    

        BACKGROUND_PATH = "Assets/ball_background.jpg"
        background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((int(self.width), int(self.height)), Image.ANTIALIAS))
        background_label = tk.Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image


        ICON_PATH = "Assets/ball3.png" 
        icon_image = ImageTk.PhotoImage(Image.open(ICON_PATH).resize((int(.25*self.width), int(.775*self.height)), Image.ANTIALIAS))
        self.label_icon = tk.Label(self, image=icon_image, borderwidth=0, highlightthickness=0, padx=0,pady=0)
        self.label_icon.grid(column=0, row=0, sticky="NSEW", padx=(20,20), pady=(15,10), rowspan=3)
        self.label_icon.image = icon_image
            
        label_x_tag = ttk.Label(
            self, 
            text='X:',
            style="LightText.TLabel"
        )
        label_x_tag.grid(column=1, row=1, sticky="EW", padx=(30,10), pady=(10,10))

        label_x = ttk.Label(
            self, 
            textvariable=self.x,
            style="LightText.TLabel"
        )
        label_x.grid(column=2, row=1, sticky="EW", padx=(10,50), pady=(10,10))

        label_y_tag = ttk.Label(
            self, 
            text='Y:',
            style="LightText.TLabel"
        )
        label_y_tag.grid(column=3, row=1, sticky="EW", padx=(20,10), pady=(10,10))

        label_y = ttk.Label(
            self, 
            textvariable=self.y,
            style="LightText.TLabel"
        )
        label_y.grid(column=4, row=1, sticky="EW", padx=(10,50), pady=(10,10))

 
    