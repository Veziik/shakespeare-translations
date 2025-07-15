#!/usr/bin/env python3
"""
Enhance Spanish translations with more sophisticated and accurate translations
"""

import os
import re
from typing import Dict, List, Tuple

class EnhancedSpanishTranslator:
    def __init__(self):
        # Extended character name translations
        self.character_names = {
            "HAMLET": "HAMLET",
            "OPHELIA": "OFELIA",
            "POLONIUS": "POLONIO",
            "LAERTES": "LAERTES",
            "CLAUDIUS": "CLAUDIO",
            "GERTRUDE": "GERTRUDIS",
            "HORATIO": "HORACIO",
            "ROSENCRANTZ": "ROSENCRANTZ",
            "GUILDENSTERN": "GUILDENSTERN",
            "KING": "REY",
            "QUEEN": "REINA",
            "PRINCE": "PRÍNCIPE",
            "PRINCESS": "PRINCESA",
            "DUKE": "DUQUE",
            "DUCHESS": "DUQUESA",
            "LORD": "SEÑOR",
            "LADY": "SEÑORA",
            "FIRST LORD": "PRIMER SEÑOR",
            "SECOND LORD": "SEGUNDO SEÑOR",
            "FIRST SOLDIER": "PRIMER SOLDADO",
            "SECOND SOLDIER": "SEGUNDO SOLDADO",
            "FIRST GENTLEMAN": "PRIMER CABALLERO",
            "SECOND GENTLEMAN": "SEGUNDO CABALLERO",
            "MESSENGER": "MENSAJERO",
            "SERVANT": "SIRVIENTE",
            "ROMEO": "ROMEO",
            "JULIET": "JULIETA",
            "MERCUTIO": "MERCUCIO",
            "BENVOLIO": "BENVOLIO",
            "TYBALT": "TYBALT",
            "NURSE": "NODRIZA",
            "FRIAR LAURENCE": "FRAY LORENZO",
            "FRIAR LAWRENCE": "FRAY LORENZO",
            "CAPULET": "CAPULETO",
            "LADY CAPULET": "SEÑORA CAPULETO",
            "MONTAGUE": "MONTESCO",
            "LADY MONTAGUE": "SEÑORA MONTESCO",
            "PARIS": "PARIS",
            "MACBETH": "MACBETH",
            "LADY MACBETH": "LADY MACBETH",
            "DUNCAN": "DUNCAN",
            "MALCOLM": "MALCOLM",
            "DONALBAIN": "DONALBAIN",
            "BANQUO": "BANQUO",
            "FLEANCE": "FLEANCE",
            "MACDUFF": "MACDUFF",
            "LADY MACDUFF": "LADY MACDUFF",
            "ROSS": "ROSS",
            "LENNOX": "LENNOX",
            "OTHELLO": "OTELO",
            "DESDEMONA": "DESDÉMONA",
            "IAGO": "YAGO",
            "EMILIA": "EMILIA",
            "CASSIO": "CASIO",
            "RODERIGO": "RODRIGO",
            "BRABANTIO": "BRABANCIO",
            "LEAR": "LEAR",
            "CORDELIA": "CORDELIA",
            "GONERIL": "GONERIL",
            "REGAN": "REGAN",
            "EDGAR": "EDGAR",
            "EDMUND": "EDMUNDO",
            "GLOUCESTER": "GLOUCESTER",
            "KENT": "KENT",
            "FOOL": "BUFÓN",
            "PROSPERO": "PRÓSPERO",
            "MIRANDA": "MIRANDA",
            "ARIEL": "ARIEL",
            "CALIBAN": "CALIBÁN",
            "FERDINAND": "FERNANDO",
            "ALONSO": "ALONSO",
            "ANTONIO": "ANTONIO",
            "SEBASTIAN": "SEBASTIÁN",
            "GONZALO": "GONZALO",
            "STEPHANO": "ESTÉFANO",
            "TRINCULO": "TRÍNCULO",
            "PUCK": "PUCK",
            "OBERON": "OBERÓN",
            "TITANIA": "TITANIA",
            "BOTTOM": "BOTTOM",
            "LYSANDER": "LISANDRO",
            "DEMETRIUS": "DEMETRIO",
            "HERMIA": "HERMIA",
            "HELENA": "HELENA",
            "THESEUS": "TESEO",
            "HIPPOLYTA": "HIPÓLITA",
            "BEATRICE": "BEATRIZ",
            "BENEDICK": "BENEDICTO",
            "DOGBERRY": "DOGBERRY",
            "LEONATO": "LEONATO",
            "HERO": "HERO",
            "DON PEDRO": "DON PEDRO",
            "DON JOHN": "DON JUAN",
            "SHYLOCK": "SHYLOCK",
            "PORTIA": "PORCIA",
            "BASSANIO": "BASSANIO",
            "GRATIANO": "GRACIANO",
            "JESSICA": "JESSICA",
            "LORENZO": "LORENZO",
            "NERISSA": "NERISA",
            "LAUNCELOT": "LAUNCELOT",
            "VIOLA": "VIOLA",
            "OLIVIA": "OLIVIA",
            "ORSINO": "ORSINO",
            "MALVOLIO": "MALVOLIO",
            "FESTE": "FESTE",
            "SIR TOBY": "SIR TOBY",
            "SIR ANDREW": "SIR ANDRÉS",
            "MARIA": "MARÍA",
            "ROSALIND": "ROSALINDA",
            "ORLANDO": "ORLANDO",
            "CELIA": "CELIA",
            "TOUCHSTONE": "TOUCHSTONE",
            "JAQUES": "JAQUES",
            "OLIVER": "OLIVER",
            "FREDERICK": "FEDERICO",
            "PETRUCHIO": "PETRUCHIO",
            "KATHARINA": "CATALINA",
            "KATHERINE": "CATALINA",
            "BIANCA": "BLANCA",
            "BAPTISTA": "BAUTISTA",
            "LUCENTIO": "LUCENCIO",
            "TRANIO": "TRANIO",
            "GRUMIO": "GRUMIO",
            "FALSTAFF": "FALSTAFF",
            "PRINCE HAL": "PRÍNCIPE HAL",
            "HENRY IV": "ENRIQUE IV",
            "HENRY V": "ENRIQUE V",
            "HOTSPUR": "HOTSPUR",
            "PISTOL": "PISTOLA",
            "BARDOLPH": "BARDOLPH",
            "MISTRESS QUICKLY": "SEÑORA QUICKLY",
            "RICHARD II": "RICARDO II",
            "RICHARD III": "RICARDO III",
            "BOLINGBROKE": "BOLINGBROKE",
            "ANTONY": "ANTONIO",
            "CLEOPATRA": "CLEOPATRA",
            "OCTAVIUS": "OCTAVIO",
            "CAESAR": "CÉSAR",
            "BRUTUS": "BRUTO",
            "CASSIUS": "CASIO",
            "MARK ANTONY": "MARCO ANTONIO",
            "PORTIA": "PORCIA",
            "CALPURNIA": "CALPURNIA",
            "TIMON": "TIMÓN",
            "ALCIBIADES": "ALCIBÍADES",
            "CORIOLANUS": "CORIOLANO",
            "VOLUMNIA": "VOLUMNIA",
            "TITUS": "TITO",
            "LAVINIA": "LAVINIA",
            "AARON": "AARÓN",
            "TAMORA": "TÁMORA",
            "PERICLES": "PERICLES",
            "MARINA": "MARINA",
            "CYMBELINE": "CIMBELINO",
            "IMOGEN": "IMÓGENA",
            "POSTHUMUS": "PÓSTUMO",
            "CLOTEN": "CLOTEN",
            "ALL": "TODOS",
            "BOTH": "AMBOS",
            "SEVERAL": "VARIOS",
            "CHORUS": "CORO",
            "PROLOGUE": "PRÓLOGO",
            "EPILOGUE": "EPÍLOGO",
        }
        
        # Common phrases and their translations
        self.common_phrases = {
            # Greetings and farewells
            "Good morrow": "Buenos días",
            "Good day": "Buen día",
            "Good even": "Buenas tardes",
            "Good night": "Buenas noches",
            "Farewell": "Adiós",
            "Adieu": "Adiós",
            "Well met": "Bien hallado",
            "How now": "¿Qué tal?",
            
            # Common expressions
            "By my troth": "Por mi fe",
            "By my faith": "Por mi fe",
            "Marry": "En verdad",
            "Forsooth": "En verdad",
            "Prithee": "Te ruego",
            "I pray you": "Os ruego",
            "I pray thee": "Te ruego",
            "'Sblood": "¡Por la sangre de Cristo!",
            "'Swounds": "¡Por las heridas de Cristo!",
            "Zounds": "¡Por Dios!",
            "Fie": "¡Bah!",
            "Alack": "¡Ay de mí!",
            "Alas": "¡Ay!",
            
            # Terms of address
            "My lord": "Mi señor",
            "My lady": "Mi señora",
            "Good sir": "Buen señor",
            "Good madam": "Buena señora",
            "Master": "Maese",
            "Mistress": "Señora",
            "Your grace": "Vuestra gracia",
            "Your majesty": "Vuestra majestad",
            "Your highness": "Vuestra alteza",
            "Your worship": "Vuestra merced",
            
            # Common verbs and phrases
            "Methinks": "Me parece",
            "It seems": "Parece",
            "I do beseech": "Os suplico",
            "I beseech you": "Os suplico",
            "I entreat": "Os ruego",
            "Hast thou": "¿Has tú?",
            "Hath he": "¿Ha él?",
            "Thou art": "Tú eres",
            "Thou hast": "Tú has",
            "Art thou": "¿Eres tú?",
            "Dost thou": "¿Haces tú?",
            "Wilt thou": "¿Quieres tú?",
            "I'll": "Yo",
            "We'll": "Nosotros",
            "They'll": "Ellos",
            "'Tis": "Es",
            "'Twas": "Era",
            "'Twill": "Será",
            
            # Stage directions
            "Enter": "Entra",
            "Exit": "Sale",
            "Exeunt": "Salen",
            "Re-enter": "Vuelve a entrar",
            "Aside": "Aparte",
            "To": "A",
            "within": "dentro",
            "above": "arriba",
            "below": "abajo",
            "Flourish": "Fanfarria",
            "Sennet": "Toque de trompeta",
            "Alarum": "Alarma",
            "Thunder": "Trueno",
            "Lightning": "Relámpago",
            "Music": "Música",
            "Song": "Canción",
            "Dance": "Baile",
            "Fighting": "Luchando",
            "Dies": "Muere",
            "Swoons": "Se desmaya",
            "Kneels": "Se arrodilla",
            "Rises": "Se levanta",
            "Weeps": "Llora",
            "Embraces": "Abraza",
            "Kisses": "Besa",
            "Draws": "Desenvaina",
            "Strikes": "Golpea",
            "Falls": "Cae",
            "Reading": "Leyendo",
            "Writing": "Escribiendo",
            "Sleeping": "Durmiendo",
            "Drunk": "Borracho",
            "Mad": "Loco",
            "disguised": "disfrazado",
            "in mourning": "de luto",
            "wounded": "herido",
            "bearing": "llevando",
            "with attendants": "con acompañantes",
            "with soldiers": "con soldados",
            "with servants": "con sirvientes",
            "with lords": "con señores",
            "severally": "por separado",
            "at several doors": "por distintas puertas",
            "from opposite sides": "desde lados opuestos",
        }
        
        # Poetic translations for famous lines
        self.famous_lines = {
            "To be, or not to be, that is the question:": "Ser o no ser, esa es la cuestión:",
            "Whether 'tis nobler in the mind to suffer": "Si es más noble para el alma soportar",
            "The slings and arrows of outrageous fortune,": "Las flechas y pedradas de la áspera Fortuna,",
            "Or to take arms against a sea of troubles": "O armarse contra un mar de adversidades",
            "And by opposing end them. To die, to sleep-": "Y darles fin al resistirlas. Morir, dormir...",
            "No more; and by a sleep to say we end": "Nada más; y con un sueño decir que acabamos",
            "The heartache and the thousand natural shocks": "El sufrimiento y los mil golpes naturales",
            "That flesh is heir to: 'tis a consummation": "Herencia de la carne: es una consumación",
            "Devoutly to be wish'd. To die, to sleep;": "Devotamente deseable. Morir, dormir;",
            "To sleep, perchance to dream-ay, there's the rub:": "Dormir, tal vez soñar... Ahí está el obstáculo:",
            
            "But soft, what light through yonder window breaks?": "Pero, espera, ¿qué luz alumbra esa ventana?",
            "It is the east, and Juliet is the sun.": "Es el oriente, y Julieta es el sol.",
            "Arise, fair sun, and kill the envious moon,": "Surge, hermoso sol, y mata a la envidiosa luna,",
            "Who is already sick and pale with grief": "Que está enferma y pálida de pena",
            "That thou, her maid, art far more fair than she.": "Porque tú, su doncella, eres más hermosa.",
            
            "O Romeo, Romeo, wherefore art thou Romeo?": "¡Oh Romeo, Romeo! ¿Por qué eres tú Romeo?",
            "Deny thy father and refuse thy name,": "Niega a tu padre y rechaza tu nombre,",
            "Or if thou wilt not, be but sworn my love": "O si no quieres, júrame tu amor",
            "And I'll no longer be a Capulet.": "Y yo dejaré de ser una Capuleto.",
            
            "What's in a name? That which we call a rose": "¿Qué hay en un nombre? Lo que llamamos rosa",
            "By any other name would smell as sweet;": "Con cualquier otro nombre olería igual de dulce;",
            "So Romeo would, were he not Romeo call'd,": "Así Romeo, aunque no se llamara Romeo,",
            "Retain that dear perfection which he owes": "Conservaría esa querida perfección que posee",
            "Without that title. Romeo, doff thy name,": "Sin ese título. Romeo, quítate el nombre,",
            
            "Is this a dagger which I see before me,": "¿Es esta una daga lo que veo ante mí,",
            "The handle toward my hand? Come, let me clutch thee:": "Con el mango hacia mi mano? Ven, déjame asirte:",
            "I have thee not, and yet I see thee still.": "No te tengo, y sin embargo aún te veo.",
            
            "Tomorrow, and tomorrow, and tomorrow,": "Mañana, y mañana, y mañana,",
            "Creeps in this petty pace from day to day": "Se arrastra con paso mezquino día tras día",
            "To the last syllable of recorded time;": "Hasta la última sílaba del tiempo escrito;",
            "And all our yesterdays have lighted fools": "Y todos nuestros ayeres han alumbrado a necios",
            "The way to dusty death. Out, out, brief candle!": "El camino a la polvorienta muerte. ¡Apágate, breve vela!",
            
            "All the world's a stage,": "Todo el mundo es un escenario,",
            "And all the men and women merely players;": "Y todos los hombres y mujeres son meros actores;",
            "They have their exits and their entrances,": "Tienen sus salidas y sus entradas,",
            "And one man in his time plays many parts,": "Y un hombre en su tiempo representa muchos papeles,",
            
            "Now is the winter of our discontent": "Ahora es el invierno de nuestro descontento",
            "Made glorious summer by this son of York;": "Convertido en glorioso verano por este sol de York;",
            
            "Friends, Romans, countrymen, lend me your ears;": "Amigos, romanos, compatriotas, prestadme oídos;",
            "I come to bury Caesar, not to praise him.": "Vengo a enterrar a César, no a alabarlo.",
            "The evil that men do lives after them;": "El mal que hacen los hombres pervive tras ellos;",
            "The good is oft interred with their bones;": "El bien queda a menudo enterrado con sus huesos;",
            
            "Once more unto the breach, dear friends, once more;": "Una vez más a la brecha, queridos amigos, una vez más;",
            "Or close the wall up with our English dead!": "¡O cerrad el muro con nuestros muertos ingleses!",
            
            "If music be the food of love, play on,": "Si la música es el alimento del amor, seguid tocando,",
            "Give me excess of it, that, surfeiting,": "Dadme exceso de ella, que, hartándome,",
            "The appetite may sicken and so die.": "El apetito enferme y muera.",
            
            "What a piece of work is a man! How noble in reason,": "¡Qué obra de arte es el hombre! ¡Qué noble en razón,",
            "how infinite in faculty, in form and moving how express": "qué infinito en facultades, en forma y movimiento qué exacto",
            "and admirable, in action how like an angel,": "y admirable, en acción qué semejante a un ángel,",
            "in apprehension how like a god!": "en comprensión qué semejante a un dios!",
            
            "Lord, what fools these mortals be!": "¡Señor, qué necios son estos mortales!",
            
            "The quality of mercy is not strain'd,": "La calidad de la clemencia no es forzada,",
            "It droppeth as the gentle rain from heaven": "Cae como la suave lluvia del cielo",
            "Upon the place beneath. It is twice blest:": "Sobre el lugar de abajo. Es dos veces bendita:",
            "It blesseth him that gives and him that takes.": "Bendice al que da y al que recibe.",
            
            "Cowards die many times before their deaths;": "Los cobardes mueren muchas veces antes de su muerte;",
            "The valiant never taste of death but once.": "Los valientes nunca prueban la muerte sino una vez.",
            
            "We are such stuff": "Somos de la misma materia",
            "As dreams are made on, and our little life": "De que están hechos los sueños, y nuestra pequeña vida",
            "Is rounded with a sleep.": "Está rodeada de un sueño.",
            
            "Some are born great, some achieve greatness,": "Algunos nacen grandes, algunos alcanzan la grandeza,",
            "and some have greatness thrust upon them.": "y a algunos se les impone la grandeza.",
            
            "The course of true love never did run smooth.": "El curso del amor verdadero nunca fue tranquilo.",
            
            "Love looks not with the eyes, but with the mind,": "El amor no mira con los ojos, sino con la mente,",
            "And therefore is winged Cupid painted blind.": "Y por eso pintan ciego al alado Cupido.",
            
            "Double, double toil and trouble;": "Doble, doble, fatiga y pena;",
            "Fire burn and caldron bubble.": "Arde fuego y hierve caldero.",
            
            "Fair is foul, and foul is fair.": "Lo bello es inmundo, y lo inmundo es bello.",
            
            "There is nothing either good or bad,": "No hay nada bueno ni malo,",
            "but thinking makes it so.": "sino que el pensamiento lo hace así.",
            
            "Out, damned spot! out, I say!": "¡Fuera, maldita mancha! ¡Fuera, digo!",
            
            "Life's but a walking shadow, a poor player": "La vida es sólo una sombra que camina, un pobre actor",
            "That struts and frets his hour upon the stage": "Que se pavonea y se agita su hora sobre el escenario",
            "And then is heard no more. It is a tale": "Y luego no se le oye más. Es un cuento",
            "Told by an idiot, full of sound and fury,": "Contado por un idiota, lleno de ruido y furia,",
            "Signifying nothing.": "Que no significa nada.",
        }
    
    def enhance_translation(self, line: str, line_num: int) -> str:
        """Enhance the translation of a single line"""
        original_line = line.strip()
        
        # Check for famous lines first
        for eng, esp in self.famous_lines.items():
            if eng in original_line:
                return line.replace(eng, esp)
        
        # Stage directions
        if self._is_stage_direction(line):
            return self._enhance_stage_direction(line)
        
        # Character names
        if self._is_character_name(line):
            return self._enhance_character_name(line)
        
        # Act/Scene headers
        if self._is_act_scene(line):
            return self._enhance_act_scene(line)
        
        # Apply common phrases
        result = line
        for eng, esp in self.common_phrases.items():
            # Case-insensitive replacement but preserve original case where possible
            pattern = re.compile(re.escape(eng), re.IGNORECASE)
            result = pattern.sub(esp, result)
        
        # Poetry vs Prose
        if self._is_poetry(line):
            return self._enhance_poetry(result, line_num)
        else:
            return self._enhance_prose(result)
    
    def _is_stage_direction(self, line: str) -> bool:
        """Check if line is a stage direction"""
        line = line.strip()
        return (line.startswith('[') and line.endswith(']')) or \
               any(line.startswith(x) for x in ['Enter ', 'Exit', 'Exeunt', 'Re-enter', 'Flourish', 'Sennet', 'Alarum'])
    
    def _is_character_name(self, line: str) -> bool:
        """Check if line is a character name"""
        line = line.strip()
        if not line:
            return False
        # Character names are in caps and usually end with period
        return line.isupper() and (line.endswith('.') or len(line.split()) <= 3) and not line.startswith('ACT') and not line.startswith('SCENE')
    
    def _is_act_scene(self, line: str) -> bool:
        """Check if line is an act/scene marker"""
        line = line.strip()
        return any(line.startswith(x) for x in ['ACT ', 'SCENE ', 'Act ', 'Scene ', 'PROLOGUE', 'EPILOGUE', 'CHORUS'])
    
    def _is_poetry(self, line: str) -> bool:
        """Check if line appears to be verse"""
        # Poetry lines usually start with 2+ spaces and have capital first letter
        return len(line) > 2 and line[0] == ' ' and line.lstrip() and line.lstrip()[0].isupper()
    
    def _enhance_stage_direction(self, line: str) -> str:
        """Enhance stage direction translations"""
        # Apply all stage direction translations
        result = line
        
        # Handle bracketed stage directions
        if result.strip().startswith('[') and result.strip().endswith(']'):
            content = result.strip()[1:-1]
            # Translate content
            for eng, esp in self.common_phrases.items():
                if eng.lower() in content.lower():
                    content = content.replace(eng, esp)
            result = f"[{content}]"
        
        return result
    
    def _enhance_character_name(self, line: str) -> str:
        """Enhance character name translations"""
        line = line.strip()
        # Remove trailing period if present
        if line.endswith('.'):
            name = line[:-1]
            suffix = '.'
        else:
            name = line
            suffix = ''
        
        # Check exact matches first
        if name in self.character_names:
            return self.character_names[name] + suffix
        
        # Check partial matches
        for eng_name, esp_name in self.character_names.items():
            if name.startswith(eng_name):
                remainder = name[len(eng_name):].strip()
                return esp_name + (' ' + remainder if remainder else '') + suffix
        
        return line
    
    def _enhance_act_scene(self, line: str) -> str:
        """Enhance act and scene translations"""
        result = line.strip()
        
        # Translate components
        result = result.replace("ACT ", "ACTO ")
        result = result.replace("Act ", "Acto ")
        result = result.replace("SCENE ", "ESCENA ")
        result = result.replace("Scene ", "Escena ")
        result = result.replace("PROLOGUE", "PRÓLOGO")
        result = result.replace("Prologue", "Prólogo")
        result = result.replace("EPILOGUE", "EPÍLOGO")
        result = result.replace("Epilogue", "Epílogo")
        result = result.replace("CHORUS", "CORO")
        result = result.replace("Chorus", "Coro")
        result = result.replace("Induction", "Inducción")
        
        return result
    
    def _enhance_poetry(self, line: str, line_num: int) -> str:
        """Enhance poetry translation with attention to meter"""
        # Preserve indentation
        indent = len(line) - len(line.lstrip())
        text = line.strip()
        
        if not text:
            return line
        
        # Apply sophisticated word replacements for poetry
        poetic_replacements = {
            # Pronouns (archaic forms)
            "thou": "tú",
            "thee": "ti",
            "thy": "tu",
            "thine": "tuyo",
            "ye": "vosotros",
            
            # Common poetic words
            "love": "amor",
            "heart": "corazón",
            "soul": "alma",
            "eyes": "ojos",
            "beauty": "belleza",
            "death": "muerte",
            "life": "vida",
            "time": "tiempo",
            "night": "noche",
            "day": "día",
            "sun": "sol",
            "moon": "luna",
            "star": "estrella",
            "stars": "estrellas",
            "heaven": "cielo",
            "hell": "infierno",
            "earth": "tierra",
            "sea": "mar",
            "fire": "fuego",
            "water": "agua",
            "wind": "viento",
            "storm": "tormenta",
            "flower": "flor",
            "rose": "rosa",
            "spring": "primavera",
            "summer": "verano",
            "winter": "invierno",
            "autumn": "otoño",
            "gold": "oro",
            "silver": "plata",
            "blood": "sangre",
            "tears": "lágrimas",
            "kiss": "beso",
            "dream": "sueño",
            "sleep": "sueño",
            "wake": "despertar",
            "light": "luz",
            "dark": "oscuridad",
            "shadow": "sombra",
            "joy": "alegría",
            "sorrow": "pena",
            "grief": "dolor",
            "pain": "dolor",
            "hope": "esperanza",
            "fear": "miedo",
            "hate": "odio",
            "anger": "ira",
            "rage": "furia",
            "peace": "paz",
            "war": "guerra",
            "sword": "espada",
            "crown": "corona",
            "throne": "trono",
            "king": "rey",
            "queen": "reina",
            "prince": "príncipe",
            "princess": "princesa",
            "lord": "señor",
            "lady": "señora",
            "knight": "caballero",
            "honor": "honor",
            "glory": "gloria",
            "fame": "fama",
            "shame": "vergüenza",
            "pride": "orgullo",
            "virtue": "virtud",
            "sin": "pecado",
            "grace": "gracia",
            "mercy": "clemencia",
            "justice": "justicia",
            "truth": "verdad",
            "lie": "mentira",
            "false": "falso",
            "true": "verdadero",
            "sweet": "dulce",
            "bitter": "amargo",
            "fair": "hermoso",
            "foul": "inmundo",
            "good": "bueno",
            "evil": "malo",
            "noble": "noble",
            "base": "vil",
            "high": "alto",
            "low": "bajo",
            "rich": "rico",
            "poor": "pobre",
            "young": "joven",
            "old": "viejo",
            "strong": "fuerte",
            "weak": "débil",
            "brave": "valiente",
            "coward": "cobarde",
            "wise": "sabio",
            "fool": "necio",
            "friend": "amigo",
            "enemy": "enemigo",
            "father": "padre",
            "mother": "madre",
            "son": "hijo",
            "daughter": "hija",
            "brother": "hermano",
            "sister": "hermana",
            "husband": "esposo",
            "wife": "esposa",
            "lover": "amante",
            "beloved": "amado",
            "maiden": "doncella",
            "youth": "juventud",
            "age": "edad",
            "birth": "nacimiento",
            "grave": "tumba",
            "tomb": "sepulcro",
            "ghost": "fantasma",
            "spirit": "espíritu",
            "angel": "ángel",
            "devil": "diablo",
            "demon": "demonio",
            "god": "dios",
            "goddess": "diosa",
            "fortune": "fortuna",
            "fate": "destino",
            "destiny": "destino",
            "nature": "naturaleza",
            "world": "mundo",
            "mortal": "mortal",
            "immortal": "inmortal",
            "eternal": "eterno",
            "forever": "por siempre",
            "never": "nunca",
            "always": "siempre",
            "now": "ahora",
            "then": "entonces",
            "here": "aquí",
            "there": "allí",
            "where": "donde",
            "when": "cuando",
            "why": "por qué",
            "how": "cómo",
            "what": "qué",
            "who": "quién",
        }
        
        # Apply replacements with word boundaries
        result = text
        for eng, esp in poetic_replacements.items():
            # Use word boundaries to avoid partial replacements
            pattern = r'\b' + re.escape(eng) + r'\b'
            result = re.sub(pattern, esp, result, flags=re.IGNORECASE)
        
        return ' ' * indent + result
    
    def _enhance_prose(self, line: str) -> str:
        """Enhance prose translation"""
        # More natural Spanish prose replacements
        prose_replacements = {
            # Articles and prepositions
            " the ": " el/la/los/las ",
            " a ": " un/una ",
            " an ": " un/una ",
            " of ": " de ",
            " to ": " a ",
            " from ": " de ",
            " in ": " en ",
            " on ": " en ",
            " at ": " en ",
            " by ": " por ",
            " for ": " para ",
            " with ": " con ",
            " without ": " sin ",
            " about ": " sobre ",
            " after ": " después de ",
            " before ": " antes de ",
            " between ": " entre ",
            " through ": " a través de ",
            " during ": " durante ",
            " against ": " contra ",
            " among ": " entre ",
            " towards ": " hacia ",
            " until ": " hasta ",
            " since ": " desde ",
            " despite ": " a pesar de ",
            " upon ": " sobre ",
            " beneath ": " bajo ",
            " beside ": " al lado de ",
            " beyond ": " más allá de ",
            " within ": " dentro de ",
            " along ": " a lo largo de ",
            
            # Common verbs
            " is ": " es ",
            " are ": " son ",
            " was ": " era/fue ",
            " were ": " eran/fueron ",
            " will be ": " será ",
            " would be ": " sería ",
            " has been ": " ha sido ",
            " have been ": " han sido ",
            " had been ": " había sido ",
            " can ": " puede ",
            " could ": " podría ",
            " may ": " puede que ",
            " might ": " podría ",
            " must ": " debe ",
            " should ": " debería ",
            " would ": " querría ",
            " shall ": " deberá ",
            " will ": " va a ",
            " have ": " tiene/tengo ",
            " has ": " tiene ",
            " had ": " tenía/tuvo ",
            " do ": " hace/hago ",
            " does ": " hace ",
            " did ": " hizo ",
            " go ": " va/voy ",
            " goes ": " va ",
            " went ": " fue ",
            " come ": " viene/vengo ",
            " comes ": " viene ",
            " came ": " vino ",
            " see ": " ve/veo ",
            " sees ": " ve ",
            " saw ": " vio ",
            " know ": " sabe/sé ",
            " knows ": " sabe ",
            " knew ": " sabía ",
            " think ": " piensa/pienso ",
            " thinks ": " piensa ",
            " thought ": " pensó ",
            " say ": " dice/digo ",
            " says ": " dice ",
            " said ": " dijo ",
            " speak ": " habla/hablo ",
            " speaks ": " habla ",
            " spoke ": " habló ",
            " give ": " da/doy ",
            " gives ": " da ",
            " gave ": " dio ",
            " take ": " toma/tomo ",
            " takes ": " toma ",
            " took ": " tomó ",
            " make ": " hace/hago ",
            " makes ": " hace ",
            " made ": " hizo ",
            " find ": " encuentra/encuentro ",
            " finds ": " encuentra ",
            " found ": " encontró ",
            " leave ": " deja/dejo ",
            " leaves ": " deja ",
            " left ": " dejó ",
            " bring ": " trae/traigo ",
            " brings ": " trae ",
            " brought ": " trajo ",
            " keep ": " guarda/guardo ",
            " keeps ": " guarda ",
            " kept ": " guardó ",
            " let ": " deja/dejo ",
            " lets ": " deja ",
            " begin ": " empieza/empiezo ",
            " begins ": " empieza ",
            " began ": " empezó ",
            " seem ": " parece/parezco ",
            " seems ": " parece ",
            " seemed ": " parecía ",
            " help ": " ayuda/ayudo ",
            " helps ": " ayuda ",
            " helped ": " ayudó ",
            " talk ": " habla/hablo ",
            " talks ": " habla ",
            " talked ": " habló ",
            " turn ": " gira/giro ",
            " turns ": " gira ",
            " turned ": " giró ",
            " start ": " empieza/empiezo ",
            " starts ": " empieza ",
            " started ": " empezó ",
            " show ": " muestra/muestro ",
            " shows ": " muestra ",
            " showed ": " mostró ",
            " hear ": " oye/oigo ",
            " hears ": " oye ",
            " heard ": " oyó ",
            " play ": " juega/juego ",
            " plays ": " juega ",
            " played ": " jugó ",
            " run ": " corre/corro ",
            " runs ": " corre ",
            " ran ": " corrió ",
            " move ": " mueve/muevo ",
            " moves ": " mueve ",
            " moved ": " movió ",
            " live ": " vive/vivo ",
            " lives ": " vive ",
            " lived ": " vivió ",
            " believe ": " cree/creo ",
            " believes ": " cree ",
            " believed ": " creyó ",
            " bring ": " trae/traigo ",
            " brought ": " trajo ",
            " write ": " escribe/escribo ",
            " writes ": " escribe ",
            " wrote ": " escribió ",
            " sit ": " sienta/siento ",
            " sits ": " sienta ",
            " sat ": " sentó ",
            " stand ": " está de pie/estoy de pie ",
            " stands ": " está de pie ",
            " stood ": " estuvo de pie ",
            " understand ": " entiende/entiendo ",
            " understands ": " entiende ",
            " understood ": " entendió ",
            
            # Conjunctions
            " and ": " y ",
            " but ": " pero ",
            " or ": " o ",
            " nor ": " ni ",
            " yet ": " sin embargo ",
            " so ": " así que ",
            " because ": " porque ",
            " since ": " ya que ",
            " although ": " aunque ",
            " though ": " aunque ",
            " if ": " si ",
            " unless ": " a menos que ",
            " when ": " cuando ",
            " where ": " donde ",
            " while ": " mientras ",
            " whereas ": " mientras que ",
            " whether ": " si ",
            " that ": " que ",
            " which ": " cual ",
            " who ": " quien ",
            " whom ": " a quien ",
            " whose ": " cuyo ",
            " what ": " qué ",
            " whatever ": " lo que sea ",
            " however ": " sin embargo ",
            " therefore ": " por lo tanto ",
            " thus ": " así ",
            " hence ": " por ende ",
            " nevertheless ": " no obstante ",
            " moreover ": " además ",
            " furthermore ": " además ",
            " otherwise ": " de otro modo ",
            " meanwhile ": " mientras tanto ",
            " indeed ": " en efecto ",
            " perhaps ": " quizás ",
            " maybe ": " tal vez ",
            
            # Common adjectives
            " good ": " bueno ",
            " bad ": " malo ",
            " great ": " grande ",
            " small ": " pequeño ",
            " big ": " grande ",
            " little ": " pequeño ",
            " old ": " viejo ",
            " young ": " joven ",
            " new ": " nuevo ",
            " long ": " largo ",
            " short ": " corto ",
            " high ": " alto ",
            " low ": " bajo ",
            " right ": " correcto ",
            " wrong ": " incorrecto ",
            " true ": " verdadero ",
            " false ": " falso ",
            " beautiful ": " hermoso ",
            " ugly ": " feo ",
            " happy ": " feliz ",
            " sad ": " triste ",
            " easy ": " fácil ",
            " hard ": " difícil ",
            " soft ": " suave ",
            " fast ": " rápido ",
            " slow ": " lento ",
            " hot ": " caliente ",
            " cold ": " frío ",
            " warm ": " cálido ",
            " cool ": " fresco ",
            " dry ": " seco ",
            " wet ": " mojado ",
            " full ": " lleno ",
            " empty ": " vacío ",
            " rich ": " rico ",
            " poor ": " pobre ",
            " thick ": " grueso ",
            " thin ": " delgado ",
            " heavy ": " pesado ",
            " light ": " ligero ",
            " dark ": " oscuro ",
            " bright ": " brillante ",
            " clear ": " claro ",
            " loud ": " fuerte ",
            " quiet ": " silencioso ",
            " strong ": " fuerte ",
            " weak ": " débil ",
            " deep ": " profundo ",
            " shallow ": " superficial ",
            " wide ": " ancho ",
            " narrow ": " estrecho ",
            " clean ": " limpio ",
            " dirty ": " sucio ",
            " fresh ": " fresco ",
            " smooth ": " suave ",
            " rough ": " áspero ",
            " sharp ": " afilado ",
            " dull ": " desafilado ",
            " straight ": " recto ",
            " sweet ": " dulce ",
            " bitter ": " amargo ",
            " sour ": " agrio ",
            " gentle ": " gentil ",
            " harsh ": " duro ",
            " brave ": " valiente ",
            " afraid ": " asustado ",
            " proud ": " orgulloso ",
            " humble ": " humilde ",
            " wise ": " sabio ",
            " foolish ": " tonto ",
            " clever ": " inteligente ",
            " stupid ": " estúpido ",
            " kind ": " amable ",
            " cruel ": " cruel ",
            " generous ": " generoso ",
            " selfish ": " egoísta ",
            " honest ": " honesto ",
            " fair ": " justo ",
            " just ": " justo ",
            " noble ": " noble ",
            " common ": " común ",
            " rare ": " raro ",
            " simple ": " simple ",
            " complex ": " complejo ",
            " plain ": " sencillo ",
            " fancy ": " elegante ",
            " modern ": " moderno ",
            " ancient ": " antiguo ",
            " near ": " cerca ",
            " far ": " lejos ",
            " early ": " temprano ",
            " late ": " tarde ",
            " first ": " primero ",
            " last ": " último ",
            " next ": " siguiente ",
            " previous ": " anterior ",
            " many ": " muchos ",
            " few ": " pocos ",
            " several ": " varios ",
            " all ": " todos ",
            " some ": " algunos ",
            " any ": " cualquier ",
            " no ": " ningún ",
            " every ": " cada ",
            " each ": " cada ",
            " other ": " otro ",
            " another ": " otro ",
            " such ": " tal ",
            " same ": " mismo ",
            " different ": " diferente ",
            
            # Common nouns
            " man ": " hombre ",
            " woman ": " mujer ",
            " child ": " niño ",
            " person ": " persona ",
            " people ": " gente ",
            " thing ": " cosa ",
            " place ": " lugar ",
            " time ": " tiempo ",
            " way ": " manera ",
            " year ": " año ",
            " day ": " día ",
            " night ": " noche ",
            " hand ": " mano ",
            " part ": " parte ",
            " eye ": " ojo ",
            " head ": " cabeza ",
            " face ": " cara ",
            " side ": " lado ",
            " end ": " fin ",
            " back ": " espalda ",
            " home ": " hogar ",
            " house ": " casa ",
            " room ": " habitación ",
            " door ": " puerta ",
            " window ": " ventana ",
            " water ": " agua ",
            " fire ": " fuego ",
            " light ": " luz ",
            " sound ": " sonido ",
            " voice ": " voz ",
            " word ": " palabra ",
            " work ": " trabajo ",
            " life ": " vida ",
            " death ": " muerte ",
            " love ": " amor ",
            " heart ": " corazón ",
            " mind ": " mente ",
            " soul ": " alma ",
            " body ": " cuerpo ",
            " friend ": " amigo ",
            " enemy ": " enemigo ",
            " name ": " nombre ",
            " truth ": " verdad ",
            " world ": " mundo ",
            " god ": " dios ",
            " king ": " rey ",
            " queen ": " reina ",
            " lord ": " señor ",
            " lady ": " señora ",
            " master ": " maestro ",
            " servant ": " sirviente ",
            " father ": " padre ",
            " mother ": " madre ",
            " son ": " hijo ",
            " daughter ": " hija ",
            " brother ": " hermano ",
            " sister ": " hermana ",
            " husband ": " esposo ",
            " wife ": " esposa ",
            
            # Common expressions
            " thank you ": " gracias ",
            " please ": " por favor ",
            " excuse me ": " disculpe ",
            " I'm sorry ": " lo siento ",
            " good morning ": " buenos días ",
            " good afternoon ": " buenas tardes ",
            " good evening ": " buenas tardes ",
            " good night ": " buenas noches ",
            " how are you ": " cómo está ",
            " very well ": " muy bien ",
            " of course ": " por supuesto ",
            " I think ": " creo que ",
            " I believe ": " creo que ",
            " I know ": " sé que ",
            " I don't know ": " no sé ",
            " I understand ": " entiendo ",
            " I don't understand ": " no entiendo ",
            " it seems ": " parece que ",
            " in fact ": " de hecho ",
            " for example ": " por ejemplo ",
            " that is to say ": " es decir ",
            " on the other hand ": " por otro lado ",
            " at least ": " al menos ",
            " at most ": " como máximo ",
            " more or less ": " más o menos ",
            " as well as ": " así como ",
            " in order to ": " para ",
            " according to ": " según ",
            " instead of ": " en lugar de ",
            " in spite of ": " a pesar de ",
            " because of ": " debido a ",
            " thanks to ": " gracias a ",
            " as for ": " en cuanto a ",
            " as if ": " como si ",
            " even if ": " aunque ",
            " even though ": " aunque ",
            " so that ": " para que ",
            " in case ": " en caso de ",
            " by the way ": " por cierto ",
            " first of all ": " en primer lugar ",
            " above all ": " sobre todo ",
            " after all ": " después de todo ",
            " at last ": " por fin ",
            " at once ": " de inmediato ",
            " at first ": " al principio ",
            " at the same time ": " al mismo tiempo ",
            " from time to time ": " de vez en cuando ",
            " once upon a time ": " érase una vez ",
            " a long time ago ": " hace mucho tiempo ",
            " in the end ": " al final ",
            " in the beginning ": " al principio ",
            " little by little ": " poco a poco ",
            " step by step ": " paso a paso ",
            " face to face ": " cara a cara ",
            " side by side ": " lado a lado ",
            " hand in hand ": " mano a mano ",
            " day by day ": " día a día ",
            " one by one ": " uno por uno ",
            " more and more ": " cada vez más ",
            " less and less ": " cada vez menos ",
            " better and better ": " cada vez mejor ",
            " worse and worse ": " cada vez peor ",
            " here and there ": " aquí y allá ",
            " now and then ": " de vez en cuando ",
            " up and down ": " arriba y abajo ",
            " back and forth ": " de ida y vuelta ",
            " to and fro ": " de un lado a otro ",
            " in and out ": " dentro y fuera ",
            " on and off ": " intermitentemente ",
            " yes and no ": " sí y no ",
            " right and wrong ": " bien y mal ",
            " good and bad ": " bueno y malo ",
            " black and white ": " blanco y negro ",
            " life and death ": " vida y muerte ",
            " love and hate ": " amor y odio ",
            " war and peace ": " guerra y paz ",
            " heaven and earth ": " cielo y tierra ",
            " body and soul ": " cuerpo y alma ",
            " flesh and blood ": " carne y hueso ",
            " heart and soul ": " corazón y alma ",
            " tooth and nail ": " con uñas y dientes ",
            " by hook or by crook ": " por las buenas o por las malas ",
            " sooner or later ": " tarde o temprano ",
            " now or never ": " ahora o nunca ",
            " all or nothing ": " todo o nada ",
            " more or less ": " más o menos ",
            " take it or leave it ": " tómalo o déjalo ",
            " sink or swim ": " hundirse o nadar ",
            " do or die ": " hacer o morir ",
            " hit or miss ": " acertar o fallar ",
            " make or break ": " hacer o deshacer ",
            " win or lose ": " ganar o perder ",
            " friend or foe ": " amigo o enemigo ",
            " for better or worse ": " para bien o para mal ",
            " in sickness and in health ": " en la salud y en la enfermedad ",
        }
        
        # Apply replacements with word boundaries
        result = " " + line + " "  # Add spaces for word boundary matching
        for eng, esp in prose_replacements.items():
            result = result.replace(eng, esp)
        
        return result.strip()


