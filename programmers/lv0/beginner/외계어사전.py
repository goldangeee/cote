def solution(spell, dic):
    spell_length = len(spell)
    set_of_spell = set(spell)
    for e in dic:
        if len(e) < spell_length:
            continue
        else:
            if set_of_spell.issubset(set(e)):
                return 1
    return 2