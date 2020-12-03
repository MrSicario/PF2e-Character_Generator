# Pathfinder 2e - Character Generator - v0.02
# Python 3.9
# Base Code
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
	def __init__(self, name, player_name):
		self.name = name
		self.player_name = player_name
		self.level = 1
		self.experience = 0
		self.hero_points = 1
		self.traits = Traits()
		self.abilities = Abilities(self)
		self.perception = Perception(self)
		self.skills = Skills(self)
#---- Traits
class Traits:
	'''This class is meant to help organize  and bookkeep traits.'''
	pass
#---- Abilities
class Abilities:
	'''Class to organize and manage character ability objects.'''
	def __init__(self, character):
		self.str = self.Ability('STR', 'Strength')
		self.dex = self.Ability('DEX', 'Dexterity')
		self.con = self.Ability('CON', 'Constitution')
		self.int = self.Ability('INT', 'Intelligence')
		self.wis = self.Ability('WIS', 'Wisdom')
		self.cha = self.Ability('CHA', 'Charisma')
		self.character = character
		self.character.str = self.str
		self.character.dex = self.dex
		self.character.con = self.con
		self.character.int = self.int
		self.character.wis = self.wis
		self.character.cha = self.cha
	class Ability:
		'''Class to generate ability objects.'''
		def __init__(self, keyword, name):
			self.keyword = keyword
			self.name = name
			self.score = 10
			self.stats = self.Related_Stats()
			self.det_mod()
		def det_mod(self):
			self.mod = (self.score-10)//2
			for x, y in vars(self.stats).items():
				y.update()
		def boost(self):
			if self.score >= 18:
				self.score += 1
			else:
				self.score += 2
			self.det_mod()
		def flaw(self):
			self.score -= 2
			self.det_mod()
		class Related_Stats:
			'''Class to bookkeep skills related to any given ability object.'''
			pass
#---- Perception
class Perception:
	'''Class to generate Perception object'''
	def __init__(self, character, proficiency='untrained'):
		self.name = 'Perception'
		self.proficiency = proficiency
		self.character = character
		self.character.wis.stats.perception = self
		self.update()
	def update(self):
		if self.proficiency == 'untrained':
			self.mod = self.character.wis.mod
		else:
			self.mod = (self.character.wis.mod + self.character.level + prof_dictionary[self.proficiency])
	def train(self, new_training):
		self.proficiency = 	new_training
		self.update()
#---- Skills
class Skills:
	'''Class to organize and manage character skills.'''
	def __init__(self, character):
		self.character = character
		self.acrobatics = self.Skill('Acrobatics',
			self.character.dex,
			self.character)
		self.arcana = self.Skill('Arcana',
			self.character.int,
			self.character)
		self.athletics = self.Skill('Athletics',
			self.character.str,
			self.character)
		self.crafting = self.Skill('Crafting',
			self.character.int,
			self.character)
		self.deception = self.Skill('Deception',
			self.character.cha,
			self.character)
		self.diplomacy = self.Skill('Deception',
			self.character.cha,
			self.character)
		self.intimidation = self.Skill('Intimidation',
			self.character.cha,
			self.character)
		self.lore1 = self.Skill('__ Lore',
			self.character.int,
			self.character)
		self.lore2 = self.Skill('__ Lore',
			self.character.int,
			self.character)
		self.medicine = self.Skill('Medicine',
			self.character.wis,
			self.character)
		self.nature = self.Skill('Nature',
			self.character.wis,
			self.character)
		self.occultism = self.Skill('Occultism',
			self.character.int,
			self.character)
		self.performance = self.Skill('Performance',
			self.character.cha,
			self.character)
		self.religion = self.Skill('Religion',
			self.character.wis,
			self.character)
		self.society = self.Skill('Society',
			self.character.int,
			self.character)
		self.stealth = self.Skill('Stealth',
			self.character.dex,
			self.character)
		self.survival = self.Skill('Survival',
			self.character.wis,
			self.character)
		self.thievery = self.Skill('Thievery',
			self.character.dex,
			self.character)
		self.character.acrobatics = self.acrobatics
		self.character.arcana = self.arcana
		self.character.athletics = self.athletics
		self.character.crafting = self.crafting
		self.character.deception = self.deception
		self.character.diplomacy = self.diplomacy
		self.character.intimidation = self.intimidation
		self.character.lore1 = self.lore1
		self.character.lore2 = self.lore2
		self.character.medicine = self.medicine
		self.character.nature = self.nature
		self.character.occultism = self.occultism
		self.character.performance = self.performance
		self.character.religion = self.religion
		self.character.society = self.society
		self.character.stealth = self.stealth
		self.character.survival = self.survival
		self.character.thievery = self.thievery
	class Skill:
		'''Class to generate character skill objects.'''
		def __init__(self, name, key_ability, character):
			self.name = name
			self.proficiency = 'untrained'
			self.character = character
			self.key_ability = key_ability
			self.key_ability.stats = self
			self.update()
		def update(self):
			if self.proficiency == 'untrained':
				self.mod = self.key_ability.mod
			else:
				self.mod = (self.key_ability.mod + self.character.level + prof_dictionary[self.proficiency])
		def train(self, new_training):
			self.proficiency = 	new_training
			self.update()
#---- Ancestry