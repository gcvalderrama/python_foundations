def one_way(sla, slb):

    if sla is None or slb is None:
        return True

    if sla == slb:
        return True

    if abs(len(sla) - len(slb)) > 1:
        return False

    if len(sla) > len(slb):
        tmp = sla
        slb = tmp
        sla = slb

    pos_a = 0
    pos_b = 0
    differences = 0

    while pos_a < len(sla) and pos_b < len(slb) and differences < 2:
        if sla[pos_a] != slb[pos_b]:
            if differences == 0:
                differences += 1
                if len(sla) == len(slb):
                    pos_b += 1
                    pos_a += 1
                else:
                    pos_b += 1

            elif differences == 1:
                return False
        else:
            pos_a += 1
            pos_b += 1

    return True


if __name__ == "__main__":
    sla = "abcde"
    slb = "abfde"
    print(one_way(sla, slb))

    sla = "abcde"
    slb = "abde"
    print(one_way(sla, slb))

    sla = "abde"
    slb = "abcde"
    print(one_way(sla, slb))

    sla = "abde"
    slb = "abcde"
    print(one_way(sla, slb))

