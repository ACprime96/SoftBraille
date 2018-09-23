import json
from pathlib import Path
# global home_path
# home_path = str(Path.home())
import os
home_path = os.getcwd()

# when project is closed
def reset_config_file():
    rf = open(home_path + "/config.json")
    config = json.load(rf)
    rf.close()
    wf = open(home_path + "/config.json","w")
    config["folder_path"] = str(Path.home())
    config["images"] = str(Path.home())
    config["english"] = str(Path.home())
    config["braille"] = str(Path.home())
    config["br_img"] = str(Path.home())
    json.dump(config,wf)
    wf.close()

# when selected project is opened
def set_project_path(f1):
    rf = open(home_path + "/config.json")
    config = json.load(rf)
    rf.close()
    wf = open(home_path + "/config.json","w")
    config["folder_path"] = f1
    config["images"] = f1 + "/images"
    config["english"] = f1 + "/eng.txt"
    config["braille"] = f1 + "/br.txt"
    config["br_img"] = f1 + "/braille_images"
    json.dump(config,wf)
    wf.close()

# when project is created
def get_file_path(f1):
    rf = open(home_path + "/config.json")
    config = json.load(rf)
    rf.close()
    wf = open(home_path + "/config.json","w")
    config["folder_path"] = f1
    config["images"] = f1 + "/images"
    config["english"] = f1 + "/eng.txt"
    config["braille"] = f1 + "/br.txt"
    config["br_img"] = f1 + "/braille_images"
    json.dump(config,wf)
    wf.close()

def get_images():
    rf = open(home_path + "/config.json")
    config = json.load(rf)
    rf.close()
    return config["images"]

def get_english():
    rf = open(home_path + "/config.json")
    config = json.load(rf)
    rf.close()
    return config["english"]

def get_braille():
    rf = open(home_path + "/config.json")
    config = json.load(rf)
    rf.close()
    return config["braille"]

def get_braille_images():
    rf = open(home_path + "/config.json")
    config = json.load(rf)
    rf.close()
    return config["br_img"]

def get_folder_path():
    rf = open(home_path + "/config.json")
    config = json.load(rf)
    rf.close()
    return config["folder_path"]
