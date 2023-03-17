import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # encode password > get sha1 hash object > convert to hexadecimal string > convert string to upper case
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # get the first 5 characters of the sha1password, and the rest of password
    first5_char, tail = sha1password[:5], sha1password[5:]

    # request the API server for passwords starting with the first 5 characters
    res = request_api_data(first5_char)

    # from the API response, grab the one that matches our password tail and return count
    return get_password_leaks_count(res, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times.. you should change your password')
        else:
            print(f'{password} was not found. Your password is safe!')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
