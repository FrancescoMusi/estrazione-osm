from random import randint

giocatori = []
squadre = []
giocatori_ext = []
squadre_ext = []

print("----------------------------")
print("estrazione posti OSM")
print("\"Q\" per uscire dall'elenco")
print("----------------------------")
print()
print("GIOCATORI:")

while True:
	while True:
		player = input("player: ")
		if player == "q" or player == "Q":
			break
		else:
			giocatori.append(player)

	print()
	print("SQUADRE:")

	while True:
		team = input("team: ")
		if team == "q" or team == "Q":
			break
		else:
			squadre.append(team)

	if len(squadre) != len(giocatori):
		print("Il numero di squadre e giocatori non coincide:")
		print("Ricomincia")
		print()
	else:
		break

print()

while len(giocatori_ext) < len(giocatori):
	input("premi invio")

	while True:
		estrazioe_gioc = giocatori[randint(0, len(giocatori)-1)]
		if not estrazioe_gioc in giocatori_ext:
			giocatori_ext.append(estrazioe_gioc)
			break

	while True:
		estrazioe_sq = squadre[randint(0, len(squadre)-1)]
		if not estrazioe_sq in squadre_ext:
			squadre_ext.append(estrazioe_sq)
			break

	print("Il/la", estrazioe_sq, "è di", estrazioe_gioc)