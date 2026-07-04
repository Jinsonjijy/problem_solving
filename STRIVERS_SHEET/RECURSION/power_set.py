"""


Power Set: Print all the possible subsequences of the String




Problem Description: Given a string, find all the possible subsequences of the string (we studied in the plus two about the power set)
"""
def power_set(s):
    res = []

    def backtrack(curr_path, i):
        # Base case: we've processed all characters
        if i == len(s):
            res.append("".join(curr_path))
            return

        # Choice 1: Include the current character
        curr_path.append(s[i])
        backtrack(curr_path, i + 1)

        # Backtrack (undo the choice)
        curr_path.pop()

        # Choice 2: Exclude the current character
        backtrack(curr_path, i + 1)

    backtrack([], 0)
    return res


print(power_set("abc"))