"""
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
> text = "X-DSPAM-Confidence:    0.8475";
output: 0.8475
"""

text = "X-DSPAM-Confidence:    0.8475"
num_pos = text.find('0')
num = text[num_pos: num_pos+6]
num_float = float(num)

print(num_float)