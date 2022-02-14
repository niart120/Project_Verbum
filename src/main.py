import json
from solver import Solver
from wordle import Wordle

def main():
    names = []
    with open("./names.json",encoding="utf-8") as js:
        names.extend(json.load(js))

    solver = Solver()

    msg = '###Pokemon Wordle Solver###'

    candidates = set(range(solver.n))
    for _ in range(10):
        q = solver.get_query(candidates)
        if len(candidates)==1:
            id = list(candidates)[0]
            q = solver.names[id]
            print(f'answer is :{q}')
            return
        msg = f'next query:{q}'
        print(msg)
        while True:
            try:
                msg = "respond ?:"
                print(msg,end='')
                respond = tuple(map(int,input().split()))
                candidates = candidates & solver.get_subset_byname(q, respond)
            except ValueError:
                msg = "Error:Invalid input"
                print(msg)
                continue
            except KeyError:
                msg = "Error:Non-existent response"
                print(msg)
                continue
            break
if __name__ == "__main__":
    main()