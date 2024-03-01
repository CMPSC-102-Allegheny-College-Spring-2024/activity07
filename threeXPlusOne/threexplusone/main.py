""" Run a simple analysis of the equation, 3x+1.
This is a recursive function in which it is defined in a system by the following.

f(x)  = {3x+1} if f(x) is odd
f(x)  = (f(x)/2) if f(x) is even.
"""

""" output :
         @ Seed number  --> 20
         0) 10  Even 
         1) 5  Odd 
         2) 16  Even  <-- Max Value 
         3) 8  Even 
         4) 4  Even 
         5) 2  Even 
         6) 1  Odd 
         Max value in sequence is 16
"""

import matplotlib.pyplot as plt
import numpy as np

from rich.console import Console
from rich import print
import typer

# TODO: Create a Typer object to support the command-line interface


def calculateSequence(result:int)->list:
    # TODO: define a list for the sequence. Use the rest of the code to determine the name of this list.


    while result != 1:
        if result % 2 == 0: #even value
            result = result/2
        else: # odd value
            result = result * 3 + 1

        # TODO: append the current result to the Collatz sequence list.            


    return collatzSequence_list

# end of calculateSequence()
    
def getMaxSeqValue(sequence_list:list) -> int:
    """ Find the largest value in the sequence. """
    # keep track of largest value for display at finish
    maxValue_int = 0 # intitial value of 

    for value in sequence_list:
        if value > maxValue_int:
            # TODO: Update the maximum value if a larger value is found.


    return int(maxValue_int)

# end of getMaxSeqValue()

def prettyPrinter(sequence_list:list, maxValue: int) -> None:
    """ Print up the list with odd or even after the sequence. """
    polarity = "Even"
    for i in enumerate(sequence_list):
        if i[1] % 2 == 0: # sequence value 
            # TODO: Set 'Even' or "Odd" as necessary
            polarity = f"[bold green] ??????????? [/bold green]"
        else:
            # TODO: Set 'Even' or "Odd" as necessary
            polarity = "[red] ??????????? [/red]"
    # check for the max value to highlight
        if i[1] == maxValue:
            polarity = polarity + f"[bold yellow] <-- Max Value [/bold yellow]"

        # TODO: Print the formatted sequence value with its polarity.

# end of prettyPrinter()

@cli.command()
def main(seed: str = typer.Option(..., prompt=True)) -> None:
    """Driver function for the math experiment using the seed number."""
    maxValue_int = 0  # largest value of sequence

    seed = int(seed) # convert string to int
    print(f"\t [purple]@ Seed number [/purple] --> {seed}")
    # check for negative numbers
    if seed < 0:
        print("\t [red] No negative numbers, please.[/red]")
        exit() # exit the program
    # TODO: Calculate the Collatz sequence based on the provided seed.


    # Determine the maximum value of the sequence
    # TODO: Find the maximum value in the sequence.
    # maxValue = 

    # print up the sequence in tidy listing
    prettyPrinter(result_sequence_list, maxValue)

    # Display the maximum value in sequence
    # TODO: Display the maximum value in the sequence.

    # Prepare a plot of results
    plotResults(result_sequence_list, len(result_sequence_list), maxValue)

# end of main()


def plotResults(result_sequence:list, seqSize_int: int, maxValue: int)->None:
    """ Function to plot list of results. """
    ypoints = np.array(result_sequence)
    plt.title(f"Collatz Sequence\n Sequence size: {seqSize_int}")
    plt.xlabel('Position in Sequence')
    plt.ylabel('Magnitude')
    # plot blue hozitonal line for max value 
    plt.axhline(y = maxValue, color = 'b', linestyle = ':', label = f"max value:\n {maxValue}") 
    # plotting the legend 
    plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper center')   
    plt.plot(ypoints)
    plt.show()
# end of plotResults()
