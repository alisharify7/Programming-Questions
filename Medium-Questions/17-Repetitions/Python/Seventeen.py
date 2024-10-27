def max_frequency(chars: str) -> tuple:
    """ This function returns the element that has the most repetitions in the DNA strand """
    prevous_max = 0
    current_max = 0
    max_char = ""
    A = len(chars) - 1
    i = 0

    while i < A:
        j = i
        current_max = 0 

        while A >= j and chars[j] == chars[i]:
            current_max += 1
            j += 1

        if current_max >= prevous_max:
            prevous_max = current_max
            max_char = chars[i]

        i += 1
    return max_char, prevous_max


def main():
    chars = "aaabbbaaabbbbbbbbaaaaaaaaaaababababababababbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    r = max_frequency(chars=chars)
    print(r)

if __name__ == "__main__":
    main()
