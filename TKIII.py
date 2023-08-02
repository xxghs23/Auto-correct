from tkinter import Tk
import tkinter as tk

from tp1_nlp import get_corrections
from tp1_nlp import get_probs
from tp1_nlp import process_data
from tp1_nlp import get_count

# Define a function to perform the autocorrection
def autocorrect(input_text):
    word_l = process_data('shakespeare.txt')
    word_count_dict = get_count(word_l)
    probs = get_probs(word_count_dict)
    vocab = set(word_l)

    # get the corrected text and its probabilities
    corrections = get_corrections(input_text, probs, vocab)

    # check if the corrections list is empty
    if not corrections:
        return input_text, 'black', 1.0

    corrected_text = corrections[0][0]
    corrected_prob = corrections[0][1]

    # set a default color value
    color = 'black'

    # update the color value based on the correction probability
    if corrected_prob > 0.5:
        color = 'green'
    else:
        color = 'red'

    # return the corrected text and its color value
    return corrected_text, color, corrected_prob


# Define the GUI
root = Tk()
root.title("Autocorrect")

input_label = tk.Label(root, text="Enter text to autocorrect:")
input_label.pack()

input_box = tk.Text(root, height=10, width=50)
input_box.pack()

output_label = tk.Label(root, text="Autocorrected text:")
output_label.pack()

output_box = tk.Text(root, height=10, width=50)
output_box.pack()

# Define a function to perform the autocorrection and display the result
def perform_autocorrect():
    input_text = input_box.get('1.0', tk.END) # get the text from the input box
    corrected_text, color, corrected_prob = autocorrect(input_text)
    output_box.delete('1.0', tk.END) # clear any existing output
    output_box.insert(tk.END, corrected_text) # display the corrected text in the output box
    output_box.tag_config("color", foreground=color) # set the color of the corrected text
    output_box.tag_add("color", "1.0", "end") # apply the color to the entire corrected text
    output_box.insert(tk.END, f"\nCorrected probability: {corrected_prob}")

autocorrect_button = tk.Button(root, text="Autocorrect", command=perform_autocorrect)
autocorrect_button.pack()

root.mainloop()
