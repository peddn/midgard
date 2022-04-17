from enum import Enum

class Case(Enum):
    NOM = "Nominativ"
    DAT = "Dativ"
    AKK = "Akkusativ"
    GEN = "Genitiv"


class Gender(Enum):
    MASKULIN = "Maskulin"
    FEMININ  = "Feminin"
    NEUTRUM  = "Neutrum"



def get_def_art(obj, case):
    if(obj.db.gender is Gender.MASKULIN):
        if(case is Case.NOM):
            return "der" 
        if(case is Case.DAT):
            return "dem"
        if(case is Case.AKK):
            return "den"
        if(case is Case.GEN):
            return "des"
    if(obj.db.gender is Gender.FEMININ):
        if(case is Case.NOM):
            return "die"
        if(case is Case.DAT):
            return "der"
        if(case is Case.AKK):
            return "die"
        if(case is Case.GEN):
            return "der"
    if(obj.db.gender is Gender.NEUTRUM):
        if(case is Case.NOM):
            return "das"
        if(case is Case.DAT):
            return "dem"
        if(case is Case.AKK):
            return "das"
        if(case is Case.GEN):
            return "des"
    else:
        return "[def_art]"