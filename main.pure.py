from abc import ABC, abstractmethod

# Абстрактный класс оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Класс меча
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

# Класс лука
class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"

# Класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def attack_with_weapon(self):
        action = self.weapon.attack()
        print(f"Боец {action}.")

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print("Боец выбирает новое оружие.")

# Класс монстра
class Monster:
    def __init__(self, health):
        self.health = health

    def is_defeated(self):
        return self.health <= 0

# Функция для симуляции боя
def battle(fighter, monster):
    while not monster.is_defeated():
        fighter.attack_with_weapon()
        monster.health -= 10  # Предполагаем, что каждая атака уменьшает здоровье монстра на 10
        if monster.is_defeated():
            print("Монстр побежден!")

# Создание бойца с мечом
sword = Sword()
fighter = Fighter(sword)

# Создание монстра
monster = Monster(health=40)

# Бой
print("Бой начинается.")
battle(fighter, monster)

# Изменение оружия на лук
bow = Bow()
fighter.change_weapon(bow)

# Новый монстр
new_monster = Monster(health=20)
print("Новый монстр появляется.")
battle(fighter, new_monster)