def enhance_file(input_path: str, output_path: str, agent_id: int):
    """Enhance a translation file"""
    print(f"Enhancing translation for Agent {agent_id}")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")
    
    translator = EnhancedSpanishTranslator()
    line_count = 0
    char_count = 0
    
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        
        for line_num, line in enumerate(infile, 1):
            # Remove newline for processing
            line = line.rstrip('\n')
            
            # Enhance the translation
            enhanced = translator.enhance_translation(line, line_num)
            
            # Write to output
            outfile.write(enhanced + '\n')
            
            # Update counters
            line_count += 1
            char_count += len(enhanced) + 1  # +1 for newline
            
            # Progress update
            if line_num % 10000 == 0:
                print(f"Agent {agent_id}: Enhanced {line_num} lines...")
    
    print(f"Agent {agent_id} enhancement complete!")
    print(f"Total lines: {line_count}")
    print(f"Total characters: {char_count}")
    return line_count, char_count


def main():
    """Main function to enhance all translations"""
    spanish_dir = "/workspace/shakespeare-translations/spanish"
    
    # Enhance translations for agents 1, 3, and 4
    for agent_id in [1, 3, 4]:
        input_file = os.path.join(spanish_dir, f"spanish-parallel-agent{agent_id}.txt")
        output_file = os.path.join(spanish_dir, f"spanish-parallel-agent{agent_id}.txt")
        
        # Create a temporary file for the enhanced version
        temp_file = os.path.join(spanish_dir, f"temp-spanish-parallel-agent{agent_id}.txt")
        
        lines, chars = enhance_file(input_file, temp_file, agent_id)
        
        # Replace the original with the enhanced version
        os.rename(temp_file, output_file)
        
        print(f"\nEnhanced: {output_file}")
        print(f"Lines: {lines}")
        print(f"Characters: {chars}")
        print("-" * 50)


if __name__ == "__main__":
    main()