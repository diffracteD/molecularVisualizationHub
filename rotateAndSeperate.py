'''
Given that a PDB having two chains (A and B), this code will rotate it 360 degree along provided Z axis.
THen seperate each chain and put them back together.
$$ UNDER TESTING 
Designed By: Abhisek Mondal, UCSF
'''

from chimera import runCommand

# Step 1: Rotate both chains (A and B) 360 degrees along the Z-axis
runCommand("turn z 1 360")  # 1-degree steps for smooth animation; 360 steps in total

# Step 2: Separate the chains spatially
# Select chain A and move it along the X-axis
runCommand("select #0:.A")  # Select chain A in model #0
runCommand("move x -10")    # Move chain A by -10 units along the X-axis

# Select chain B and move it along the X-axis in the opposite direction
runCommand("select #0:.B")  # Select chain B in model #0
runCommand("move x 10")     # Move chain B by +10 units along the X-axis

# Step 3: Bring the chains back together
runCommand("select #0:.A")  # Select chain A again
runCommand("move x 10")     # Move chain A back to its original position

runCommand("select #0:.B")  # Select chain B again
runCommand("move x -10")    # Move chain B back to its original position

# Clear the selection to tidy up
runCommand("select clear")
