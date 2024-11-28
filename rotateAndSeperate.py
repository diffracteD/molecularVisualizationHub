'''
Given that a PDB having two chains (A and B), this code will rotate it 360 degree along provided Y axis.
Then render the chain in cartoon. Make chain A opaque and make another B chain at 70% transparent and rotates along Y axis.
More features soo.
$$ UNDER TESTING 
Designed By: Abhisek Mondal, UCSF
'''

from chimera import runCommand

# Step 1: Rotate both chains (A and B) 360 degrees along the Y-axis
runCommand("turn y 1 360")  # 1-degree steps for smooth animation; 360 steps in total

# Step 2: Set chain representations and transparency
# Display chain A as a cartoon and set 0% transparency
runCommand("select #0:.A")          # Select chain A in model #0
runCommand("display")               # Ensure chain A is visible
runCommand("cartoon")               # Set representation to cartoon
runCommand("transparency 0 target c")  # Set 0% transparency (c = cartoon)

# Display chain B as a cartoon and set 70% transparency
runCommand("select #0:.B")          # Select chain B in model #0
runCommand("display")               # Ensure chain B is visible
runCommand("cartoon")               # Set representation to cartoon
runCommand("transparency 70 target c")  # Set 70% transparency (c = cartoon)

# Step 3: Clear the selection to tidy up
runCommand("select clear")

