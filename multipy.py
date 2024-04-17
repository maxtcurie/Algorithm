def multi(a, b, dig=5):
    if len(a) < dig and len(b) < dig:
        return int(a) * int(b)

    max_len = max(len(a), len(b))
    split_position = max_len // 2

    a1 = int(a[:-split_position]) if len(a) > split_position else 0
    a0 = int(a[-split_position:])

    b1 = int(b[:-split_position]) if len(b) > split_position else 0
    b0 = int(b[-split_position:])

    z2 = multi(str(a1), str(b1), dig)
    z0 = multi(str(a0), str(b0), dig)
    z1 = multi(str(a1 + a0), str(b1 + b0), dig) - z2 - z0

    return (z2 * 10**(2*split_position)) + (z1 * 10**split_position) + z0


if __name__ == "__main__":
    result = multi('1234567890123456789012345678901234567890', '2345678901234567890123456789012345678901', dig=5)
    print(result)
    print(1234567890123456789012345678901234567890 * 2345678901234567890123456789012345678901)
