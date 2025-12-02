from sympy import divisors

def read_data(input_file: str) -> list[range]:
    data: list[range] = list()
    with open(input_file, 'r') as f:
        ranges: list[str] = f.readline().strip().split(",")
        for actual_range in ranges:
            a, b = actual_range.split("-")
            data.append(range(int(a), int(b)+1))
    return data

def bad_ids_twice(rango: range) -> list[int]:
    bad: list[int] = list()
    for n in rango:
        n_str: str = str(n)
        l = len(n_str)
        if l%2 != 0: # Only happens if len is even
            continue
        j: int = l//2
        if n_str[:j] * 2 == n_str:
            bad.append(n)
    return bad

def bad_ids_any(rango: range) -> list[int]:
    bad: list[int] = list()
    divisors_cache = {}
    for n in rango:
        n_str: str = str(n)
        l: int = len(n_str)
        if l not in divisors_cache:
            divs: list[int] = divisors(l)[1:]
            divisors_cache[l] = divs
        for i in divisors_cache[l]:
            j = l // i
            if n_str[:j] * i == n_str:
                bad.append(n)
                break
    return bad

def get_bad_ids(ranges: list[range], function) -> list[int]:
    bad_ids: list[int] = list()
    for rango in ranges:
        bad_ids.extend(function(rango))
    return bad_ids

if __name__ == "__main__":
    INPUT_FILE: str = "input.txt"
    ranges: list[range] = read_data(INPUT_FILE)

    bad_ids_twice = get_bad_ids(ranges, bad_ids_twice)
    print(f"The invalid IDs (twice pattern) sum up {sum(bad_ids_twice)}")

    bad_ids_any = get_bad_ids(ranges, bad_ids_any)
    print(f"The invalid IDs (any pattern) sum up {sum(bad_ids_any)}")
