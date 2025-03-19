#!/usr/bin/env -S python3 -OO
"""
TODO:
- ensure password integrity (at least one lower, one upper, one number, one symbol)
- feature: don't use the same character more than once
- feature: don't use sequential characters (e.g. abc, 789)
"""

import argparse, secrets, string
from pyperclip import copy

def getOps() -> argparse.Namespace:
  parser = argparse.ArgumentParser(prog="genpass",
                                   description="CLI random password generator")

  parser.add_argument("-l", "--length",
                      type=int,
                      required=False,
                      default=16,
                      help="length of password (default 16, minimum 8)")
  parser.add_argument("-c", "--copy",
                      action="store_true",
                      required=False,
                      help="copy password to clipboard")
  parser.add_argument("-e", "--exclude",
                      nargs="+",
                      required=False,
                      help="list of characters to exclude from password")

  return parser.parse_args()

def main() -> None:
  args = getOps()
  characters = string.ascii_letters + string.digits + string.punctuation
  length = args.length if args.length >= 8 else 8

  if args.exclude:
    for c in "".join(args.exclude):
      characters = characters.replace(c, "")

  password = "".join(secrets.choice(list(characters)) for _ in range(length))

  if args.copy:
    try:
      copy(password)
      print("Password copied to clipboard")
    except e:
      print("Couldn't copy password:", e)
  else:
    print(password)

if __name__ == "__main__":
  main()
