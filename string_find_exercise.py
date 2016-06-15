# 6.5 Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

start_pos = text.find('0')
end_pos = len(text) - 1
end = end_pos + 1

num = float(text[start_pos:end])

print num