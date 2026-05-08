# Print all permutations of a string

def permute(s, left, right):

    if left == right:
        print("".join(s))

    else:
        for i in range(left, right + 1):

            # Swap characters
            s[left], s[i] = s[i], s[left]

            # Recursive call
            permute(s, left + 1, right)

            # Backtrack (swap back)
            s[left], s[i] = s[i], s[left]


# Input string
string = "ABC"

# Convert string to list
s = list(string)

# Call function
permute(s, 0, len(s) - 1)