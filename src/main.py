import json
from solver import Solver
from wordle import Wordle

def main():
    names = []
    with open("./names.json",encoding="utf-8") as js:
        names.extend(json.load(js))
    wordle = Wordle(names)
    solver = Solver()

    print(f"(answer is '{wordle.get_answer()}')")

    candidates = set(range(solver.n))
    for _ in range(10):
        q = solver.get_query(candidates)
        if len(candidates)==1:
            id = candidates.pop()
            q = solver.names[id]
        respond = wordle.query(q)
        parsed = Wordle.parse(respond)
        print(f"question:{q}/respond:{parsed}")
        if Wordle.is_correct(respond):
            break
        #update candidates
        candidates = candidates & solver.get_subset_byname(q, respond)
if __name__ == "__main__":
    main()