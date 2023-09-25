import os
import subprocess
code_dir = os.path.abspath(__file__)
script_directory = os.path.dirname(code_dir)
os.chdir(script_directory)
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-code", help="", action = 'store_true')
parser.add_argument("-code_folder",'-f', help="", action = 'store_true')
parser.add_argument("-o", help="", action = 'store_true')
# parser.add_argument("resume_type")

args = parser.parse_args()

if args.code:
    os.startfile(code_dir)
    exit()

if args.code_folder:
    os.startfile(script_directory)
    exit()

type_dict = {
    'intern' : ['header','profile','education25','skill','work','research','honors'],
    'full' : ['header','profile','education24','skill','work','research','honors'],
    'ds' : ['header','education25','skill','work','research','honors']
}

if args.o:
    os.startfile(script_directory + '/output')
os.chdir(script_directory + '/output')
for resume_type in type_dict:

    content_list = [ "\input{../section/" + x + ".tex}"  for x in type_dict[resume_type]]

    with open(script_directory + '/template.tex', 'r') as f:
        content = f.read()

    content = content.replace('%%%Content%%%', "\n".join(content_list))

    output_file = script_directory + f'/output/Dongyang_He_Resume_{resume_type}.tex'
    with open(output_file, 'w') as f:
        f.write(content)

    subprocess.run(["pdflatex", output_file], check=True)
        
files = os.listdir(script_directory + '/output')
for filename in files:
    file_path = os.path.join(script_directory + '/output', filename)
    
    if os.path.isfile(file_path):
        if not filename.lower().endswith('.pdf'):
            os.remove(file_path)
            print(f"Deleted: {filename}")
