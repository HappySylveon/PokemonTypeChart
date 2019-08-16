# By HappySylveon :)

import time

a = ("normal")
b = ("fighting")
c = ("flying")
d = ("poison")
e = ("ground")
f = ("rock")
g = ("bug")
h = ("ghost")
i = ("steel")
j = ("fire")
k = ("water")
l = ("grass")
m = ("electric")
n = ("psychic")
o = ("ice")
p = ("dragon")
q = ("dark")
r = ("fairy")

types = ("Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy")


count = 0
while (count < 1):
    owo = input("Insert type: ")
    owo
    if owo == a:
        print("Weaknesses: Fighting", "\nResistances: none", "\nImmunities: Ghost")
    elif owo == b:
        print("Weaknesses: Fairy, Flying, Psychic", "\nResistances: Bug, Dark, Rock", "\nImmunities: None")
    elif owo == c:
        print("Weaknesses: Electric, Ice, Rock", "\nResistances: Bug, Fighting, Grass", "\nImmunities: Ground")
    elif owo == d:
        print("Weaknesses: Ground, Psychic", "\nResistances: Bug, Fairy, Fighting, Grass, Poison", "\nImmunities: None")
    elif owo == e:
        print("Weaknesses: Grass, Ice, Water", "\nResistances: Poison, Rock", "\nImmunities: Electric")
    elif owo == f:
        print("Weaknesses: Fighting, Grass, Ground, Steel, Water", "\nResistances: Fire, Flying, Normal, Poison", "\nImmunities: None")
    elif owo == g:
        print("Weaknesses: Fire, Flying, Rock", "\nResistances: Fighting, Grass, Ground", "\nImmunities: None")
    elif owo == h:
        print("Weaknesses: Dark, Ghost", "\nResistances: Bug, Poison", "\nImmunities: Fighting, Normal")
    elif owo == i:
        print("Weaknesses: Fighting, Fire, Ground", "\nResistances: Bug, Dragon, Fairy, Flying, Grass, Ice, Normal, Psychic, Rock, Steel", "\nImmunities: Poison")
    elif owo == j:
        print("Weaknesses: Ground, Rock, Water", "\nResistances: Bug, Fairy, Fire, Grass, Ice, Steel", "\nImmunities: None")
    elif owo == k:
        print("Weaknesses: Electric, Grass", "\nResistances: Fire, Ice, Steel, Water", "\nImmunities: None")
    elif owo == l:
        print("Weaknesses: Bug, Fire, Flying, Ice, Poison", "\nResistances: Electric, Grass, Ground, Water", "\nImmunities: None")
    elif owo == m:
        print("Weaknesses: Ground", "\nResistances: Electric, Flying, Steel", "\nImmunities: None")
    elif owo == n:
        print("Weaknesses: Bug, Dark, Ghost", "\nResistances: Fighting, Psychic", "\nImmunities: None")
    elif owo == o:
        print("Weaknesses: Fighting, Fire, Rock, Steel", "\nResistances: Ice", "\nImmunities: None")
    elif owo == p:
        print("Weaknesses: Dragon, Fairy, Ice", "\nResistances: Electric, Fire, Grass, Water", "\nImmunities: None")
    elif owo == q:
        print("Weaknesses: Bug, Fairy, Fighting", "\nResistances: Dark, Ghost", "\nImmunities: Psychic")
    elif owo == r:
        print("Weaknesses: Poison, Steel", "\nResistances: Bug, Dark, Fighting", "\nImmunities: Dragon")
    elif owo == (a + " " + b) or owo == (b + " " + a):
        print("Weaknesses: Fairy, Fighting, Flying, Psychic", "\nResistances: Bug, Dark, Rock", "\nImmunities: Ghost")
    elif owo == (a + " " + c) or owo == (c + " " + a):
        print("Weaknesses: Electric, Ice, Rock", "\nResistances: Bug, Grass", "\nImmunities: Ghost, Ground")
    elif owo == (a + " " + d) or owo == (d + " " + a):
        print("Weaknesses: Ground, Psychic", "\nResistances: Grass, Poison, Bug, Fairy", "\nImmunities: Ghost")
    elif owo == (a + " " + e) or owo == (e + " " + a):
        print("Weaknesses: Fighting, Grass, Ice, Water", "\nResistances: Poison, Rock", "\nImmunities: Electric, Ghost")
    elif owo == (a + " " + f) or owo == (f + " " + a):
        print("Weaknesses: Water, Grass, Fighting, Ground", "\nResistances: Normal, Fire, Poison, Flying", "\nImmunities: Ghost")
    elif owo == (a + " " + g) or owo == (g + " " + a):
        print("Weaknesses: Fire, Flying, Rock", "\nResistances: Grass, Ground", "\nImmunities: Ghost")
    elif owo == (a + " " + h) or owo == (h + " " + a):
        print("Weaknesses: Dark", "\nResistances: Poison, Bug", "\nImmunities: Normal, Fighting, Ghost")
    elif owo == (a + " " + i) or owo == (i + " " + a):
        print("Weaknesses: Fire, Fighting, Ground", "\nResistances: Fire, Grass, Ice, Flying, Psychic, Bug, Rock, Dragon, Steel, Fairy", "\nImmunities: Poison, Normal")
    elif owo == (a + " " + j) or owo == (j + " " + a):
        print("Weaknesses: Fighting, Ground, Rock, Water", "\nResistances: Bug, Fairy, Fire, Grass, Ice, Steel", "\nImmunities: Ghost")
    elif owo == (a + " " + k) or owo == (k + " " + a):
        print("Weaknesses: Electric, Fighting, Grass", "\nResistances: Fire, Ice, Steel, Water", "\nImmunities: Ghost")
    elif owo == (a + " " + l) or owo == (l + " " + a):
        print("Weaknesses: Bug, Fighting, Fire, Flying, Ice, Poison", "\nResistances: Electric, Grass, Ground, Water", "\nImmunities: Ghost")
    elif owo == (a + " " + m) or owo == (m + " " + a):
        print("Weaknesses: Fighting, Ground", "\nResistances: Electric, Flying, Steel", "\nImmunities: Ghost")
    elif owo == (a + " " + m) or owo == (m + " " + a):
        print("Weaknesses: Fighting, Ground", "\nResistances: Electric, Flying, Steel", "\nImmunities: Ghost")
    elif owo == (a + " " + n) or owo == (n + " " + a):
        print("Weaknesses: Bug, Dark", "\nResistances: Psychic", "\nImmunities: Ghost")
    elif owo == (a + " " + o) or owo == (o + " " + a):
        print("Weaknesses: Fire, Fighting, Rock, Steel", "\nResistances: Ice", "\nImmunities: Ghost")
    elif owo == (a + " " + p) or owo == (p + " " + a):
        print("Weaknesses: Dragon, Fairy, Fighting, Ice", "\nResistances: Electric, Fire, Grass, Water", "\nImmunities: Ghost")
    elif owo == (a + " " + q) or owo == (q + " " + a):
        print("Weaknesses: Bug, Fairy, Fighting", "\nResistances: Dark", "\nImmunities: Ghost, Psychic")
    elif owo == (a + " " + r) or owo == (r + " " + a):
        print("Weaknesses: Poison, Steel", "\nResistances: Bug, Dark", "\nImmunities: Dragon, Ghost")
    elif owo == (b + " " + c) or owo == (c + " " + b):
        print("Weaknesses: Electric, Fairy, Flying, Ice, Psychic", "\nResistances: Bug, Dark, Fighting, Grass", "\nImmunities: Ground")
    elif owo == (b + " " + d) or owo == (d + " " + b):
        print("Weaknesses: Flying, Ground, Psychic", "\nResistances: Bug, Dark, Fighting, Grass, Poison, Rock", "\nImmunities: None")
    elif owo == (b + " " + e) or owo == (e + " " + b):
        print("Weaknesses: Water, Grass, Ice, Flying, Psychic, Fairy", "\nResistances: Poison, Bug, Rock, Dark", "\nImmunities: Electric")
    elif owo == (b + " " + f) or owo == (f + " " + b):
        print("Weaknesses: Fairy, Fighting, Grass, Ground, Psychic, Steel, Water", "\nResistances: Bug, Dark, Fire, Normal, Poison, Rock", "\nImmunities: None")
    elif owo == (b + " " + g) or owo == (g + " " + b):
        print("Weaknesses: Fairy, Fire, Flying, Psychic", "\nResistances: Bug, Dark, Fighting, Grass, Ground", "\nImmunities: None")
    elif owo == (b + " " + h) or owo == (h + " " + b):
        print("Weaknesses: Fairy, Flying, Ghost, Psychic", "\nResistances: Bug, Poison, Rock", "\nImmunities: Fighting, Normal")
    elif owo == (b + " " + i) or owo == (i + " " + b):
        print("Weaknesses: Fighting, Fire, Ground", "\nResistances: Bug, Dark, Dragon, Grass, Ice, Normal, Rock, Steel", "\nImmunities: Poison")
    elif owo == (b + " " + j) or owo == (j + " " + b):
        print("Weaknesses: Flying, Ground, Psychic, Water", "\nResistances: Bug, Dark, Fire, Grass, Ice, Steel", "\nImmunities: None")
    elif owo == (b + " " + k) or owo == (k + " " + b):
        print("Weaknesses: Electric, Fairy, Flying, Grass, Psychic", "\nResistances: Bug, Dark, Fire, Ice, Rock, Steel, Water", "\nImmunities: None")
    elif owo == (b + " " + l) or owo == (l + " " + b):
        print("Weaknesses: Fairy, Fire, Flying, Ice, Poison, Psychic", "\nResistances: Dark, Electric, Grass, Ground, Rock, Water", "\nImmunities: None")
    elif owo == (b + " " + m) or owo == (m + " " + b):
        print("Weaknesses: Ground, Psychic, Fairy", "\nResistances: Electric, Bug, Rock, Dark, Steel", "\nImmunities: None")
    elif owo == (b + " " + n) or owo == (n + " " + b):
        print("Weaknesses: Fairy, Flying, Ghost", "\nResistances: Fighting, Rock", "\nImmunities: None")
    elif owo == (b + " " + o) or owo == (o + " " + b):
        print("Weaknesses: Fairy, Fighting, Fire, Flying, Psychic, Steel", "\nResistances: Bug, Dark, Ice", "\nImmunities: None")
    elif owo == (b + " " + p) or owo == (p + " " + b):
        print("Weaknesses: Dragon, Fairy, Flying, Ice, Psychic", "\nResistances: Bug, Dark, Electric, Fire, Grass, Rock, Water", "\nImmunities: None")
    elif owo == (b + " " + q) or owo == (q + " " + b):
        print("Weaknesses: Fairy, Fighting, Flying", "\nResistances: Dark, Ghost, Rock", "\nImmunities: Psychic")
    elif owo == (b + " " + r) or owo == (r + " " + b):
        print("Weaknesses: Poison, Flying, Psychic, Steel, Fairy", "\nResistances: Fighting, Bug, Rock, Dark", "\nImmunities: Dragon")
    elif owo == (c + " " + d) or owo == (d + " " + c):
        print("Weaknesses: Electric, Ice, Psychic, Rock", "\nResistances: Bug, Fairy, Fighting, Grass, Poison", "\nImmunities: Ground")
    elif owo == (c + " " + e) or owo == (e + " " + c):
        print("Weaknesses: Ice, Water", "\nResistances: Bug, Fighting, Poison", "\nImmunities: Electric, Ground")
    elif owo == (c + " " + f) or owo == (f + " " + c):
        print("Weaknesses: Electric, Ice, Rock, Steel, Water", "\nResistances: Bug, Fire, Flying, Normal, Poison", "\nImmunities: Ground")
    elif owo == (c + " " + g) or owo == (g + " " + c):
        print("Weaknesses: Electric, Fire, Flying, Ice, Rock", "\nResistances: Bug, Fighting, Grass", "\nImmunities: Ground")
    elif owo == (c + " " + h) or owo == (h + " " + c):
        print("Weaknesses: Dark, Electric, Ghost, Ice, Rock", "\nResistances: Bug, Grass, Poison", "\nImmunities: Fighting, Ground, Normal")
    elif owo == (c + " " + i) or owo == (i + " " + c):
        print("Weaknesses: Electric, Fire", "\nResistances: Bug, Dragon, Fairy, Flying, Grass, Normal, Psychic, Steel", "\nImmunities: Ground, Poison")
    elif owo == (c + " " + j) or owo == (j + " " + c):
        print("Weaknesses: Electric, Rock, Water", "\nResistances: Bug, Fairy, Fighting, Fire, Grass, Steel", "\nImmunities: Ground")
    elif owo == (c + " " + k) or owo == (k + " " + c):
        print("Weaknesses: Electric, Rock", "\nResistances: Bug, Fighting, Fire, Steel, Water", "\nImmunities: Ground")
    elif owo == (c + " " + l) or owo == (l + " " + c):
        print("Weaknesses: Fire, Flying, Ice, Poison, Rock", "\nResistances: Fighting, Grass, Water", "\nImmunities: Ground")
    elif owo == (c + " " + m) or owo == (m + " " + c):
        print("Weaknesses: Ice, Rock", "\nResistances: Bug, Fighting, Flying, Grass, Steel", "\nImmunities: Ground")
    elif owo == (c + " " + n) or owo == (n + " " + c):
        print("Weaknesses: Dark, Electric, Ghost, Ice, Rock", "\nResistances: Fighting, Grass, Psychic", "\nImmunities: Ground")
    elif owo == (c + " " + o) or owo == (o + " " + c):
        print("Weaknesses: Electric, Fire, Rock, Steel", "\nResistances: Bug, Grass", "\nImmunities: Ground")
    elif owo == (c + " " + p) or owo == (p + " " + c):
        print("Weaknesses: Dragon, Fairy, Ice, Rock", "\nResistances: Bug, Fighting, Fire, Grass, Water", "\nImmunities: Ground")
    elif owo == (c + " " + q) or owo == (q + " " + c):
        print("Weaknesses: Electric, Fairy, Ice, Rock", "\nResistances: Dark, Ghost, Grass", "\nImmunities: Ground, Psychic")
    elif owo == (c + " " + r) or owo == (r + " " + c):
        print("Weaknesses: Electric, Ice, Poison, Rock, Steel", "\nResistances: Bug, Dark, Fighting, Grass", "\nImmunities: Dragon, Ground")
    elif owo == (d + " " + e) or owo == (e + " " + d):
        print("Weaknesses: Ground, Ice, Psychic, Water", "\nResistances: Bug, Fairy, Fighting, Poison, Rock", "\nImmunities: Electric")
    elif owo == (d + " " + f) or owo == (f + " " + d):
        print("Weaknesses: Ground, Psychic, Steel, Water", "\nResistances: Bug, Fairy, Fire, Flying, Normal, Poison", "\nImmunities: None")
    elif owo == (d + " " + g) or owo == (g + " " + d):
        print("Weaknesses: Fire, Flying, Psychic, Rock", "\nResistances: Bug, Fairy, Fighting, Grass, Poison", "\nImmunities: None")
    elif owo == (d + " " + h) or owo == (h + " " + d):
        print("Weaknesses: Dark, Ghost, Ground, Psychic", "\nResistances: Bug, Fairy, Grass, Poison", "\nImmunities: Fighting, Normal")
    elif owo == (d + " " + i) or owo == (i + " " + d):
        print("Weaknesses: Fire, Ground", "\nResistances: Normal, Grass, Ice, Flying, Bug, Rock, Dragon, Steel, Fairy", "\nImmunities: Poison")
    elif owo == (d + " " + j) or owo == (j + " " + d):
        print("Weaknesses: Ground, Psychic, Rock, Water", "\nResistances: Bug, Fairy, Fighting, Fire, Grass, Ice, Poison, Steel", "\nImmunities: None")
    elif owo == (d + " " + k) or owo == (k + " " + d):
        print("Weaknesses: Electric, Ground, Psychic", "\nResistances: Bug, Fairy, Fighting, Fire, Ice, Poison, Steel, Water", "\nImmunities: None")
    elif owo == (d + " " + l) or owo == (l + " " + d):
        print("Weaknesses: Fire, Flying, Ice, Psychic", "\nResistances: Electric, Fairy, Fighting, Grass, Water", "\nImmunities: None")
    elif owo == (d + " " + m) or owo == (m + " " + d):
        print("Weaknesses: Ground, Psychic", "\nResistances: Electric, Grass, Fighting, Poison, Flying, Bug, Steel, Fairy", "\nImmunities: None")
    elif owo == (d + " " + n) or owo == (n + " " + d):
        print("Weaknesses: Ground, Ghost, Dark", "\nResistances: Grass, Fighting, Poison, Fairy", "\nImmunities: None")
    elif owo == (d + " " + o) or owo == (o + " " + d):
        print("Weaknesses: Fire, Ground, Psychic, Rock, Steel", "\nResistances: Grass, Ice, Poison, Bug, Fairy", "\nImmunities: None")
    elif owo == (d + " " + p) or owo == (p + " " + d):
        print("Weaknesses: Dragon, Ground, Ice, Psychic", "\nResistances: Bug, Electric, Fighting, Fire, Grass, Poison, Water", "\nImmunities: None")
    elif owo == (d + " " + q) or owo == (q + " " + d):
        print("Weaknesses: Ground", "\nResistances: Dark, Ghost, Grass, Poison", "\nImmunities: Psychic")
    elif owo == (d + " " + r) or owo == (r + " " + d):
        print("Weaknesses: Ground, Psychic, Steel", "\nResistances: Grass, Fighting, Bug, Dark, Fairy", "\nImmunities: Dragon")
    elif owo == (e + " " + f) or owo == (f + " " + e):
        print("Weaknesses: Fighting, Grass, Ground, Ice, Steel, Water", "\nResistances: Fire, Flying, Normal, Poison, Rock", "\nImmunities: Electric")
    elif owo == (e + " " + g) or owo == (g + " " + e):
        print("Weaknesses: Fire, Flying, Ice, Water", "\nResistances: Fighting, Ground, Poison", "\nImmunities: Electric")
    elif owo == (e + " " + h) or owo == (h + " " + e):
        print("Weaknesses: Dark, Ghost, Grass, Ice, Water", "\nResistances: Bug, Poison, Rock", "\nImmunities: Electric, Fighting, Normal")
    elif owo == (e + " " + i) or owo == (i + " " + e):
        print("Weaknesses: Fighting, Fire, Ground, Water", "\nResistances: Bug, Dragon, Fairy, Flying, Normal, Psychic, Rock, Steel", "\nImmunities: Electric, Poison")
    elif owo == (e + " " + j) or owo == (j + " " + e):
        print("Weaknesses: Ground, Water", "\nResistances: Bug, Fairy, Fire, Poison, Steel", "\nImmunities: Electric")
    elif owo == (e + " " + k) or owo == (k + " " + e):
        print("Weaknesses: Grass", "\nResistances: Fire, Poison, Rock, Steel", "\nImmunities: Electric")
    elif owo == (e + " " + l) or owo == (l + " " + e):
        print("Weaknesses: Bug, Fire, Flying, Ice", "\nResistances: Ground, Rock", "\nImmunities: Electric")
    elif owo == (e + " " + m) or owo == (m + " " + e):
        print("Weaknesses: Grass, Ground, Ice, Water", "\nResistances: Flying, Poison, Rock, Steel", "\nImmunities: Electric")
    elif owo == (e + " " + n) or owo == (n + " " + e):
        print("Weaknesses: Bug, Dark, Ghost, Grass, Ice, Water", "\nResistances: Fighting, Poison, Psychic, Rock", "\nImmunities: Electric")
    elif owo == (e + " " + o) or owo == (o + " " + e):
        print("Weaknesses: Fighting, Fire, Grass, Steel, Water", "\nResistances: Poison", "\nImmunities: Electric")
    elif owo == (e + " " + p) or owo == (p + " " + e):
        print("Weaknesses: Dragon, Fairy, Ice", "\nResistances: Fire, Poison, Rock", "\nImmunities: Electric")
    elif owo == (e + " " + q) or owo == (q + " " + e):
        print("Weaknesses: Bug, Fairy, Fighting, Grass, Ice, Water", "\nResistances: Dark, Ghost, Poison, Rock", "\nImmunities: Electric, Psychic")
    elif owo == (e + " " + r) or owo == (r + " " + e):
        print("Weaknesses: Water, Grass, Ice, Steel", "\nResistances: Fighting, Bug, Rock, Dark", "\nImmunities: Electric, Dragon")
    elif owo == (f + " " + g) or owo == (g + " " + f):
        print("Weaknesses: Rock, Steel, Water", "\nResistances: Normal, Poison", "\nImmunities: None")
    elif owo == (f + " " + h) or owo == (h + " " + f):
        print("Weaknesses: Water, Grass, Ground, Ghost, Dark, Steel", "\nResistances: Fire, Poison, Flying, Bug", "\nImmunities: Normal, Fighting")
    elif owo == (f + " " + i) or owo == (i + " " + f):
        print("Weaknesses: Fighting, Ground, Water", "\nResistances: Bug, Dragon, Fairy, Flying, Ice, Normal, Psychic, Rock", "\nImmunities: Poison")
    elif owo == (f + " " + j) or owo == (j + " " + f):
        print("Weaknesses: Fighting, Ground, Rock, Water", "\nResistances: Bug, Fairy, Fire, Flying, Ice, Normal, Poison", "\nImmunities: None")
    elif owo == (f + " " + k) or owo == (k + " " + f):
        print("Weaknesses: Electric, Fighting, Grass, Ground", "\nResistances: Fire, Flying, Ice, Normal, Poison", "\nImmunities: None")
    elif owo == (f + " " + l) or owo == (l + " " + f):
        print("Weaknesses: Bug, Fighting, Ice, Steel", "\nResistances: Electric, Normal", "\nImmunities: None")
    elif owo == (f + " " + m) or owo == (m + " " + f):
        print("Weaknesses: Fighting, Grass, Ground, Water", "\nResistances: Electric, Fire, Flying, Normal, Poison", "\nImmunities: None")
    elif owo == (f + " " + n) or owo == (n + " " + f):
        print("Weaknesses: Bug, Dark, Ghost, Grass, Ground, Steel, Water", "\nResistances: Fire, Flying, Normal, Poison, Psychic", "\nImmunities: None")
    elif owo == (f + " " + o) or owo == (o + " " + f):
        print("Weaknesses: Fighting, Grass, Ground, Rock, Steel, Water", "\nResistances: Flying, Ice, Normal, Poison", "\nImmunities: None")
    elif owo == (f + " " + p) or owo == (p + " " + f):
        print("Weaknesses: Dragon, Fairy, Fighting, Ground, Ice, Steel", "\nResistances: Electric, Fire, Flying, Normal, Poison", "\nImmunities: None")
    elif owo == (f + " " + q) or owo == (q + " " + f):
        print("Weaknesses: Bug, Fairy, Fighting, Grass, Ground, Steel, Water", "\nResistances: Dark, Fire, Flying, Ghost, Normal, Poison", "\nImmunities: Psychic")
    elif owo == (f + " " + r) or owo == (r + " " + f):
        print("Weaknesses: Grass, Ground, Steel, Water", "\nResistances: Bug, Dark, Fire, Flying, Normal", "\nImmunities: Dragon")
    elif owo == (g + " " + h) or owo == (h + " " + g):
        print("Weaknesses: Dark, Fire, Flying, Ghost, Rock", "\nResistances: Bug, Grass, Ground, Poison", "\nImmunities: Fighting, Normal")
    elif owo == (g + " " + i) or owo == (i + " " + g):
        print("Weaknesses: Fire", "\nResistances: Bug, Dragon, Fairy, Grass, Ice, Normal, Psychic, Steel", "\nImmunities: Poison")
    elif owo == (g + " " + j) or owo == (j + " " + g):
        print("Weaknesses: Flying, Rock, Water", "\nResistances: Bug, Fairy, Fighting, Grass, Ice, Steel", "\nImmunities: None")
    elif owo == (g + " " + k) or owo == (k + " " + g):
        print("Weaknesses: Electric, Flying, Rock", "\nResistances: Fighting, Ground, Ice, Steel, Water", "\nImmunities: None")
    elif owo == (g + " " + l) or owo == (l + " " + g):
        print("Weaknesses: Bug, Fire, Flying, Ice, Poison, Rock", "\nResistances: Electric, Fighting, Grass, Ground, Water", "\nImmunities: None")
    elif owo == (g + " " + m) or owo == (m + " " + g):
        print("Weaknesses: Fire, Rock", "\nResistances: Electric, Fighting, Grass, Steel", "\nImmunities: None")
    elif owo == (g + " " + n) or owo == (n + " " + g):
        print("Weaknesses: Fire, Flying, Bug, Rock, Ghost, Dark", "\nResistances: Grass, Fighting, Ground, Psychic", "\nImmunities: None")
    elif owo == (g + " " + o) or owo == (o + " " + g):
        print("Weaknesses: Fire, Flying, Rock, Steel", "\nResistances: Grass, Ice, Ground", "\nImmunities: None")
    elif owo == (g + " " + p) or owo == (p + " " + g):
        print("Weaknesses: Ice, Flying, Rock, Dragon, Fairy", "\nResistances: Water, Electric, Fighting, Ground", "\nImmunities: None")
    elif owo == (g + " " + q) or owo == (q + " " + g):
        print("Weaknesses: Fire, Flying, Bug, Rock, Fairy", "\nResistances: Grass, Ground, Ghost, Dark", "\nImmunities: Psychic")
    elif owo == (g + " " + r) or owo == (r + " " + g):
        print("Weaknesses: Fire, Flying, Poison, Rock, Steel", "\nResistances: Bug, Dark, Fighting, Grass, Ground", "\nImmunities: Dragon")
    elif owo == (h + " " + i) or owo == (i + " " + h):
        print("Weaknesses: Dark, Fire, Ghost, Ground", "\nResistances: Bug, Dragon, Fairy, Flying, Grass, Ice, Psychic, Rock, Steel", "\nImmunities: Fighting, Normal, Poison")
    elif owo == (h + " " + j) or owo == (j + " " + h):
        print("Weaknesses: Dark, Ghost, Ground, Rock, Water", "\nResistances: Bug, Fairy, Fire, Grass, Ice, Poison, Steel", "\nImmunities: Fighting, Normal")
    elif owo == (h + " " + k) or owo == (k + " " + h):
        print("Weaknesses: Dark, Electric, Ghost, Grass", "\nResistances: Bug, Fire, Ice, Poison, Steel, Water", "\nImmunities: Fighting, Normal")
    elif owo == (h + " " + l) or owo == (l + " " + h):
        print("Weaknesses: Dark, Fire, Flying, Ghost, Ice", "\nResistances: Electric, Grass, Ground, Water", "\nImmunities: Fighting, Normal")
    elif owo == (h + " " + m) or owo == (m + " " + h):
        print("Weaknesses: Dark, Ghost, Ground", "\nResistances: Bug, Electric, Flying, Poison, Steel", "\nImmunities: Fighting, Normal")
    elif owo == (h + " " + n) or owo == (n + " " + h):
        print("Weaknesses: Dark, Ghost", "\nResistances: Poison, Psychic", "\nImmunities: Fighting, Normal")
    elif owo == (h + " " + o) or owo == (o + " " + h):
        print("Weaknesses: Dark, Fire, Ghost, Rock, Steel", "\nResistances: Bug, Ice, Poison", "\nImmunities: Fighting, Normal")
    elif owo == (h + " " + p) or owo == (p + " " + h):
        print("Weaknesses: Dark, Dragon, Fairy, Ghost, Ice", "\nResistances: Bug, Electric, Fire, Grass, Poison, Water", "\nImmunities: Fighting, Normal")
    elif owo == (h + " " + q) or owo == (q + " " + h):
        print("Weaknesses: Fairy", "\nResistances: Poison", "\nImmunities: Fighting, Normal, Psychic")
    elif owo == (h + " " + r) or owo == (r + " " + h):
        print("Weaknesses: Ghost, Steel", "\nResistances: Bug", "\nImmunities: Dragon, Fighting, Normal")
    elif owo == (i + " " + j) or owo == (j + " " + i):
        print("Weaknesses: Fighting, Ground, Water", "\nResistances: Bug, Dragon, Fairy, Flying, Grass, Ice, Normal, Psychic, Steel", "\nImmunities: Poison")
    elif owo == (i + " " + k) or owo == (k + " " + i):
        print("Weaknesses: Electric, Fighting, Ground", "\nResistances: Bug, Dragon, Fairy, Flying, Ice, Normal, Psychic, Rock, Steel, Water", "\nImmunities: Poison")
    elif owo == (i + " " + l) or owo == (l + " " + i):
        print("Weaknesses: Fighting, Fire", "\nResistances: Dragon, Electric, Fairy, Grass, Normal, Psychic, Rock, Steel, Water", "\nImmunities: Poison")
    elif owo == (i + " " + m) or owo == (m + " " + i):
        print("Weaknesses: Fighting, Fire, Ground", "\nResistances: Bug, Dragon, Electric, Fairy, Flying, Grass, Ice, Normal, Psychic, Rock, Steel", "\nImmunities: Poison")
    elif owo == (i + " " + n) or owo == (n + " " + i):
        print("Weaknesses: Dark, Fire, Ghost, Ground", "\nResistances: Dragon, Fairy, Flying, Grass, Ice, Normal, Psychic, Rock, Steel", "\nImmunities: Poison")
    elif owo == (i + " " + o) or owo == (o + " " + i):
        print("Weaknesses: Fighting, Fire, Ground", "\nResistances: Bug, Dragon, Fairy, Flying, Grass, Ice, Normal, Psychic", "\nImmunities: Poison")
    elif owo == (i + " " + p) or owo == (p + " " + i):
        print("Weaknesses: Fighting, Ground", "\nResistances: Bug, Electric, Flying, Grass, Normal, Psychic, Rock, Steel, Water", "\nImmunities: Poison")
    elif owo == (i + " " + q) or owo == (q + " " + i):
        print("Weaknesses: Fighting, Fire, Ground", "\nResistances: Dark, Dragon, Flying, Ghost, Grass, Ice, Normal, Rock, Steel", "\nImmunities: Poison, Psychic")
    elif owo == (i + " " + r) or owo == (r + " " + i):
        print("Weaknesses: Fire, Ground", "\nResistances: Bug, Dark, Fairy, Flying, Grass, Ice, Normal, Psychic, Rockl", "\nImmunities: Dragon, Poison")
    elif owo == (j + " " + k) or owo == (k + " " + j):
        print("Weaknesses: Electric, Ground, Rock", "\nResistances: Bug, Fairy, Fire, Ice, Steel", "\nImmunities: None")
    elif owo == (j + " " + l) or owo == (l + " " + j):
        print("Weaknesses: Poison, Flying, Rock", "\nResistances: Electric, Grass, Steel, Fairy", "\nImmunities: None")
    elif owo == (j + " " + m) or owo == (m + " " + j):
        print("Weaknesses: Ground, Rock, Water", "\nResistances: Bug, Electric, Fairy, Fire, Flying, Grass, Ice, Steel", "\nImmunities: None")
    elif owo == (j + " " + n) or owo == (n + " " + j):
        print("Weaknesses: Dark, Ghost, Ground, Rock, Water", "\nResistances: Fairy, Fighting, Fire, Grass, Ice, Psychic, Steel", "\nImmunities: None")
    elif owo == (j + " " + o) or owo == (o + " " + j):
        print("Weaknesses: Water, Fighting, Ground, Rock", "\nResistances: Grass, Ice, Bug, Fairy", "\nImmunities: None")
    elif owo == (j + " " + p) or owo == (p + " " + j):
        print("Weaknesses: Dragon, Ground, Rock", "\nResistances: Bug, Electric, Fire, Grass, Steel", "\nImmunities: None")
    elif owo == (j + " " + q) or owo == (q + " " + j):
        print("Weaknesses: Fighting, Ground, Rock, Water", "\nResistances: Dark, Fire, Ghost, Grass, Ice, Steel", "\nImmunities: Psychic")
    elif owo == (j + " " + r) or owo == (r + " " + j):
        print("Weaknesses: Water, Poison, Ground, Rock", "\nResistances: Fire, Grass, Ice, Fighting, Bug, Dark, Fairy", "\nImmunities: Dragon")
    elif owo == (k + " " + l) or owo == (l + " " + k):
        print("Weaknesses: Bug, Flying, Poison", "\nResistances: Ground, Steel, Water", "\nImmunities: None")
    elif owo == (k + " " + m) or owo == (m + " " + k):
        print("Weaknesses: Grass, Ground", "\nResistances: Fire, Flying, Ice, Steel, Water", "\nImmunities: None")
    elif owo == (k + " " + n) or owo == (n + " " + k):
        print("Weaknesses: Bug, Dark, Electric, Ghost, Grass", "\nResistances: Fighting, Fire, Ice, Psychic, Steel, Water", "\nImmunities: None")
    elif owo == (k + " " + o) or owo == (o + " " + k):
        print("Weaknesses: Electric, Fighting, Grass, Rock", "\nResistances: Ice, Water", "\nImmunities: None")
    elif owo == (k + " " + p) or owo == (p + " " + k):
        print("Weaknesses: Dragon, Fairy", "\nResistances: Fire, Steel, Water", "\nImmunities: None")
    elif owo == (k + " " + q) or owo == (q + " " + k):
        print("Weaknesses: Bug, Electric, Fairy, Fighting, Grass", "\nResistances: Dark, Fire, Ghost, Ice, Steel, Water", "\nImmunities: Psychic")
    elif owo == (k + " " + r) or owo == (r + " " + k):
        print("Weaknesses: Electric, Grass, Poison", "\nResistances: Bug, Dark, Fighting, Fire, Ice, Water", "\nImmunities: Dragon")
    elif owo == (l + " " + m) or owo == (m + " " + l):
        print("Weaknesses: Bug, Fire, Ice, Poison", "\nResistances: Electric, Grass, Steel, Water", "\nImmunities: None")
    elif owo == (l + " " + n) or owo == (n + " " + l):
        print("Weaknesses: Bug, Dark, Fire, Flying, Ghost, Ice, Poison", "\nResistances: Electric, Fighting, Grass, Ground, Psychic, Water", "\nImmunities: None")
    elif owo == (l + " " + o) or owo == (o + " " + l):
        print("Weaknesses: Bug, Fighting, Fire, Flying, Poison, Rock, Steel", "\nResistances: Electric, Grass, Ground, Water", "\nImmunities: None")
    elif owo == (l + " " + p) or owo == (p + " " + l):
        print("Weaknesses: Bug, Dragon, Fairy, Flying, Ice, Poison", "\nResistances: Electric, Grass, Ground, Water", "\nImmunities: None")
    elif owo == (l + " " + q) or owo == (q + " " + l):
        print("Weaknesses: Bug, Fairy, Fighting, Fire, Flying, Ice, Poison", "\nResistances: Dark, Electric, Ghost, Grass, Ground, Water", "\nImmunities: Psychic")
    elif owo == (l + " " + r) or owo == (r + " " + l):
        print("Weaknesses: Fire, Flying, Ice, Poison, Steel", "\nResistances: Dark, Electric, Fighting, Grass, Ground, Water", "\nImmunities: Dragon")
    elif owo == (m + " " + n) or owo == (n + " " + m):
        print("Weaknesses: Bug, Dark, Ghost, Ground", "\nResistances: Electric, Fighting, Flying, Psychic, Steel", "\nImmunities: None")
    elif owo == (m + " " + o) or owo == (o + " " + m):
        print("Weaknesses: Fighting, Fire, Ground, Rock", "\nResistances: Electric, Flying, Ice", "\nImmunities: None")
    elif owo == (m + " " + p) or owo == (p + " " + m):
        print("Weaknesses: Dragon, Fairy, Ground, Ice", "\nResistances: Electric, Fire, Flying, Grass, Steel, Water", "\nImmunities: None")
    elif owo == (m + " " + q) or owo == (q + " " + m):
        print("Weaknesses: Fighting, Ground, Bug, Fairy", "\nResistances: Electric, Flying, Ghost, Dark", "\nImmunities: Psychic")
    elif owo == (m + " " + r) or owo == (r + " " + m):
        print("Weaknesses: Ground, Poison", "\nResistances: Bug, Dark, Electric, Fighting, Flying", "\nImmunities: Dragon")
    elif owo == (n + " " + o) or owo == (o + " " + n):
        print("Weaknesses: Bug, Dark, Fire, Ghost, Rock, Steel", "\nResistances: Ice, Psychic", "\nImmunities: None")
    elif owo == (n + " " + p) or owo == (p + " " + n):
        print("Weaknesses: Bug, Dark, Dragon, Fairy, Ghost, Ice", "\nResistances: Electric, Fighting, Fire, Grass, Psychic, Water", "\nImmunities: None")
    elif owo == (n + " " + q) or owo == (q + " " + n):
        print("Weaknesses: Bug, Fairy", "\nResistances: None", "\nImmunities: Psychic")
    elif owo == (n + " " + r) or owo == (r + " " + n):
        print("Weaknesses: Ghost, Poison, Steel", "\nResistances: Fighting, Psychic", "\nImmunities: Dragon")
    elif owo == (o + " " + p) or owo == (p + " " + o):
        print("Weaknesses: Dragon, Fairy, Fighting, Rock, Steel", "\nResistances: Electric, Grass, Water", "\nImmunities: None")
    elif owo == (o + " " + q) or owo == (q + " " + o):
        print("Weaknesses: Bug, Fairy, Fighting, Fire, Rock, Steel", "\nResistances: Dark, Ghost, Ice", "\nImmunities: Psychic")
    elif owo == (o + " " + r) or owo == (r + " " + o):
        print("Weaknesses: Fire, Poison, Rock, Steel", "\nResistances: Bug, Dark, Ice", "\nImmunities: Dragon")
    elif owo == (p + " " + q) or owo == (q + " " + p):
        print("Weaknesses: Bug, Dragon, Fairy, Fighting, Ice", "\nResistances: Dark, Electric, Fire, Ghost, Grass, Water", "\nImmunities: Psychic")
    elif owo == (p + " " + r) or owo == (r + " " + p):
        print("Weaknesses: Fairy, Ice, Poison, Steel", "\nResistances: Bug, Dark, Electric, Fighting, Fire, Grass, Water", "\nImmunities: Dragon")
    elif owo == (q + " " + r) or owo == (r + " " + q):
        print("Weaknesses: Poison, Steel, Fairy", "\nResistances: Ghost, Dark", "\nImmunities: Psychic, Dragon")
    elif owo == ("types"):
        print(types)
    elif owo == ("who"):
        print("Made by HappySylveon")


    time.sleep(1)
