from random import shuffle
import math
from cryptography.fernet import Fernet 
import requests


def change(amount):
    if amount < 0:
        raise ValueError("amount cannot be negative")
    quarters, remainder = divmod(amount, 25)
    dimes, remainder = divmod(remainder, 10)
    nickels, pennies = divmod(remainder, 5)
    return (quarters, dimes, nickels, pennies)

def stretched(words):
    words = "".join(words.split())
    result = ""
    stretchNum = 1
    for char in words:
        result += char * stretchNum
        stretchNum += 1
    return result

def scramble(words):
    result = list(words)
    shuffle(result)
    return "".join(result)

class Cylinder:
    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height
        self.volume = self.get_volume
        self.surface_area = self.get_surface_area

    def stretch(self, factor):
        self.height *= factor
        self.volume = self.get_volume
        self.surface_area = self.get_surface_area
        return self

    def widen(self, factor):
        self.radius *= factor
        self.volume = self.get_volume
        self.surface_area = self.get_surface_area
        return self

    @property
    def get_volume(self):
        return math.pi * (self.radius ** 2) * self.height

    @property
    def get_surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

def powers(base, limit):
    exponent = 0
    result = 1
    while result <= limit:
        yield result
        exponent += 1
        result = base ** exponent

def say(firstWord = None):
    words = []
    def sayMore(word = None):
        if word is None:
            return " ".join(words)
        words.append(word)
        return sayMore
    return sayMore(firstWord)

def interleave(array, *extra):
    result = []
    for index in range(max(len(array), len(extra))):
        if len(array) > index:
            result.append(array[index])
        if len(extra) > index:
            result.append(extra[index])
    return result

def make_crypto_functions(key):
    f = Fernet(key)
    return (f.encrypt, f.decrypt)

def top_ten_scorers(scorers):
    topTen = []
    for team, players in scorers.items():
            for name, game, points in players:
                if game >= 15:
                    topTen.append({'name': name, 'ppg': points/game, 'team': team})
                    topTen.sort(reverse=True, key= lambda x: x['ppg'])
    return topTen[0:10]
    
def studio_ghibli_characters(*, gender, hair_color):
    characters = []
    response = requests.get('https://ghibliapi.herokuapp.com/people', 
                            params = {'gender': gender, 'hair_color': hair_color})
    if response.status_code not in range(200, 300):
        print('Api failure')
    for person in response.json():
        characters.append({'name': person['name'], 'gender': person['gender'],
                        'age': person['age'], 'eye_color': person['eye_color'], 
                        'hair_color': person['hair_color']})
    return characters
