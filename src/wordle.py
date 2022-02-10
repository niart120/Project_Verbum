import random
class Wordle():
    def __init__(self, problems, questions=None,seed=None):
        if seed is not None:
            random.seed(seed)
        
        self.problems = set(problems)
        self.questions = set(problems)
        if questions is not None:
            self.questions = set(questions)
        self.set_answer()
    
    def set_answer(self):
        self.answer = random.choice(list(self.problems))
    
    def get_answer(self):
        return self.answer

    def query(self, q:str):
        if q in self.questions:
            return Wordle.distance(q,self.answer)
        else:
            raise ValueError("Exception: The word does not exist.")

    def distance(question,answer):
        """[summary]

        Args:
            question ([type]): [description]
            answer ([type]): [description]

        Returns:
            [type]: [description]
        """

        a,b = list(question), list(answer)
        r = [2]*5
        for i in range(5):
            if a[i] == b[i]:
                r[i] = 0
                a[i] = "_"
                b[i] = "#"
        
        for i in range(4):
            for j in range(i+1,5):
                if a[i]==b[j]:
                    r[i] = 1
                    a[i] = "_"
                    b[j] = "#"
        
        result = tuple(r)
        return result

    def parse(distance):
        def color(text: str, code: int, bold: bool = True):
            prefix = '\033[1m'
            prefix += f'\033[{code}m'
            return prefix + text + '\033[0m'

        def green(text: str):
            return color(text,32)

        def yellow(text: str):
            return color(text,33)
        def default(text: str):
            return color(text, 0)

        result = []
        for r_i in distance:
            if r_i==0:
                result.append(green("■"))
            if r_i==1:
                result.append(yellow("■"))
            if r_i==2:
                result.append(default("■"))
        result.append(default(""))
        result = "".join(result)
        return result

    def is_correct(respond):
        return sum(respond)==0