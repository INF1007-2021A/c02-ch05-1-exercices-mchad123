#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	TAX_RATE = 0.15

	sum = 0
	for item in data:
		qty = item[INDEX_QUANTITY]
		price = item[INDEX_PRICE]
		sum += qty * price

	taxes = TAX_RATE * sum
	total = sum + taxes

	formatted_bill = name
	#solution sans répétition
	bill_lines = [
		("SOUS TOTAL", sum),
		("TAXES     ", taxes),
		("TOTAL     ", total)
	]
	# avec la boucle for tu passes a travers toutes les lignes
	# du tableau et tu affiches le contenu
	for line in bill_lines:
		formatted_bill += "\n" + f"{line[0]} {line[1]:>10.2f} $"
	# solution avec réptétition de code
	# "\n" veut dire retour a la ligne, newline
	# 10.2f veut dire formater float avec 10 chiffres avant la virgule et 2 apres
	# remplir d'Espaces les chiffres manquants
	# :> alignement a droite
	# :< alignement a gauche

	# Sans la boucle for tu dois passer le meme code pour chaque ligne
	# ce qui n'est pas du bon code
	formatted_bill += "\n" + f"SOUS TOTAL {sum:>10.2f} $"
	formatted_bill += "\n" + f"TAXES      {taxes:>10.2f} $"
	formatted_bill += "\n" + f"TOTAL      {total:>10.2f} $"


	return ""


def format_number(number, num_decimal_digits):
	return ""

def get_triangle(num_rows):
	BORDER_CHAR = "+"
	TRIANGLE_CHAR = "A"

	triangle_width = 1 + 2 * (num_rows - 1)

	border_row = (triangle_width + 2) * BORDER_CHAR

	result = border_row
	#pour chaque rangée du triangle
	for i in range(num_rows):
		num_triangle_chars = 1 + 2 * i
		#ajouter un retour de ligne
		result += "\n"
		# ajouter un plus
		result += "+"
		# ajouter les espaces
		result += " " * (triangle_width - num_triangle_chars) // 2
		# ajouter les 'A'
		result += TRIANGLE_CHAR * num_triangle_chars
		# ajouter les espaces
		" " * (triangle_width - num_triangle_chars) // 2
		# ajouter les + 
		result += BORDER_CHAR
		# ajouter la rangée
	result += "\n" + border_row
	return result


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
	sum = 765.8765453
	print(f"SOUS TOTAL {sum:<10.2f} $")
	print(f"SOUS TOTAL {sum:>10.2f} $")
