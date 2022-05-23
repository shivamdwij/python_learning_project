def mcd(text):
    first_letter=text[0]
    inbetween_words=text[1:3]   # indexing & slicing
    fourth_letter=text[3]
    rest=text[4:]
    return first_letter.upper() + inbetween_words + fourth_letter.upper().upper() + rest

text='macdonalds'

results = mcd(text)
print(results)


# SLEEKER WAY 
""" def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'  """