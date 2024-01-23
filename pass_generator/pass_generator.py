import random


class PassGenerator:

    def pass_generator(self, length, upper, special, numbers):
        char_list = list('abcdefghijklmnopqrstuvxyz')
        generated_password = ''

        if upper:
            char_list.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

        if special:
            char_list.extend(list('_-?[]?$%&#@'))

        if numbers:
            char_list.extend(list('123456789'))

        for x in range(length):
            generated_password += random.choice(char_list)
        return generated_password
