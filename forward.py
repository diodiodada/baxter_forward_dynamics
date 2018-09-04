import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


def rotate_y(theta_Y):
    ratate = np.array([[math.cos(theta_Y), 0, math.cos(theta_Y + math.pi / 2)],
                       [0, 1, 0],
                       [math.sin(theta_Y), 0, math.sin(theta_Y + math.pi / 2)]])
    return ratate


def rotate_x(theta_X):
    ratate = np.array([[1, 0, 0],
                       [0, math.cos(theta_X), math.cos(theta_X + math.pi / 2)],
                       [0, math.sin(theta_X), math.sin(theta_X + math.pi / 2)]])
    return ratate


def translation_along_x(l):
    return np.array([l, 0, 0])


def translation_along_z(l):
    return np.array([0, 0, -l])


def forward(theta_1, theta_2, theta_3, theta_4, theta_5, theta_6):

    z_1 = 10
    x_2 = 374.29
    z_3 = 69
    x_4 = 364.35
    z_5 = 69
    x_6 = 270.35

    hand2wrist_down = np.array([229.525, 0, 0])

    hand2wrist_up = np.dot(rotate_y(theta_1), hand2wrist_down) + translation_along_z(z_1)

    hand2elbow_down = np.dot(rotate_x(theta_2), hand2wrist_up) + translation_along_x(x_2)

    hand2elbow_up = np.dot(rotate_y(theta_3), hand2elbow_down) + translation_along_z(z_3)

    hand2shoulder_down = np.dot(rotate_x(theta_4), hand2elbow_up) + translation_along_x(x_4)

    hand2shoulder_up = np.dot(rotate_y(theta_5), hand2shoulder_down) + translation_along_z(z_5)

    hand2base = np.dot(rotate_x(theta_6), hand2shoulder_up) + translation_along_x(x_6)

    # ======================================================================================

    wrist_down2wrist_up = np.array([0, 0, -10])

    wrist_down2elbow_down = np.dot(rotate_x(theta_2), wrist_down2wrist_up) + translation_along_x(x_2)

    wrist_down2elbow_up = np.dot(rotate_y(theta_3), wrist_down2elbow_down) + translation_along_z(z_3)

    wrist_down2shoulder_down = np.dot(rotate_x(theta_4), wrist_down2elbow_up) + translation_along_x(x_4)

    wrist_down2shoulder_up = np.dot(rotate_y(theta_5), wrist_down2shoulder_down) + translation_along_z(z_5)

    wrist_down2base = np.dot(rotate_x(theta_6), wrist_down2shoulder_up) + translation_along_x(x_6)

    # ======================================================================================

    wrist_up2elbow_down = np.array([374.29, 0, 0])

    wrist_up2elbow_up = np.dot(rotate_y(theta_3), wrist_up2elbow_down) + translation_along_z(z_3)

    wrist_up2shoulder_down = np.dot(rotate_x(theta_4), wrist_up2elbow_up) + translation_along_x(x_4)

    wrist_up2shoulder_up = np.dot(rotate_y(theta_5), wrist_up2shoulder_down) + translation_along_z(z_5)

    wrist_up2base = np.dot(rotate_x(theta_6), wrist_up2shoulder_up) + translation_along_x(x_6)

    # ======================================================================================

    elbow_down2elbow_up = np.array([0, 0, -69])

    elbow_down2shoulder_down = np.dot(rotate_x(theta_4), elbow_down2elbow_up) + translation_along_x(x_4)

    elbow_down2shoulder_up = np.dot(rotate_y(theta_5), elbow_down2shoulder_down) + translation_along_z(z_5)

    elbow_down2base = np.dot(rotate_x(theta_6), elbow_down2shoulder_up) + translation_along_x(x_6)

    # ======================================================================================

    elbow_up2shouler_down = np.array([364.35, 0, 0])

    elbow_up2shoulder_up = np.dot(rotate_y(theta_5), elbow_up2shouler_down) + translation_along_z(z_5)

    elbow_up2base = np.dot(rotate_x(theta_6), elbow_up2shoulder_up) + translation_along_x(x_6)

    # ======================================================================================

    shoulder_down2shoulder_up = np.array([0, 0, -69])

    shoulder_down2base = np.dot(rotate_x(theta_6), shoulder_down2shoulder_up) + translation_along_x(x_6)

    # ======================================================================================

    shoulder_up2base = np.array([270.35, 0, 0])

    # ======================================================================================

    base2base = np.array([0, 0, 0])

    return np.array([hand2base,
                     wrist_down2base, wrist_up2base,
                     elbow_down2base, elbow_up2base,
                     shoulder_down2base, shoulder_up2base,
                     base2base])

# ===================================================================


def make_data():

    r = []

    for degree3 in np.linspace(-math.pi, math.pi, 10):
        for degree2 in np.linspace(-math.pi, math.pi, 25):
            for degree1 in np.linspace(-math.pi, math.pi, 25):
                point = forward(0, 0, 0, 0, 0, 0).T

                r.append(point)

    r = np.array(r)

    return r


def update_lines(num, dataLines, lines):
    lines.set_data(dataLines[num, 0:2, :])
    lines.set_3d_properties(dataLines[num, 2, :])
    return lines


fig = plt.figure()
ax = p3.Axes3D(fig)

data = make_data()

lines = ax.plot(data[0, 0, 0:1], data[0, 1, 0:1], data[0, 2, 0:1])[0]

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

ax.set_xlim(-1200, 1200)
ax.set_ylim(-1200, 1200)
ax.set_zlim(-1200, 1200)

line_ani = animation.FuncAnimation(fig, update_lines, 25*25*10, fargs=(data, lines),
                                   interval=1, blit=False)

plt.show()
