#!/usr/bin/env python3
"""
French Translation Helper for Shakespeare's Works
Assists in translating Shakespeare's complete works into French
"""

import re
import json
from typing import Dict, List, Tuple

class FrenchTranslationHelper:
    def __init__(self):
        # Common Shakespeare -> French translations
        self.common_words = {
            'thou': 'tu',
            'thee': 'toi',
            'thy': 'ton/ta/tes',
            'thine': 'tien/tienne',
            'hath': 'a',
            'doth': 'fait',
            'art': 'es',
            'wilt': 'veux',
            'shalt': 'dois',
            'canst': 'peux',
            'wouldst': 'voudrais',
            'shouldst': 'devrais',
            'hast': 'as',
            'dost': 'fais',
            'ere': 'avant',
            "'tis": "c'est",
            'wherefore': 'pourquoi',
            'whence': "d'où",
            'whither': 'où',
            'prithee': 'je te prie',
            'forsooth': 'en vérité',
            'methinks': 'il me semble',
            'perchance': 'peut-être',
            'anon': 'bientôt',
            'betwixt': 'entre',
            'nay': 'non',
            'yea': 'oui',
            'oft': 'souvent',
            'ne\'er': 'jamais',
            'e\'er': 'jamais',
            'o\'er': 'sur',
            'Love': 'Amour',
            'Time': 'Temps',
            'Death': 'Mort',
            'Beauty': 'Beauté',
            'Youth': 'Jeunesse',
            'Age': 'Âge',
            'Nature': 'Nature',
            'Fortune': 'Fortune',
            'Heaven': 'Ciel',
            'Hell': 'Enfer',
            'God': 'Dieu',
            'Lord': 'Seigneur',
            'Lady': 'Dame',
            'King': 'Roi',
            'Queen': 'Reine',
            'Prince': 'Prince',
            'Princess': 'Princesse',
            'Duke': 'Duc',
            'Count': 'Comte',
            'knight': 'chevalier',
            'fair': 'beau/belle',
            'sweet': 'doux/douce',
            'gentle': 'gentil/gentille',
            'true': 'vrai/vraie',
            'false': 'faux/fausse',
            'good': 'bon/bonne',
            'evil': 'mauvais/mal',
            'love': 'amour/aimer',
            'hate': 'haine/haïr',
            'life': 'vie',
            'death': 'mort',
            'heart': 'cœur',
            'soul': 'âme',
            'mind': 'esprit',
            'eye': 'œil',
            'eyes': 'yeux',
            'hand': 'main',
            'face': 'visage',
            'beauty': 'beauté',
            'rose': 'rose',
            'flower': 'fleur',
            'sun': 'soleil',
            'moon': 'lune',
            'star': 'étoile',
            'stars': 'étoiles',
            'night': 'nuit',
            'day': 'jour',
            'light': 'lumière',
            'dark': 'sombre',
            'darkness': 'ténèbres',
            'shadow': 'ombre',
            'dream': 'rêve',
            'sleep': 'sommeil',
            'wake': 'éveiller',
            'time': 'temps',
            'hour': 'heure',
            'year': 'année',
            'spring': 'printemps',
            'summer': 'été',
            'autumn': 'automne',
            'winter': 'hiver'
        }
        
        # Common phrases
        self.common_phrases = {
            'to be or not to be': 'être ou ne pas être',
            'all the world\'s a stage': 'le monde entier est un théâtre',
            'wherefore art thou': 'pourquoi es-tu',
            'parting is such sweet sorrow': 'se séparer est un si doux chagrin',
            'what\'s in a name': 'qu\'y a-t-il dans un nom',
            'the course of true love': 'le cours du véritable amour',
            'never did run smooth': 'n\'a jamais été sans encombre',
            'to thine own self be true': 'sois fidèle à toi-même',
            'though this be madness': 'bien que ce soit folie',
            'yet there is method in\'t': 'il y a pourtant méthode',
            'something is rotten': 'quelque chose est pourri',
            'frailty, thy name is woman': 'fragilité, ton nom est femme',
            'brevity is the soul of wit': 'la brièveté est l\'âme de l\'esprit',
            'the lady doth protest too much': 'la dame proteste trop',
            'all that glisters is not gold': 'tout ce qui brille n\'est pas or',
            'the quality of mercy': 'la qualité de la clémence',
            'is not strained': 'n\'est pas forcée',
            'double, double toil and trouble': 'double, double labeur et peine',
            'fair is foul, and foul is fair': 'le beau est laid, et le laid est beau',
            'out, damned spot': 'sors, maudite tache',
            'a plague on both your houses': 'peste sur vos deux maisons',
            'star-crossed lovers': 'amants maudits par les étoiles',
            'what light through yonder window breaks': 'quelle lumière perce à cette fenêtre',
            'it is the east': 'c\'est l\'orient',
            'and Juliet is the sun': 'et Juliette est le soleil',
            'once more unto the breach': 'encore une fois dans la brèche',
            'we few, we happy few': 'nous quelques-uns, nous heureux quelques-uns',
            'we band of brothers': 'nous bande de frères',
            'now is the winter of our discontent': 'voici l\'hiver de notre mécontentement',
            'a horse, a horse': 'un cheval, un cheval',
            'my kingdom for a horse': 'mon royaume pour un cheval',
            'is this a dagger which I see before me': 'est-ce un poignard que je vois devant moi',
            'life\'s but a walking shadow': 'la vie n\'est qu\'une ombre qui marche',
            'a poor player': 'un pauvre acteur',
            'full of sound and fury': 'plein de bruit et de fureur',
            'signifying nothing': 'ne signifiant rien',
            'lord, what fools these mortals be': 'seigneur, quels fous sont ces mortels',
            'the course of true love never did run smooth': 'le cours du véritable amour n\'a jamais été sans encombre',
            'love looks not with the eyes': 'l\'amour ne regarde pas avec les yeux',
            'but with the mind': 'mais avec l\'esprit'
        }
        
        # Character names (maintain consistency)
        self.character_names = {
            'Romeo': 'Roméo',
            'Juliet': 'Juliette',
            'Hamlet': 'Hamlet',
            'Ophelia': 'Ophélie',
            'Macbeth': 'Macbeth',
            'Lady Macbeth': 'Lady Macbeth',
            'Othello': 'Othello',
            'Desdemona': 'Desdémone',
            'Iago': 'Iago',
            'King Lear': 'Le Roi Lear',
            'Cordelia': 'Cordélia',
            'Prospero': 'Prospero',
            'Miranda': 'Miranda',
            'Caliban': 'Caliban',
            'Ariel': 'Ariel',
            'Bottom': 'Bottom',
            'Puck': 'Puck',
            'Oberon': 'Obéron',
            'Titania': 'Titania',
            'Shylock': 'Shylock',
            'Portia': 'Portia',
            'Brutus': 'Brutus',
            'Caesar': 'César',
            'Antony': 'Antoine',
            'Cleopatra': 'Cléopâtre',
            'Falstaff': 'Falstaff',
            'Prince Hal': 'Prince Hal',
            'Henry': 'Henri',
            'Richard': 'Richard',
            'Katherine': 'Catherine',
            'Petruchio': 'Petruchio',
            'Beatrice': 'Béatrice',
            'Benedick': 'Bénédict',
            'Rosalind': 'Rosalinde',
            'Orlando': 'Orlando',
            'Viola': 'Viola',
            'Malvolio': 'Malvolio',
            'Touchstone': 'Pierre de Touche',
            'Jacques': 'Jacques'
        }
        
    def count_syllables_french(self, line: str) -> int:
        """Count syllables in a French line (approximate)"""
        # Remove punctuation
        line = re.sub(r'[^\w\s]', '', line)
        # Count vowel groups as syllables (simplified)
        syllables = 0
        vowels = 'aeiouyàâäéèêëïîôùûü'
        prev_was_vowel = False
        
        for char in line.lower():
            if char in vowels:
                if not prev_was_vowel:
                    syllables += 1
                prev_was_vowel = True
            else:
                prev_was_vowel = False
                
        # Handle silent 'e' at end of words
        words = line.split()
        for word in words:
            if word.endswith('e') and len(word) > 2:
                syllables -= 1
                
        return max(1, syllables)
    
    def format_as_alexandrine(self, line: str) -> str:
        """Try to format a line as an alexandrine (12 syllables)"""
        syllables = self.count_syllables_french(line)
        # This is a placeholder - real alexandrine formatting is complex
        return line
    
    def translate_common_terms(self, text: str) -> str:
        """Replace common Shakespearean terms with French equivalents"""
        for eng, fr in self.common_words.items():
            # Use word boundaries to avoid partial replacements
            text = re.sub(r'\b' + eng + r'\b', fr, text, flags=re.IGNORECASE)
        return text
    
    def maintain_character_names(self, text: str) -> str:
        """Ensure character names are consistently translated"""
        for eng, fr in self.character_names.items():
            text = text.replace(eng, fr)
        return text
    
    def format_stage_directions(self, text: str) -> str:
        """Format stage directions in French style"""
        # Convert [Enter ...] to [Entre ...]
        text = re.sub(r'\[Enter\s+', '[Entre ', text)
        text = re.sub(r'\[Exit\s+', '[Sort ', text)
        text = re.sub(r'\[Exeunt\s+', '[Sortent ', text)
        text = re.sub(r'\[Aside\]', '[À part]', text)
        text = re.sub(r'\[Within\]', '[De l\'intérieur]', text)
        text = re.sub(r'\[Dies\]', '[Meurt]', text)
        text = re.sub(r'\[Sleeps\]', '[S\'endort]', text)
        text = re.sub(r'\[Wakes\]', '[Se réveille]', text)
        return text
    
    def detect_verse_type(self, text: str) -> str:
        """Detect if text is verse, prose, or stage direction"""
        lines = text.strip().split('\n')
        if not lines:
            return 'empty'
        
        # Stage directions usually in brackets or all caps
        if text.strip().startswith('[') or text.strip().startswith('ACT') or text.strip().startswith('SCENE'):
            return 'stage_direction'
        
        # Verse typically has regular line lengths and capitals at start
        verse_score = 0
        for line in lines[:5]:  # Check first 5 lines
            if line.strip() and line.strip()[0].isupper():
                verse_score += 1
            if 40 < len(line) < 80:  # Typical verse line length
                verse_score += 1
        
        if verse_score > len(lines[:5]):
            return 'verse'
        return 'prose'
    
    def process_chunk(self, chunk_text: str) -> Dict[str, any]:
        """Process a chunk of text and prepare translation helpers"""
        stats = {
            'total_lines': len(chunk_text.split('\n')),
            'verse_lines': 0,
            'prose_lines': 0,
            'stage_directions': 0,
            'characters_found': set(),
            'common_phrases_found': []
        }
        
        # Find character names
        for char in self.character_names:
            if char in chunk_text:
                stats['characters_found'].add(char)
        
        # Find common phrases
        for phrase in self.common_phrases:
            if phrase.lower() in chunk_text.lower():
                stats['common_phrases_found'].append(phrase)
        
        return stats

