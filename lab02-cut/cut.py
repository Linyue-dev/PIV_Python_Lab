import math


def cut(infile_name: str, format_spec: str, delimiter: str = "\t"):
    """
    Extract specified fields from the input data structured in columns by a delimiter.

    :param infile_name: The file name to read the data from, if blank then read from standard input.

    :param format_spec: The columns to include in the output. Comma delimited numbers and/or number
                   range corresponding to the columns in the input data. Ex: "1,2,3" would output
                   columns 1, 2 and 3 the output (comma delimited). You can specify ranges "1-3"
                   or open-ended ranges "-5" or "2-". Columns always appear in ascending order in the
                   output, ex: "2,3,1" and "1,2,3" produce the same output.

    :param delimiter: The character delimiting the columns in the input file (tab by default).
    """


def main():
    cut("in1.txt", "2,3,1", ",")


if __name__ == "__main__":
    main()
