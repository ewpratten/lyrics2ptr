import argparse
import sys
import re

def main() -> int:
    # Handle program arguments
    ap = argparse.ArgumentParser(prog='lyrics2ptr')
    ap.add_argument("text_file", help="Text file containing lyrics")
    ap.add_argument(
        "--addr-prefix", help="Optional prefix for the generated address byte", default="")
    ap.add_argument(
        "--addr-suffix", help="Optional suffix for the generated address byte", default="")
    args = ap.parse_args()

    # Open text file
    with open(args.text_file, 'r') as f:
        text = f.read()

    # Convert text to pointer record hostnames
    for i, line in enumerate(text.splitlines()):

        # Strip bracketed text
        matches = re.findall(r"(.*)\(|(.*)", line)
        if not matches:
            continue
        line_clean = matches[0][0] if matches[0][0] else matches[0][1]

        line_clean = line_clean.lower().replace(' ', '.').replace("'", '').replace(",", '')
        addr = "{:04x}".format(i)
        print(f"{args.addr_prefix}{addr}{args.addr_suffix} {line_clean}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
