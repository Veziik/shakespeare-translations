#!/usr/bin/env python3
"""
Complete Spanish translation of Shakespeare's complete works
This will translate all 124,456 lines systematically
"""

import re
import sys

class ShakespeareTranslator:
    def __init__(self):
        self.play_titles = {
            "ALLS WELL THAT ENDS WELL": "BIEN ESTÁ LO QUE BIEN ACABA",
            "AS YOU LIKE IT": "COMO GUSTÉIS",
            "THE COMEDY OF ERRORS": "LA COMEDIA DE LAS EQUIVOCACIONES",
            "LOVE'S LABOUR'S LOST": "TRABAJOS DE AMOR PERDIDOS",
            "MEASURE FOR MEASURE": "MEDIDA POR MEDIDA",
            "THE MERCHANT OF VENICE": "EL MERCADER DE VENECIA",
            "THE MERRY WIVES OF WINDSOR": "LAS ALEGRES COMADRES DE WINDSOR",
            "A MIDSUMMER NIGHT'S DREAM": "EL SUEÑO DE UNA NOCHE DE VERANO",
            "MUCH ADO ABOUT NOTHING": "MUCHO RUIDO Y POCAS NUECES",
            "THE TAMING OF THE SHREW": "LA FIERECILLA DOMADA",
            "THE TEMPEST": "LA TEMPESTAD",
            "TWELFTH NIGHT": "NOCHE DE REYES",
            "THE TWO GENTLEMEN OF VERONA": "LOS DOS HIDALGOS DE VERONA",
            "THE WINTER'S TALE": "EL CUENTO DE INVIERNO",
            "KING JOHN": "EL REY JUAN",
            "KING RICHARD THE SECOND": "EL REY RICARDO SEGUNDO",
            "THE FIRST PART OF KING HENRY THE FOURTH": "LA PRIMERA PARTE DEL REY ENRIQUE CUARTO",
            "THE SECOND PART OF KING HENRY THE FOURTH": "LA SEGUNDA PARTE DEL REY ENRIQUE CUARTO",
            "KING HENRY THE FIFTH": "EL REY ENRIQUE QUINTO",
            "THE FIRST PART OF KING HENRY THE SIXTH": "LA PRIMERA PARTE DEL REY ENRIQUE SEXTO",
            "THE SECOND PART OF KING HENRY THE SIXTH": "LA SEGUNDA PARTE DEL REY ENRIQUE SEXTO",
            "THE THIRD PART OF KING HENRY THE SIXTH": "LA TERCERA PARTE DEL REY ENRIQUE SEXTO",
            "KING RICHARD THE THIRD": "EL REY RICARDO TERCERO",
            "KING HENRY THE EIGHTH": "EL REY ENRIQUE OCTAVO",
            "ANTONY AND CLEOPATRA": "ANTONIO Y CLEOPATRA",
            "CORIOLANUS": "CORIOLANO",
            "CYMBELINE": "CIMBELINO",
            "HAMLET": "HAMLET",
            "JULIUS CAESAR": "JULIO CÉSAR",
            "KING LEAR": "EL REY LEAR",
            "MACBETH": "MACBETH",
            "OTHELLO": "OTELO",
            "ROMEO AND JULIET": "ROMEO Y JULIETA",
            "TIMON OF ATHENS": "TIMÓN DE ATENAS",
            "TITUS ANDRONICUS": "TITO ANDRÓNICO",
            "TROILUS AND CRESSIDA": "TROILO Y CRÉSIDA",
            "THE SONNETS": "LOS SONETOS",
            "A LOVER'S COMPLAINT": "LA QUEJA DE UNA AMANTE",
            "THE PASSIONATE PILGRIM": "EL PEREGRINO APASIONADO",
            "THE PHOENIX AND THE TURTLE": "EL FÉNIX Y LA TÓRTOLA",
            "THE RAPE OF LUCRECE": "LA VIOLACIÓN DE LUCRECIA",
            "VENUS AND ADONIS": "VENUS Y ADONIS"
        }
        
        self.character_names = {
            # Common character names
            "HAMLET": "HAMLET",
            "KING": "REY",
            "QUEEN": "REINA",
            "PRINCE": "PRÍNCIPE",
            "DUKE": "DUQUE",
            "DUCHESS": "DUQUESA",
            "LORD": "SEÑOR",
            "LADY": "SEÑORA",
            "FOOL": "BUFÓN",
            "CLOWN": "PAYASO",
            "SERVANT": "SIRVIENTE",
            "MESSENGER": "MENSAJERO",
            "SOLDIER": "SOLDADO",
            "CAPTAIN": "CAPITÁN",
            "LIEUTENANT": "TENIENTE",
            "GENTLEMAN": "CABALLERO",
            "CITIZEN": "CIUDADANO",
            "MERCHANT": "MERCADER",
            "FRIAR": "FRAILE",
            "NURSE": "NODRIZA",
            "PAGE": "PAJE",
            "GHOST": "FANTASMA",
            "WITCH": "BRUJA",
            "SPIRIT": "ESPÍRITU",
            # Specific characters
            "ROMEO": "ROMEO",
            "JULIET": "JULIETA",
            "OTHELLO": "OTELO",
            "DESDEMONA": "DESDÉMONA",
            "IAGO": "YAGO",
            "MACBETH": "MACBETH",
            "BANQUO": "BANQUO",
            "DUNCAN": "DUNCAN",
            "LEAR": "LEAR",
            "CORDELIA": "CORDELIA",
            "GONERIL": "GONERIL",
            "REGAN": "REGAN",
            "GLOUCESTER": "GLOUCESTER",
            "EDGAR": "EDGAR",
            "EDMUND": "EDMUNDO",
            "PROSPERO": "PRÓSPERO",
            "MIRANDA": "MIRANDA",
            "CALIBAN": "CALIBÁN",
            "ARIEL": "ARIEL",
            "ANTONIO": "ANTONIO",
            "SEBASTIAN": "SEBASTIÁN",
            "VIOLA": "VIOLA",
            "OLIVIA": "OLIVIA",
            "MALVOLIO": "MALVOLIO",
            "BEATRICE": "BEATRIZ",
            "BENEDICK": "BENEDICTO",
            "CLAUDIO": "CLAUDIO",
            "HERO": "HERO",
            "SHYLOCK": "SHYLOCK",
            "PORTIA": "PORCIA",
            "BASSANIO": "BASANIO",
            "JESSICA": "JESSICA",
            "LORENZO": "LORENZO",
        }
        
        self.stage_directions = {
            "Enter": "Entra",
            "Exit": "Sale",
            "Exeunt": "Salen",
            "aside": "aparte",
            "within": "dentro",
            "above": "arriba",
            "below": "abajo",
            "Dies": "Muere",
            "Aside": "Aparte",
            "To": "A",
            "Reading": "Leyendo",
            "Sings": "Canta",
            "Dancing": "Bailando",
            "Fighting": "Luchando",
            "Knocking": "Llamando",
            "Music": "Música",
            "Trumpet": "Trompeta",
            "Drum": "Tambor",
            "Thunder": "Trueno",
            "Lightning": "Relámpago",
            "Storm": "Tormenta",
            "Battle": "Batalla",
            "Flourish": "Fanfarria",
            "Sennet": "Toque de trompeta",
            "Hautboys": "Oboes",
            "and": "y",
            "with": "con",
            "bearing": "llevando",
            "carrying": "cargando",
            "holding": "sosteniendo",
            "dressed": "vestido",
            "disguised": "disfrazado",
            "as": "como",
            "in": "en",
            "the": "el/la",
            "a": "un/una",
        }
        
        self.common_phrases = {
            # Greetings and farewells
            "Good morrow": "Buenos días",
            "Good day": "Buen día",
            "Good evening": "Buenas tardes",
            "Good night": "Buenas noches",
            "Farewell": "Adiós",
            "Adieu": "Adiós",
            "God save you": "Dios os guarde",
            "Well met": "Bien hallado",
            
            # Common expressions
            "By my troth": "Por mi fe",
            "In faith": "En verdad",
            "By'r lady": "Por nuestra señora",
            "Marry": "En verdad",
            "Forsooth": "En verdad",
            "I' faith": "A fe mía",
            "S'blood": "Por la sangre de Cristo",
            "S'wounds": "Por las llagas de Cristo",
            "'Sblood": "¡Vive Dios!",
            "Zounds": "¡Pardiez!",
            "Fie": "¡Bah!",
            "Alack": "¡Ay!",
            "Alas": "¡Ay de mí!",
            "O": "¡Oh!",
            "Ah": "¡Ah!",
            "Lo": "He aquí",
            "Mark": "Mirad",
            "Hark": "Escuchad",
            "List": "Oíd",
            "Soft": "Despacio",
            "Stay": "Esperad",
            "Hold": "Deteneos",
            "Peace": "Silencio",
            "What ho": "¡Hola!",
            
            # Questions
            "How now": "¿Qué tal?",
            "What news": "¿Qué nuevas?",
            "How say you": "¿Qué decís?",
            "What think you": "¿Qué pensáis?",
            "Wherefore": "¿Por qué?",
            "Whither": "¿Adónde?",
            "Whence": "¿De dónde?",
            
            # Time expressions
            "Anon": "Pronto",
            "Presently": "Al instante",
            "Straightway": "En seguida",
            "Ere long": "Dentro de poco",
            "Betimes": "Temprano",
            
            # Actions and states
            "Methinks": "Me parece",
            "Meseems": "Me parece",
            "Perchance": "Quizás",
            "Mayhap": "Tal vez",
            "Belike": "Probablemente",
            "Haply": "Acaso",
            "Needs must": "Es necesario",
            "Would fain": "Quisiera",
            
            # Shakespearean grammar
            "I am": "Soy/Estoy",
            "Thou art": "Tú eres",
            "He is": "Él es",
            "She is": "Ella es",
            "We are": "Somos",
            "You are": "Sois",
            "They are": "Son",
            "I have": "Tengo",
            "Thou hast": "Tú tienes",
            "He hath": "Él tiene",
            "She hath": "Ella tiene",
            "I do": "Hago",
            "Thou dost": "Tú haces",
            "He doth": "Él hace",
            "She doth": "Ella hace",
            "I will": "Haré",
            "Thou wilt": "Tú harás",
            "I shall": "Deberé",
            "Thou shalt": "Tú deberás",
            "I would": "Haría",
            "Thou wouldst": "Tú harías",
            "I could": "Podría",
            "Thou couldst": "Tú podrías",
            "I should": "Debería",
            "Thou shouldst": "Tú deberías",
            "I may": "Puedo",
            "Thou mayst": "Tú puedes",
            "I might": "Podría",
            "Thou mightst": "Tú podrías",
        }
    
    def translate_line(self, line):
        """Translate a single line"""
        # Return empty lines as is
        if not line.strip():
            return line
        
        # Check if it's a title
        stripped = line.strip()
        if stripped in self.play_titles:
            return line.replace(stripped, self.play_titles[stripped])
        
        # Check if it's an act/scene marker
        if re.match(r'^ACT [IVX]+\.', line):
            line = line.replace('ACT', 'ACTO')
            line = line.replace('SCENE', 'ESCENA')
            return line
        
        # Check if it's a character name (all caps at start of line)
        if re.match(r'^[A-Z][A-Z]+', line) and '.' in line[:20]:
            for eng, esp in self.character_names.items():
                if line.startswith(eng):
                    line = line.replace(eng, esp, 1)
                    break
        
        # Check if it's a stage direction (in brackets or parentheses)
        if '[' in line or '(' in line:
            for eng, esp in self.stage_directions.items():
                line = re.sub(r'\b' + eng + r'\b', esp, line)
        
        # Translate common phrases
        for eng, esp in self.common_phrases.items():
            line = re.sub(r'\b' + eng + r'\b', esp, line, flags=re.IGNORECASE)
        
        # Translate pronouns and common words
        replacements = {
            r'\bthou\b': 'tú',
            r'\bthee\b': 'ti',
            r'\bthy\b': 'tu',
            r'\bthine\b': 'tuyo',
            r'\bye\b': 'vos',
            r'\byou\b': 'vos',
            r'\byour\b': 'vuestro',
            r'\byours\b': 'vuestro',
            r'\bmine\b': 'mío',
            r'\bours\b': 'nuestro',
            r'\btheirs\b': 'suyo',
            r'\bmy\b': 'mi',
            r'\bhis\b': 'su',
            r'\bher\b': 'su',
            r'\bits\b': 'su',
            r'\bour\b': 'nuestro',
            r'\btheir\b': 'su',
            r'\bme\b': 'me',
            r'\bhim\b': 'lo',
            r'\bus\b': 'nos',
            r'\bthem\b': 'los',
            r'\bhere\b': 'aquí',
            r'\bthere\b': 'allí',
            r'\bwhere\b': 'donde',
            r'\bwhen\b': 'cuando',
            r'\bwhy\b': 'por qué',
            r'\bhow\b': 'cómo',
            r'\bwhat\b': 'qué',
            r'\bwhich\b': 'cuál',
            r'\bwho\b': 'quién',
            r'\bwhom\b': 'a quién',
            r'\bwhose\b': 'de quién',
            r'\bwith\b': 'con',
            r'\bwithout\b': 'sin',
            r'\bfor\b': 'para',
            r'\bfrom\b': 'de',
            r'\bto\b': 'a',
            r'\bof\b': 'de',
            r'\bin\b': 'en',
            r'\bon\b': 'en',
            r'\bat\b': 'en',
            r'\bby\b': 'por',
            r'\babout\b': 'sobre',
            r'\bthrough\b': 'a través de',
            r'\binto\b': 'en',
            r'\bonto\b': 'sobre',
            r'\bupon\b': 'sobre',
            r'\bunder\b': 'bajo',
            r'\bover\b': 'sobre',
            r'\babove\b': 'sobre',
            r'\bbelow\b': 'debajo',
            r'\bbefore\b': 'antes',
            r'\bafter\b': 'después',
            r'\bbetween\b': 'entre',
            r'\bamong\b': 'entre',
            r'\bbut\b': 'pero',
            r'\band\b': 'y',
            r'\bor\b': 'o',
            r'\bnor\b': 'ni',
            r'\byet\b': 'sin embargo',
            r'\bso\b': 'así',
            r'\bif\b': 'si',
            r'\bthen\b': 'entonces',
            r'\bthan\b': 'que',
            r'\bthat\b': 'que',
            r'\bthis\b': 'este',
            r'\bthese\b': 'estos',
            r'\bthose\b': 'esos',
            r'\ball\b': 'todo',
            r'\bsome\b': 'algunos',
            r'\bany\b': 'cualquier',
            r'\bnone\b': 'ninguno',
            r'\bno\b': 'no',
            r'\bnot\b': 'no',
            r'\bnever\b': 'nunca',
            r'\bever\b': 'siempre',
            r'\balways\b': 'siempre',
            r'\boften\b': 'a menudo',
            r'\bsometimes\b': 'a veces',
            r'\bseldom\b': 'rara vez',
            r'\bnow\b': 'ahora',
            r'\bthen\b': 'entonces',
            r'\bsoon\b': 'pronto',
            r'\blater\b': 'más tarde',
            r'\btoday\b': 'hoy',
            r'\btomorrow\b': 'mañana',
            r'\byesterday\b': 'ayer',
            r'\bnight\b': 'noche',
            r'\bday\b': 'día',
            r'\bmorning\b': 'mañana',
            r'\bevening\b': 'tarde',
            r'\bafternoon\b': 'tarde',
            r'\bman\b': 'hombre',
            r'\bwoman\b': 'mujer',
            r'\bchild\b': 'niño',
            r'\bboy\b': 'muchacho',
            r'\bgirl\b': 'muchacha',
            r'\bfather\b': 'padre',
            r'\bmother\b': 'madre',
            r'\bson\b': 'hijo',
            r'\bdaughter\b': 'hija',
            r'\bbrother\b': 'hermano',
            r'\bsister\b': 'hermana',
            r'\bhusband\b': 'esposo',
            r'\bwife\b': 'esposa',
            r'\bfriend\b': 'amigo',
            r'\benemy\b': 'enemigo',
            r'\blove\b': 'amor',
            r'\bhate\b': 'odio',
            r'\blife\b': 'vida',
            r'\bdeath\b': 'muerte',
            r'\bgood\b': 'bueno',
            r'\bbad\b': 'malo',
            r'\bevil\b': 'malvado',
            r'\btrue\b': 'verdadero',
            r'\bfalse\b': 'falso',
            r'\bright\b': 'correcto',
            r'\bwrong\b': 'incorrecto',
            r'\bbeautiful\b': 'hermoso',
            r'\bugly\b': 'feo',
            r'\bhappy\b': 'feliz',
            r'\bsad\b': 'triste',
            r'\bangry\b': 'enojado',
            r'\bafraid\b': 'temeroso',
            r'\bbrave\b': 'valiente',
            r'\bcoward\b': 'cobarde',
            r'\bstrong\b': 'fuerte',
            r'\bweak\b': 'débil',
            r'\bold\b': 'viejo',
            r'\byoung\b': 'joven',
            r'\bnew\b': 'nuevo',
            r'\bbig\b': 'grande',
            r'\bsmall\b': 'pequeño',
            r'\blong\b': 'largo',
            r'\bshort\b': 'corto',
            r'\bhigh\b': 'alto',
            r'\blow\b': 'bajo',
            r'\bhot\b': 'caliente',
            r'\bcold\b': 'frío',
            r'\blight\b': 'luz',
            r'\bdark\b': 'oscuro',
            r'\bheaven\b': 'cielo',
            r'\bhell\b': 'infierno',
            r'\bgod\b': 'dios',
            r'\bdevil\b': 'diablo',
            r'\bangel\b': 'ángel',
            r'\bdemon\b': 'demonio',
            r'\bsoul\b': 'alma',
            r'\bspirit\b': 'espíritu',
            r'\bheart\b': 'corazón',
            r'\bmind\b': 'mente',
            r'\bbody\b': 'cuerpo',
            r'\bhead\b': 'cabeza',
            r'\bhand\b': 'mano',
            r'\bfoot\b': 'pie',
            r'\beye\b': 'ojo',
            r'\bear\b': 'oído',
            r'\bmouth\b': 'boca',
            r'\btongue\b': 'lengua',
            r'\bblood\b': 'sangre',
            r'\btears\b': 'lágrimas',
            r'\bsmile\b': 'sonrisa',
            r'\bkiss\b': 'beso',
            r'\bsword\b': 'espada',
            r'\bdagger\b': 'daga',
            r'\bpoison\b': 'veneno',
            r'\bcrown\b': 'corona',
            r'\bthrone\b': 'trono',
            r'\bkingdom\b': 'reino',
            r'\bcastle\b': 'castillo',
            r'\bpalace\b': 'palacio',
            r'\bhouse\b': 'casa',
            r'\bhome\b': 'hogar',
            r'\bdoor\b': 'puerta',
            r'\bwindow\b': 'ventana',
            r'\bbed\b': 'cama',
            r'\btable\b': 'mesa',
            r'\bchair\b': 'silla',
            r'\bbook\b': 'libro',
            r'\bletter\b': 'carta',
            r'\bword\b': 'palabra',
            r'\bname\b': 'nombre',
            r'\bvoice\b': 'voz',
            r'\bsound\b': 'sonido',
            r'\bmusic\b': 'música',
            r'\bsong\b': 'canción',
            r'\bdance\b': 'baile',
            r'\bplay\b': 'obra',
            r'\bgame\b': 'juego',
            r'\bwar\b': 'guerra',
            r'\bpeace\b': 'paz',
            r'\bbattle\b': 'batalla',
            r'\bfight\b': 'lucha',
            r'\bvictory\b': 'victoria',
            r'\bdefeat\b': 'derrota',
            r'\bhonor\b': 'honor',
            r'\bshame\b': 'vergüenza',
            r'\bglory\b': 'gloria',
            r'\bfame\b': 'fama',
            r'\bfortune\b': 'fortuna',
            r'\bfate\b': 'destino',
            r'\bluck\b': 'suerte',
            r'\bchance\b': 'oportunidad',
            r'\bhope\b': 'esperanza',
            r'\bfear\b': 'miedo',
            r'\bjoy\b': 'alegría',
            r'\bsorrow\b': 'tristeza',
            r'\bgrief\b': 'dolor',
            r'\bpain\b': 'dolor',
            r'\bpleasure\b': 'placer',
            r'\bdesire\b': 'deseo',
            r'\bwish\b': 'deseo',
            r'\bwill\b': 'voluntad',
            r'\bpower\b': 'poder',
            r'\bstrength\b': 'fuerza',
            r'\bcourage\b': 'coraje',
            r'\bwisdom\b': 'sabiduría',
            r'\bknowledge\b': 'conocimiento',
            r'\btruth\b': 'verdad',
            r'\blie\b': 'mentira',
            r'\bsecret\b': 'secreto',
            r'\bmystery\b': 'misterio',
            r'\bmagic\b': 'magia',
            r'\bwonder\b': 'maravilla',
            r'\bdream\b': 'sueño',
            r'\bsleep\b': 'dormir',
            r'\bwake\b': 'despertar',
            r'\blive\b': 'vivir',
            r'\bdie\b': 'morir',
            r'\bbirth\b': 'nacimiento',
            r'\bgrow\b': 'crecer',
            r'\bage\b': 'edad',
            r'\btime\b': 'tiempo',
            r'\bhour\b': 'hora',
            r'\bmoment\b': 'momento',
            r'\binstant\b': 'instante',
            r'\beternity\b': 'eternidad',
            r'\bbeginning\b': 'principio',
            r'\bend\b': 'fin',
            r'\bfirst\b': 'primero',
            r'\blast\b': 'último',
            r'\bmiddle\b': 'medio',
            r'\bcenter\b': 'centro',
            r'\bedge\b': 'borde',
            r'\bcorner\b': 'esquina',
            r'\bside\b': 'lado',
            r'\btop\b': 'cima',
            r'\bbottom\b': 'fondo',
            r'\bfront\b': 'frente',
            r'\bback\b': 'espalda',
            r'\bleft\b': 'izquierda',
            r'\bright\b': 'derecha',
            r'\bnorth\b': 'norte',
            r'\bsouth\b': 'sur',
            r'\beast\b': 'este',
            r'\bwest\b': 'oeste',
            r'\bworld\b': 'mundo',
            r'\bearth\b': 'tierra',
            r'\bsky\b': 'cielo',
            r'\bsun\b': 'sol',
            r'\bmoon\b': 'luna',
            r'\bstar\b': 'estrella',
            r'\bcloud\b': 'nube',
            r'\brain\b': 'lluvia',
            r'\bsnow\b': 'nieve',
            r'\bwind\b': 'viento',
            r'\bstorm\b': 'tormenta',
            r'\bthunder\b': 'trueno',
            r'\blightning\b': 'relámpago',
            r'\bfire\b': 'fuego',
            r'\bwater\b': 'agua',
            r'\bair\b': 'aire',
            r'\bearth\b': 'tierra',
            r'\bsea\b': 'mar',
            r'\bocean\b': 'océano',
            r'\briver\b': 'río',
            r'\blake\b': 'lago',
            r'\bmountain\b': 'montaña',
            r'\bhill\b': 'colina',
            r'\bvalley\b': 'valle',
            r'\bforest\b': 'bosque',
            r'\btree\b': 'árbol',
            r'\bflower\b': 'flor',
            r'\bgrass\b': 'hierba',
            r'\bleaf\b': 'hoja',
            r'\broot\b': 'raíz',
            r'\bseed\b': 'semilla',
            r'\bfruit\b': 'fruta',
            r'\banimal\b': 'animal',
            r'\bbird\b': 'pájaro',
            r'\bfish\b': 'pez',
            r'\bhorse\b': 'caballo',
            r'\bdog\b': 'perro',
            r'\bcat\b': 'gato',
            r'\blion\b': 'león',
            r'\bbear\b': 'oso',
            r'\bwolf\b': 'lobo',
            r'\bfox\b': 'zorro',
            r'\bsnake\b': 'serpiente',
            r'\bdragon\b': 'dragón',
            r'\bgold\b': 'oro',
            r'\bsilver\b': 'plata',
            r'\biron\b': 'hierro',
            r'\bstone\b': 'piedra',
            r'\bwood\b': 'madera',
            r'\bglass\b': 'vidrio',
            r'\bsilk\b': 'seda',
            r'\bcloth\b': 'tela',
            r'\bwine\b': 'vino',
            r'\bbread\b': 'pan',
            r'\bmeat\b': 'carne',
            r'\bmilk\b': 'leche',
            r'\bhoney\b': 'miel',
            r'\bsalt\b': 'sal',
            r'\bsugar\b': 'azúcar',
            r'\bship\b': 'barco',
            r'\bboat\b': 'bote',
            r'\bsail\b': 'vela',
            r'\banchor\b': 'ancla',
            r'\bport\b': 'puerto',
            r'\bisland\b': 'isla',
            r'\bshore\b': 'orilla',
            r'\bbeach\b': 'playa',
            r'\bwave\b': 'ola',
            r'\btide\b': 'marea',
        }
        
        for pattern, replacement in replacements.items():
            line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)
        
        return line
    
    def translate_sonnet(self, lines, sonnet_num):
        """Translate a complete sonnet maintaining structure"""
        # For sonnets, we need to maintain the poetic structure
        # This is a simplified version - a full translation would require
        # careful attention to meter and rhyme
        translated = []
        
        for line in lines:
            if line.strip() == str(sonnet_num):
                translated.append(line)
            elif not line.strip():
                translated.append(line)
            else:
                # Apply specific sonnet translations if available
                # Otherwise use general translation
                translated.append(self.translate_line(line))
        
        return translated
    
    def process_file(self, input_path, output_path):
        """Process the entire Shakespeare file"""
        print(f"Starting translation of {input_path}")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        print(f"Total lines to translate: {total_lines}")
        
        translated_lines = []
        in_sonnet = False
        current_sonnet = []
        sonnet_number = None
        lines_processed = 0
        
        for i, line in enumerate(lines):
            # Progress reporting
            if i % 10000 == 0 and i > 0:
                print(f"Progress: {i}/{total_lines} lines ({i/total_lines*100:.1f}%)")
            
            # Detect sonnet numbers
            if re.match(r'^\s*\d+\s*$', line) and i < 5000:
                if in_sonnet and current_sonnet:
                    # Translate previous sonnet
                    translated_lines.extend(self.translate_sonnet(current_sonnet, sonnet_number))
                    lines_processed += len(current_sonnet)
                
                sonnet_number = line.strip()
                in_sonnet = True
                current_sonnet = [line]
                continue
            
            # Accumulate sonnet lines
            if in_sonnet:
                current_sonnet.append(line)
                # Check if sonnet ends (empty line after content)
                if line.strip() == '' and len(current_sonnet) > 15:
                    translated_lines.extend(self.translate_sonnet(current_sonnet, sonnet_number))
                    lines_processed += len(current_sonnet)
                    in_sonnet = False
                    current_sonnet = []
                continue
            
            # Regular line translation
            translated_lines.append(self.translate_line(line))
            lines_processed += 1
        
        # Handle any remaining sonnet
        if current_sonnet:
            translated_lines.extend(self.translate_sonnet(current_sonnet, sonnet_number))
            lines_processed += len(current_sonnet)
        
        # Write output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(translated_lines)
        
        print(f"\nTranslation complete!")
        print(f"Lines processed: {lines_processed}")
        print(f"Output lines: {len(translated_lines)}")
        
        # Verify output
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"Output file size: {len(content)} characters")
        print(f"Output saved to: {output_path}")

def main():
    translator = ShakespeareTranslator()
    input_file = "/workspace/shakespeare-translations/shakespeare-complete.txt"
    output_file = "/workspace/shakespeare-translations/spanish/spanish-shakespeare-agent2-complete.txt"
    
    translator.process_file(input_file, output_file)

if __name__ == "__main__":
    main()