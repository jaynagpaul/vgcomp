# Names to start the scraper with

START = [
    {
        "name": "L3oN",
        "region": "eu"
    },
    {
        "name": "iBANG",
        "region": "na"
    },
    {
        "name": "ShadedTalent",
        "region": "na"
    },
    {
        "name": "DNZio",
        "region": "na"
    },
    {
        "name": "BestChuckNa",
        "region": "na"
    },
    {
        "name": "IraqiZorro",
        "region": "na"
    },
    {
        "name": "LookMyVGPRO",
        "region": "eu"
    },
    {
        "name": "Mowglie",
        "region": "eu"
    },
    {
        "name": "KValafar",
        "region": "eu"
    },
    {
        "name": "druid",
        "region": "ea"
    },
    {
        "name": "Cassandra",
        "region": "sg"
    },
    {
        "name": "MiniDookie",
        "region": "sa"
    },
    {
        "name": "MrDogCK",
        "region": "cn"
    }
]


# Correct hero API names https://raw.githubusercontent.com/madglory/gamelocker-vainglory/master/resources/actors.json
HEROES = [ { "friendlyName": "Adagio", "name": "*Adagio*" }, { "friendlyName": "Alpha", "name": "*Alpha*" }, { "friendlyName": "Ardan", "name": "*Ardan*" }, { "friendlyName": "Baptiste", "name": "*Baptiste*" }, { "friendlyName": "Baron", "name": "*Baron*" }, { "friendlyName": "Blackfeather", "name": "*Blackfeather*" }, { "friendlyName": "Catherine", "name": "*Catherine*" }, { "friendlyName": "Celeste", "name": "*Celeste*" }, { "friendlyName": "Flicker", "name": "*Flicker*" }, { "friendlyName": "Fortress", "name": "*Fortress*" }, { "friendlyName": "Glaive", "name": "*Glaive*" }, { "friendlyName": "Grumpjaw", "name": "*Grumpjaw*" }, { "friendlyName": "Gwen", "name": "*Gwen*" }, { "friendlyName": "Krul", "name": "*Hero009*" }, { "friendlyName": "Krul", "name": "*Krul*" }, { "friendlyName": "Skaarf", "name": "*Hero010*" }, { "friendlyName": "Skaarf", "name": "*Skaarf*" }, { "friendlyName": "Rona", "name": "*Hero016*" }, { "friendlyName": "Rona", "name": "*Rona*" }, { "friendlyName": "Idris", "name": "*Idris*" }, { "friendlyName": "Joule", "name": "*Joule*" }, { "friendlyName": "Kestrel", "name": "*Kestrel*" }, { "friendlyName": "Koshka", "name": "*Koshka*" }, { "friendlyName": "Lance", "name": "*Lance*" }, { "friendlyName": "Lyra", "name": "*Lyra*" }, { "friendlyName": "Ozo", "name": "*Ozo*" }, { "friendlyName": "Petal", "name": "*Petal*" }, { "friendlyName": "Phinn", "name": "*Phinn*" }, { "friendlyName": "Reim", "name": "*Reim*" }, { "friendlyName": "Ringo", "name": "*Ringo*" }, { "friendlyName": "SAW", "name": "*SAW*" }, { "friendlyName": "Samuel", "name": "*Samuel*" }, { "friendlyName": "Taka", "name": "*Sayoc*" }, { "friendlyName": "Taka", "name": "*Taka*" }, { "friendlyName": "Skye", "name": "*Skye*" }, { "friendlyName": "Vox", "name": "*Vox*" }, { "friendlyName": "Reza", "name": "*Reza*" }, { "friendlyName": "Grace", "name": "*Grace*" } ]

def convHero(name: str) -> str:
    """
    Converts the API hero name to the clean hero name
    """
    for h in HEROES:
        if h["name"] == name:
            return h['friendlyName'].lower()
    return name.lower()