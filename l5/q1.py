# CSCI 331 - Lab 5
# Author: Jasper Charlinski
# Date: April 29th, 2023

'''
This program parses the anchor  elements of a web page provided as a command line argument, 
and retrieves all anchor elements linking to .docx files. The files are then saved to the docs/ directory.
Each docx file in the docs/ directory is then converted to a .txt file and saved to the txts/ directory. 

for testing use link: https://www.presidencia.gob.ec/discursos/
'''

from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from user_agent import generate_user_agent
import docxpy
import os
import random
import sys

def printSeparator(character='*', times=13):
    print(character * times)

if __name__ == '__main__':
    numDocs = 5
    docDir = 'docs/'
    txtDir = 'txts/'
    url = sys.argv[1]
    headers = {'User-Agent': generate_user_agent()}

    try: # try to connect to given url

        with get(url=url, headers=headers) as request:
        
            if request.status_code != 200: # if connection request failed
                raise RequestException ('Request to', url, 'failed, received code: ', request.status_code)

            else:
                soup = BeautifulSoup(request.content, 'html.parser') # create BeautifulSoup from website content

    except RequestException as e:
        print(e)

    else: # if connection request was successful

        print ('connection successful...')

        docx_links = []

        for link in soup.find_all('a', href=True): # find all links to .docx files in the webpage and append it to docx_links    
            if link['href'].endswith('.docx'):
                docx_links.append(link['href']) 

        if len(docx_links) == 0: # check if url links to any docx files
            printSeparator()
            print (url, 'has no .docx files linked')
            
        else:
            
            rdm_links = []

            for i in range(numDocs): # randomly select a given number of .docx files from docx_links
                rdm_links.append(random.choice(docx_links))

            for link in rdm_links: # write each .docx file that is linked in rdm_links to the docs/ directory
                printSeparator()
                print ('Retrieving: ', link)

                try: # try to connect to link (to .docx file)
    
                    with get(url=link, headers=headers) as docx_file_request: 

                        if request.status_code != 200: # if connection request failed
                            raise RequestException ('Request to', link, 'failed, received code: ', request.status_code)

                        else:
                            docx_file = 'docs/' + os.path.basename(link)

                            try: # try to write .docx file to docs/ directory

                                with open(docx_file, 'wb') as f:
                                    f.write(docx_file_request.content)

                            except OSError:
                                print ('Failed to write to file: ', docx_file)

                except RequestException as e:
                    print(e)

            docs = 'docs' # directory name of where .docx files are stored
            txts = 'txts' # directory name of where .txt files are stored
            
            for docx_file in os.listdir(docs): # convert each docx file in the docs/ directory to a text file

                docx_path = os.path.join(docs, docx_file)
                txt_path = os.path.join(txts, os.path.splitext(docx_file)[0]) + '.txt'

                txt_content = docxpy.process(docx_path)

                try:

                    with open(txt_path, 'w', encoding='utf-8') as f:
                        f.write(txt_content)

                except OSError:
                    print ('Failed to write to file: ', txt_path)


                printSeparator()
                print ('txt file saved: ', txt_path)
            
    finally: # connection requests are closed automatically since they are created using with
        printSeparator()
        print('closing connection...')
