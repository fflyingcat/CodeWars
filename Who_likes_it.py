def likes(names):
    # get the total names
    n = len(names)

    # if none
    if n == 0:
        return 'no one likes this'
    # if one
    elif n == 1:
        return f"{names[0]} likes this"
    # if two
    elif n == 2:
        return f"{names[0]} and {names[1]} like this"
    # if three
    elif n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    # if more than three
    else:
        return f"{names[0]}, {names[1]} and {n - 2} others like this"

#https://www.codewars.com/kata/5266876b8f4bf2da9b000362