from .FileParsers import *

parsers = {
        'Pubmed (xml format)'               : PubmedFileParser,
        'Web of Science (ISI format)'       : IsiFileParser,
        'Scopus (RIS format)'               : RisFileParser,
        'Zotero (RIS format)'               : ZoteroFileParser,
        'Jstor (RIS format)'                : JstorFileParser,
        #'Europress'                        : EuropressFileParser,
        'Europress (French)'                : EuropressFileParser,
        'Europress (English)'               : EuropressFileParser,
        'CSVParser'                         : CSVParser,
        'ISTex'                             : ISTex,
    }

