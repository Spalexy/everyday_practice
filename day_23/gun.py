
class OutOfMagazines(Exception):
    pass


class Gun:
    def __init__(self):
        self.magazines = 10
        self.magazine_capacity = 15
        self.bullets_in_the_current_magazine = 0

    def get_magazines_amount(self):
        return self.magazines

    def get_bullets_amount(self):
        return self.magazine_capacity * self.magazines + self.bullets_in_the_current_magazine

    def take_a_shot(self):
        if self.bullets_in_the_current_magazine == 0:
            self.reload()
        self.bullets_in_the_current_magazine -= 1
        print("Puf!")

    def reload(self):
        if self.magazines > 0:
            self.magazines -= 1
            self.bullets_in_the_current_magazine = self.magazine_capacity
            print("Reloaded")
        else:
            raise OutOfMagazines('No ammunition')


gun = Gun()


print(gun.get_bullets_amount())
gun.take_a_shot()
print(gun.get_magazines_amount())
print(gun.get_bullets_amount())

gun.reload()
gun.take_a_shot()

print(gun.get_magazines_amount())
print(gun.get_bullets_amount())
