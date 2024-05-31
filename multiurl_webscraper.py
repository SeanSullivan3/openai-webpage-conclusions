import os

import requests
from bs4 import BeautifulSoup
from openai_conclusions import get_ai_conclusions

dir_in = "Input"
dir_out = "Output"
input_files = []
output_files = []
industries = []

for file in os.listdir(dir_in):
    input_files.append(os.path.join(dir_in, file))
    output_files.append(os.path.join(dir_out, file[0:file.find(".txt")] + "Output.txt"))

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64)'}


def write_webpage_info_to(html_soup, f_out):
    for tag in html_soup.find_all():
        if tag.name == "h1" or tag.name == "h2" or tag.name == "h3" or tag.name == "h4" or tag.name == "h5":
            if tag.getText() != "" and tag.getText() != " ":
                f_out.write("\n" + tag.getText() + "\n")
        if tag.name == "a" or tag.name == "p" or tag.name == "span":
            if tag.getText() != "" and tag.getText() != " ":
                f_out.write(" " + tag.getText())


for input_file, output_file in zip(input_files, output_files):

    f_in = open(input_file, "r")
    industries.append(f_in.readline().strip())
    urls = []
    for line in f_in:
        urls.append(str(line).strip())

    f_out = open(output_file, "a")
    for url in urls:
        html_data = requests.get(url, headers=header).content
        soup = BeautifulSoup(html_data, "html.parser")
        f_out.write("\n\n\nThe following information is from the website: " + url + "\n\n")
        write_webpage_info_to(soup, f_out)


get_ai_conclusions(output_files, industries)
