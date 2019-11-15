# Ask for input to determine height
height = int(input("Enter an integer between 1-8: "))

# Check if input is an integer between 1-8
if 0 < height < 9:
    # Increment number of hashtags in each row
    for x in range(height):
        for y in range(x + 1):
            print("#", end="")
        # Line break after every row
        print()


# Error if input is not integer between 1-8
else:
    print("Invalid entry")
    exit