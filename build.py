from jinja2 import Template, Environment, FileSystemLoader
from os import path as opath
import os

def change(env, path):
    for p in os.listdir(path):
        if opath.isdir(p):
            print(p)
            change(Environment(loader=FileSystemLoader(f"{path}/{p}", encoding='utf8')), path + p)
        else:
            # print(p)
            tpl = env.get_template(p)
            with open("./html/" + p.replace(".j2", ".html"), "w") as f:
                f.write(tpl.render())
                
change(Environment(loader=FileSystemLoader("jinja2", encoding='utf8')), "jinja2/")
