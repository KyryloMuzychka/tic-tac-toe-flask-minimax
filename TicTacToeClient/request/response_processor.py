class ResponseProcessor:
    def process_response(self, response):
        try:
            response_json = response.json()
        except ValueError:
            response_json = {}        
        if response.status_code == 200:                        
            return {
                'valid': True, 
                'info': response_json.get('message'), 
                'player_info': response_json.get('player_info')
            }
        else:
            return {'valid': False, 'info': response_json.get('message')}
