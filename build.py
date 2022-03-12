from jinja2 import Template, Environment, FileSystemLoader
from os import path as opath
import os

def change(path):
    for p in os.listdir(path):
        if opath.isdir(p):
            change(path + p)
        else:
            env = Environment(loader=FileSystemLoader(p, encoding='utf8'))
            tpl = env.get_template(p)
            with open("./html/" + tpl.replace(".j2", ".html"), "w") as f:
                f.write(tpl.render())
                
change("jinja2")
