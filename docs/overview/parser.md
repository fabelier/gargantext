# HOW TO: Reference a new webscrapper/API + parser

## Global scope
Three main mooves to do:
- develop and index parser
in gargantext.util.parsers
- developp and index a scrapper
in gargantext.moissonneurs

- adapt forms for a new source
in templates and views

## Reference parser into gargantext website
gargantext website is stored in gargantext/gargantext

### reference your new parser into contants.py
* import your parser l.125
```
from gargantext.util.parsers import \
    EuropressParser, RISParser, PubmedParser, ISIParser, CSVParser, ISTexParser, CernParser
```
The parser corresponds to the name of the parser referenced in gargantext/util/parser
here  name is CernParser


* index your RESOURCETYPE
int RESOURCETYPES (l.145) **at the end of the list**
```
# type 10
   {    "name": 'SCOAP (XML MARC21 Format)',
        "parser": CernParser,
        "default_language": "en",
        'accepted_formats':["zip","xml"],
   },
```
    A noter le nom ici est composé de l'API_name(SCOAP) + (GENERICFILETYPE FORMAT_XML Format)
    La complexité du nommage correspond à trois choses:
        * le nom de l'API (different de l'organisme de production)
        * le type de format: XML
        * la norme XML de ce format : MARC21 (cf. CernParser in gargantext/util/parser/Cern.py )

The default_langage corresponds to the default accepted lang that **should load** the default corresponding tagger


```
from gargantext.util.taggers import NltkTagger
```
    TO DO: charger à la demander les types de taggers en fonction des langues et de l'install
    TO DO: proposer un module pour télécharger des parsers supplémentaires
    TO DO: provide install tagger module scripts inside lib

Les formats correspondent aux types de fichiers acceptées lors de l'envoi du fichier dans le formulaire de
parsing disponible dans `gargantext/view/pages/projects.py` et
exposé dans `/templates/pages/projects/project.html`

## reference your parser script

## add your parser script into folder gargantext/util/parser/
here my filename was Cern.py

##declare it into gargantext/util/parser/__init__.py
from .Cern  import CernParser

At this step, you will be able to see your parser and add a file with the form
but nothing will occur

## the good way to write the scrapper script

Three main and only requirements:
* your parser class should inherit from the base class _Parser()
`gargantext/gargantext/util/parser/_Parser`
* your parser class must have a parse method that take a **file buffer** as input
* you parser must structure and store data into **hyperdata_list** variable name
to be properly indexed by toolchain
! Be careful of date format: provide a publication_date in  a string format YYYY-mm-dd HH:MM:SS

# Adding a scrapper API to offer search option:
En cours
* Add pop up question Do you have a corpus
option search in /templates/pages/projects/project.html line 181


## Reference a scrapper (moissonneur) into gargantext

* adding accepted_formats in constants
* adding check_file routine in Form check ==> but should inherit from utils/files.py
that also have implmented the size upload limit check

# Suggestion 4 next steps:
* XML parser MARC21 UNIMARC ...
* A project type is qualified by the first element add i.e:
the first element determine the type of corpus of all the corpora within the project

