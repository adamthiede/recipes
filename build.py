#!/usr/bin/env python3

import glob
import os
import subprocess

MARKDOWN = "/usr/bin/markdown"

# index.html header and footer
headfile = open("templates/head.html", "r")
html_head = headfile.read().strip()
headfile.close()
footfile = open("templates/foot.html", "r")
html_foot = footfile.read().strip()
footfile.close()
# individual recipe header and footer
rhead = open("templates/recipe_head.html", "r")
rhead_html = rhead.read().strip()
rhead.close()
rfoot = open("templates/recipe_foot.html", "r")
rfoot_html = rfoot.read().strip()
rfoot.close()

src_dir = "src"
gen_dir = "recipes"

if not os.path.exists(gen_dir):
    os.makedirs(gen_dir)


def convert_files():
    index_list = []
    for file in glob.glob(f"{src_dir}/*.md"):
        md_name = os.path.basename(file)
        md_title = ""
        with open(file) as f:
            first_line = f.readline().strip('\n')
            md_title = first_line.lstrip("# ")
        html_name = md_name[:-2] + "html"
        print(f"Writing {html_name} from {md_name}")
        html_output = subprocess.check_output([MARKDOWN, file])
        index_list.append(
            f"<li><a href='{gen_dir}/{html_name}'>{md_title}</a></li>")
        with open(f"{gen_dir}/{html_name}", "w") as f:
            str_data = html_output.decode("utf-8")
            f.write(rhead_html + f"<title>{md_title}</title>" + str_data +
                    rfoot_html)
    return index_list


def __main__():
    index_list = convert_files()
    index_list.sort()
    index_list_txt = "\n".join(index_list)
    html = html_head + "\n" + index_list_txt + "\n" + html_foot
    index = open("index.html", "w")
    index.write(html)
    index.close()


if __name__ == '__main__':
    __main__()
