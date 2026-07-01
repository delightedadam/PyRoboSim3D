import arm_config
import display_arm
import numpy as np

position_arm = np.array([0.0, 0.0, 0.0])
arm = arm_config.robotis(position_arm)

display = display_arm.Display_arm(arm)
display.animate_arm(block=True)

