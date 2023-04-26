import sys
import os
import random
import requests as req
import user_agent as ua

from bs4 import BeautifulSoup
from pytictoc import TicToc
from typing import TextIO


class Class1:
    def __init__(self) -> None:
        self.link  = 'https://www.eaglewingtours.com/marine-mammals-guide/'
        self.mammals = []
        
    def connect(self) -> bool:
        headers = {'User-Agent': ua.generate_user_agent()}
        response = req.get(self.link, headers=headers)
        if response.status_code == 200:
            self.html_content = response.content
            return True
        else:
            return False
    
    def parse(self) -> None:
        soup = BeautifulSoup(self.html_content, 'html.parser')

        mammals = soup.find_all('div', class_='card-cpt-marine-mammals')
        mammal_name = ''
        mammal_subname = ''
        mammal_img = ''

        for mammal in mammals:
            mammal_name = mammal.find('p', class_='card-post-name').text.replace('\n', '').replace(' ', '')
            if mammal_name:
                setattr(self, mammal_name, {})
                self.mammals.append(mammal_name)

                mammal_info = getattr(self, mammal_name)
                mammal_info['name'] = mammal_name
                mammal_info['subname'] = mammal.find('p', class_='card-post-subname').text.replace('\n', '')
                mammal_info['img'] = mammal.find('img').get('src')

    def print(self):
        
        for m in self.mammals:
            print(m)
            for key, value in getattr(self, m).items():
                print(f"{key}: {value}")
            print('\n', '-' * 50, '\n')
    
if __name__ == '__main__':

    t = TicToc()
    t.tic() # start timer
    
    c1 = Class1()
    c1.connect()
    c1.parse()
    c1.print()

    t.toc()