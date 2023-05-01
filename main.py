# Test python env

def print_hello():
    animals = ['dogs', 'cat', 'hamster', 'tigers'] # in one line
    foods = [
	'Spaghetti',
	'Pizza',
	'bibimbab'
    ] # without trailing comma
    names = [
        'John',
        'Jane',
	'Gil-dong',
	'Dong-eun',
    ] # with trailing comma
    for f_name in names:
        print(f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()
