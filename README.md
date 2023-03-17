# password-checker

checkmypass.py is a Python script that checks whether your password has been exposed in data breaches. The script uses the API provided on the [haveibeenpwned](https://haveibeenpwned.com/API/v3#PwnedPasswords) website.

The script works better than direct searching on the webpage due to 3 reasons:
1. Using the API locally on your own machine prevents direct input of your password on the internet, therefore preventing your password from being stored by your browser or some foreign server somewhere in the world.
2. The password is stored as a SHA-1 hash.
3. The API also implements a k-Anonymity model that only searches the password by partial hash.

To run the script, type the following in your terminal:
`python checkmypass.py <password1> <password2>`

You can check as many passwords as you want, with each password being separated by a space.
