import os

def importTextfile() -> list[str]:
    script_dir = os.path.dirname(__file__)               
    file_path = os.path.join(script_dir, "input.txt")    

    return open(file_path).read().split()

def countZeros(inputs: str) -> int:
    amount_zeros = 0
    value = 50
    results = []

    for input in inputs:
        steps = int(input[1:])
        sign = 1 if input[0] == 'R' else -1
        value = (value + steps*sign) % 100
        
        results.append(value)
    
    amount_zeros = results.count(0)

    return amount_zeros


if __name__ == "__main__":
    inputs = importTextfile()
    print(countZeros(inputs))