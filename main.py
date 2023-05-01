# Test python env

def print_hello():
    animals = ['dogs', 'cat', 'hamster'] # in one line
    foods = [
	'Spaghetti',
	'Pizza'
    ] # without trailing comma
    names = [
        'John',
        'Jane',
	'Gil-dong',
    ] # with trailing comma
    for f_name in names:
        print(f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()
