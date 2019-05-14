#!/usr/bin/env python3

""" Script to be run after converting table from libre
office calc to Tex using https://www.tablesgenerator.com/"""

import pathlib


def postprocess(path):
    write_out = []
    with path.open() as table_file:
        for i, line in enumerate(table_file):
            line = line.strip() + "\n"
            if "\\begin{tab" in line:
                continue
            if "\\end{tab" in line:
                continue
            write_out.append(line)
            write_out.append("\\hline\n")
    # Remove last \hline
    write_out.pop(-1)
    with path.open("w") as table_file:
        table_file.writelines(write_out)
                

if __name__ == "__main__":
    this_dir = pathlib.Path(__file__).parent
    input_dir = this_dir / ".." / "input"
    table_input = input_dir / "table.tex"
    postprocess(table_input)
