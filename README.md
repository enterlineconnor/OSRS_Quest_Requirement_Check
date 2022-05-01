# Summary:

## OSRS Wiki web scraper to return all required quests, as well as the largest figure of their skills, based on a quest input

![cool image](https://oldschool.runescape.wiki/images/thumb/Sins_of_the_Father.png/1200px-Sins_of_the_Father.png?300c3)


## Use Case:

My friend asked me to make this because of a clarity issue within the OSRS Wiki.
The wiki will inform you of the skill levels needed to complete a quest, but does
not make it clear that there are seperate skill requirements for prior quests.

## Example:

The quest "Sins of the Father" lists these requirements:

```
Woodcutting 62 Woodcutting (not boostable)
Fletching 60 Fletching (not boostable)
Crafting 56 Crafting (not boostable)
Agility 52 Agility (not boostable)
Attack 50 Attack (not boostable)
Slayer 50 Slayer (not boostable)
Magic 49 Magic (not boostable)
```

This would lead you to believe that these would be the required skills
throughout the entire quest tree. However, the quest "A Taste of Hope"
lists that you must have 40 Herblore in order to complete it.

Logically, this means that you need 40 Herblore before you can attempt "Sins of the Father"

# Usage:
## Sample Input:
```
python osrs_wiki_scrap.py "Sins of the Father"
```
## Sample Output:
```
Required Quests
===========================================
Vampyre Slayer
A Taste of Hope
Darkness of Hallowvale
In Aid of the Myreque
In Search of the Myreque
Nature Spirit
Priest in Peril
The Restless Ghost
===========================================
Required Skills (Ceiling of all parent quests)
===========================================
Woodcutting: 62
Fletching: 60
Crafting: 56
Agility: 52
Attack: 50
Slayer: 50
Construction: 5
Magic: 49
Herblore: 40
Strength: 40
Thieving: 22
Mining: 20
```
 
