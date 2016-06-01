from tinydb import TinyDB

db = TinyDB('../roleplaying_systems/5e.json')
race = db.table('race')
race.insert({'Name': 'Elf', 'val': 'Common, Elvish'})
