from kanren import Relation, facts, run, var
from kanren.core import lall, conde

homem = Relation()
mulher = Relation()
progenitor = Relation()

facts(homem, "jose", "joao", "mario", "carlos")
facts(mulher, "maria", "ana", "helena", "joana")

facts(progenitor, 
      ("jose", "joao"), 
      ("maria", "joao"),
      ("jose", "ana"), 
      ("maria", "ana"),
      ("ana", "helena"),
      ("ana", "joana"),
      ("joao", "mario"),
      ("helena", "carlos"),
      ("mario", "carlos")
)

def pai(x, y):
    return lall(progenitor(x, y), homem(x))

def mae(x, y):
    return lall(progenitor(x, y), mulher(x))

def filho(x, y):
    return lall(progenitor(y, x), homem(x))

def filha(x, y):
    return lall(progenitor(y, x), mulher(x))

def irmao(x, y):
    p = var()
    return lall(progenitor(p, x), progenitor(p, y), homem(x), (x != y))

def irma(x, y):
    p = var()
    return lall(progenitor(p, x), progenitor(p, y), mulher(x), (x != y))

def primo(x, y):
    px, py = var(), var()
    return lall(
        progenitor(px, x),
        progenitor(py, y),
        irmao(px, py),
        (x != y)
    )

def gerou(x, y):
    return conde([pai(x, y)], [mae(x, y)])

x = var()

# a) Joana é filha de Ana?
resposta_a = run(0, x, filha("joana", "ana"))

# b) Quem são os filhos de Maria?
resposta_b = run(0, x, filho(x, "maria"))

# c) Mário é primo de José?
resposta_c = run(0, x, primo("mario", "jose"))

# d) Quem é a mãe de Carlos?
resposta_d = run(0, x, mae(x, "carlos"))

# e) Quem gerou Helena?
resposta_e = run(0, x, gerou(x, "helena"))

# Resultados
print("a) Joana é filha de Ana?", bool(resposta_a))
print("b) Filhos de Maria:", resposta_b)
print("c) Mário é primo de José?", bool(resposta_c))
print("d) Mãe de Carlos:", resposta_d)
print("e) Quem gerou Helena:", resposta_e)
