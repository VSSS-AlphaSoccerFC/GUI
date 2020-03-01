# GUI Repository 
TKinter graphic interface to display our Game Sate in Live Time

---
## Dependencies
* `TKinter`
* `PIL`
* ` Python 3` *(tested on Python 3.7.4)*

---

## Structure of the Repository

* **Python Scripts**
    * **`main.py`** creates a TKinter window which contains 2 Frames:
        * **`dashboard.py`** is the frame where the game's data is displayed and the control panel allocated. It contains the following frames:
            * **`team.py`** is the frame where the robots are placed and where a color bar is displayed representing the team's color *(Blue/Orange)*, therefore they are going to be two of them, containing each one 3 of the following frames:
                * **`robot.py`** is a frame that simulates a flash card composed by:
                    * **`robot_main_panel`** is the front part of the simulated flash card and it displays the robot's position in rectangular coordinates, it's angle given by the computer vision script, the angle given by the MPU6050 *(Gyroscope/Accelerometer)* only for the allies robots, the player mode *(Goalkeeper/Player)* and it's color.
                    * **`robot_info_panel`** is the back part of the simulated flash card only for the allies robots where it's displayed a general overview of the robot's initial configuration parameters, such as its Alias, IP Address, MAC Address, Server Port and Client Port.
            * **`ball.py`** is the frame where the ball's data given by the computer vision script is displayed such as its position in rectagular coordinates.
            * **`control_panel.py`** is the frame where the game state can be manipulated, such as start the game, stopped it, end it, etc. And can also control our team's stategies via buttons.
        * **`settings.py`** is the frame where all of initial configuration data can be manipulated such as the Alias, IP Address, MAC Address, Server Port, Client Port, Team Color, Robot Color, Team Number, Player Mode, and more.

<br>

* **Folders**
    * **`Assets`** contains all the assets so that the GUI can work adequately such as images, animations, etc.

    * **`Configuration`** contains the configuration files listed below:
        * `initial_configuration.csv` is a csv file where the initial configuration for the robots is saved and modified by the Settings Frame.

---

## Preview

![](https://drive.google.com/uc?id=1MrcBCusFpwx9bjcRHtaYPyb2CglUsUf2)
![](https://drive.google.com/uc?id=1HL8Q7GyzoswSPQQ2rvAKV_38cBP2c3W3)

---