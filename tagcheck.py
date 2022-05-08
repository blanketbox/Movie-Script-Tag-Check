import os
import re

cont = re.compile(r"</?cont>")
slug = re.compile(r"</?slug>")
dlg = re.compile(r"</?dlg>")
hdg = re.compile(r"</?hdg>")
title = re.compile(r"</?title>")
char = re.compile(r"</?char>")
act = re.compile(r"</?act>")
end_scene = re.compile(r"</scene>")
end_turn = re.compile(r"</turn>")
end_screenplay = re.compile(r"</screenplay>")
par = re.compile(r"</?par>")
pgn = re.compile(r"</?pgn>")
trans = re.compile(r"</?trans>")
unc = re.compile(r"</?unc>")  # exclude unc from logs?
scene = re.compile(r"""<scene +id=".*" +heading=".+">""")
screenplay = re.compile(
    r"""<screenplay +title=".*" +authors=".*" +genres=".*">""")
turn = re.compile(r"""<turn +char=".+" +ext=".*" *>""")
open_sgl_tags = re.compile(r"< *[a-z]+ *>")
close_sgl_tags = re.compile(r"</ *[a-z]+ *>")

cwd = os.getcwd()

# CREATE FOLDER AND LIST XML-FILES

if "Tag Logs" not in os.listdir(cwd):
    os.chdir(cwd)
    os.mkdir(os.path.join(cwd, "Tag Logs"))

dir_content = os.listdir(cwd)
xml_files = [file for file in dir_content if file.endswith(".xml")]

# LOOP THROUGH XML-FILES

x = 0

for file in xml_files:
    xml_file = open(file, "r", encoding="iso-8859-1")
    log_file = open("{}_tags.txt".format(file[:-4]), "w")
    all_lines = xml_file.readlines()
    x += 1 

    # FIND MISSPELLED TAGS

    for line in all_lines:
        if line.__contains__("<") or line.__contains__(">"):
            if not re.findall(cont, line):
                if not re.findall(slug, line):
                    if not re.findall(dlg, line):
                        if not re.findall(hdg, line):
                            if not re.findall(title, line):
                                if not re.findall(char, line):
                                    if not re.findall(act, line):
                                        if not re.findall(end_scene, line):
                                            if not re.findall(end_turn, line):
                                                if not re.findall(end_screenplay, line):
                                                    if not re.findall(par, line):
                                                        if not re.findall(scene, line):
                                                            if not re.findall(screenplay, line):
                                                                if not re.findall(turn, line):
                                                                    if not re.findall(pgn, line): 
                                                                        if not re.findall(trans, line):
                                                                            # print("l." + str(all_lines.index(line)+1) + "\t" + line)  # print wrong lines to terminal
                                                                            log_file.write(
                                                                                "l." + str(all_lines.index(line)+1) + "\t" + line)
                                                                            log_file.write(
                                                                                "\n")
    # DETERMINE FREQUENCIES FOR TAGS

    frequencies = dict()
    for line in all_lines:

        # ADD FREQUENCIES FOR MULTI WORD TAGS

        if re.findall(scene, line):
            found_scn_tags = re.findall(scene, line)
            for tag in found_scn_tags:
                frequencies["<scene...>"] = frequencies.get(
                    "<scene...>", 0) + 1

        if re.findall(screenplay, line):
            found_scr_tags = re.findall(screenplay, line)
            for tag in found_scr_tags:
                frequencies["<screenplay...>"] = frequencies.get(
                    "<screenplay...>", 0) + 1

        if re.findall(turn, line):
            found_trn_tags = re.findall(turn, line)
            for tag in found_trn_tags:
                frequencies["<turn...>"] = frequencies.get("<turn...>", 0) + 1

        # ADD FREQUENCIES FOR SINGLE WORD TAGS

        if re.findall(open_sgl_tags, line):
            found_open_tags = re.findall(open_sgl_tags, line)
            for tag in found_open_tags:
                frequencies[tag] = frequencies.get(tag, 0) + 1

        if re.findall(close_sgl_tags, line):
            found_close_tags = re.findall(close_sgl_tags, line)
            for tag in found_close_tags:
                frequencies[tag] = frequencies.get(tag, 0) + 1

    for tag_name, tag_count in frequencies.items():
        log_file.write("{}: {}\n".format(tag_name, tag_count))

    frequencies = dict()

    xml_file.close()
    log_file.close()
    print("'{}_tags.txt' created in 'Tag Logs'".format(file[:-4]))

    # MOVE NEW FILES TO SEPARATE FOLDER

    orig_path = os.path.join(cwd, "{}_tags.txt".format(file[:-4]))
    new_path = os.path.join(cwd, "Tag Logs", "{}_tags.txt".format(file[:-4]))
    os.rename(orig_path, new_path)
print("{} file(s) created in total\nDone".format(x))

