def fizz_buzz(begin, and):
	if begin > end:
		return ''
	else:
		source = ''
		for i in range (begin, end+1):
			if i % 3 == 0 and i % 5 == 0:
				source += 'FizzBuzz '
			elif i % 3 == 0:
				source += 'Fizz '
			elif i % 5 == 0:
				source += 'Buzz '
			else:
				source += f'{str(i)} '
	return source[:len(source)-1]
