import random
import string
import logging as logger

def generate_random_string(length=10, prefix=None, suffix=None):

    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))

    if prefix:
        random_string = prefix + random_string
    if suffix:
        random_string = random_string + suffix

    return random_string
    
def generate_random_email_and_password(domain='supersqa.com', email_prefix='testuser', elength=10):
    """
    Generates a random email and password combination.
    :param domain:
    :param email_prefix:
    :return: dictionary. A dictionary with keys 'email' & 'password'
    """

    random_string = ''.join(random.choices(string.ascii_lowercase, k=elength))
    # email = email_prefix + '_' + random_string + '@' + domain
    email = f'{email_prefix}_{random_string}@{domain}'

    password_length = 20
    password_string = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f"Randomly generated email and password: {random_info}")

    return random_info

