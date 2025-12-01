def read_data(input_file: str) -> list[int]:
    rotations: list[int] = list()
    with open(input_file, 'r') as f:
        for rotation in f.readlines():
            direction, n = rotation[0], int(rotation[1:])
            if direction == "L":
                rotations.append(n * -1)
            else:
                rotations.append(n)

    return rotations

def count_position_zero(START_POS: int, LIMIT: int, rotations: list[int], only_final=True) -> int:
    pos: int = START_POS
    contador: int = 0
    for rotation in rotations:
        prev_pos: int = pos
        if not only_final: 
            contador += abs(rotation)//(LIMIT + 1)
        if rotation > 0:
            rotation = rotation%(LIMIT + 1)
        else: rotation = rotation%-(LIMIT + 1)
        
        pos += rotation
        if pos < 0:
            pos = LIMIT + pos + 1
            if not only_final and prev_pos and pos: contador += 1
        elif pos > LIMIT:
            pos = pos - LIMIT - 1
            if not only_final and prev_pos and pos: contador += 1
        if pos == 0:
            contador += 1
    return contador

if __name__ == "__main__":
    INPUT_FILE: str = "input.txt"
    START_POS: int = 50
    LIMIT: int = 99
    rotations: list[int] = read_data(INPUT_FILE)
    passwd_1: str = count_position_zero(START_POS, LIMIT, rotations)
    print(f"Password 1 is: {passwd_1}")
    passwd_2: str = count_position_zero(START_POS, LIMIT, rotations, only_final=False)
    print(f"Password 2 is: {passwd_2}")