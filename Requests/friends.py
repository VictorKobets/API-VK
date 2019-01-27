import requests
from vk import Client_API_VK


def calc_age(uid):
    user = Client_API_VK(uid)
    friends = user.get_friends()
    
    age = dict()
    for friend in friends:
        if 'bdate' in friend:
            data = friend['bdate'].split('.')
            if len(data) == 3:
                years_old = 2018 - int(data[2])
                if years_old in age:
                    age[years_old] += 1
                else:
                    age[years_old] = 1
    
    answer = list()
    for key in sorted(age):
        answer.append((key, age[key]))
    
    return sorted(answer, key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
