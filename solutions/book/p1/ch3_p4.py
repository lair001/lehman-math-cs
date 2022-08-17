from sys import argv


def get_truth_value_array(n: int) -> list[list[bool]]:
    result: list[list[bool]] = [[]]
    _add_truth_values(n, result[0], result)
    return result


def _add_truth_values(n: int, curr: list[bool], result: list[list[bool]]):
    if n == 0:
        return
    new: list[bool] = curr.copy()

    curr.append(True)
    new.append(False)

    _add_truth_values(n - 1, curr, result)
    _add_truth_values(n - 1, new, result)

    result.append(new)


def _bool_to_str(b: bool):
    return "T" if b else "F"


def _main():
    n: int = int(argv[1]) if len(argv) > 1 else 4
    print("n: {}".format(n))
    print()
    result: list[list[bool]] = get_truth_value_array(n)
    for row in result:
        print(" ".join(map(_bool_to_str, row)))
    print()
    print("total rows: {}".format(len(result)))


if __name__ == "__main__":
    _main()
