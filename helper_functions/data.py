import random
import string

class PersonalData:
    login_email = 'lunina_17_qa-python_theory_123@ya.ru'
    login_password = 'qwerty_17_qa-python_theory'
    login_name = 'Анастасия'

class RandomUserGenerator:
    def __init__(self):
        self.domains = ['gmail.com', 'ya.ru', 'rambler.ru', 'icloud.com', 'yandex.com']
        self.first_names = ['Анастасия', 'Антон', 'Максим', 'Ольга', 'Владимир', 'Ксения']

    def generate_name(self):
        first_name = random.choice(self.first_names)
        return first_name

    def generate_email(self, name):
        username = name.replace(" ", ".").lower()
        domain = random.choice(self.domains)
        return f"{username}@{domain}"

    def generate_password(self, length=8):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    def generate_user(self, password_length=8):
        name = self.generate_name()
        email = self.generate_email(name)
        password = self.generate_password(password_length)
        return {
            "name": name,
            "email": email,
            "password": password
        }