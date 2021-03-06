from tkinter import ttk
import tkinter as tk
from team import Team
from settings import Settings
from dashboard import Dashboard

import socket
from threading import Thread

from game import Ball, State, Robot


COLOR_PRIMARY = "black"
COLOR_SECONDARY = "#293846"
COLOR_LIGHT_BACKGROUND = "#fff"
COLOR_LIGHT_TEXT = "#eee"
COLOR_DARK_TEXT = "#8095a8"



class Main(tk.Tk):
    def __init__(self, read_socket):
        super().__init__()

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Dashboard.TFrame", background=COLOR_LIGHT_BACKGROUND)

        style.configure("BackgroundRED.TFrame", background="red")
        style.configure("BackgroundBLUE.TFrame", background="blue")
        style.configure("BackgroundGREEN.TFrame", background="green")
        style.configure("BackgroundYELLOW.TFrame", background="yellow")
        style.configure("BackgroundPURPLE.TFrame", background="purple")
        style.configure("BackgroundWHITE.TFrame", background="white")
        style.configure("BackgroundORANGE.TFrame", background="orange")
        style.configure("BackgroundPINK.TFrame", background="pink")


        style.configure("Background.TFrame", background=COLOR_PRIMARY)
        style.configure(
            "Dashboard.TLabel",
            background=COLOR_LIGHT_BACKGROUND,
            foreground=COLOR_DARK_TEXT,
            font="Courier 46"
        )


        style.configure(
            "LightText.TLabel",
            background=COLOR_PRIMARY,
            foreground=COLOR_LIGHT_TEXT,
            font=("TkDefaultFont", 11)
        )

        style.configure(
            "Button.TButton",
            background=[COLOR_SECONDARY],
            foreground=COLOR_LIGHT_TEXT,
            font=("TkDefaultFont", 11)
        )

        style.configure(
            "info_button.TButton",
            background="black",
            foreground="white",
            font=("TkDefaultFont", 11)
        )

        style.map(
            "Button.TButton",
            background=[("active", COLOR_PRIMARY), ("disabled", COLOR_LIGHT_TEXT)]
        )

        SCREEN_WIDTH = self.winfo_screenwidth()
        SCREEN_HEIGHT = self.winfo_screenheight()

        self["background"] = COLOR_PRIMARY

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        container = ttk.Frame(self)
        container["height"] = SCREEN_HEIGHT
        container["width"] = SCREEN_WIDTH
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = {}
        self.is_powered_on = False

        settings_frame = Settings(container, self, lambda: self.show_frame(Dashboard), height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
        dashboard_frame = Dashboard(container, self, lambda: self.show_frame(Settings), height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
        settings_frame.grid(row=0, column=0, sticky="NESW")
        dashboard_frame.grid(row=0, column=0, sticky="NESW")

        self.frames[Settings] = settings_frame
        self.frames[Dashboard] = dashboard_frame
        
        self.show_frame(Dashboard)

        self.title('ALPHA SOCCER FC v1.0')
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.resizable(False, False)

        print(SCREEN_HEIGHT, SCREEN_WIDTH)

        self.global_state = State(
            home_robots=[Robot(rid=0, team=1, color="blue", sock=None, x=0, y=0, yaw=0), Robot(rid=1, team=1, color="green", sock=None, x=0, y=0, yaw=0), Robot(rid=2, team=1, color="red", sock=None, x=0, y=0, yaw=0)],
            away_robots=[Robot(rid=0, team=2, color="blue", sock=None, x=0, y=0, yaw=0), Robot(rid=1, team=2, color="green", sock=None, x=0, y=0, yaw=0), Robot(rid=2, team=2, color="red", sock=None, x=0, y=0, yaw=0)],
            ball=Ball()
            )

        self.read_socket = read_socket

        

        self.update()
        
       
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


    def update(self):
        #Team 1
        self.frames[Dashboard].team1.robot1.x.set(self.global_state.home_robots[0].x)
        self.frames[Dashboard].team1.robot1.y.set(self.global_state.home_robots[0].y)
        self.frames[Dashboard].team1.robot1.vision_angle.set(self.global_state.home_robots[0].yaw)

        self.frames[Dashboard].team1.robot2.x.set(self.global_state.home_robots[1].x)
        self.frames[Dashboard].team1.robot2.y.set(self.global_state.home_robots[1].y)
        self.frames[Dashboard].team1.robot2.vision_angle.set(self.global_state.home_robots[1].yaw)

        self.frames[Dashboard].team1.robot3.x.set(self.global_state.home_robots[2].x)
        self.frames[Dashboard].team1.robot3.y.set(self.global_state.home_robots[2].y)
        self.frames[Dashboard].team1.robot3.vision_angle.set(self.global_state.home_robots[2].yaw)
        
        #Team 2

        self.frames[Dashboard].team2.robot1.y.set(self.global_state.away_robots[0].y)
        self.frames[Dashboard].team2.robot1.x.set(self.global_state.away_robots[0].x)

        self.frames[Dashboard].team2.robot2.y.set(self.global_state.away_robots[1].y)
        self.frames[Dashboard].team2.robot2.x.set(self.global_state.away_robots[1].x)

        self.frames[Dashboard].team2.robot3.y.set(self.global_state.away_robots[2].y)
        self.frames[Dashboard].team2.robot3.x.set(self.global_state.away_robots[2].x)

        #Ball
        self.frames[Dashboard].ball.x.set(self.global_state.ball.x)
        self.frames[Dashboard].ball.y.set(self.global_state.ball.y)

        
        self.after(30, self.update)


    def listen(self):
        self.read_socket.listen(0)
        while True:
            client, addr = self.read_socket.accept()
            while True:
                content = client.recv(45) # Serialized protobuff data
                if len(content) ==0:
                    break
                else:
                    self.global_state.update(content)
                    
            client.close()
            


if __name__ == '__main__':     
    # Server configuration
    read_socket = socket.socket()
    read_socket.bind(('0.0.0.0', 4000))

    root = Main(read_socket)

    p = Thread(target=root.listen)
    p.start()
    root.mainloop()
    p.join()




