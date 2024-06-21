from request.request_handler import RequestHandler
from request.response_processor import ResponseProcessor

class RequestFacade:
    def __init__(self, url):
        self.request_handler = RequestHandler(url)
        self.response_processor = ResponseProcessor()

    def register_user(self, login, password):
        response = self.request_handler.register_user(login, password)
        return self.response_processor.process_response(response)

    def login_user(self, login, password):
        response = self.request_handler.login_user(login, password)
        return self.response_processor.process_response(response)

    def get_player_info(self):
        response = self.request_handler.get_player_info()
        return self.response_processor.process_response(response)
    
    def update_login(self, new_login):
        response = self.request_handler.update_login(new_login)
        return self.response_processor.process_response(response)

    def update_password(self, new_password):
        response = self.request_handler.update_password(new_password)
        return self.response_processor.process_response(response)

    def update_wins(self, wins):
        response = self.request_handler.update_wins(wins)
        return self.response_processor.process_response(response)

    def update_losses(self, losses):
        response = self.request_handler.update_losses(losses)
        return self.response_processor.process_response(response)
    
    def update_draws(self, draws):
        response = self.request_handler.update_draws(draws)
        return self.response_processor.process_response(response)

    def soft_delete(self, login):
        response = self.request_handler.soft_delete(login)
        return self.response_processor.process_response(response)

    def top_players(self):
        response = self.request_handler.top_players()
        return self.response_processor.process_response(response)
    
    def get_player_rank(self):
        response = self.request_handler.get_player_rank()
        return self.response_processor.process_response(response)
