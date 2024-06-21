import requests
from PySide6.QtCore import Slot

class RequestHandler:
    def __init__(self, url):
        self.base_url = url
        self.session = requests.Session()
        
    @Slot(str, str)
    def register_user(self, login, password):
        return self._post_request('/register', {'login': login, 'password': password})

    @Slot(str, str)
    def login_user(self, login, password):
        return self._post_request('/login', {'login': login, 'password': password})

    @Slot()
    def get_player_info(self):
        return self._get_request('/get_player_info')
    
    @Slot(str)
    def update_login(self, new_login):
        return self._put_request('/update_login', {'new_login': new_login})

    @Slot(str)
    def update_password(self, new_password):
        return self._put_request('/update_password', {'new_password': new_password})

    @Slot(int)
    def update_wins(self, wins):
        return self._put_request('/update_wins', {'wins': wins})

    @Slot(int)
    def update_losses(self, losses):
        return self._put_request('/update_losses', {'losses': losses})
    
    @Slot(int)
    def update_draws(self, draws):
        return self._put_request('/update_draws', {'draws': draws})

    @Slot(str)
    def soft_delete(self, login):
        return self._put_request('/soft_delete', {'login': login})

    @Slot()
    def top_players(self):
        return self._get_request('/top_players')
    
    @Slot()
    def get_player_rank(self):
        return self._get_request('/get_player_rank')

    def _post_request(self, endpoint, json_data):
        response = self.session.post(f'{self.base_url}{endpoint}', json=json_data)
        return response

    def _put_request(self, endpoint, json_data):
        response = self.session.put(f'{self.base_url}{endpoint}', json=json_data)
        return response

    def _get_request(self, endpoint):
        response = self.session.get(f'{self.base_url}{endpoint}')
        return response
