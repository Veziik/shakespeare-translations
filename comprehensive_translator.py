#!/usr/bin/env python3
"""
Comprehensive French Translation System for Shakespeare
Using advanced poetic translation techniques
"""

import re
import json
from typing import Dict, List, Tuple

class ComprehensiveFrenchTranslator:
    def __init__(self):
        # Comprehensive Shakespeare-French dictionary
        self.shakespeare_dict = {
            # Pronouns and basic words
            'thou': 'tu', 'thee': 'toi', 'thy': 'ton', 'thine': 'tien',
            'ye': 'vous', 'hath': 'a', 'doth': 'fait', 'art': 'es',
            'wilt': 'voudras', 'shalt': 'devras', 'canst': 'peux',
            'wouldst': 'voudrais', 'shouldst': 'devrais', 'couldst': 'pourrais',
            'hast': 'as', 'dost': 'fais', 'didst': 'fis',
            'ere': 'avant', "'tis": "c'est", 'twas': "c'était",
            'wherefore': 'pourquoi', 'whence': "d'où", 'whither': 'où',
            'hence': "d'ici", 'thence': 'de là', 'hither': 'ici',
            'thither': 'là', 'prithee': 'je te prie', 'marry': 'ma foi',
            'forsooth': 'en vérité', 'verily': 'vraiment',
            'methinks': 'il me semble', 'mayhap': 'peut-être',
            'perchance': 'par hasard', 'belike': 'sans doute',
            'anon': 'bientôt', 'betimes': 'de bonne heure',
            'erewhile': 'naguère', 'oft': 'souvent', 'oft-times': 'souvent',
            'nay': 'non', 'yea': 'oui', 'ay': 'oui', 'aye': 'oui',
            
            # Verbs
            'love': 'aimer', 'loved': 'aimé', 'loves': 'aime',
            'loving': 'aimant', 'hate': 'haïr', 'hated': 'haï',
            'die': 'mourir', 'died': 'mort', 'dying': 'mourant',
            'live': 'vivre', 'lived': 'vécu', 'living': 'vivant',
            'come': 'venir', 'came': 'vint', 'coming': 'venant',
            'go': 'aller', 'went': 'alla', 'going': 'allant',
            'see': 'voir', 'saw': 'vit', 'seen': 'vu',
            'know': 'savoir', 'knew': 'sut', 'known': 'su',
            'think': 'penser', 'thought': 'pensé', 'thinking': 'pensant',
            'speak': 'parler', 'spoke': 'parla', 'spoken': 'parlé',
            'make': 'faire', 'made': 'fit', 'making': 'faisant',
            'take': 'prendre', 'took': 'prit', 'taken': 'pris',
            'give': 'donner', 'gave': 'donna', 'given': 'donné',
            'find': 'trouver', 'found': 'trouvé', 'finding': 'trouvant',
            'leave': 'laisser', 'left': 'laissé', 'leaving': 'laissant',
            'bring': 'apporter', 'brought': 'apporté', 'bringing': 'apportant',
            'bear': 'porter', 'bore': 'porta', 'born': 'né',
            'break': 'briser', 'broke': 'brisa', 'broken': 'brisé',
            'weep': 'pleurer', 'wept': 'pleura', 'weeping': 'pleurant',
            'sleep': 'dormir', 'slept': 'dormit', 'sleeping': 'dormant',
            'dream': 'rêver', 'dreamt': 'rêva', 'dreaming': 'rêvant',
            'wake': 'éveiller', 'woke': 'éveilla', 'waking': 'éveillant',
            
            # Nouns
            'love': 'amour', 'heart': 'cœur', 'soul': 'âme',
            'mind': 'esprit', 'eye': 'œil', 'eyes': 'yeux',
            'hand': 'main', 'hands': 'mains', 'face': 'visage',
            'beauty': 'beauté', 'youth': 'jeunesse', 'age': 'âge',
            'time': 'temps', 'death': 'mort', 'life': 'vie',
            'world': 'monde', 'earth': 'terre', 'heaven': 'ciel',
            'hell': 'enfer', 'god': 'dieu', 'lord': 'seigneur',
            'lady': 'dame', 'king': 'roi', 'queen': 'reine',
            'prince': 'prince', 'princess': 'princesse', 'duke': 'duc',
            'duchess': 'duchesse', 'count': 'comte', 'countess': 'comtesse',
            'knight': 'chevalier', 'squire': 'écuyer', 'page': 'page',
            'man': 'homme', 'woman': 'femme', 'child': 'enfant',
            'father': 'père', 'mother': 'mère', 'son': 'fils',
            'daughter': 'fille', 'brother': 'frère', 'sister': 'sœur',
            'friend': 'ami', 'enemy': 'ennemi', 'lover': 'amant',
            'husband': 'époux', 'wife': 'épouse', 'widow': 'veuve',
            'rose': 'rose', 'flower': 'fleur', 'garden': 'jardin',
            'tree': 'arbre', 'forest': 'forêt', 'sea': 'mer',
            'river': 'rivière', 'mountain': 'montagne', 'star': 'étoile',
            'stars': 'étoiles', 'sun': 'soleil', 'moon': 'lune',
            'night': 'nuit', 'day': 'jour', 'morning': 'matin',
            'evening': 'soir', 'dawn': 'aube', 'dusk': 'crépuscule',
            'spring': 'printemps', 'summer': 'été', 'autumn': 'automne',
            'winter': 'hiver', 'year': 'année', 'month': 'mois',
            'week': 'semaine', 'hour': 'heure', 'minute': 'minute',
            
            # Adjectives
            'fair': 'beau', 'beautiful': 'beau', 'sweet': 'doux',
            'gentle': 'gentil', 'kind': 'bon', 'cruel': 'cruel',
            'true': 'vrai', 'false': 'faux', 'good': 'bon',
            'evil': 'mauvais', 'bad': 'mauvais', 'poor': 'pauvre',
            'rich': 'riche', 'young': 'jeune', 'old': 'vieux',
            'new': 'nouveau', 'high': 'haut', 'low': 'bas',
            'great': 'grand', 'small': 'petit', 'long': 'long',
            'short': 'court', 'wide': 'large', 'narrow': 'étroit',
            'deep': 'profond', 'shallow': 'peu profond', 'bright': 'brillant',
            'dark': 'sombre', 'light': 'léger', 'heavy': 'lourd',
            'quick': 'rapide', 'slow': 'lent', 'hot': 'chaud',
            'cold': 'froid', 'warm': 'tiède', 'soft': 'mou',
            'hard': 'dur', 'smooth': 'lisse', 'rough': 'rugueux',
            'noble': 'noble', 'base': 'vil', 'proud': 'fier',
            'humble': 'humble', 'bold': 'hardi', 'fearful': 'craintif',
            'brave': 'brave', 'coward': 'lâche', 'wise': 'sage',
            'foolish': 'fou', 'happy': 'heureux', 'sad': 'triste',
            'joyful': 'joyeux', 'sorrowful': 'affligé', 'angry': 'fâché',
            'calm': 'calme', 'peaceful': 'paisible', 'violent': 'violent'
        }
        
        # Famous phrases translations
        self.famous_phrases = {
            "to be or not to be": "être ou ne pas être",
            "that is the question": "telle est la question",
            "all the world's a stage": "le monde entier est un théâtre",
            "wherefore art thou": "pourquoi es-tu",
            "romeo, romeo": "roméo, roméo",
            "parting is such sweet sorrow": "se séparer est un si doux chagrin",
            "what's in a name": "qu'y a-t-il dans un nom",
            "a rose by any other name": "une rose sous un autre nom",
            "would smell as sweet": "sentirait aussi bon",
            "the course of true love": "le cours du véritable amour",
            "never did run smooth": "n'a jamais été sans encombre",
            "to thine own self be true": "sois fidèle à toi-même",
            "though this be madness": "bien que ce soit folie",
            "yet there is method in't": "il y a pourtant méthode",
            "something is rotten": "quelque chose est pourri",
            "in the state of denmark": "au royaume de danemark",
            "frailty, thy name is woman": "fragilité, ton nom est femme",
            "brevity is the soul of wit": "la brièveté est l'âme de l'esprit",
            "the lady doth protest too much": "la dame proteste trop",
            "all that glisters is not gold": "tout ce qui brille n'est pas or",
            "the quality of mercy": "la qualité de la clémence",
            "is not strained": "n'est pas forcée",
            "it droppeth as the gentle rain": "elle tombe comme la douce pluie",
            "from heaven": "du ciel",
            "double, double toil and trouble": "double, double labeur et peine",
            "fire burn and cauldron bubble": "feu brûle et chaudron bouillonne",
            "fair is foul, and foul is fair": "le beau est laid, et le laid est beau",
            "out, damned spot": "sors, maudite tache",
            "a plague on both your houses": "peste sur vos deux maisons",
            "star-crossed lovers": "amants maudits par les étoiles",
            "what light through yonder window breaks": "quelle lumière perce à cette fenêtre",
            "it is the east": "c'est l'orient",
            "and juliet is the sun": "et juliette est le soleil",
            "once more unto the breach": "encore une fois dans la brèche",
            "dear friends": "chers amis",
            "we few, we happy few": "nous quelques-uns, nous heureux quelques-uns",
            "we band of brothers": "nous bande de frères",
            "now is the winter of our discontent": "voici l'hiver de notre mécontentement",
            "made glorious summer": "fait glorieux été",
            "a horse, a horse": "un cheval, un cheval",
            "my kingdom for a horse": "mon royaume pour un cheval",
            "is this a dagger which i see before me": "est-ce un poignard que je vois devant moi",
            "the handle toward my hand": "la poignée vers ma main",
            "life's but a walking shadow": "la vie n'est qu'une ombre qui marche",
            "a poor player": "un pauvre acteur",
            "that struts and frets": "qui se pavane et s'agite",
            "his hour upon the stage": "son heure sur la scène",
            "full of sound and fury": "plein de bruit et de fureur",
            "signifying nothing": "ne signifiant rien",
            "lord, what fools these mortals be": "seigneur, quels fous sont ces mortels",
            "love looks not with the eyes": "l'amour ne regarde pas avec les yeux",
            "but with the mind": "mais avec l'esprit",
            "shall i compare thee": "te comparerai-je",
            "to a summer's day": "à un jour d'été",
            "thou art more lovely": "tu es plus beau",
            "and more temperate": "et plus tempéré"
        }
        
    def translate_text(self, text: str) -> str:
        """Main translation function"""
        # First, translate famous phrases
        text_lower = text.lower()
        for eng_phrase, fr_phrase in self.famous_phrases.items():
            if eng_phrase in text_lower:
                # Case-insensitive replacement
                pattern = re.compile(re.escape(eng_phrase), re.IGNORECASE)
                text = pattern.sub(fr_phrase, text)
        
        # Then translate individual words
        words = text.split()
        translated_words = []
        
        for word in words:
            # Preserve punctuation
            prefix = ""
            suffix = ""
            clean_word = word
            
            # Extract punctuation
            while clean_word and not clean_word[0].isalnum():
                prefix += clean_word[0]
                clean_word = clean_word[1:]
            
            while clean_word and not clean_word[-1].isalnum():
                suffix = clean_word[-1] + suffix
                clean_word = clean_word[:-1]
            
            # Translate the word
            translated = self.translate_word(clean_word)
            translated_words.append(prefix + translated + suffix)
        
        return ' '.join(translated_words)
    
    def translate_word(self, word: str) -> str:
        """Translate a single word"""
        # Check exact match first
        if word.lower() in self.shakespeare_dict:
            translation = self.shakespeare_dict[word.lower()]
            # Preserve capitalization
            if word[0].isupper():
                translation = translation[0].upper() + translation[1:]
            if word.isupper():
                translation = translation.upper()
            return translation
        
        # Return original if no translation found
        return word
    
    def translate_to_alexandrine(self, line: str) -> str:
        """Convert a line to French alexandrine format"""
        translated = self.translate_text(line)
        
        # Count syllables (simplified)
        syllables = self.count_french_syllables(translated)
        
        # If close to 12 syllables, return as is
        if 10 <= syllables <= 14:
            return translated
        
        # Otherwise, try to adjust (this is very simplified)
        if syllables < 10:
            # Add poetic flourishes
            translated = self.expand_line(translated)
        elif syllables > 14:
            # Condense
            translated = self.condense_line(translated)
        
        return translated
    
    def count_french_syllables(self, text: str) -> int:
        """Approximate French syllable count"""
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        
        # Count vowel groups
        vowels = 'aeiouyàâäéèêëïîôùûüÿæœ'
        syllables = 0
        prev_vowel = False
        
        for char in text.lower():
            if char in vowels:
                if not prev_vowel:
                    syllables += 1
                prev_vowel = True
            else:
                prev_vowel = False
        
        # Adjust for silent 'e' at end of words
        words = text.split()
        for word in words:
            if word.endswith('e') and len(word) > 2:
                syllables -= 1
        
        return max(1, syllables)
    
    def expand_line(self, line: str) -> str:
        """Expand a line to reach alexandrine length"""
        # Add poetic particles
        expansions = {
            ' le ': ' le beau ',
            ' la ': ' la douce ',
            ' un ': ' un grand ',
            ' une ': ' une belle ',
            ' est ': ' est donc ',
            ' sont ': ' sont bien ',
            ' et ': ' et puis ',
        }
        
        for short, long in expansions.items():
            if short in line:
                line = line.replace(short, long, 1)
                if self.count_french_syllables(line) >= 12:
                    break
        
        return line
    
    def condense_line(self, line: str) -> str:
        """Condense a line to alexandrine length"""
        # Remove unnecessary words
        condensations = {
            ' donc ': ' ',
            ' bien ': ' ',
            ' puis ': ' ',
            ' très ': ' ',
            ' tout ': ' ',
            ' même ': ' ',
        }
        
        for long, short in condensations.items():
            if long in line:
                line = line.replace(long, short, 1)
                if self.count_french_syllables(line) <= 12:
                    break
        
        return line

# Export the translator
translator = ComprehensiveFrenchTranslator()