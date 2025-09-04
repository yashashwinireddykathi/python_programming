#all ASCII charecters with their values
def ascii():
    for i in range(0, 128):  # ASCII values range from 0 to 127
        print(f"Character: '{chr(i)}' -> ASCII Value: {i}")# from 0-32 values are null
ascii()