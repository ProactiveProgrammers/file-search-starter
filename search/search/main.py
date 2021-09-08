# TODO: add a module-level docstring to describe the purpose of this program

from rich.console import Console

from pathlib import Path

import typer

# TODO: create a Typer object to support the command-line interface


def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # TODO: determine if the file is not None and if it is a file
    # TODO: return a value to indicate if the file is valid
    return False


def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # TODO: determine if the boolean value is True or False
    # if it is True, then return "Yes"
    # if it is False, then return "No"


def word_search(text: str, word: str) -> bool:
    """Determine whether or not a word is found in the text in case-sensitive fashion."""
    # TODO: perform a case-sensitive search for the word in the provided text


@cli.command()
def word(
    word: str = typer.Option(None),
    dir: Path = typer.Option(None),
    file: Path = typer.Option(None),
):
    """Process a file by searching for a specified word."""
    # create a console for rich text output
    console = Console()
    # add extra space after the command to run the program
    console.print()
    # create the full name of the file
    file_fully_qualified = dir / file
    # TODO: display a message to explain the file that will be input
    # TODO: confirm the file is valid and so the program should search through it for the word
    # --> TODO: read in the contents of the file
    # --> TODO: search for the word in the contents of the file by calling function
    # --> TODO: display a message about whether the word was or was not found
    # TODO: since the file was not valid and thus you cannot install it display a message
