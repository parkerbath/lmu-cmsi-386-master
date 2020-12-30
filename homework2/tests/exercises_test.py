import re
import math
import pytest
from exercises import (change, stretched, scramble, Cylinder,
                       powers, say,  interleave, make_crypto_functions,
                       top_ten_scorers, studio_ghibli_characters)


def test_change():
    assert change(0) == (0, 0, 0, 0)
    assert change(97) == (3, 2, 0, 2)
    assert change(8) == (0, 0, 1, 3)
    assert change(250) == (10, 0, 0, 0)
    assert change(144) == (5, 1, 1, 4)
    assert change(97) == (3, 2, 0, 2)
    assert change(100000000000) == (4000000000, 0, 0, 0)
    with pytest.raises(ValueError) as excinfo:
        change(-50)
    assert str(excinfo.value) == 'amount cannot be negative'


def test_stretched():
    assert stretched('') == ''
    assert stretched('H e   l\t\tlo') == 'Heelllllllooooo'
    assert stretched('$#') == '$##'
    assert stretched('       ') == ''
    assert stretched('A = πr²') == 'A==πππrrrr²²²²²'


def test_scramble():
    for s in ['a', 'rat', 'JavaScript testing', '', 'zzz', '^*))^*>^▱ÄÈËɡɳɷ']:
        assert sorted(s) == sorted(scramble(s))
    possibilities = set(['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'])
    for _ in range(200):
        possibilities.discard(scramble('ABC'))
    assert not possibilities


def test_cylinder():
    c = Cylinder(radius=10, height=5)
    assert c.height == 5
    assert c.radius == 10
    c = Cylinder(height=5)
    assert c.height == 5
    assert c.radius == 1
    c = Cylinder(radius=5)
    assert c.height == 1
    assert c.radius == 5
    c = Cylinder()
    assert c.height == 1
    assert c.radius == 1
    c = Cylinder(radius=2, height=10)
    assert pytest.approx(c.volume, 0.000001) == 40 * math.pi
    assert pytest.approx(c.surface_area, 0.000001) == 48 * math.pi
    c.widen(3)
    assert c.radius == 6
    c.stretch(2)
    assert c.height == 20
    assert pytest.approx(c.surface_area, 0.000001) == 312 * math.pi
    assert pytest.approx(c.volume, 0.000001) == 720 * math.pi


def test_powers():
    p = powers(2, 10)
    assert next(p) == 1
    assert next(p) == 2
    assert next(p) == 4
    assert next(p) == 8
    with pytest.raises(StopIteration):
        next(p)
    assert list(powers(2, -5)) == []
    assert list(powers(7, 0)) == []
    assert list(powers(3, 1)) == [1]
    assert list(powers(2, 63)) == [1, 2, 4, 8, 16, 32]
    assert list(powers(2, 64)) == [1, 2, 4, 8, 16, 32, 64]


def test_say():
    assert say() == ''
    assert say('hi')() == 'hi'
    assert say('hi')('there')() == 'hi there'
    assert say('hello')('my')('name')('is')(
        'Colette')() == 'hello my name is Colette'


def test_interleave():
    assert interleave([]) == []
    assert interleave([1, 4, 6]) == [1, 4, 6]
    assert interleave([], 2, 3) == [2, 3]
    assert interleave([1], 9) == [1, 9]
    assert interleave([8, 8, 3, 9], 1) == [8, 1, 8, 3, 9]
    assert interleave([2], 7, '8', {}) == [2, 7, '8', {}]
    a = [1, 2, 3, 4]
    assert interleave(a, 10, 20, 30) == [1, 10, 2, 20, 3, 30, 4]
    # Test input list not destroyed
    assert a == [1, 2, 3, 4]


def test_crypto():
    assert isinstance(make_crypto_functions(
        b"A2qK5XG3qX1MfLrGacD9AGVG2sbZYkvFFki94qbkVhE="), tuple)
    encrypt, decrypt = make_crypto_functions(
        b"A2qK5XG3qX1MfLrGacD9AGVG2sbZYkvFFki94qbkVhE=")
    for s in [b'', b'\xfe9iP\x05\x22\x490opXZ@1##', b'Helllllllllooooooo world']:
        assert decrypt(encrypt(s)) == s


