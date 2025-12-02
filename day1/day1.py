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

def countClicks(inputs: list[str]) -> int:
    value = 50
    results = []

    for input in inputs:
        steps = int(input[1:])
        sign = 1 if input[0] == 'R' else -1
        main, value = divmod((value + steps*sign), 100) 
        
        results.append(abs(main))
    
    amount_clicks = sum(i for i in results if i != 0)

    return amount_clicks

if __name__ == "__main__":
    inputs = importTextfile()
    #inputs = ["L68", "L30","R48","L5","R60","L55","L1","L99","R14","L82"]
    #print(countZeros(inputs))
    print(countClicks(inputs))