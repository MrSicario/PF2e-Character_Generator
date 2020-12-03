# Pathfinder 2e - Character Generator - Python 3.9
#-- Imports
import math
#-- Variables & Values
#---- Dictionary of Proficiency
prof_dictionary = {
    'untrained':0,
    'trained':2,
    'expert':4,
    'master':6,
    'legendary':8}
#-- Core Classes
# This section defines essential classes.
#---- Character Sheet
class Character_Sheet:
    #-- __init__
        def __init__(self, name, player_name):
            #-- Basic Information
                self.name = name
                self.player_name = player_name
                self.traits = []
                self.level = 1
                self.experience = 0
            #-- Abilities
                self.abilities = self.Abilities(self)
                self.str = self.abilities.str
                self.dex = self.abilities.dex
                self.con = self.abilities.con
                self.int = self.abilities.int
                self.wis = self.abilities.wis
                self.cha = self.abilities.cha
            #-- Skills
                self.skills = self.Skills(self)
                self.perception = self.skills.perception
                self.acrobatics = self.skills.acrobatics
                self.arcana = self.skills.arcana
                self.athletics = self.skills.athletics
                self.crafting = self.skills.crafting
                self.deception = self.skills.deception
                self.diplomacy = self.skills.diplomacy
                self.intimidation = self.skills.intimidation
                self.lore1 = self.skills.lore1
                self.lore2 = self.skills.lore2
                self.medicine = self.skills.medicine 
                self.nature = self.skills.nature
                self.occultism = self.skills.occultism
                self.performance = self.skills.performance
                self.religion = self.skills.religion
                self.society = self.skills.society
                self.stealth = self.skills.stealth
                self.survival = self.skills.survival
                self.thievery = self.skills.thievery
                self.abilities.link_skills()
            #-- Ancestry
                self.ancestry = None
                self.heritage = None
                self.languages = []
                self.background = None
                self.character_class = None
                self.general_feats = []
                self.proficiencies = []
                self.equipment = []
                self.armor_class = 0
                self.movement = {}
                self.senses = []
                self.hp = 0
    #-- Methods
        def level_up(self, n=1):
            self.level += n
            for x in self.skills:
                x.level = self.level
                x.update()
        def add_exp(self, exp):
            self.experience += exp
            if self.experience >= 1000:
                self.experience -= 1000
                self.level_up()
        def set_ancestry(self, ancestry):
            self.ancestry = self.Ancestry.Dwarf(self, ancestry)
    #-- Inner Classes
        #---- Abilities
        class Abilities:
            def __init__(self, character):
                self.character = character
                self.str = self.Ability_Score('Strength')
                self.dex = self.Ability_Score('Dexterity')
                self.con = self.Ability_Score('Constitution')
                self.int = self.Ability_Score('Intelligence')
                self.wis = self.Ability_Score('Wisdom')
                self.cha = self.Ability_Score('Charisma')
            def __repr__(self):
                string = ''
                for x, y in vars(self).items():
                    if y != self.character:
                        string += str(y) + '\n'
                return string
            #-- Methods
            def link_skills(self):
                self.str.skills.athletics = self.character.athletics
                self.str.athletics = self.character.athletics
                self.dex.skills.acrobatics = self.character.acrobatics
                self.dex.skills.stealth = self.character.stealth
                self.dex.skills.thievery = self.character.thievery
                self.dex.acrobatics = self.character.acrobatics
                self.dex.stealth = self.character.stealth
                self.dex.thievery = self.character.thievery
                self.int.skills.arcana = self.character.arcana
                self.int.skills.crafting = self.character.crafting
                self.int.skills.lore1 = self.character.lore1
                self.int.skills.lore2 = self.character.lore2
                self.int.skills.occultism = self.character.occultism
                self.int.skills.society = self.character.society
                self.int.arcana = self.character.arcana
                self.int.crafting = self.character.crafting
                self.int.lore1 = self.character.lore1
                self.int.lore2 = self.character.lore2
                self.int.occultism = self.character.occultism
                self.int.society = self.character.society
                self.wis.skills.perception = self.character.perception
                self.wis.skills.medicine = self.character.medicine
                self.wis.skills.nature = self.character.nature
                self.wis.skills.religion = self.character.religion
                self.wis.skills.survival = self.character.survival
                self.wis.perception = self.character.perception
                self.wis.medicine = self.character.medicine
                self.wis.nature = self.character.nature
                self.wis.religion = self.character.religion
                self.wis.survival = self.character.survival
                self.cha.skills.deception = self.character.deception
                self.cha.skills.diplomacy = self.character.diplomacy
                self.cha.skills.intimidation = self.character.intimidation
                self.cha.skills.performance = self.character.performance
                self.cha.deception = self.character.deception
                self.cha.diplomacy = self.character.diplomacy
                self.cha.intimidation = self.character.intimidation
                self.cha.performance = self.character.performance
            #-- Inner Classes
            #---- Ability Score
            class Ability_Score:
                def __init__(self, name):
                    self.name = name
                    self.score = 10
                    self.mod = (self.score-10)//2
                    self.skills = self.Related_Skills()
                def __repr__(self):
                    string = self.name
                    while len(string) < 13:
                        string += ' '
                    if self.mod >= 0:
                        return string + '|' + str(self.score) + '|+' + str(self.mod)
                    else:
                        return string + '| ' + str(self.score) + '|' + str(self.mod)                
                #-- Methods
                def boost(self):
                    if self.score >= 18:
                        self.score += 1
                    else:
                        self.score += 2
                    self.mod = (self.score-10)//2
                    for x, y in vars(self.skills).items():
                        y.update()
                def flaw(self):
                    self.score -= 2
                    self.mod = (self.score-10)//2
                    for x, y in vars(self.skills).items():
                        y.update()
                #-- Inner Classes
                #---- Related Skills
                class Related_Skills:
                    pass
                    def __repr__(self):
                        string = ''
                        for x, y in vars(self).items():
                            string += str(y) + '\n'
                        return string
        #---- Skills
        class Skills:
            def __init__(self, character):
                self.character = character
                self.perception = self.Skill('Perception', self.character.wis, self.character.level)
                self.acrobatics = self.Skill('Acrobatics', self.character.dex, self.character.level)
                self.arcana = self.Skill('Arcana', self.character.int, self.character.level)
                self.athletics = self.Skill('Athletics', self.character.str, self.character.level)
                self.crafting = self.Skill('Crafting', self.character.int, self.character.level)
                self.deception = self.Skill('Deception', self.character.cha, self.character.level)
                self.diplomacy = self.Skill('Diplomacy', self.character.cha, self.character.level)
                self.intimidation = self.Skill('Intimidation', self.character.cha, self.character.level)
                self.lore1 = self.Skill('__ Lore', self.character.int, self.character.level)
                self.lore2 = self.Skill('__ Lore', self.character.int, self.character.level)
                self.medicine = self.Skill('Medicine', self.character.wis, self.character.level)
                self.nature = self.Skill('Nature', self.character.wis, self.character.level)
                self.occultism = self.Skill('Occultism', self.character.int, self.character.level)
                self.performance = self.Skill('Performance', self.character.cha, self.character.level)
                self.religion = self.Skill('Religion', self.character.wis, self.character.level)
                self.society = self.Skill('Society', self.character.int, self.character.level)
                self.stealth = self.Skill('Stealth', self.character.dex, self.character.level)
                self.survival = self.Skill('Survival', self.character.wis, self.character.level)
                self.thievery = self.Skill('Thievery', self.character.dex, self.character.level)
            def __repr__(self):
                string = ''
                for x, y in vars(self).items():
                    if y != self.character:
                        string += str(y) + '\n'
                return string
            #-- Inner Classes
            #---- Skill
            class Skill:
                def __init__(self, name, key, level,proficiency='untrained'):
                    self.name = name
                    self.key = key
                    self.proficiency = proficiency
                    self.level = level
                    if self.proficiency != 'untrained':
                        self.prof_bonus = prof_dictionary[self.proficiency] + self.level
                    else:
                        self.prof_bonus = 0
                    self.mod = self.key.mod + self.prof_bonus
                def __repr__(self):
                    string = self.name
                    while len(string) < 13:
                        string += ' '
                    if self.mod > 0:
                        return string + '|+' + str(self.mod)
                    else:
                        return string + '|' + str(self.mod)
                #-- Methods
                def update(self):
                    if self.proficiency != 'untrained':
                        self.prof_bonus = prof_dictionary[self.proficiency] + self.level
                    else:
                        self.prof_bonus = 0
                    self.mod = self.key.mod + self.prof_bonus
                def training(self, proficiency):
                    self.proficiency = proficiency
                    self.update()
        #---- Ancestry
        class Ancestry:
            class Dwarf:
                def __init__(self, character, free_boost):
                    self.speed = 25
                    self.hp = 10
                    self.free_boost = free_boost
                    self.character = character
                    self.character.traits.extend(['DWARF', 'HUMANOID'])
                    self.character.hp += self.hp
                    self.character.movement['STRIDING'] = self.speed
                    self.character.con.boost()
                    self.character.wis.boost()
                    self.character.cha.flaw()
                    for x, y in vars(self.character.abilities).items():
                        if x == free_boost and x != 'con' and x != 'wis':
                            y.boost()
                    self.character.languages.extend(['Dwarven', 'Common'])
                    self.character.senses.append('Darkvision')
                    self.character.equipment.append('Clan Dagger')
                def __repr__(self):
                    return 'Dwarf'