import requests


class Client_API_VK:
    _api_version_ = '5.71'

    def __init__(self, user_name, access_token=None):
        self.user_name = user_name
        self.access_token = access_token or ('17da724517da724517da72458517b8'+
            'abce117da17da72454d235c274f1a2be5f45ee711')
        self.id = self.get_id()

    def url(self, method):
        return(
            f'https://api.vk.com/method/{method}?v=5.71'+
            f'&access_token={self.access_token}'
            )

    def get_id(self):
        url = self.url('users.get') + f'&user_ids={self.user_name}'
        inf = requests.get(url).json()
        return inf['response'][0]['id']

    def get_friends(self):
        url = self.url('friends.get') + f'&user_id={self.id}&fields=bdate'
        inf = requests.get(url).json()
        return inf['response']['items']
