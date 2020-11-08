
def cal_score(team_lst):
    team_result = []
    for i in team_lst:
        team_result.append([i["name"],{"points":3 * i["wins"] + 0 * i["loss"] + 1 * i["draws"]},{"gd": i["scored"] - i["conceded"]}])
    return team_result


def selection_sort(n):
    for i in range(len(n)):
        min_index = i
        for j in range(i+1, len(n)):
            if n[min_index][1]["points"] < n[j][1]["points"]:
                min_index = j
            elif n[min_index][1]["points"] == n[j][1]["points"]:
                if n[min_index][2]["gd"] < n[j][2]["gd"]:
                    min_index = j
        n[i], n[min_index] = n[min_index], n[i]
    return n


n = input("Enter Input : ").split('/')
team = dict()
team_lst = []
for i in n:
    i = i.split(',')
    team["name"] = team.get("name",i[0])
    team["wins"] = team.get("wins",int(i[1]))
    team["loss"] = team.get("loss",int(i[2]))
    team["draws"] = team.get("draws",int(i[3]))
    team["scored"] = team.get("scored",int(i[4]))
    team["conceded"] = team.get("conceded",int(i[5]))
    team_lst.append(team.copy())
    team.clear()
print("== results ==",*selection_sort(cal_score(team_lst)),sep="\n")