import pytest
from Code import Josh_Higginson_Python_Assessment_1


def test_one():
    assert Josh_Higginson_Python_Assessment_1.one("hi", "hello") == "hello"
    assert Josh_Higginson_Python_Assessment_1.one("three", "two") == "three"
    assert Josh_Higginson_Python_Assessment_1.one("three", "hello") == "three hello"
    assert Josh_Higginson_Python_Assessment_1.one("echo", "print") == "print"
    assert Josh_Higginson_Python_Assessment_1.one("fire", "rib") == "fire"


def test_two():
    assert Josh_Higginson_Python_Assessment_1.two("bertclivebert") == "clive"
    assert Josh_Higginson_Python_Assessment_1.two("xxbertfridgebertyy") == "fridge"
    assert Josh_Higginson_Python_Assessment_1.two("xxBertfridgebERtyy") == "fridge"
    assert Josh_Higginson_Python_Assessment_1.two("xxbertyy") == ""
    assert Josh_Higginson_Python_Assessment_1.two("xxbeRTyy") == ""


def test_three():
    assert Josh_Higginson_Python_Assessment_1.three(3) == "fizz"
    assert Josh_Higginson_Python_Assessment_1.three(10) == "buzz"
    assert Josh_Higginson_Python_Assessment_1.three(15) == "fizzbuzz"
    assert Josh_Higginson_Python_Assessment_1.three(8) == "null"
    assert Josh_Higginson_Python_Assessment_1.three(75) == "fizzbuzz"


def test_four():
    assert Josh_Higginson_Python_Assessment_1.four("55 72 86") == 14
    assert Josh_Higginson_Python_Assessment_1.four("15 72 80 164") == 11
    assert Josh_Higginson_Python_Assessment_1.four("555 72 86 45 10") == 15
    assert Josh_Higginson_Python_Assessment_1.four("98 63 34 1 13") == 17
    assert Josh_Higginson_Python_Assessment_1.four("98 107 415") == 17


def test_five():
    assert Josh_Higginson_Python_Assessment_1.five("Jeff,random.py,False,1445") == ["Jeff"]
    assert Josh_Higginson_Python_Assessment_1.five(
        "Bert,numberGen.py,True,1447,Bert,integers.py,True,1318,Jeff,floats.py,False,1445") == ["Jeff"]
    assert Josh_Higginson_Python_Assessment_1.five(
        "Bert,boolean.py,False,1447,Bert,conditions.py,False,1318,Jeff,loops.py,False,1445") == ["Bert", "Jeff"]
    assert Josh_Higginson_Python_Assessment_1.five(
        "Bert,prime.py,True,1447,Bert,ISBN.py,False,1318,Jeff,OOP.py,False,1445") == ["Bert", "Jeff"]
    assert Josh_Higginson_Python_Assessment_1.five(
        "Bert,files.py,True,1447,Bert,tests.py,True,1318,Jeff,app.py,True,1445") == []


def test_six():
    assert Josh_Higginson_Python_Assessment_1.six("ceiling") == True
    assert Josh_Higginson_Python_Assessment_1.six("believe") == True
    assert Josh_Higginson_Python_Assessment_1.six("glacier") == False
    assert Josh_Higginson_Python_Assessment_1.six("height") == False
    assert Josh_Higginson_Python_Assessment_1.six("receive") == True


def test_seven():
    assert Josh_Higginson_Python_Assessment_1.seven("Hello") == 2
    assert Josh_Higginson_Python_Assessment_1.seven("hEelLoooO") == 6
    assert Josh_Higginson_Python_Assessment_1.seven("WhitEboarD") == 4
    assert Josh_Higginson_Python_Assessment_1.seven("as") == 1
    assert Josh_Higginson_Python_Assessment_1.seven("pass") == 1


def test_eight():
    assert Josh_Higginson_Python_Assessment_1.eight(1) == 1
    assert Josh_Higginson_Python_Assessment_1.eight(3) == 6
    assert Josh_Higginson_Python_Assessment_1.eight(4) == 24
    assert Josh_Higginson_Python_Assessment_1.eight(6) == 720
    assert Josh_Higginson_Python_Assessment_1.eight(8) == 40320


def test_nine():
    assert Josh_Higginson_Python_Assessment_1.nine("This is a Sentence", "s") == 4
    assert Josh_Higginson_Python_Assessment_1.nine("This is a Sentence", "S") == 8
    assert Josh_Higginson_Python_Assessment_1.nine("Fridge for sale", "z") == -1
    assert Josh_Higginson_Python_Assessment_1.nine("I love Python", "L") == -1
    assert Josh_Higginson_Python_Assessment_1.nine("I LOVE PYTHON", "L") == 2


def test_ten():
    assert Josh_Higginson_Python_Assessment_1.ten("The", 2, "h") == True
    assert Josh_Higginson_Python_Assessment_1.ten("AAbb", 1, "b") == False
    assert Josh_Higginson_Python_Assessment_1.ten("Hi-There", 10, "e") == False
    assert Josh_Higginson_Python_Assessment_1.ten("HEY", 2, "e") == True
    assert Josh_Higginson_Python_Assessment_1.ten("on-premise", 3, "-") == True
