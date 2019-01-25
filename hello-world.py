hello = True

while hello:
	print('Hello, world!')
	bye = input('Goodbye, world? ')
	if bye == 'y' or bye == 'yes':
		hello = False
		print('Bye!')
	elif bye == 'n' or bye == 'no':
		continue
	else:
		bye = input('Please type "yes" or "no." ')
		if bye == 'yes' or bye == 'y':
			print('Bye!')
			hello = False
