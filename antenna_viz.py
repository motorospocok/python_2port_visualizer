import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import CheckButtons
from mpl_toolkits.mplot3d import Axes3D

version = "v1.0"

def get_input(prompt, default):
    val = input(f"{prompt} [{default}]: ").strip()
    return float(val) if val else default

A1    = get_input("1. port amplitúdója", 1.0)
pol1  = get_input("1. port polarizációs szöge (fok)", 45.0)
A2    = get_input("2. port amplitúdója", 1.0)
pol2  = get_input("2. port polarizációs szöge (fok)", -45.0)
phase_deg = get_input("Fáziseltérés (fok, 2. port - 1. port)", 90.0)

phase = np.radians(phase_deg)
p1    = np.radians(pol1)
p2    = np.radians(pol2)

x = np.linspace(0, 4 * np.pi, 300)

fig = plt.figure(figsize=(13, 7))
fig.suptitle(f"A1={A1} @{pol1}°  |  A2={A2} @{pol2}°  |  Δφ={phase_deg}°", fontsize=12)

ax = fig.add_axes([0.05, 0.05, 0.70, 0.90], projection="3d")
ax_check = fig.add_axes([0.78, 0.4, 0.18, 0.2])

line1,    = ax.plot([], [], [], color="royalblue", lw=1.5, label=f"1. port ({pol1}°)")
line2,    = ax.plot([], [], [], color="tomato",    lw=1.5, label=f"2. port ({pol2}°)")
line_res, = ax.plot([], [], [], color="seagreen",  lw=2,   label="Eredő")

lim = A1 + A2 + 0.5
ax.set_xlim(x[0], x[-1])
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)
ax.set_xlabel("Terjedési irány")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend(loc="upper left", fontsize=8)

labels     = ["1. port", "2. port", "Eredő"]
visibility = [True, True, True]
lines      = [line1, line2, line_res]

check = CheckButtons(ax_check, labels, visibility)

def on_toggle(label):
    idx = labels.index(label)
    visibility[idx] = not visibility[idx]

check.on_clicked(on_toggle)

def update(t):
    s1 = A1 * np.sin(x - t)
    s2 = A2 * np.sin(x - t + phase)

    # polarizáció: a hullám amplitúdóját Y és Z komponensre bontjuk
    y1, z1 = s1 * np.cos(p1), s1 * np.sin(p1)
    y2, z2 = s2 * np.cos(p2), s2 * np.sin(p2)

    data = [
        (y1, z1),
        (y2, z2),
        (y1 + y2, z1 + z2),
    ]

    for line, (yd, zd), visible in zip(lines, data, visibility):
        if visible:
            line.set_data(x, yd)
            line.set_3d_properties(zd)
        else:
            line.set_data([], [])
            line.set_3d_properties([])

    return lines

frames = np.linspace(0, 2 * np.pi, 120)
ani = animation.FuncAnimation(fig, update, frames=frames, interval=30, blit=False)

plt.show()
