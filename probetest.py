import numpy as np

print("G28")
for x in np.arange(150-2.5, 150+2.5, 0.2):
    for y in np.arange(150-2.5, 150+2.5, 0.2):
        print("M48 P10 X%6.2f Y%6.2f"%(x, y))