def test_top_ten_scorers():
    assert top_ten_scorers({}) == []
    assert top_ten_scorers({'T1': [['A', 3, 300]]}) == []
    input = {'T1': [['A', 30, 300]]}
    expected = [{'name': 'A', 'ppg': 10, 'team': 'T1'}]
    assert top_ten_scorers(input) == expected
    input = {
        'ATL': [
            ['Betnijah Laney', 16, 263],
            ['Courtney Williams', 14, 193],
        ],
        'CHI': [
            ['Kahleah Copper', 17, 267],
            ['Allie Quigley', 17, 260],
            ['Courtney Vandersloot', 17, 225],
        ],
        'CONN': [
            ['DeWanna Bonner', 16, 285],
            ['Alyssa Thomas', 16, 241],
        ],
        'DAL': [
            ['Arike Ogunbowale', 16, 352],
            ['Satou Sabally', 12, 153],
        ],
        'IND': [
            ['Kelsey Mitchell', 16, 280],
            ['Tiffany Mitchell', 13, 172],
            ['Candice Dupree', 16, 202],
        ],
        'LA': [
            ['Nneka Ogwumike', 14, 172],
            ['Chelsea Gray', 16, 224],
            ['Candace Parker', 16, 211],
        ],
        'LV': [
            ['A’ja Wilson', 15, 304],
            ['Dearica Hamby', 15, 188],
            ['Angel McCoughtry', 15, 220],
        ],
        'MIN': [
            ['Napheesa Collier', 16, 262],
            ['Crystal Dangerfield', 16, 254],
        ],
        'NY': [
            ['Layshia Clarendon', 15, 188]
        ],
        'PHX': [
            ['Diana Taurasi', 13, 236],
            ['Brittney Griner', 12, 212],
            ['Skylar Diggins-Smith', 16, 261],
            ['Bria Hartley', 13, 190],
        ],
        'SEA': [
            ['Breanna Stewart', 16, 317],
            ['Jewell Loyd', 16, 223],
        ],
        'WSH': [
            ['Emma Meesseman', 13, 158],
            ['Ariel Atkins', 15, 212],
            ['Myisha Hines-Allen', 15, 236],
        ],
    }
    expected = [
        {'name': 'Arike Ogunbowale', 'ppg': 22, 'team': 'DAL'},
        {'name': 'A’ja Wilson', 'ppg': 20.266666666666666, 'team': 'LV'},
        {'name': 'Breanna Stewart', 'ppg': 19.8125, 'team': 'SEA'},
        {'name': 'DeWanna Bonner', 'ppg': 17.8125, 'team': 'CONN'},
        {'name': 'Kelsey Mitchell', 'ppg': 17.5, 'team': 'IND'},
        {'name': 'Betnijah Laney', 'ppg': 16.4375, 'team': 'ATL'},
        {'name': 'Napheesa Collier', 'ppg': 16.375, 'team': 'MIN'},
        {'name': 'Skylar Diggins-Smith', 'ppg': 16.3125, 'team': 'PHX'},
        {'name': 'Crystal Dangerfield', 'ppg': 15.875, 'team': 'MIN'},
        {'name': 'Myisha Hines-Allen', 'ppg': 15.733333333333333, 'team': 'WSH'},
    ]
    assert top_ten_scorers(input) == expected


def test_studio_ghibli_characters():
    people = studio_ghibli_characters(gender='Male', hair_color='Purple')
    assert people == []
    people = studio_ghibli_characters(gender='Female', hair_color='Black')
    assert people == [
        {
            "name": "Lusheeta Toel Ul Laputa",
            "gender": "Female",
            "age": "13",
            "eye_color": "Black",
            "hair_color": "Black"
        },
        {
            "name": "Eboshi",
            "gender": "Female",
            "age": "Unspecified/Adult",
            "eye_color": "Hazel",
            "hair_color": "Black"
        }
    ]
    people = studio_ghibli_characters(hair_color='Blue', gender='NA')
    assert people == [
        {
            "name": "Chu Totoro",
            "gender": "NA",
            "age": "",
            "eye_color": "Black",
            "hair_color": "Blue"
        }
    ]
