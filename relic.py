from enum import Enum, auto

class RELIC_PIECE(Enum):
    HEAD = auto()
    HANDS = auto()
    BODY = auto()
    FEET = auto()
    SPHERE = auto()
    ROPE = auto()


class RELIC_STATS(Enum):
    HP = auto()
    ATK = auto()
    SPD = auto()
    DEF = auto()
    HP_P = auto()
    ATK_P = auto()
    DEF_P = auto()
    CRIT_RATE = auto()
    CRIT_DMG = auto()
    HEALING_BOOST = auto()
    EFFECT_HIT_RATE = auto()
    BREAK_EFFECT = auto()
    EFFECT_RES = auto()
    ENERGY_REGEN_RATE = auto()
    PHYSICAL_DMG_BOOST = auto()
    QUANTUM_DMG_BOOST = auto()
    IMAGINARY_DMG_BOOST = auto()
    FIRE_DMG_BOOST = auto()
    WIND_DMG_BOOST = auto()
    ICE_DMG_BOOST = auto()
    LIGHTNING_DMG_BOOST = auto()
    
    


class Relic:
    set_name = ""
    set_piece = ""
    language = ""
    main_stat_name = ""
    main_stat_value = ""

    sub_stat_1_name = ""
    sub_stat_2_name = ""
    sub_stat_3_name = ""
    sub_stat_4_name = ""

    sub_stat_1_value = ""
    sub_stat_2_value = ""
    sub_stat_3_value = ""
    sub_stat_4_value = ""
    
    def stat_rule_self_check(self):
        pass

    def to_csv_row(self):
        return [self.set_name, self.set_piece, self.main_stat_name, self.main_stat_value, self.sub_stat_1_name,self.sub_stat_1_value,self.sub_stat_2_name,self.sub_stat_2_value,self.sub_stat_3_name,self.sub_stat_3_value,self.sub_stat_4_name,self.sub_stat_4_value]