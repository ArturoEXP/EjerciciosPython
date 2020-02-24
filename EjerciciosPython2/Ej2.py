caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
guerrero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
arquero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }

caballero['vida'] = int(guerrero['vida']) * 2
caballero['defensa'] = int(guerrero['defensa']) * 2
guerrero['ataque'] = int(caballero['ataque']) * 2
guerrero['alcance'] = int(guerrero['alcance']) * 2
arquero['ataque'] = guerrero['ataque']
arquero['alcance'] = int(guerrero['alcance']) * 2
arquero['vida'] = arquero['vida']
arquero['defensa'] = int(guerrero['defensa'] / 2)

print(caballero)
print(guerrero)
print(arquero)