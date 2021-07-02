"""
Simple site access validator which launches URL's from given .txt file, checking their accessibility,
splitting them to ones that can and cannot be reached and creates two .txt files:
one for sites that can be reached and another for sites that cannot be reached.
"""

import requests

fileName = input("Type name of the file with sites listed for access validation: ")

def site_validator(fileName):
    
    siteList = []

    with open ((fileName + ".txt"), "r", encoding = "UTF-8") as file:
        for line in file:
            siteList.append(line.replace("\n", ""))

    validSites = []

    invalidSites = []

    try:
        for site in siteList:
            response = requests.get(site)
            
            if response.status_code == 200:
                validSites.append(site)

            elif response.status_code == 404:
                invalidSites.append(site)
                       
        
    except requests.exceptions.MissingSchema:
        "Data in a format other than the URL present in the file"


    with open ("valid_sites.txt", "a+", encoding = "UTF-8") as file:
        file.write("List of sites that can be reached:" + "\n")
        for site in validSites:
            file.write(site + "\n")

    with open ("invalid_sites.txt", "a+", encoding = "UTF-8") as file:
        file.write("List of sites that cannot be reached:" + "\n")
        for site in invalidSites:
            file.write(site + "\n")

site_validator(fileName)   

