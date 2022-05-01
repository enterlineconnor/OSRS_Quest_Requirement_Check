from ast import arg
import sys
from bs4 import BeautifulSoup
from cv2 import split
import requests
import sys

def osrs_soupify(url):
    url = "https://oldschool.runescape.wiki/w/{}".format(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list(soup.children)
    table = soup.find_all('ul')
    return table

def skills_search(req, skill, skill_map = {}):
    if skill in req:
        skill_level = req[req.find(skill_level_start)+len(skill_level_start):req.rfind(skill_level_end)]
        skill_name = req[req.find(skill_name_start)+len(skill_name_start):req.rfind(skill_name_end)]
        if skill_name not in skill_map.keys():
            skill_map[skill_name] = skill_level
        elif int(skill_map[skill_name]) < int(skill_level):
            skill_map[skill_name] = skill_level
    return skill_map

quest_input = sys.argv[1].lower()
x,quest,skill="Completion of the following quests","<li><a href=","data-level="
quest_array, skill_map = [],{}
quest_start,quest_end,skill_level_start,skill_level_end,skill_name_start,skill_name_end = '">','</a',"data-level=\"","\" data-skill","\" data-skill=\"","\"><a"
table = osrs_soupify(quest_input)
for t in table:
    '''
    t = requirements section of wiki
    '''
    if x in str(t):
        individual_req = str(t).split('\n')
        for req in individual_req:
            skills_map = skills_search(req,skill,skill_map)
            if quest in req:
                quest_array.append(req[req.find(quest_start)+len(quest_start):req.rfind(quest_end)])
        break

'''
Iterate through all child quests to determine the skill rating for each of them

if the skill rating already exists within our current map, compare
the value in the existing skill map and with the value onn the current quest.
If the current quests skill cap is larger than the existing one, replace it with that number

if the skill does not exist within our list already, add it and move on
'''
print()
print("Required Quests")
print("===========================================")
for indiv_quest in quest_array:
    print(indiv_quest)
    child = osrs_soupify(indiv_quest)
    for c in child:
        if x in str(c):
            individual_req = str(c).split('\n')
            for req in individual_req:
                skills_map = skills_search(req,skill,skill_map)

print("===========================================")
print("Required Skills (Ceiling of all parent quests)")
print("===========================================")
skill_map = sorted(skill_map.items(), key=lambda x: x[1], reverse=True)
for skill in skill_map:
    print('{}: {}'.format(skill[0],skill[1]))
 
