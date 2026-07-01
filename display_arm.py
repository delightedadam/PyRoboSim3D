import maths_tools

import numpy as np
import matplotlib.pyplot as plt
import arm_config
import copy


class Display_arm:
    def __init__(self, arm):
        self.articulation_active = 1
        self.arm = arm

    def on_key(self, event):
        delta_angle = 0.1
        if event.key == "right":
            self.articulation_active = self.articulation_active + 1
            if self.articulation_active >= len(self.arm.axes):
                self.articulation_active = 1
        elif event.key == "left":
            self.articulation_active = self.articulation_active - 1
            if self.articulation_active < 1:
                self.articulation_active = len(self.arm.axes) - 1
        elif event.key == "up":
            self.arm.angles[self.articulation_active] += delta_angle
        elif event.key == "down":
            self.arm.angles[self.articulation_active] -= delta_angle
        elif event.key == "z":
            for i in range(1, len(self.arm.angles)):
                self.arm.angles = copy.deepcopy(self.arm.repos_angles)
        self.draw_robot()


    #
    # Inspered from stackoverflow :
    # https://stackoverflow.com/questions/27023068/plotting-3d-vectors
    # Autors : Seanny123
    # Date : feb 15, 2017 at 10:27
    #
    def draw_robot(self):
        self.ax.clear()
        self.ax.set_box_aspect((1, 1, 1))

        P = maths_tools.position_bras(self.arm.angles, self.arm.axes, self.arm.vectors, self.arm.depart)
        
        for i in range(0, len(P)-1):
            arrow = P[i+1] - P[i]
            epaisseur = 6 if i == self.articulation_active else 2
            
            SIZE_ARROW = 1.0
            self.ax.quiver(
                P[i][0],
                P[i][1],
                P[i][2],
                arrow[0],
                arrow[1],
                arrow[2],
                color=self.arm.couleurs[i],
                arrow_length_ratio=0.12,
                linewidth=epaisseur,
                length=SIZE_ARROW,
            )

        xmin, xmax = -100, 100
        ymin, ymax = -100, 100
        zmin, zmax = 0, 120
        self.ax.set_xlim([xmin, xmax])
        self.ax.set_ylim([ymin, ymax])
        self.ax.set_zlim([zmin, zmax])
        self.ax.set_xlabel("X (cm)")
        self.ax.set_ylabel("Y (cm)")
        self.ax.set_zlabel("Z (cm)")
        self.ax.set_title(
            f"Axe actif : V{self.articulation_active} ({self.arm.axes[self.articulation_active].upper()})"
        )
        self.fig.canvas.draw_idle()

    def animate_arm(self, block=True):
        self.articulation_active = 1


        self.fig = plt.figure(figsize=(9, 7))
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.fig.canvas.mpl_connect("key_press_event", self.on_key)

        self.draw_robot()
        plt.show(block=block)