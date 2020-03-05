import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Control_Panel(ttk.Frame):
    def __init__(self, parent, height, width):
        super().__init__(parent)

        self.height = int(height)
        self.width = int(width)


        self.parent = parent

        print(self.parent.controller)


        self["height"] = self.height
        self["width"] =  self.width
        self["style"] = "BackgroundPURPLE.TFrame"

        self.grid_propagate(0) #disables grid shrinking

        BACKGROUND_PATH = "Assets/panel_background.jpg"
        background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((int(self.width), int(self.height)), Image.ANTIALIAS))
        background_label = tk.Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        IMAGE_POWER_ON_BUTTON_PATH = "Assets/powered_off_button.png" 
        power_on_button_image = ImageTk.PhotoImage(Image.open(IMAGE_POWER_ON_BUTTON_PATH).resize((int(.06*self.width), int(.55*self.height)), Image.ANTIALIAS))
        
        self.power_on_button = tk.Button(
                    self, 
                    image=power_on_button_image, 
                    borderwidth=0, 
                    highlightthickness=0, 
                    padx=0,
                    pady=0,
                    cursor="hand2",
                    command=self.alternate_power_status
                    )
        self.power_on_button.grid(row=0, column=0, pady=(10, 10), padx=(20,20))
        self.power_on_button.image = power_on_button_image

        IMAGE_STOP_BUTTON_PATH = "Assets/b3.png" 
        stop_button_image = ImageTk.PhotoImage(Image.open(IMAGE_STOP_BUTTON_PATH).resize((int(.056*self.width), int(.48*self.height)), Image.ANTIALIAS))

        stop_button = tk.Button(
                    self, 
                    image=stop_button_image, 
                    borderwidth=0, 
                    highlightthickness=0, 
                    padx=0,
                    pady=0,
                    cursor="hand2",
                    # command=show_info_panel
                    )
        stop_button.grid(row=0, column=1, pady=(10, 10), padx=(int(.31*self.width),20))
        stop_button.image = stop_button_image

        IMAGE_PLAY_BUTTON_PATH = "Assets/b2.png" 
        play_button_image = ImageTk.PhotoImage(Image.open(IMAGE_PLAY_BUTTON_PATH).resize((int(.056*self.width), int(.48*self.height)), Image.ANTIALIAS))

        play_button = tk.Button(
                    self, 
                    image=play_button_image, 
                    borderwidth=0, 
                    highlightthickness=0, 
                    padx=0,
                    pady=0,
                    cursor="hand2",
                    command=self.alternate_power_status
                    )
        play_button.grid(row=0, column=2, pady=(10, 10), padx=(20,20))
        play_button.image = play_button_image

        IMAGE_PAUSE_BUTTON_PATH = "Assets/b1.png" 
        pause_button_image = ImageTk.PhotoImage(Image.open(IMAGE_PAUSE_BUTTON_PATH).resize((int(.056*self.width), int(.48*self.height)), Image.ANTIALIAS))

        pause_button = tk.Button(
                    self, 
                    image=pause_button_image, 
                    borderwidth=0, 
                    highlightthickness=0, 
                    padx=0,
                    pady=0,
                    cursor="hand2",
                    #command=
                    )
        pause_button.grid(row=0, column=3, pady=(10, 10), padx=(20,20))
        pause_button.image = pause_button_image

        IMAGE_SETTINGS_BUTTON_PATH = "Assets/settings_icon.png" 
        settings_button_image = ImageTk.PhotoImage(Image.open(IMAGE_SETTINGS_BUTTON_PATH).resize((int(.056*self.width), int(.48*self.height)), Image.ANTIALIAS))

        settings_button = tk.Button(
                    self, 
                    image=settings_button_image, 
                    borderwidth=0, 
                    highlightthickness=0, 
                    padx=0,
                    pady=0,
                    cursor="hand2",
                    #command=
                    )
        settings_button.grid(row=0, column=4, pady=(10, 10), padx=(int(.3*self.width),20))
        settings_button.image = settings_button_image

    def alternate_power_status(self):
        self.parent.controller.is_powered_on = not self.parent.controller.is_powered_on
        IMAGE_POWER_ON_BUTTON_PATH = "Assets/powered_on_button.png" if self.parent.controller.is_powered_on else "Assets/powered_off_button.png"
        power_on_button_image = ImageTk.PhotoImage(Image.open(IMAGE_POWER_ON_BUTTON_PATH).resize((int(.06*self.width), int(.55*self.height)), Image.ANTIALIAS))
        self.power_on_button["image"] = power_on_button_image
        self.power_on_button.image = power_on_button_image

        

        