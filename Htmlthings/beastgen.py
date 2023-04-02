import sys
import math
import cgi, cgitb

def calcStats(level, species, iv_hp, iv_mp, iv_atk, iv_def, iv_matk, iv_mdef, iv_spd, ev_hp, ev_mp, ev_atk, ev_def, ev_matk, ev_mdef, ev_spd, temp_a, temp_b):
    evs = {"HP":ev_hp, "MP":ev_mp, "ATK":ev_atk, "DEF":ev_def, "MATK":ev_matk, "MDEF":ev_mdef, "SPD":ev_spd}
    ivs = {"HP": iv_hp, "MP":iv_mp, "ATK":iv_atk, "DEF":iv_def, "MATK":iv_matk, "MDEF": iv_mdef, "SPD":ev_spd}
    stats = {"HP":0, "MP":0, "ATK":0, "DEF":0, "MATK":0, "MDEF":0, "SPD":0}
    species_list = [{"name":"bolar","HP":40,"MP":28,"ATK":20,"DEF":40,"MATK":20,"MDEF":45,"SPD":10},
                    {"name":"bris","HP":25,"MP":35,"ATK":25,"DEF":30,"MATK":30,"MDEF":25,"SPD":35},
                    {"name":"bulboid","HP":36,"MP":26,"ATK":26,"DEF":30,"MATK":34,"MDEF":30,"SPD":30},
                    {"name":"buoybie","HP":36,"MP":28,"ATK":26,"DEF":30,"MATK":28,"MDEF":40,"SPD":18},
                    {"name":"buzzle","HP":32,"MP":25,"ATK":31,"DEF":33,"MATK":22,"MDEF":26,"SPD":34},
                    {"name":"cherrybud","HP":40,"MP":26,"ATK":36,"DEF":18,"MATK":36,"MDEF":18,"SPD":40},
                    {"name":"cumulus","HP":20,"MP":40,"ATK":15,"DEF":20,"MATK":42,"MDEF":50,"SPD":30},
                    {"name":"demianj","HP":30,"MP":30,"ATK":27,"DEF":28,"MATK":37,"MDEF":38,"SPD":20},
                    {"name":"dogrop","HP":30,"MP":30,"ATK":40,"DEF":25,"MATK":20,"MDEF":28,"SPD":28},
                    {"name":"druttle","HP":28,"MP":32,"ATK":30,"DEF":50,"MATK":20,"MDEF":20,"SPD":20},
                    {"name":"firefly","HP":33,"MP":27,"ATK":30,"DEF":23,"MATK":30,"MDEF":23,"SPD":50},
                    {"name":"greml","HP":30,"MP":30,"ATK":35,"DEF":28,"MATK":35,"MDEF":28,"SPD":30},
                    {"name":"grubb","HP":30,"MP":30,"ATK":31,"DEF":34,"MATK":28,"MDEF":30,"SPD":25},
                    {"name":"guppea","HP":30,"MP":30,"ATK":26,"DEF":28,"MATK":30,"MDEF":34,"SPD":32},
                    {"name":"henn","HP":22,"MP":16,"ATK":15,"DEF":20,"MATK":15,"MDEF":23,"SPD":30},
                    {"name":"hob","HP":40,"MP":20,"ATK":33,"DEF":27,"MATK":33,"MDEF":27,"SPD":30},
                    {"name":"inkus","HP":26,"MP":40,"ATK":15,"DEF":15,"MATK":55,"MDEF":35,"SPD":30},
                    {"name":"iosgrubb","HP":32,"MP":28,"ATK":36,"DEF":26,"MATK":22,"MDEF":30,"SPD":28},
                    {"name":"kee","HP":25,"MP":35,"ATK":36,"DEF":28,"MATK":28,"MDEF":28,"SPD":38},
                    {"name":"larva","HP":33,"MP":33,"ATK":33,"DEF":33,"MATK":33,"MDEF":33,"SPD":15},
                    {"name":"nagrop","HP":36,"MP":33,"ATK":35,"DEF":28,"MATK":35,"MDEF":22,"SPD":22},
                    {"name":"nullsprite","HP":30,"MP":30,"ATK":30,"DEF":30,"MATK":30,"MDEF":30,"SPD":30},
                    {"name":"omgull","HP":27,"MP":30,"ATK":30,"DEF":20,"MATK":20,"MDEF":35,"SPD":50},
                    {"name":"orly","HP":25,"MP":31,"ATK":35,"DEF":25,"MATK":25,"MDEF":30,"SPD":35},
                    {"name":"oskapo","HP":40,"MP":20,"ATK":30,"DEF":50,"MATK":10,"MDEF":35,"SPD":10},
                    {"name":"roglop","HP":32,"MP":28,"ATK":40,"DEF":20,"MATK":35,"MDEF":25,"SPD":30},
                    {"name":"sekil","HP":33,"MP":27,"ATK":33,"DEF":44,"MATK":26,"MDEF":20,"SPD":27},
                    {"name":"shufl","HP":34,"MP":30,"ATK":30,"DEF":20,"MATK":35,"MDEF":40,"SPD":22},
                    {"name":"sprighte","HP":22,"MP":46,"ATK":20,"DEF":20,"MATK":38,"MDEF":35,"SPD":35},
                    {"name":"sprite","HP":30,"MP":30,"ATK":30,"DEF":30,"MATK":30,"MDEF":30,"SPD":30},
                    {"name":"sputnik","HP":35,"MP":35,"ATK":20,"DEF":30,"MATK":40,"MDEF":40,"SPD":15},
                    {"name":"tricken","HP":22,"MP":16,"ATK":8,"DEF":25,"MATK":8,"MDEF":25,"SPD":30},
                    {"name":"ug","HP":44,"MP":16,"ATK":40,"DEF":36,"MATK":10,"MDEF":20,"SPD":26},
                    {"name":"woot","HP":30,"MP":30,"ATK":30,"DEF":28,"MATK":30,"MDEF":28,"SPD":36},
                    {"name":"yarly","HP":25,"MP":35,"ATK":25,"DEF":25,"MATK":35,"MDEF":35,"SPD":30},
                    {"name":"zeode","HP":30,"MP":30,"ATK":34,"DEF":26,"MATK":34,"MDEF":26,"SPD":30},
                    {"name":"9mmkiwi","HP":44,"MP":50,"ATK":63,"DEF":36,"MATK":30,"MDEF":40,"SPD":60},
                    {"name":"anj","HP":46,"MP":60,"ATK":34,"DEF":40,"MATK":65,"MDEF":70,"SPD":55},
                    {"name":"arkizard","HP":56,"MP":60,"ATK":63,"DEF":58,"MATK":52,"MDEF":59,"SPD":45},
                    {"name":"babawin","HP":50,"MP":50,"ATK":55,"DEF":48,"MATK":50,"MDEF":52,"SPD":54},
                    {"name":"bgeln","HP":60,"MP":42,"ATK":64,"DEF":64,"MATK":36,"MDEF":45,"SPD":45},
                    {"name":"birdrak","HP":54,"MP":40,"ATK":61,"DEF":38,"MATK":55,"MDEF":40,"SPD":65},
                    {"name":"bladebee","HP":44,"MP":40,"ATK":70,"DEF":30,"MATK":50,"MDEF":50,"SPD":70},
                    {"name":"brownstoat","HP":60,"MP":40,"ATK":55,"DEF":45,"MATK":40,"MDEF":44,"SPD":70},
                    {"name":"bunsurn","HP":55,"MP":55,"ATK":50,"DEF":37,"MATK":62,"MDEF":43,"SPD":50},
                    {"name":"chakasi","HP":54,"MP":50,"ATK":52,"DEF":62,"MATK":53,"MDEF":50,"SPD":40},
                    {"name":"cloudra","HP":65,"MP":70,"ATK":50,"DEF":24,"MATK":60,"MDEF":83,"SPD":52},
                    {"name":"crystatus","HP":44,"MP":64,"ATK":51,"DEF":36,"MATK":57,"MDEF":70,"SPD":41},
                    {"name":"dargun","HP":50,"MP":50,"ATK":65,"DEF":60,"MATK":40,"MDEF":60,"SPD":35},
                    {"name":"demicampus","HP":58,"MP":52,"ATK":55,"DEF":56,"MATK":46,"MDEF":65,"SPD":35},
                    {"name":"demiphage","HP":60,"MP":50,"ATK":23,"DEF":60,"MATK":45,"MDEF":102,"SPD":30},
                    {"name":"deserteagle","HP":36,"MP":50,"ATK":68,"DEF":32,"MATK":30,"MDEF":22,"SPD":60},
                    {"name":"djingo","HP":49,"MP":50,"ATK":62,"DEF":40,"MATK":36,"MDEF":50,"SPD":70},
                    {"name":"dracret","HP":56,"MP":60,"ATK":50,"DEF":48,"MATK":56,"MDEF":60,"SPD":42},
                    {"name":"drak","HP":50,"MP":50,"ATK":65,"DEF":40,"MATK":58,"MDEF":40,"SPD":55},
                    {"name":"drakee","HP":47,"MP":50,"ATK":61,"DEF":45,"MATK":45,"MDEF":45,"SPD":65},
                    {"name":"fallen","HP":43,"MP":62,"ATK":44,"DEF":35,"MATK":72,"MDEF":70,"SPD":60},
                    {"name":"firefox","HP":46,"MP":60,"ATK":32,"DEF":34,"MATK":64,"MDEF":55,"SPD":56},
                    {"name":"flareial","HP":50,"MP":40,"ATK":44,"DEF":40,"MATK":44,"MDEF":56,"SPD":70},
                    {"name":"florg","HP":52,"MP":50,"ATK":50,"DEF":52,"MATK":50,"MDEF":52,"SPD":47},
                    {"name":"forestfish","HP":50,"MP":50,"ATK":48,"DEF":60,"MATK":48,"MDEF":44,"SPD":58},
                    {"name":"Foulmouth","HP":56,"MP":56,"ATK":40,"DEF":60,"MATK":56,"MDEF":60,"SPD":20},
                    {"name":"frigit","HP":46,"MP":46,"ATK":60,"DEF":35,"MATK":55,"MDEF":40,"SPD":66},
                    {"name":"gobbldegak","HP":60,"MP":40,"ATK":70,"DEF":60,"MATK":28,"MDEF":40,"SPD":50},
                    {"name":"gote","HP":50,"MP":50,"ATK":56,"DEF":46,"MATK":48,"MDEF":56,"SPD":43},
                    {"name":"grigg","HP":33,"MP":63,"ATK":36,"DEF":56,"MATK":60,"MDEF":45,"SPD":70},
                    {"name":"grundle","HP":60,"MP":45,"ATK":62,"DEF":65,"MATK":35,"MDEF":45,"SPD":30},
                    {"name":"gruul","HP":60,"MP":40,"ATK":60,"DEF":58,"MATK":14,"MDEF":44,"SPD":50},
                    {"name":"halkneona","HP":50,"MP":55,"ATK":52,"DEF":45,"MATK":55,"MDEF":65,"SPD":50},
                    {"name":"hobldegak","HP":66,"MP":35,"ATK":61,"DEF":63,"MATK":25,"MDEF":45,"SPD":44},
                    {"name":"imp","HP":46,"MP":54,"ATK":60,"DEF":26,"MATK":60,"MDEF":26,"SPD":80},
                    {"name":"indra","HP":50,"MP":60,"ATK":55,"DEF":26,"MATK":66,"MDEF":66,"SPD":56},
                    {"name":"kelpip","HP":35,"MP":70,"ATK":25,"DEF":30,"MATK":60,"MDEF":50,"SPD":40},
                    {"name":"koy","HP":48,"MP":56,"ATK":37,"DEF":44,"MATK":68,"MDEF":59,"SPD":68},
                    {"name":"krekab","HP":60,"MP":40,"ATK":64,"DEF":64,"MATK":35,"MDEF":30,"SPD":35},
                    {"name":"lunaris","HP":50,"MP":60,"ATK":30,"DEF":60,"MATK":70,"MDEF":80,"SPD":20},
                    {"name":"lupup","HP":48,"MP":45,"ATK":64,"DEF":42,"MATK":28,"MDEF":44,"SPD":76},
                    {"name":"minimon","HP":58,"MP":43,"ATK":65,"DEF":55,"MATK":38,"MDEF":48,"SPD":50},
                    {"name":"monitor","HP":50,"MP":50,"ATK":70,"DEF":50,"MATK":30,"MDEF":50,"SPD":50},
                    {"name":"monocera","HP":60,"MP":60,"ATK":56,"DEF":70,"MATK":50,"MDEF":58,"SPD":36},
                    {"name":"nereid","HP":40,"MP":70,"ATK":28,"DEF":29,"MATK":63,"MDEF":73,"SPD":64},
                    {"name":"novacryst","HP":50,"MP":60,"ATK":45,"DEF":65,"MATK":45,"MDEF":65,"SPD":45},
                    {"name":"osflorg","HP":30,"MP":50,"ATK":55,"DEF":100,"MATK":48,"MDEF":28,"SPD":35},
                    {"name":"pixelroggle","HP":50,"MP":50,"ATK":50,"DEF":50,"MATK":50,"MDEF":50,"SPD":50},
                    {"name":"pixie","HP":36,"MP":60,"ATK":33,"DEF":28,"MATK":60,"MDEF":66,"SPD":66},
                    {"name":"promethal","HP":56,"MP":56,"ATK":55,"DEF":48,"MATK":52,"MDEF":48,"SPD":47},
                    {"name":"pyorg","HP":50,"MP":50,"ATK":42,"DEF":66,"MATK":55,"MDEF":65,"SPD":34},
                    {"name":"quillwheel","HP":36,"MP":50,"ATK":8,"DEF":25,"MATK":80,"MDEF":80,"SPD":40},
                    {"name":"raqth","HP":50,"MP":50,"ATK":63,"DEF":37,"MATK":63,"MDEF":44,"SPD":56},
                    {"name":"roggle","HP":54,"MP":45,"ATK":60,"DEF":50,"MATK":46,"MDEF":53,"SPD":50},
                    {"name":"roper","HP":43,"MP":60,"ATK":35,"DEF":35,"MATK":71,"MDEF":66,"SPD":32},
                    {"name":"roturret","HP":50,"MP":30,"ATK":80,"DEF":70,"MATK":30,"MDEF":30,"SPD":30},
                    {"name":"salamander","HP":50,"MP":56,"ATK":54,"DEF":38,"MATK":60,"MDEF":48,"SPD":50},
                    {"name":"saur","HP":54,"MP":43,"ATK":64,"DEF":65,"MATK":30,"MDEF":50,"SPD":36},
                    {"name":"scurver","HP":62,"MP":39,"ATK":67,"DEF":77,"MATK":32,"MDEF":40,"SPD":40},
                    {"name":"seavolver","HP":44,"MP":50,"ATK":65,"DEF":26,"MATK":46,"MDEF":20,"SPD":65},
                    {"name":"shakasi","HP":34,"MP":40,"ATK":52,"DEF":65,"MATK":60,"MDEF":50,"SPD":40},
                    {"name":"silma","HP":35,"MP":70,"ATK":14,"DEF":20,"MATK":74,"MDEF":60,"SPD":40},
                    {"name":"skellington","HP":20,"MP":50,"ATK":58,"DEF":150,"MATK":17,"MDEF":40,"SPD":28},
                    {"name":"skullroggle","HP":30,"MP":33,"ATK":66,"DEF":100,"MATK":38,"MDEF":30,"SPD":26},
                    {"name":"skullbug","HP":47,"MP":50,"ATK":47,"DEF":60,"MATK":61,"MDEF":60,"SPD":40},
                    {"name":"snowolf","HP":50,"MP":50,"ATK":56,"DEF":40,"MATK":56,"MDEF":46,"SPD":62},
                    {"name":"solrotor","HP":50,"MP":60,"ATK":30,"DEF":64,"MATK":64,"MDEF":64,"SPD":20},
                    {"name":"songun","HP":50,"MP":60,"ATK":46,"DEF":60,"MATK":50,"MDEF":34,"SPD":55},
                    {"name":"sphenodon","HP":47,"MP":60,"ATK":56,"DEF":51,"MATK":54,"MDEF":58,"SPD":40},
                    {"name":"stywrack","HP":62,"MP":30,"ATK":58,"DEF":82,"MATK":38,"MDEF":30,"SPD":26},
                    {"name":"terrnip","HP":66,"MP":70,"ATK":25,"DEF":30,"MATK":69,"MDEF":63,"SPD":66},
                    {"name":"tikihuka","HP":45,"MP":70,"ATK":25,"DEF":30,"MATK":62,"MDEF":65,"SPD":55},
                    {"name":"tikiraedel","HP":45,"MP":70,"ATK":37,"DEF":30,"MATK":69,"MDEF":64,"SPD":60},
                    {"name":"triangulon","HP":50,"MP":50,"ATK":30,"DEF":50,"MATK":70,"MDEF":50,"SPD":50},
                    {"name":"tweed","HP":35,"MP":70,"ATK":15,"DEF":30,"MATK":80,"MDEF":70,"SPD":50},
                    {"name":"twurqqlon","HP":49,"MP":51,"ATK":56,"DEF":44,"MATK":35,"MDEF":65,"SPD":50},
                    {"name":"unit","HP":40,"MP":50,"ATK":60,"DEF":30,"MATK":60,"MDEF":30,"SPD":60},
                    {"name":"vega","HP":55,"MP":55,"ATK":30,"DEF":55,"MATK":55,"MDEF":55,"SPD":60},
                    {"name":"volnar","HP":42,"MP":40,"ATK":64,"DEF":57,"MATK":12,"MDEF":50,"SPD":76},
                    {"name":"whiteermine","HP":50,"MP":60,"ATK":45,"DEF":40,"MATK":60,"MDEF":48,"SPD":70},
                    {"name":"winguard","HP":60,"MP":50,"ATK":70,"DEF":70,"MATK":50,"MDEF":40,"SPD":25},
                    {"name":"zarlek","HP":58,"MP":40,"ATK":72,"DEF":40,"MATK":30,"MDEF":60,"SPD":55},
                    {"name":"zelth","HP":48,"MP":60,"ATK":61,"DEF":39,"MATK":64,"MDEF":45,"SPD":60},
                    {"name":"zombog","HP":120,"MP":50,"ATK":55,"DEF":25,"MATK":55,"MDEF":35,"SPD":26},
                   ]
    selected_species = next((item for item in species_list if item["name"] == species), None)
    for i in ["HP", "MP", "ATK", "DEF", "MATK", "MDEF", "SPD"]:
        stats[i] = math.floor((selected_species[i] * (1+(level/20)) + evs[i]/10 ) * (1 + (ivs[i] - 10) * 0.0125))
    if(temp_a == "C") | (temp_b == "C"):
        stats["ATK"] *= 1.1
        stats["MATK"] *= 0.9
    if(temp_a == "P") | (temp_b == "P"):
        stats["MDEF"] *= 1.1
        stats["SPD"] *= 0.9
    if(temp_a == "S") | (temp_b == "S"):
        stats["SPD"] *= 1.1
        stats["MDEF"] *= 0.9
    if(temp_a == "M") | (temp_b == "M"):
        stats["MATK"] *= 1.1
        stats["ATK"] *= 0.9
    for i in stats:
        stats[i] = math.floor(stats[i])
    actual_hp = int(stats["HP"] * 2 + (stats["MP"] / 3) * level)
    actual_mp = stats["MP"]
    #print(stats)
    #print("Actual HP is: " + str(actual_hp))
    #print("Actual MP is: " + str(actual_mp))
    return stats, actual_hp, actual_mp

level = sys.argv[0]
statslist, actual_hp, actual_mp = calcStats(level, species, iv_hp, iv_mp, iv_atk, iv_def, iv_matk, iv_mdef, iv_spd, ev_hp, ev_mp, ev_atk, ev_def, ev_matk, ev_mdef, ev_spd, temp_a, temp_b)

return level
