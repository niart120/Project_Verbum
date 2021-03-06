import json
import math
from collections import Counter

class Solver(object):
    def __init__(self):
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
            
            for i in range(5):
                for j in range(5):
                    if i==j:continue
                    if a[i]==b[j]:
                        r[i] = 1
                        a[i] = "_"
                        b[j] = "#"
            
            result = tuple(r)
            return result

        names = []
        with open("./names.json",encoding="utf-8") as js:
            names.extend(json.load(js))
        n = len(names)

        reverse_dict = {}
        subset_dict_list = [{} for _ in range(n)]

        for i in range(n):
            answer = names[i]
            reverse_dict[names[i]] = i
            for j in range(n):
                question = names[j]
                d = distance(question,answer)
                if d in subset_dict_list[j]:
                    subset_dict_list[j][d].append(i)
                else:
                    subset_dict_list[j][d] = [i]
        
        for subset_dict in subset_dict_list:
            for k,v in subset_dict.items():
                subset_dict[k] = set(v)

        self.subset_dict_list = subset_dict_list
        self.n = n
        self.names = names
        self.reverse_dict = reverse_dict

    def get_query(self, candidates = None):
        if candidates is None:
            candidates = set(range(self.n))
        lst = []
        for i in range(self.n):
            eta = self.get_entropy(i, candidates), self.names[i]
            lst.append(eta)
        score, query = max(lst)
        return query

    def get_entropy(self, id, eventset = None):
        if eventset is None:
            eventset = set(range(self.n))
        eventset = set(eventset)
        n = len(eventset)
        entropy = 0
        for subset in self.subset_dict_list[id].values():
            #joint probability
            jointset = subset & eventset
            k = len(jointset)
            p = k/n
            if p==0:continue
            entropy += p*math.log2(p)
        entropy = -entropy
        return entropy

    def get_entropy_byname(self, name, eventset = None):
        id = self.reverse_dict[name]
        return self.get_entropy(id,eventset)

    def get_informationcontent(self, id, respond, eventset = None):
        if eventset is None:
            eventset = set(range(self.n))
        eventset = set(eventset)
        n = len(eventset)
        jointset = subset & eventset
        k = len(jointset)
        p = k/n
        entropy = 0
        if p!=0:
            entropy = -math.log2(p)
        return entropy

    def get_informationcontent_byname(self, name, respond, eventset=None):
        id = self.reverse_dict[name]
        return self.get_informationcontent(id, respond)

    def get_subset(self, id, respond):
        return self.subset_dict_list[id][respond]
    
    def get_subset_byname(self, name, respond):
        return self.get_subset(self.reverse_dict[name], respond)

if __name__ == "__main__":
    solver = Solver()
    lst = []
    for i in range(solver.n):
        eta = solver.get_entropy(i), solver.names[i]
        lst.append(eta)
    lst = sorted(lst)[::-1]
    print("entropy top 5")
    for e,name in lst[:5]:
        print(e,name)