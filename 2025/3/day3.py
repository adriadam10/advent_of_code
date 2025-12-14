def read_data(input_file: str) -> list[list[int]]:
    banks: list[int] = list()
    with open(input_file, 'r') as f:
        for line in f.readlines():
            banks.append([int(a) for a in str(line.strip())])
    return banks

def max_jolts_two(banks: list[list[int]]) -> int:
    jolts: int = 0
    for bank in banks:
        start: tuple[int, int] = [0,0]
        # Coger número mas grande sin contar el ultimo
        for i, battery in enumerate(bank[:-1]):
            if battery > start[0]:
                start = [battery, i]
        # Coger número mas grande a partir del anterior
        end = max(bank[start[1]+1:])
        jolts += start[0] * 10 + end

    return jolts

def max_jolts_twelve(banks: list[list[int]]) -> int:
    jolts: int = 0
    for bank in banks:
        n_restantes = len(bank) - 12

        # Elegir maximo de los n_restantes primeros números
        start: tuple[int, int] = [0,0]
        for i, battery in enumerate(bank[:n_restantes]):
            if battery > start[0]:
                start = [battery, i]
        jolts += start[0] * 10**(n_restantes - 1)

        # De los números que quedan buscar el mas grande restante saltando (si podemos)
        actual_pos = start[1] + 1
        for i in range(len(bank) - n_restantes - 2, -1, -1):
            saltos = actual_pos + n_restantes
            j, maximo = max(enumerate(bank[actual_pos:min(len(bank), max(actual_pos+1,actual_pos + saltos))]), key=lambda x: x[1])
            n_restantes -= actual_pos - j - 1
            actual_pos = j + 1
            jolts += maximo * 10**i
    
    return jolts


if __name__ == "__main__":
    INPUT_FILE: str = "input_test.txt"
    banks: list[list[int]] = read_data(INPUT_FILE)

    jolts_two: int = max_jolts_two(banks)
    print(f"Max jolts choosing two batteries: {jolts_two}")

    jolts_twelve: int = max_jolts_twelve(banks)
    print(f"Max jolts choosing twelve batteries: {jolts_twelve}")