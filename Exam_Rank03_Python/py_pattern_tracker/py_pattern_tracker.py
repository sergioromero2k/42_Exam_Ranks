def pattern_tracker(text: str) -> int:
    counter = 0

    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i + 1].isdigit():
            if int(text[i + 1]) == int(text[i]) + 1:
                counter += 1

    return counter
