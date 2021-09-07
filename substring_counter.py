# Python program to count every repeated substring
# along a string  of random characters and random
# length


def count_substrings(string):
    """


    Parameters
    ----------
    string : str
        String of random characters
        and random length.

    Returns
    -------
    repeated : dict
        Data structure that contains
        the substrings that repeat and
        hoy many times they appear.

    """

    # Initialize empty data structure
    substring_counts = {}

    # Iterate over the string to get the
    # substrings

    for i in range(len(string) - 3):
        substring = string[i:i+4]

        # validate if the substring exists in
        # the data structure to accumulate or
        # add it to it

        if substring not in substring_counts:
            substring_counts[substring] = 1
        else:
            substring_counts[substring] += 1

    # Get just the substrings that appear more
    # than once
    repeated = {k: v for k, v in substring_counts.items() if v > 1}

    return repeated


if __name__ == "__main__":

    # Definition of the string
    s = "abcabcabcuioabcxcr"

    # Count substrings
    print(count_substrings(s))
