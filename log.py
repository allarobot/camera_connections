import pandas as pd
class Log:
    def __init__(self):
        self.file = open("data/log.txt","a+")

    def save(self,data):
        str_data = ",".join(data)+"\n"
        self.file.write(str_data)

    def update(self):
        self.file = open("data/log.txt","a+")

