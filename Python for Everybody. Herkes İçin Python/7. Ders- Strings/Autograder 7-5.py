text = "X-DSPAM-Confidence:    0.8475";



index = text.find(':')

result = text.strip()[index+1:]

print(float(result))
