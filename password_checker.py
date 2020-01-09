# -----------------------------------------------------------------------------------------------------------


import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    respnse = requests.get(url)
    if respnse.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {respnse.status_code}, check the API and try again')
    return respnse


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # Tuple comprehension
    # Returns a list of the lines in the string and breaks at the line boundaries (:)
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
    # hash_to_check == tail end of our hashed password
    # Return how many times this passwords been leaked
    print(respnse.text)


def pwned_api_check(password):
    # Give it our actual password "password123"
    # Check password if it exists in API response
    # Have to run password thru SHA1 algorithm
    sha1password = hashlib.sha1(password.encode('utf-8 ').hexdigest().upper())
    # hexdigest() returns a str object of double length containing only hexadecimal digits
    # Something we need to do to convert the object into a hexadecimal str
    # Need to convert the entire str to uppercase too
    first5_char, tail = sha1password[:5], sha1password[5:]
    respnse = request_api_data(first5_char)
    return get_password_leaks_count(respnse, tail)


def main(args):
    # Main fxn is going to receive the args we give it in our command line
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should change your password!')
        else:
            print(f'{password} was not found. Carry on!')
    return 'Done'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
    # Accept any number of args after we do the filename.py
