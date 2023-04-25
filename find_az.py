import sys
import os
import random
import requests as req
import user_agent as ua

from bs4 import BeautifulSoup
from pytictoc import TicToc
from typing import TextIO


class find_az:
    def __init__(self) -> None:
        self.link  = 'https://golden.com/wiki/Hans_Zimmer-Y4M9B'
        self.mammals = []
        self.alphabet = {
            'A': [],
            'B': [],
            'C': [],
            'D': [],
            'E': [],
            'F': [],
            'G': [],
            'H': [],
            'I': [],
            'J': [],
            'K': [],
            'L': [],
            'M': [],
            'N': [],
            'O': [],
            'P': [],
            'Q': [],
            'R': [],
            'S': [],
            'T': [],
            'U': [],
            'V': [],
            'W': [],
            'X': [],
            'Y': [],
            'Z': []
        }


        
    def connect(self) -> bool:
        headers = {'User-Agent': ua.generate_user_agent()}

        response = req.get(self.link, headers=headers)
        if response.status_code == 200:
            self.html_content = response.content
            return True
        else:
            return False
    
    def get_words(self) -> None:
        soup = BeautifulSoup(self.html_content, 'html.parser')

        paragraphs = soup.find_all('p')

        for paragraph in paragraphs:      
            
            text = paragraph.text.split()
            for word in text:
                if word[0].upper() in list(self.alphabet.keys()):
                    self.alphabet[word[0].upper()] += [word]

    def print(self):
        for key, value in self.alphabet.items():
            if len(value) > 0:
                print(f"{key}: {random.choice(value)}")
                print('\n', '-' * 50, '\n')
    
if __name__ == '__main__':

    t = TicToc()
    t.tic() # start timer
    
    f_az = find_az()
    if f_az.connect():    
        f_az.get_words()
        f_az.print()
    else:
        print("connection failed")


    t.toc()