# Helper functions for the translation process
def create_translation_guidelines():
    """Create guidelines for French translation of Shakespeare"""
    guidelines = """
# Directives de Traduction - Shakespeare en Français

## Principes Généraux
1. **Alexandrins** : Utiliser des vers de 12 syllabes pour les passages poétiques
2. **Césure** : Respecter la césure après la 6e syllabe dans les alexandrins
3. **Rimes** : Maintenir le schéma de rimes quand possible (ABAB, ABBA, etc.)
4. **Registre** : Adapter le niveau de langue selon le personnage
5. **Jeux de mots** : Trouver des équivalents français plutôt que traduire littéralement

## Structure des Vers
- Alexandrin classique : 6 + 6 syllabes
- Alexandrin romantique : plus libre, mais toujours 12 syllabes
- Pour les sonnets : maintenir 14 vers

## Vocabulaire Shakespearien
- Thou/Thee → Tu/Toi (tutoiement pour l'intimité)
- You → Vous (vouvoiement pour le respect)
- Adapter les métaphores à la culture française
- Préserver les images poétiques essentielles

## Conventions Théâtrales
- [Entre X] pour [Enter X]
- [Sort X] pour [Exit X]
- [À part] pour [Aside]
- Didascalies en italique

## Noms Propres
- Franciser quand une tradition existe (Roméo, Juliette)
- Garder l'original sinon (Hamlet, Macbeth)
- Titres : traduire (Le Roi Lear, Le Marchand de Venise)
"""
    return guidelines

if __name__ == "__main__":
    helper = FrenchTranslationHelper()
    print("French Translation Helper initialized")
    print(f"Loaded {len(helper.common_words)} common word translations")
    print(f"Loaded {len(helper.common_phrases)} common phrase translations")
    print(f"Loaded {len(helper.character_names)} character name translations")