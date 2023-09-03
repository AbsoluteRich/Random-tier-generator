import random


def generate_tower(limit: int = 1, crosspath: bool = True):
    path = [0, 0, 0]
    chosen_paths = []

    path_index = random.randint(0, 2)
    upgrade = random.randint(1, limit)
    if upgrade == 6:  # If a 6-x-x tower is generated, return a 5-5-5 to signify a Paragon
        return [5, 5, 5]

    path[path_index] = upgrade
    chosen_paths.append(path_index)

    if crosspath and path_index > 0:
        path_index = random.randint(0, 2)
        while path_index in chosen_paths:
            path_index = random.randint(0, 2)

        upgrade = random.randint(1, 2)
        path[path_index] = upgrade
        chosen_paths.append(path_index)

    return path


if __name__ == '__main__':
    list_of_towers = [
        "Dart Monkey",
        "Boomerang Monkey",
        "Bomb Shooter",
        "Tack Shooter",
        "Ice Monkey",
        "Glue Gunner",
        "Sniper Monkey",
        "Monkey Sub",
        "Monkey Buccaneer",
        "Monkey Ace",
        "Heli Pilot",
        "Mortar Monkey",
        "Dartling Gunner",
        "Wizard Monkey",
        "Super Monkey",
        "Ninja Monkey",
        "Alchemist",
        "Druid",
        "Banana Farm",
        "Spike Factory",
        "Monkey Village",
        "Engineer Monkey",
        "Beast Handler"]
    game_phase = 1

    while True:
        console = input(f"{game_phase} >> ")
        try:
            int(console)
        except ValueError or TypeError:
            upgrade = '-'.join(map(str, generate_tower(game_phase)))
            tower = random.choice(list_of_towers)
            print(f"You must place a [{upgrade}] {tower}")
        else:
            game_phase = int(console)
            print("Updated.")
