import re
from aoc import read_input
import math
from typing import Self
from copy import deepcopy

lines = read_input(split_lines=False)
armies_str = lines.split("\n\n")


class Group:
    def __init__(
        self,
        num_units,
        unit_hp,
        unit_attack,
        initiative,
        attack_type,
        weak_to,
        immune_to,
    ):
        self.num_units = num_units
        self.unit_hp = unit_hp
        self.unit_attack = unit_attack
        self.initiative = initiative
        self.attack_type = attack_type
        self.weak_to = weak_to
        self.immune_to = immune_to

    def effective_power(self):
        return self.num_units * self.unit_attack

    def to_sortable(self):
        return (self.effective_power(), self.initiative)

    def damage(self, other: Self):
        dmg = self.effective_power()
        if self.attack_type in other.immune_to:
            dmg = 0
        elif self.attack_type in other.weak_to:
            dmg *= 2
        return dmg

    def deal_damage(self, other: Self):
        if self.num_units == 0:
            return
        dmg = self.damage(other)
        remaining_hp = max(other.unit_hp * other.num_units - dmg, 0)
        other.num_units = math.ceil(remaining_hp / other.unit_hp)


class Army:
    def __init__(self, groups):
        self.groups = groups

    def select_targets(self, enemy: Self):
        ordered = sorted(self.groups, key=lambda g: g.to_sortable(), reverse=True)
        targets = [g for g in enemy.groups if g.num_units > 0]
        pairs = []
        for group in ordered:
            if len(targets) == 0:
                continue

            def sort_key(target):
                return (
                    group.damage(target),
                    target.effective_power(),
                    target.initiative,
                )

            to_attack = max(targets, key=sort_key)
            if group.damage(to_attack) > 0:
                pairs.append((group, to_attack))
                targets.remove(to_attack)

        return pairs

    def has_units(self):
        return any(g.num_units > 0 for g in self.groups)


for army, name in zip(armies_str, ["immune", "infection"]):
    groups = []
    for group in army.split("\n")[1:]:
        num_units, unit_hp, unit_attack, initiative = [
            int(n) for n in re.findall("\d+", group)
        ]
        (attack_type,) = re.search("that does \d+ (\w+) damage", group).groups()

        weak_to_match = re.search("weak to ([\w, ]+)(?:;|\\))", group)
        if weak_to_match:
            (weak_to_lst,) = weak_to_match.groups()
            weak_to = weak_to_lst.split(", ")
        else:
            weak_to = []

        immune_to_match = re.search("immune to ([\w, ]+)(?:;|\\))", group)
        if immune_to_match:
            (immune_to_lst,) = immune_to_match.groups()
            immune_to = immune_to_lst.split(", ")
        else:
            immune_to = []

        groups.append(
            Group(
                num_units,
                unit_hp,
                unit_attack,
                initiative,
                attack_type,
                weak_to,
                immune_to,
            )
        )

    army = Army(groups)
    if name == "immune":
        immune_army = army
    else:
        infection_army = army


def fight(boost):
    imm_army = deepcopy(immune_army)
    inf_army = deepcopy(infection_army)
    for g in imm_army.groups:
        g.unit_attack += boost
    while imm_army.has_units() and inf_army.has_units():
        immune_pairs = imm_army.select_targets(inf_army)
        infection_pairs = inf_army.select_targets(imm_army)
        pairs = immune_pairs + infection_pairs
        sorted_pairs = sorted(pairs, key=lambda p: p[0].initiative, reverse=True)
        for attacker, attacked in sorted_pairs:
            attacker.deal_damage(attacked)

    if imm_army.has_units():
        return "immune", sum([g.num_units for g in imm_army.groups])
    else:
        return "infection", sum([g.num_units for g in inf_army.groups])


print(fight(0)[1])

# found this number manually
# keep increasing the boost until immune starts winning, find the turning point
# right before the turning point, the fight will last indefinitely since it will start dealing damage less than the unit_hp
# so skip those fights until immune clearly wins
print(fight(35)[1])
