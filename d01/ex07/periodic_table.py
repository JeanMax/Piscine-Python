#!/usr/bin/env python3

import sys


class Parse:
    data = []

    def __parseLine(line):
        """Parse the given line"""

        # extract name
        name_len = line.index(" ")
        name = line[:name_len]
        line = line[name_len + 3:]

        # array-ize 'electron' val
        elec_pos = line.index("electron") + 9
        line = line[:elec_pos] + '[' + line[elec_pos:].replace(' ', ',') + ']'

        # quote 'small' val
        line = line.replace(' ', '')
        line = line.replace('small:', 'small:"').replace(',molar', '",molar')

        # quote all keys
        for i in ["position", "number", "small", "molar", "electron"]:
            line = line.replace(i, '"' + i + '"')

        return eval('{"name":"' + name + '",' + line + '}')

    def parseFile(filename):
        """Parse the given file"""

        Parse.data = []
        with open(filename, "r") as f:
            for line in f:
                Parse.data += [Parse.__parseLine(line)]
        return Parse.data


class Write:
    def __writeHeader(fd):
        """Write html header"""

        print(
            "<!DOCTYPE html>",
            "<html>",
            " <head>",
            "  <title>Super Tableau 3000</title>",
            "  <meta charset='utf-8' />",
            "  <style>",  # ty alex for css!
            "   table  { border-collapse: collapse; }",
            "   td     { border: solid; }",
            "   h4, li { font-size:10px; }",
            "   .empty { border: 0px; }",
            "  </style>",
            " </head>",
            " <body>",
            "  <table>",
            sep="\n",
            file=fd
        )

    def __writeFooter(fd):
        """Write html footer"""

        print(
            "  </table>",
            " </body>",
            "</html>",
            sep="\n",
            file=fd
        )

    def __openRow(fd):
        """Write opening html table row"""

        print("   <tr>", file=fd)

    def __closeRow(fd):
        """Write closing html table row"""

        print("   </tr>", file=fd)

    def __writeElement(fd, elm):
        """Write html table cell"""

        print(
            "    <td>",
            "     <h4>" + elm["name"] + "</h4>",
            "     <ul>",
            "      <li>" + str(elm["number"]) + "</li>",
            "      <li>" + elm["small"] + "</li>",
            "      <li>" + str(elm["molar"]) + "</li>",
            "     </ul>",
            "    </td>",
            sep="\n",
            file=fd
        )

    def __writeEmptyElement(fd):
        """Write html empty table cell"""

        print("    <td class='empty'></td>", file=fd)

    def writeFile(filename):
        """Write our awesome html file"""

        with open(filename, "w") as f:
            Write._writeHeader(f)

            Write._openRow(f)
            i = 0
            for elm in Parse.data:
                while i != elm["position"]:
                    Write._writeEmptyElement(f)
                    i += 1

                Write._writeElement(f, elm)
                i += 1

                if elm["position"] == 17:
                    i = 0
                    Write._closeRow(f)
                    if elm["number"] != 118:
                        Write._openRow(f)

            Write._writeFooter(f)


def doTheJob(input_file):
    """Do all we need"""

    Parse.parseFile(input_file)
    Write.writeFile(input_file.replace(".txt", ".html"))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        doTheJob(sys.argv[1])
    else:
        doTheJob("./ex07/periodic_table.txt")
