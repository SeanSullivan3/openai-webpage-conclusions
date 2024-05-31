import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
output_file = "Conclusions.txt"


def get_ai_conclusions(input_files, industries):

    for input_file, industry in zip(input_files, industries):

        f_in = open(input_file, "r")
        file_content = ''
        for line in f_in:
            file_content += line.strip()

        response = client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "You are a researcher providing me with important information on what to include"
                                          " in my " + industry + " company's website based upon the information these industry "
                                          "leaders included in their websites"},
            {"role": "user", "content": f"{file_content}"},
            ])

        answer: str = ""
        for choice in response.choices:
            answer += choice.message.content

        f_out = open(output_file,"a")
        f_out.write("Openai's insight for building a website for the " + industry + " industry:\n\n")
        f_out.write(answer)
        f_out.write("\n\n")