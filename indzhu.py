class Brawler:
    def _init_(self, name, health, armor, weapon, attack_power):
        self.name = name
        self.health = health
        self.armor = armor
        self.weapon = weapon
        self.attack_power = attack_power

    # метод приветствия
    def greet(self):
        print(f"Я бравлер {self.name}! У меня {self.health} HP и оружие: {self.weapon}")

    # метод атаки
    def attack(self, enemy):
        damage = self.attack_power - enemy.armor
        if damage < 0:
            damage = 0

        enemy.health -= damage
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона!")
        print(f"У {enemy.name} осталось {enemy.health} здоровья")


# создаём бравлеров
b1 = Brawler("Шелли", 5000, 100, "дробовик", 400)
b2 = Brawler("Кольт", 4500, 50, "пистолеты", 350)

# проверка
b1.greet()
b2.greet()

b1.attack(b2)
b2.attack(b1)