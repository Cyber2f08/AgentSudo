import json
import base64

# Author: Cyber2f08
# Github: https://www.github.com/Cyber2f08

update_logs = {
        0: {
            "date": "Nov 5, 2021",
            "title": "Terminal webapp",
            "author": "Cyber2f08, cyber.2f08@gmail.com",
            "status": "Success",
            "description": "Added color, rich module template with flask framework. Still need css Styling tho."
            },
        1: {
            "date": "Nov 8, 2021",
            "title": "Added active bar loader, typo fixes. exported update log",
            "author": "Cyber2f08, cyber.2f08@gmail.com",
            "status": "Success",
            "description": "Fixed typo on previous update log on author column, and added active bar loader and exporting update logs into json in other file."
            },
        2: {
            "date": "Nov 9-10, 2021",
            "title": "Whatsapp API, Weather, Books and Uniform API for class Group Chat",
            "author": "Cyber2f08, cyber.2f08@gmail.com",
            "status": "Working..",
            "description": "Added whatsapp api webserver using flask and the client application is on android 11, and added more api things. Future updates maybe UI of web styling or URLShortener..."
            },
        3: {
            "date": "Nov 12, 2021",
            "title": "Uploaded On Github, Typo Fixes",
            "author": "Cyber2f08, cyber.2f08@gmail.com",
            "status": "Success",
            "description": "Uploaded on github with project name 'Koop' on 'https://github.com/Cyber2f08/Koop' and added a little bit of .gitignore file. Fixes typo in the previous update log"
            },
        4: {
            "date": "Nov 13, 2021",
            "title": "Whatsapp API now Supported command arguments",
            "author": "Cyber2f08, cyber.2f08@gmail.com",
            "status": "Working...", 
            "description": "Added command arguments to the API"
            }
}

flask_confp = {
    "debug": False,
    "codebug": False,
    "ngrok": False,
    "port": 80
}

emails = {
    "Cyber2f08": "cyber.2f08@gmail.com",
    "sp0f.p12": "sp0f.p12@yahoo.com"
}
passwd = {
    "cyber.2f08@gmail.com": "admin0x0",
    "sp0f.p12@yahoo.com": "inevcure"
}

email_d = ["cyber.2f08@gmail.com", "sp0f.p12@yahoo.com"]

def get_update_logs():
    return update_logs

def flask_conf():
    return flask_confp

def get_emailp():
    return emails

def get_passwdp():
    return passwd

def get_emaild():
    return email_d