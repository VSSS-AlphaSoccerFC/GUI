import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Strategy_Panel(ttk.Frame):
    def __init__(self, parent, height, width):
        super().__init__(parent)

        self.height = int(height)
        self.width = int(width)

        self.parent = parent

        self["height"] = self.height
        self["width"] =  self.width
        self["style"] = "BackgroundPURPLE.TFrame"

        self.grid_propagate(0) #disables grid shrinking

        BACKGROUND_PATH = "Assets/panel_background_2.jpg"
        background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((int(self.width), int(self.height)), Image.ANTIALIAS))
        background_label = tk.Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        
        stategy_buttons = {}

        # 8 es 3   13 es 4  14 es 2  16 es 1
        
        for button_num in range(8):
            IMAGE_BUTTON_PATH = f"Assets/button{int(button_num%4+1)}.png" #if button_num%4 != 1 else "Assets/btn6.png"
            silver_button_image = ImageTk.PhotoImage(Image.open(IMAGE_BUTTON_PATH).resize((int(.2*self.width), int(.3*self.height)), Image.ANTIALIAS))

            stategy_buttons[f"strategy_button_{button_num}"] = tk.Button(
                        self, 
                        image=silver_button_image, 
                        borderwidth=0, 
                        highlightthickness=0, 
                        padx=0,
                        pady=0,
                        cursor="hand2",
                        text="",
                        compound="center"
                        # command=show_info_panel
                        )
            stategy_buttons[f"strategy_button_{button_num}"].grid(row=button_num//4, column=button_num%4, pady=(20, 0), padx=(30,10))
            stategy_buttons[f"strategy_button_{button_num}"].image = silver_button_image
