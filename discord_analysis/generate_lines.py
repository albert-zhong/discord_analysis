from unidecode import unidecode

def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))

def generate_lines(name, file_location):
    lines = open("/home/albert/workspace/discord_analysis/data/western_frontier.txt", "r+")
    person_lines = open(file_location, "w")

    last_line = ""
    for current_line in lines:
        if not current_line.isspace() and "Changed the channel name." not in current_line and "Added a recipient." not in current_line and "Started a call." not in current_line and "https" not in current_line:
            if name in last_line:
                current_line = remove_non_ascii(current_line)
                person_lines.write(current_line)
        last_line = current_line