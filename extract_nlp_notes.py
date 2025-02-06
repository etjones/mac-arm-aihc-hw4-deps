#! /usr/bin/env python3

import argparse
from dataclasses import dataclass
from textwrap import dedent
from pathlib import Path
import sqlite_utils
from typing import TypeAlias

DB = sqlite_utils.Database("../mimic3.db")

DBRow: TypeAlias = dict[str, str | int]
SQLQuery: TypeAlias = str


def main():
    args = parse_all_args()

    output_path = args.output
    deck_content = collect_slides()
    # TODO: ... other slides ...
    with open(output_path, "w") as f:
        f.write(deck_content)
    print(f"Wrote {output_path}")


def collect_slides() -> str:
    slide_funcs = [
        first_slide,
        slide_extract_laryngomalacia_notes,
    ]

    slides_text = "\n---\n".join([dedent(f()) for f in slide_funcs])
    return slides_text


def slide_extract_laryngomalacia_notes() -> str:
    return """    
    # First: Extract Laryngomalacia notes:

    ```sql
    SELECT * FROM noteevents WHERE LOWER(TEXT) LIKE '%laryngomalacia%';
    ```

    **Results:** 93 rows, 10 seconds on my local SQLite database.
    """


def extract_laryngomalacia_notes() -> tuple[SQLQuery, list[DBRow]]:
    # Find all notes containing 'laryngomalacia'.
    # Laryngomalacia is a condition where the voice box (the part of the throat
    # that produces voice) is enlarged. It's common in newborns and usually
    # resolves with age in the first months of life.
    # We might also be interested in its common name, 'stridor'
    query_str = r"SELECT * FROM noteevents WHERE LOWER(TEXT) LIKE '%laryngomalacia%';"
    res = DB.query(query_str)
    rows = list(res)
    return (query_str, rows)


def first_slide(*args, **kwargs) -> str:
    # Note: initial slide spacing seems very fussy, so be careful.
    # I needed `autoscale` on the first line, and needed no indents in this slide
    return dedent("""autoscale: true
theme: next, 1

## AI In Healthcare, Homework 4: Mimic NLP
### [Evan Jones](mailto:evan_jones@utexas.edu), UT ID:  `ej8387`

    """)


def parse_all_args(args_in=None):
    """Set up argparser and return a namespace with named
    values from the command line arguments.
    If help is requested (-h / --help) the help message will be printed
    and the program will exit.
    """
    program_description = """Extract NLP notes from mimic-iii, process them, and make a slide deck to explain it"""

    parser = argparse.ArgumentParser(
        description=program_description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Replace these with your arguments below
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="path to Markdown output file",
        default="aihc_hw4_deck_ej8387.md",
    )

    # # If no arguments were supplied, print help
    # if len(sys.argv) == 1:
    #     sys.argv.append("-h")

    # If args_in isn't specified, args will be taken from sys.argv
    args_namespace = parser.parse_args(args_in)
    return args_namespace


if __name__ == "__main__":
    main()
