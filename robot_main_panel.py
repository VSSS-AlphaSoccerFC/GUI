import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Main_Panel(ttk.Frame):
    def __init__(self, container, robot, show_info_panel):
        super().__init__(container)

        self.robot = robot

        self.height = self.robot.height
        self.width = self.robot.width

        self["height"] = self.height
        self["width"] = self.width
        
        self["style"] = "Background.TFrame"

        background_label = tk.Label(self, image=self.robot.BACKGROUND_IMAGE)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = self.robot.BACKGROUND_IMAGE

        self.grid_propagate(0) #disables grid shrinking

        ICON_PATH = "Assets/goalkeeper.png" if self.robot.player_mode == 'goalkeeper' else "Assets/soccer_player.png"
        icon_image = ImageTk.PhotoImage(Image.open(ICON_PATH).resize((int(.2*self.width), int(.3*self.height)), Image.ANTIALIAS))
        self.label_icon = tk.Label(self, image=icon_image, borderwidth=0, highlightthickness=0, padx=0,pady=0)
        self.label_icon.grid(column=0, row=0, sticky="NSEW", padx=(20,20), pady=(85,60), rowspan=3)
        self.label_icon.image = icon_image

        label_x_tag = ttk.Label(
            self, 
            text='X:',
            style="LightText.TLabel"
        )
        label_x_tag.grid(column=1, row=0, sticky="EW", padx=(30,10), pady=(70,10))

        label_x = ttk.Label(
            self, 
            textvariable=self.robot.x,
            style="LightText.TLabel"
        )
        label_x.grid(column=2, row=0, sticky="EW", padx=(10,50), pady=(70,10))

        label_y_tag = ttk.Label(
            self, 
            text='Y:',
            style="LightText.TLabel"
        )
        label_y_tag.grid(column=3, row=0, sticky="EW", padx=(20,10), pady=(70,10))

        label_y = ttk.Label(
            self, 
            textvariable=self.robot.y,
            style="LightText.TLabel"
        )
        label_y.grid(column=4, row=0, sticky="EW", padx=(10,50), pady=(70,10))

        label_vision_angle_tag = ttk.Label(
            self,
            text= 'Vision Angle:',
            style="LightText.TLabel"
        )
        label_vision_angle_tag.grid(column=1, row=1, sticky="EW", padx=(30,0), pady=(10,10), columnspan=2)

        label_vision_angle = ttk.Label(
            self,
            textvariable=self.robot.vision_angle,
            style="LightText.TLabel"
        )
        label_vision_angle.grid(column=3, row=1, sticky="EW", padx=(30,0), pady=(10,10), columnspan=2)

        
        self.color_bar = tk.Label(self, bg=self.robot.color)
        self.color_bar.grid(row=0, column=4, sticky="NS", pady=(80, 0), padx=(110,15), rowspan=2 if self.robot.team_number == "team1" else 1, columnspan=2)

        I_ICON_PATH = "Assets/i_icon.png"
        i_icon_image = ImageTk.PhotoImage(Image.open(I_ICON_PATH).resize((int(.07*self.width), int(.125*self.height)), Image.ANTIALIAS))

        if self.robot.team_number == "team1":
            label_giroscope_angle_tag = ttk.Label(
            self, 
            text='Giroscope Angle:',
            style="LightText.TLabel"
            )
            label_giroscope_angle_tag.grid(column=1, row=2, sticky="EW", padx=(30,0), pady=(10,60), columnspan=2)

            label_giroscope_angle = ttk.Label(
                self, 
                textvariable=self.robot.giroscope_angle,
                style="LightText.TLabel"
            )
            label_giroscope_angle.grid(column=3, row=2, sticky="EW", padx=(30,0), pady=(10,60), columnspan=2)

            info_button = tk.Button(
                self, 
                image=i_icon_image, 
                borderwidth=0, 
                highlightthickness=0, 
                padx=0,
                pady=0,
                cursor="hand2",
                command=show_info_panel
            )
            info_button.grid(row=2, column=1, columnspan=5, pady=(10, 0), padx=(int(self.width*.62),0))
            info_button.image = i_icon_image
