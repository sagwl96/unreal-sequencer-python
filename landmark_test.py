import tkinter
from tkinter import filedialog

# Used to select the video file to run pose tracking on
tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
file = filedialog.askopenfilenames()

f = open(file[0])

data = f.read().split("\n\n")

for frames in data:
    landmarks = frames.split(",")
    x = 0
    y = 0
    z = 0
    for items in landmarks:
        if "x" in items:
            print("x:", float(items[items.index("x"):items.index("y")].split(" ")[1]))
        if "y" in items:
            print("y:", float(items[items.index("y"):items.index("z")].split(" ")[1]))
        if "z" in items:
            print("z:", float(items[items.index("z"):items.index("v")].split(" ")[1]))
    try:
        frame_number = int(landmarks[0].split("\n")[0])
    except:
        pass
    #print(landmarks)

