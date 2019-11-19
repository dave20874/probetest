# probetest
Analyze performance of a 3D printer probe on a build surface.

The objective is to measure the surface of a 3D print bed in a small area, 5x5mm.

## Process overview

To collect the data, use prconsole to run probes.gcode and collect the output messages.

Then, edit the output text into a CSV file with these columns:
X, Y, Mean, Min, Max, Range, StdDev.

Finally, view the results by running the Probes.ipynb Jupyter notebook.

### Running Prconsole
With a PC connected to the 3D printer, launch prconsole from a CMD window.  Best start with a fresh command window since we'll be
grabbing all the text from it in the post-processing steps.

```bash
> cd \"Program Files"\Prusa3D\Pronterface
> pronsole
connect com7  (use the COM port of your 3D printer)
load <path-to-gcode>/probes.gcode
print

<About 8-9 hours later>
exit
```

### Capture the output
Select all text from that CMD window and paste it into a file, save as output.txt.  I did.  
You can see my results here in the repo.

Edit output.txt to create probes.csv.  Find the lines with the mean,
min, max, range and the next line with standard deviation.  Isolate
just the values, separated by commas, on a single line.  Then add on
the X, Y coordinates for each line.  You can find them in the
probes.csv included in this repo.  (I did this steps with Emacs using
macros.  If necessary, I could write a simple Python script to merge
the data into a CSV.)

### Analyze the data.  Run the Jupyter notebook, probes.ipynb.  When
you run all the cells, it will read your probes.csv file and show the
results in the graphs.



