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
unc = re.compile(r"</?unc>")  # exclude unc from logs?
scene = re.compile(r"""<scene +id=".*" +heading=".+">""")
screenplay = re.compile(
    r"""<screenplay +title=".*" +authors=".*" +genres=".*">""")
turn = re.compile(r"""<turn +char=".+" +ext=".*" *>""")


cwd = os.getcwd()

if "Tag Logs" not in os.listdir(cwd):
    os.chdir(cwd)
    os.mkdir(os.path.join(cwd, "Tag Logs"))

dir_content = os.listdir(cwd)
xml_files = [file for file in dir_content if file.endswith(".xml")]

for file in xml_files:
    xml_file = open(file, "r")
    log_file = open("{}_tags.txt".format(file[:-4]), "w")
    all_lines = xml_file.readlines()
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
                                                                    # print("l." + str(all_lines.index(line)+1) + "\t" + line)  # print wrong lines to terminal
                                                                    log_file.write(
                                                                        "l." + str(all_lines.index(line)+1) + "\t" + line)
                                                                    log_file.write(
                                                                        "\n")
    xml_file.close()
    log_file.close()
    print("created txt-file '{}_tags.txt' in 'Tag Logs'".format(file[:-4]))
    orig_path = os.path.join(cwd, "{}_tags.txt".format(file[:-4]))
    new_path = os.path.join(cwd, "Tag Logs", "{}_tags.txt".format(file[:-4]))
    os.rename(orig_path, new_path)
    # print("Done")
