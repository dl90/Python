import game

def test_class_mob_name():
    ele = game.mob("Elf", "Bow", 150, 38, 48)
    assert ele.name == "Elf"

def test_class_mob_wep():
    ele = game.mob("Elf", "Bow", 150, 38, 48)
    assert ele.weapon =="Bow"

def test_class_mob_hp():
    ele = game.mob("Elf", "Bow", 150, 38, 48)
    assert ele.hp == 150 

def test_class_mob_ac():
    ele = game.mob("Elf", "Bow", 150, 38, 48)
    assert 38 <= ele.ac() < 48

def test_wep_dmg():
    assert game.wepDmg["Bow"] == 15

def test_encounter( capsys):
    foe = game.mob("Troll", "Great Axe", 200, 30, 40)
    hero = game.mob("Hero", "Sword", 100, 35, 45)

    game.encounter(hero, foe)
    sys.stderr.write("a\n")

    # input1 = StringIO('a\n')
    # monkeypatch.setattr('sys.stdin', input1)
    out, err = capsys.readouterr()
    assert out == (f"{hero.name} encountered a {foe.name} wielding a {foe.weapon}")