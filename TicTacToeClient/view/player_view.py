from style import getLabelErrorStyle, getLabelSuccessStyle

class PlayerView:
    def __init__(self, tic_tac_toe_form, auth_form, request):
        self.tic_tac_toe_form = tic_tac_toe_form
        self.auth_form = auth_form
        self.request = request        
        
    def update_login_password(self):        
        new_login = self.tic_tac_toe_form.editNewLogin.text()
        new_password = self.tic_tac_toe_form.editNewPassword.text()

        if new_login and new_password:
            self.update_login(new_login)
            self.update_password(new_password)
        elif new_login:
            self.update_login(new_login)
        elif new_password:
            self.update_password(new_password)
        else:
            self.tic_tac_toe_form.labelResultUpdatePassword.setText('Fill in at least one field')
            self.tic_tac_toe_form.labelResultUpdateLogin.setText('Fill in at least one field')
            self.tic_tac_toe_form.labelResultUpdatePassword.setStyleSheet(getLabelErrorStyle())
            self.tic_tac_toe_form.labelResultUpdateLogin.setStyleSheet(getLabelErrorStyle())

    def update_login(self, new_login):
        update_login_result = self.request.update_login(new_login)
        if update_login_result['valid']:
            self.tic_tac_toe_form.labelResultUpdateLogin.setText("Successfully updated")
            self.tic_tac_toe_form.labelResultUpdateLogin.setStyleSheet(getLabelSuccessStyle())
            self.tic_tac_toe_form.labelLoginName.setText(f'Login: {new_login}')
        else:
            self.tic_tac_toe_form.labelResultUpdateLogin.setText(f"Error: {update_login_result['info']}")
            self.tic_tac_toe_form.labelResultUpdateLogin.setStyleSheet(getLabelErrorStyle())

    def update_password(self, new_password):
        update_password_result = self.request.update_password(new_password)
        if update_password_result['valid']:
            self.tic_tac_toe_form.labelResultUpdatePassword.setText("Successfully updated")
            self.tic_tac_toe_form.labelResultUpdatePassword.setStyleSheet(getLabelSuccessStyle())
        else:
            self.tic_tac_toe_form.labelResultUpdatePassword.setText(f"Error: {update_password_result['info']}")
            self.tic_tac_toe_form.labelResultUpdatePassword.setStyleSheet(getLabelErrorStyle())

    def soft_delete(self):
        response = self.request.get_player_info()
        login = response['player_info']['login']
        soft_delete_result = self.request.soft_delete(login)
        if soft_delete_result['valid']:
            self.tic_tac_toe_form.close()
            self.auth_form.show()            
