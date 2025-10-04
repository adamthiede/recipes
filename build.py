#!/usr/bin/env python3

import glob
import os

headfile = open("templates/head.html", "r")
html_head = headfile.read().strip()
headfile.close()

footfile = open("templates/foot.html", "r")
html_foot = footfile.read().strip()
footfile.close()

gen_dir = "recipes"


def gen_index():
    recipes = ""
    return recipes


def __main__():
    html = html_head + gen_index() + html_foot
    index = open("index.html", "w")
    index.write(html)
    index.close()


if __name__ == '__main__':
    __main__()
