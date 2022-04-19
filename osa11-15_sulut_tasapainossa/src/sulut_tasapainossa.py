def sulut_tasapainossa(merkkijono: str):
    merkkijono = "".join([a for a in merkkijono if a in "([)]"])
    if len(merkkijono) == 0:
        return True
    if (merkkijono[0] == '(' and merkkijono[-1] == ')') or (merkkijono[0] == '[' and merkkijono[-1] == ']'):
        return sulut_tasapainossa(merkkijono[1:-1])
    return False


if __name__ == "__main__":

    ok = sulut_tasapainossa("(s()ddd)")

    
    print(ok)

    
