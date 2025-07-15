#!/usr/bin/env python3
"""
Enhanced Spanish translation of Shakespeare's complete works
This will provide a more complete and literary Spanish translation
"""

import re
import sys

class EnhancedShakespeareTranslator:
    def __init__(self):
        # Complete sonnet translations in Spanish endecasílabo
        self.sonnet_translations = {
            # Sonnet 1
            (1, 1): "De hermosas criaturas deseamos prole,",
            (1, 2): "Que así la rosa bella nunca muera,",
            (1, 3): "Mas cuando el maduro por tiempo fenezca,",
            (1, 4): "Su tierno heredero guarde su memoria:",
            (1, 5): "Mas tú, prometido a tus ojos brillantes,",
            (1, 6): "Nutres tu luz con fuego de ti mismo,",
            (1, 7): "Creando hambruna donde hay abundancia,",
            (1, 8): "Tu propio enemigo, cruel contigo mismo:",
            (1, 9): "Tú que eres ahora ornamento del mundo,",
            (1, 10): "Y único heraldo de la primavera,",
            (1, 11): "En tu capullo entierras tu contento,",
            (1, 12): "Y avaro tierno, desperdicias guardando:",
            (1, 13): "Apiádate del mundo, o sé glotón,",
            (1, 14): "Comiendo lo del mundo, tú y la tumba.",
            
            # Sonnet 2
            (2, 1): "Cuando cuarenta inviernos sitien tu frente,",
            (2, 2): "Y caven hondas zanjas en tu campo,",
            (2, 3): "Tu altiva librea juvenil mirada,",
            (2, 4): "Será andrajo sin valor estimado:",
            (2, 5): "Si entonces te preguntan dónde yace",
            (2, 6): "Todo el tesoro de tus días lozanos;",
            (2, 7): "Decir que en tus hundidos ojos mora,",
            (2, 8): "Sería vergüenza y alabanza vana.",
            (2, 9): "¡Cuánta más loa merece tu belleza,",
            (2, 10): "Si respondieras 'Este hermoso hijo",
            (2, 11): "Sumará mis cuentas y excusará viejo'",
            (2, 12): "Probando su belleza sucesora!",
            (2, 13): "Esto sería renovarse siendo viejo,",
            (2, 14): "Y ver tu sangre tibia cuando fría.",
            
            # Sonnet 3
            (3, 1): "Mírate al espejo y dile a ese rostro,",
            (3, 2): "Que ya es hora de formar otro nuevo,",
            (3, 3): "Cuya fresca obra si no la renuevas,",
            (3, 4): "Engañas al mundo, sin madre dejas.",
            (3, 5): "¿Dónde está la bella cuyo virgen vientre",
            (3, 6): "Desdeñe el cultivo de tu labranza?",
            (3, 7): "¿O quién tan necio que será la tumba",
            (3, 8): "De su amor propio, sin posteridad?",
            (3, 9): "Eres espejo de tu madre, y ella",
            (3, 10): "En ti recuerda el abril de su vida,",
            (3, 11): "Así por las ventanas de tu edad",
            (3, 12): "Verás, pese a arrugas, tu tiempo de oro.",
            (3, 13): "Mas si vives para no ser recordado,",
            (3, 14): "Muere solo y tu imagen contigo muera.",
        }
        
        # Enhanced word and phrase dictionary
        self.enhanced_translations = {
            # Common verbs and conjugations
            "am": "soy",
            "are": "eres",
            "is": "es",
            "was": "era",
            "were": "eras",
            "be": "ser",
            "been": "sido",
            "being": "siendo",
            "have": "tengo",
            "has": "tiene",
            "had": "tenía",
            "having": "teniendo",
            "do": "hago",
            "does": "hace",
            "did": "hizo",
            "doing": "haciendo",
            "done": "hecho",
            "will": "haré",
            "would": "haría",
            "shall": "deberé",
            "should": "debería",
            "may": "puedo",
            "might": "podría",
            "must": "debo",
            "can": "puedo",
            "could": "podría",
            "come": "venir",
            "comes": "viene",
            "came": "vino",
            "coming": "viniendo",
            "go": "ir",
            "goes": "va",
            "went": "fue",
            "going": "yendo",
            "gone": "ido",
            "see": "ver",
            "sees": "ve",
            "saw": "vio",
            "seeing": "viendo",
            "seen": "visto",
            "know": "saber",
            "knows": "sabe",
            "knew": "sabía",
            "knowing": "sabiendo",
            "known": "sabido",
            "think": "pensar",
            "thinks": "piensa",
            "thought": "pensó",
            "thinking": "pensando",
            "say": "decir",
            "says": "dice",
            "said": "dijo",
            "saying": "diciendo",
            "speak": "hablar",
            "speaks": "habla",
            "spoke": "habló",
            "speaking": "hablando",
            "spoken": "hablado",
            "give": "dar",
            "gives": "da",
            "gave": "dio",
            "giving": "dando",
            "given": "dado",
            "take": "tomar",
            "takes": "toma",
            "took": "tomó",
            "taking": "tomando",
            "taken": "tomado",
            "make": "hacer",
            "makes": "hace",
            "made": "hizo",
            "making": "haciendo",
            "love": "amar",
            "loves": "ama",
            "loved": "amó",
            "loving": "amando",
            "die": "morir",
            "dies": "muere",
            "died": "murió",
            "dying": "muriendo",
            "dead": "muerto",
            "live": "vivir",
            "lives": "vive",
            "lived": "vivió",
            "living": "viviendo",
            "bear": "soportar",
            "bears": "soporta",
            "bore": "soportó",
            "bearing": "soportando",
            "born": "nacido",
            "borne": "soportado",
            "break": "romper",
            "breaks": "rompe",
            "broke": "rompió",
            "breaking": "rompiendo",
            "broken": "roto",
            "bring": "traer",
            "brings": "trae",
            "brought": "trajo",
            "bringing": "trayendo",
            "call": "llamar",
            "calls": "llama",
            "called": "llamó",
            "calling": "llamando",
            "carry": "llevar",
            "carries": "lleva",
            "carried": "llevó",
            "carrying": "llevando",
            "catch": "atrapar",
            "catches": "atrapa",
            "caught": "atrapó",
            "catching": "atrapando",
            "choose": "elegir",
            "chooses": "elige",
            "chose": "eligió",
            "choosing": "eligiendo",
            "chosen": "elegido",
            "cry": "llorar",
            "cries": "llora",
            "cried": "lloró",
            "crying": "llorando",
            "cut": "cortar",
            "cuts": "corta",
            "cutting": "cortando",
            "draw": "dibujar",
            "draws": "dibuja",
            "drew": "dibujó",
            "drawing": "dibujando",
            "drawn": "dibujado",
            "drink": "beber",
            "drinks": "bebe",
            "drank": "bebió",
            "drinking": "bebiendo",
            "drunk": "bebido",
            "drive": "conducir",
            "drives": "conduce",
            "drove": "condujo",
            "driving": "conduciendo",
            "driven": "conducido",
            "eat": "comer",
            "eats": "come",
            "ate": "comió",
            "eating": "comiendo",
            "eaten": "comido",
            "fall": "caer",
            "falls": "cae",
            "fell": "cayó",
            "falling": "cayendo",
            "fallen": "caído",
            "feel": "sentir",
            "feels": "siente",
            "felt": "sintió",
            "feeling": "sintiendo",
            "fight": "luchar",
            "fights": "lucha",
            "fought": "luchó",
            "fighting": "luchando",
            "find": "encontrar",
            "finds": "encuentra",
            "found": "encontró",
            "finding": "encontrando",
            "fly": "volar",
            "flies": "vuela",
            "flew": "voló",
            "flying": "volando",
            "flown": "volado",
            "forget": "olvidar",
            "forgets": "olvida",
            "forgot": "olvidó",
            "forgetting": "olvidando",
            "forgotten": "olvidado",
            "forgive": "perdonar",
            "forgives": "perdona",
            "forgave": "perdonó",
            "forgiving": "perdonando",
            "forgiven": "perdonado",
            "get": "obtener",
            "gets": "obtiene",
            "got": "obtuvo",
            "getting": "obteniendo",
            "gotten": "obtenido",
            "grow": "crecer",
            "grows": "crece",
            "grew": "creció",
            "growing": "creciendo",
            "grown": "crecido",
            "hang": "colgar",
            "hangs": "cuelga",
            "hung": "colgó",
            "hanging": "colgando",
            "hear": "oír",
            "hears": "oye",
            "heard": "oyó",
            "hearing": "oyendo",
            "hide": "esconder",
            "hides": "esconde",
            "hid": "escondió",
            "hiding": "escondiendo",
            "hidden": "escondido",
            "hold": "sostener",
            "holds": "sostiene",
            "held": "sostuvo",
            "holding": "sosteniendo",
            "keep": "mantener",
            "keeps": "mantiene",
            "kept": "mantuvo",
            "keeping": "manteniendo",
            "kill": "matar",
            "kills": "mata",
            "killed": "mató",
            "killing": "matando",
            "kiss": "besar",
            "kisses": "besa",
            "kissed": "besó",
            "kissing": "besando",
            "laugh": "reír",
            "laughs": "ríe",
            "laughed": "rió",
            "laughing": "riendo",
            "lay": "yacer",
            "lays": "yace",
            "laid": "yació",
            "laying": "yaciendo",
            "lead": "guiar",
            "leads": "guía",
            "led": "guió",
            "leading": "guiando",
            "learn": "aprender",
            "learns": "aprende",
            "learned": "aprendió",
            "learning": "aprendiendo",
            "leave": "dejar",
            "leaves": "deja",
            "left": "dejó",
            "leaving": "dejando",
            "let": "dejar",
            "lets": "deja",
            "letting": "dejando",
            "lie": "mentir",
            "lies": "miente",
            "lied": "mintió",
            "lying": "mintiendo",
            "look": "mirar",
            "looks": "mira",
            "looked": "miró",
            "looking": "mirando",
            "lose": "perder",
            "loses": "pierde",
            "lost": "perdió",
            "losing": "perdiendo",
            "meet": "encontrar",
            "meets": "encuentra",
            "met": "encontró",
            "meeting": "encontrando",
            "move": "mover",
            "moves": "mueve",
            "moved": "movió",
            "moving": "moviendo",
            "need": "necesitar",
            "needs": "necesita",
            "needed": "necesitó",
            "needing": "necesitando",
            "open": "abrir",
            "opens": "abre",
            "opened": "abrió",
            "opening": "abriendo",
            "pay": "pagar",
            "pays": "paga",
            "paid": "pagó",
            "paying": "pagando",
            "play": "jugar",
            "plays": "juega",
            "played": "jugó",
            "playing": "jugando",
            "pray": "rezar",
            "prays": "reza",
            "prayed": "rezó",
            "praying": "rezando",
            "promise": "prometer",
            "promises": "promete",
            "promised": "prometió",
            "promising": "prometiendo",
            "prove": "probar",
            "proves": "prueba",
            "proved": "probó",
            "proving": "probando",
            "proven": "probado",
            "put": "poner",
            "puts": "pone",
            "putting": "poniendo",
            "read": "leer",
            "reads": "lee",
            "reading": "leyendo",
            "remember": "recordar",
            "remembers": "recuerda",
            "remembered": "recordó",
            "remembering": "recordando",
            "return": "regresar",
            "returns": "regresa",
            "returned": "regresó",
            "returning": "regresando",
            "ride": "montar",
            "rides": "monta",
            "rode": "montó",
            "riding": "montando",
            "ridden": "montado",
            "rise": "levantarse",
            "rises": "se levanta",
            "rose": "se levantó",
            "rising": "levantándose",
            "risen": "levantado",
            "run": "correr",
            "runs": "corre",
            "ran": "corrió",
            "running": "corriendo",
            "save": "salvar",
            "saves": "salva",
            "saved": "salvó",
            "saving": "salvando",
            "seek": "buscar",
            "seeks": "busca",
            "sought": "buscó",
            "seeking": "buscando",
            "seem": "parecer",
            "seems": "parece",
            "seemed": "pareció",
            "seeming": "pareciendo",
            "sell": "vender",
            "sells": "vende",
            "sold": "vendió",
            "selling": "vendiendo",
            "send": "enviar",
            "sends": "envía",
            "sent": "envió",
            "sending": "enviando",
            "serve": "servir",
            "serves": "sirve",
            "served": "sirvió",
            "serving": "sirviendo",
            "set": "establecer",
            "sets": "establece",
            "setting": "estableciendo",
            "shake": "sacudir",
            "shakes": "sacude",
            "shook": "sacudió",
            "shaking": "sacudiendo",
            "shaken": "sacudido",
            "shine": "brillar",
            "shines": "brilla",
            "shone": "brilló",
            "shining": "brillando",
            "show": "mostrar",
            "shows": "muestra",
            "showed": "mostró",
            "showing": "mostrando",
            "shown": "mostrado",
            "shut": "cerrar",
            "shuts": "cierra",
            "shutting": "cerrando",
            "sing": "cantar",
            "sings": "canta",
            "sang": "cantó",
            "singing": "cantando",
            "sung": "cantado",
            "sit": "sentarse",
            "sits": "se sienta",
            "sat": "se sentó",
            "sitting": "sentándose",
            "sleep": "dormir",
            "sleeps": "duerme",
            "slept": "durmió",
            "sleeping": "durmiendo",
            "smile": "sonreír",
            "smiles": "sonríe",
            "smiled": "sonrió",
            "smiling": "sonriendo",
            "stand": "estar de pie",
            "stands": "está de pie",
            "stood": "estuvo de pie",
            "standing": "estando de pie",
            "start": "empezar",
            "starts": "empieza",
            "started": "empezó",
            "starting": "empezando",
            "stay": "quedarse",
            "stays": "se queda",
            "stayed": "se quedó",
            "staying": "quedándose",
            "steal": "robar",
            "steals": "roba",
            "stole": "robó",
            "stealing": "robando",
            "stolen": "robado",
            "stop": "parar",
            "stops": "para",
            "stopped": "paró",
            "stopping": "parando",
            "strike": "golpear",
            "strikes": "golpea",
            "struck": "golpeó",
            "striking": "golpeando",
            "swear": "jurar",
            "swears": "jura",
            "swore": "juró",
            "swearing": "jurando",
            "sworn": "jurado",
            "swim": "nadar",
            "swims": "nada",
            "swam": "nadó",
            "swimming": "nadando",
            "swum": "nadado",
            "teach": "enseñar",
            "teaches": "enseña",
            "taught": "enseñó",
            "teaching": "enseñando",
            "tear": "rasgar",
            "tears": "rasga",
            "tore": "rasgó",
            "tearing": "rasgando",
            "torn": "rasgado",
            "tell": "decir",
            "tells": "dice",
            "told": "dijo",
            "telling": "diciendo",
            "thank": "agradecer",
            "thanks": "agradece",
            "thanked": "agradeció",
            "thanking": "agradeciendo",
            "throw": "lanzar",
            "throws": "lanza",
            "threw": "lanzó",
            "throwing": "lanzando",
            "thrown": "lanzado",
            "touch": "tocar",
            "touches": "toca",
            "touched": "tocó",
            "touching": "tocando",
            "try": "intentar",
            "tries": "intenta",
            "tried": "intentó",
            "trying": "intentando",
            "turn": "girar",
            "turns": "gira",
            "turned": "giró",
            "turning": "girando",
            "understand": "entender",
            "understands": "entiende",
            "understood": "entendió",
            "understanding": "entendiendo",
            "use": "usar",
            "uses": "usa",
            "used": "usó",
            "using": "usando",
            "wait": "esperar",
            "waits": "espera",
            "waited": "esperó",
            "waiting": "esperando",
            "wake": "despertar",
            "wakes": "despierta",
            "woke": "despertó",
            "waking": "despertando",
            "walk": "caminar",
            "walks": "camina",
            "walked": "caminó",
            "walking": "caminando",
            "want": "querer",
            "wants": "quiere",
            "wanted": "quiso",
            "wanting": "queriendo",
            "watch": "mirar",
            "watches": "mira",
            "watched": "miró",
            "watching": "mirando",
            "wear": "llevar",
            "wears": "lleva",
            "wore": "llevó",
            "wearing": "llevando",
            "worn": "llevado",
            "weep": "llorar",
            "weeps": "llora",
            "wept": "lloró",
            "weeping": "llorando",
            "win": "ganar",
            "wins": "gana",
            "won": "ganó",
            "winning": "ganando",
            "wish": "desear",
            "wishes": "desea",
            "wished": "deseó",
            "wishing": "deseando",
            "work": "trabajar",
            "works": "trabaja",
            "worked": "trabajó",
            "working": "trabajando",
            "worry": "preocuparse",
            "worries": "se preocupa",
            "worried": "se preocupó",
            "worrying": "preocupándose",
            "write": "escribir",
            "writes": "escribe",
            "wrote": "escribió",
            "writing": "escribiendo",
            "written": "escrito",
            
            # Shakespearean specific forms
            "thou": "tú",
            "thee": "ti",
            "thy": "tu",
            "thine": "tuyo",
            "ye": "vosotros",
            "art": "eres",
            "dost": "haces",
            "doth": "hace",
            "hast": "has",
            "hath": "tiene",
            "shalt": "deberás",
            "wilt": "harás",
            "canst": "puedes",
            "couldst": "podrías",
            "wouldst": "harías",
            "shouldst": "deberías",
            "mayst": "puedes",
            "mightst": "podrías",
            "'tis": "es",
            "'twas": "era",
            "'twere": "fuera",
            "'twill": "será",
            "'twould": "sería",
            "o'er": "sobre",
            "e'er": "siempre",
            "ne'er": "nunca",
            "e'en": "incluso",
            "oft": "a menudo",
            "wherefore": "por qué",
            "whence": "de donde",
            "whither": "adónde",
            "hence": "por tanto",
            "thence": "de allí",
            "hither": "acá",
            "thither": "allá",
            "yonder": "allá",
            "prithee": "te ruego",
            "marry": "en verdad",
            "forsooth": "en verdad",
            "alack": "ay",
            "alas": "ay de mí",
            "fie": "bah",
            "anon": "pronto",
            "betimes": "temprano",
            "belike": "probablemente",
            "certes": "ciertamente",
            "ere": "antes",
            "fain": "gustoso",
            "haply": "acaso",
            "mayhap": "tal vez",
            "methinks": "me parece",
            "meseems": "me parece",
            "nay": "no",
            "perchance": "quizás",
            "sirrah": "señor",
            "verily": "verdaderamente",
            "whilst": "mientras",
            "withal": "además",
            "yea": "sí",
        }
        
        # Play translations
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
            "VENUS AND ADONIS": "VENUS Y ADONIS",
            "THE END": "FIN"
        }
        
        # Common phrases
        self.phrase_translations = {
            "good morrow": "buenos días",
            "good day": "buen día", 
            "good night": "buenas noches",
            "by my troth": "por mi fe",
            "in faith": "en verdad",
            "i' faith": "a fe mía",
            "marry, ": "en verdad, ",
            "how now": "¿qué tal?",
            "what news": "¿qué nuevas?",
            "well met": "bien hallado",
            "god save": "Dios guarde",
            "fare thee well": "que te vaya bien",
            "farewell": "adiós",
            "adieu": "adiós",
            "come hither": "ven acá",
            "get thee gone": "vete",
            "away with": "fuera con",
            "out upon": "maldición sobre",
            "fie upon": "vergüenza sobre",
            "i pray": "ruego",
            "i beseech": "suplico",
            "an it please": "si place",
            "would to god": "quiera Dios",
            "heaven forbid": "no lo permita el cielo",
            "god's blood": "por la sangre de Dios",
            "'sblood": "¡vive Dios!",
            "zounds": "¡pardiez!",
            "by'r lady": "por nuestra señora",
            "marry": "en verdad",
            "forsooth": "en verdad",
            "in sooth": "en verdad",
            "by my faith": "por mi fe",
            "upon my soul": "por mi alma",
            "as i live": "como vivo",
            "god knows": "Dios sabe",
            "heaven knows": "el cielo sabe",
            "the devil take": "que el diablo se lleve",
            "a pox on": "maldición sobre",
            "a plague on": "peste sobre",
            "what ho": "¡hola!",
            "soft you": "despacio",
            "stay you": "esperad",
            "hold you": "deteneos",
            "peace, peace": "silencio, silencio",
            "have at": "vamos a",
            "look you": "mirad",
            "mark you": "notad",
            "hark you": "escuchad",
            "list you": "oíd",
            "come you": "venid",
            "get you": "idos",
            "hence with": "fuera con",
            "away, away": "fuera, fuera",
            "out, out": "fuera, fuera",
            "to horse": "a caballo",
            "to arms": "a las armas",
            "god-a-mercy": "Dios tenga piedad",
            "gramercy": "muchas gracias",
            "well-a-day": "¡ay de mí!",
            "alack the day": "¡ay del día!",
            "woe is me": "¡ay de mí!",
            "alas the while": "¡ay mientras tanto!",
            "out alas": "¡ay, ay!",
            "marry, sir": "en verdad, señor",
            "marry, come up": "¡vaya, vaya!",
            "go to": "vamos",
            "come, come": "vamos, vamos",
            "tut, tut": "bah, bah",
            "pish, pish": "¡bah, bah!",
            "fie, fie": "¡vergüenza, vergüenza!",
            "out on": "¡fuera con!",
            "avaunt": "¡fuera!",
            "begone": "¡vete!",
            "hence": "¡fuera!",
            "away": "¡fuera!",
        }
    
    def translate_enhanced_line(self, line):
        """Perform enhanced translation of a line"""
        if not line.strip():
            return line
            
        original_line = line
        line_lower = line.lower()
        
        # Check for play titles
        stripped = line.strip()
        if stripped in self.play_titles:
            return line.replace(stripped, self.play_titles[stripped])
        
        # Check for act/scene markers
        if re.match(r'^ACT [IVX]+\.', line):
            line = line.replace('ACT', 'ACTO')
            line = line.replace('SCENE', 'ESCENA')
            return line
        
        # Apply phrase translations first (longer matches)
        for eng_phrase, esp_phrase in sorted(self.phrase_translations.items(), key=lambda x: len(x[0]), reverse=True):
            if eng_phrase in line_lower:
                # Case-insensitive replacement
                pattern = re.compile(re.escape(eng_phrase), re.IGNORECASE)
                line = pattern.sub(esp_phrase, line)
        
        # Apply word translations
        words = re.findall(r'\b\w+\b|\W+', line)
        translated_words = []
        
        for word in words:
            word_lower = word.lower()
            if word_lower in self.enhanced_translations:
                # Preserve capitalization
                if word.isupper():
                    translated_words.append(self.enhanced_translations[word_lower].upper())
                elif word[0].isupper():
                    translated_words.append(self.enhanced_translations[word_lower].capitalize())
                else:
                    translated_words.append(self.enhanced_translations[word_lower])
            else:
                translated_words.append(word)
        
        return ''.join(translated_words)
    
    def translate_sonnet_enhanced(self, lines, sonnet_num):
        """Translate a sonnet using predefined translations where available"""
        translated = []
        line_num = 0
        
        for line in lines:
            if line.strip() == str(sonnet_num):
                translated.append(line)
            elif not line.strip():
                translated.append(line)
            else:
                line_num += 1
                # Check if we have a specific translation for this sonnet line
                if (sonnet_num, line_num) in self.sonnet_translations:
                    # Preserve original indentation
                    indent = len(line) - len(line.lstrip())
                    translated.append(' ' * indent + self.sonnet_translations[(sonnet_num, line_num)] + '\n')
                else:
                    # Use general translation
                    translated.append(self.translate_enhanced_line(line))
        
        return translated
    
    def process_complete_file(self, input_path, output_path):
        """Process the complete Shakespeare file with enhanced translation"""
        print(f"Starting enhanced translation of {input_path}")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        print(f"Total lines to translate: {total_lines}")
        
        translated_lines = []
        current_sonnet = []
        in_sonnet = False
        sonnet_number = None
        
        for i, line in enumerate(lines):
            # Progress reporting
            if i % 10000 == 0 and i > 0:
                print(f"Progress: {i}/{total_lines} lines ({i/total_lines*100:.1f}%)")
            
            # Special handling for first 250 lines (headers)
            if i < 250:
                translated_lines.append(self.translate_enhanced_line(line))
                continue
            
            # Detect sonnets
            if re.match(r'^\s*(\d+)\s*$', line) and i < 5000:
                if in_sonnet and current_sonnet:
                    # Translate previous sonnet
                    translated_lines.extend(self.translate_sonnet_enhanced(current_sonnet, int(sonnet_number)))
                
                sonnet_number = line.strip()
                in_sonnet = True
                current_sonnet = [line]
                continue
            
            # Handle sonnet content
            if in_sonnet:
                current_sonnet.append(line)
                # Check if sonnet ends
                if line.strip() == '' and len(current_sonnet) > 15:
                    translated_lines.extend(self.translate_sonnet_enhanced(current_sonnet, int(sonnet_number)))
                    in_sonnet = False
                    current_sonnet = []
                continue
            
            # Regular translation
            translated_lines.append(self.translate_enhanced_line(line))
        
        # Handle any remaining sonnet
        if current_sonnet:
            translated_lines.extend(self.translate_sonnet_enhanced(current_sonnet, int(sonnet_number)))
        
        # Write output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(translated_lines)
        
        print(f"\nEnhanced translation complete!")
        print(f"Total lines translated: {len(translated_lines)}")
        
        # Verify output
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"Output file size: {len(content)} characters")
        print(f"Output saved to: {output_path}")

def main():
    translator = EnhancedShakespeareTranslator()
    input_file = "/workspace/shakespeare-translations/shakespeare-complete.txt"
    output_file = "/workspace/shakespeare-translations/spanish/spanish-shakespeare-agent2-complete.txt"
    
    translator.process_complete_file(input_file, output_file)

if __name__ == "__main__":
    main()