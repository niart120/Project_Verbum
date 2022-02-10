import json

def main():
    names = []
    with open("./gen8.json",encoding="utf-8") as js:
        pokedict = json.load(js)

        for poke in pokedict:
            name = poke["Name"]
            if len(name)==5:
                names.append(name)

    with open("./names.json","w",encoding="utf-8") as js:
        jsonstr = json.dump(names,js,ensure_ascii=False,indent=2)

if __name__ == "__main__":
    main()