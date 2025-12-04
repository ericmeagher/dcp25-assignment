def parse_abc_file(filepath):
    tunes = []          # all tunes from this file
    current_tune = {}   # current tune dictionary
    music_lines = []    # music lines for current tune

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # loop over each raw line from the file
    for raw_line in lines:
        line = raw_line.strip()   # trim spaces and \n

        # X: means a new tune starts
        if line.startswith("X:"):
            # finish previous tune if there was one
            if current_tune:
                current_tune["body"] = "\n".join(music_lines)
                tunes.append(current_tune)
                current_tune = {}
                music_lines = []

            # start new tune, save index after "X:"
            x = int(line[2:])        # retrieve the index number
            current_tune = {"x": x}  # new tune dict with x field

        # T: title
        elif line.startswith("T:"):
            current_tune["title"] = line[2:].strip()

        # M: meter
        elif line.startswith("M:"):
            current_tune["meter"] = line[2:].strip()

        # K: key
        elif line.startswith("K:"):
            current_tune["key"] = line[2:].strip()

        # R: rhythm/type
        elif line.startswith("R:"):
            current_tune["rtype"] = line[2:].strip()

        else:
            # anything else is part of the body; use the original raw_line
            if line or music_lines:
                music_lines.append(raw_line.rstrip("\n"))

    # save last tune at end of file
    if current_tune:
        current_tune["body"] = "\n".join(music_lines)
        tunes.append(current_tune)

    return tunes
  #code from Lab5
