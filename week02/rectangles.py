def get_positif_value(prompt_text):

    #promt the value
    value = float(input(prompt_text))

    #check if the value is positif and reprompt if needed
    while value < 0:
        print("Sorry, the value cannot be negative.")
        value = float(input(prompt_text))

    # Return the value
    return value

length = get_positif_value("What's The Length of the rectangle? ")
width = get_positif_value("What's The width of the rectangle? ")

area = length * width

print(f"The area is: {area}")