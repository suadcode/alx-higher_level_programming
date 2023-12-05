#!/usr/bin/python3
"""This contains read_file function"""


def read_file(filename=""):
    """""text file(UTF8) is read and printed to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        files = file.read()
        print(files, end="")
