# Modelo de rotina para sorteio de strings com orderm aleatória utilizando o módulo random shuffle.
# Exemplo abaixo: sorteio da ordem de prioridade da biblioteca de jogos para serem jogados.

from random import shuffle
lista = [
    'PUBG Mobile',
    'COD Mobile',
    'PES Mobile',
    'Fifa 18',
    'Diablo 3 Reaper of Souls',
    'Gta San Andreas',
    'Assassins Creed Unity',
    'Paladins',
    'Destiny 2',
    'Monster Hunter World',
    'Risk of Rain',
    'Divinity Original Sin(Classic)',
    'Divinity Original Sin Enhanced Edition',
    'Terraria',
    'Bloodstained Ritual of the Night',
    'Trilogia Batman Arkham Knight',
    'Rayman Legends',
    'Surviving Mars',
    'Metro: 2033 Redux',
    'Alan Wake American Nightmare',
    ]
shuffle(lista)
for n, x in enumerate(lista):
    print(n, x)
