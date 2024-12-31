from stack import Stack
class CityData:
    def __init__(self, name, outcount, outcons):
        self.name = name
        self.outcount = outcount
        self.outcons = outcons
        self.seen =  False
        self.pred = -1



def main():
    cities = []
    with open('pb.txt', 'r') as file:
        n = int(file.readline())
        for i in range(n):
            s = file.readline()
            part1 , part2 = s.split(',')
            num , name = part1.split(' ')
            part2 = part2.split()
            count = int(part2[0])
            city = part2[1:]
            for j in range(len(city)):
                city[j] = int(city[j])
            #print(name, count, city)
            cd = CityData(name.lower(),count,city)
            cities.append(cd)
    start = input('Enter starting city:').lower()
    end = input('Enter ending city:').lower()
    n = len(cities)
    s_ = e_ = False
    for i in range(n):
        if start == cities[i].name:
            s_ = True
            index = i
        if end == cities[i].name:
            e_ = True
    yes = False
    index = False
    if not s_:
        print(f'{start} is not a valid city! Enter again')
        yes = True
    if  not e_:
        print(f'{end} is not a valid city!Enter again')
        yes = True
    if yes:
        main()
    starting = cities[index]
    stak = Stack()
    # print(starting.outcount)
    for i in range(starting.outcount):
        stak.push(starting.outcons[i])
    if stak.is_empty():
        print('Path does not exist')
    while not stak.is_empty():
        cc = stak.pop()
        if cities[cc].name == end.lower():
            print('Path is found')
        else:
            ccc  = cities[cc].outcons
            for k in ccc:
                if not cities[k].seen: 
                    cities[k].seen = True
                    cities[k].pred = cities[cc].name
                    stak.push(k)
    if stak.is_empty():
        print('Path not found')
main()