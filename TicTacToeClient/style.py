def getNewGameButtonStyle():
    return ("QPushButton{"
            "   color:#fff;"
            "   background: none;"
            "   border:none;"
            "   border-radius:19px;"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.955, stop:0 rgba(89, 156, 208, 255), stop:1 rgba(65, 118, 184, 255));"            
            "   font-size:16px;"
            "   min-width: 200px;"
            "   max-width: 300px;"
            "   height: 40px;"
            "}"
            "QPushButton::hover{"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.955, stop:0 rgba(104, 173, 226, 255), stop:1 rgba(79, 144, 223, 255));"
            "}"
            "QPushButton::pressed{"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.955, stop:0 rgba(89, 156, 208, 255), stop:1 rgba(65, 118, 184, 255));"
            "}")

def getLoginAccountButtonStyle():
   return ("QPushButton{"
            "   color:#fff;"
            "   background: none;"
            "   border:none;"
            "   border-radius:19px;"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.955, stop:0 rgba(89, 156, 208, 255), stop:1 rgba(65, 118, 184, 255));"            
            "   font-size:16px;"
            "   max-width: 300px;"
            "   height: 40px;"
            "}"
            "QPushButton::hover{"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.955, stop:0 rgba(104, 173, 226, 255), stop:1 rgba(79, 144, 223, 255));"
            "}"
            "QPushButton::pressed{"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.955, stop:0 rgba(89, 156, 208, 255), stop:1 rgba(65, 118, 184, 255));"
            "}")

def getSaveNewDataButtonStyle():
    return ("QPushButton{"
            "   color:#fff;"
            "   background: none;"
            "   border:none;"
            "   border-radius:19px;"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.955, stop:0 rgba(89, 156, 208, 255), stop:1 rgba(65, 118, 184, 255));"            
            "   font-size:16px;"
            "   max-width: 300px;"
            "   height: 40px;"
            "}"
            "QPushButton::hover{"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.955, stop:0 rgba(104, 173, 226, 255), stop:1 rgba(79, 144, 223, 255));"
            "}"
            "QPushButton::pressed{"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.955, stop:0 rgba(89, 156, 208, 255), stop:1 rgba(65, 118, 184, 255));"
            "}")

def getDeleteAccountButtonStyle():
    return ("QPushButton{"
            "   color:#fff;"
            "   background: none;"
            "   border:none;"
            "   border-radius:19px;"
            "   background-color: qlineargradient(spread:pad, x1:0.006, y1:0, x2:0, y2:1, stop:0 rgba(212, 46, 96, 255), stop:1 rgba(255, 121, 119, 255));"            
            "   font-size:16px;"
            "   max-width: 300px;"
            "   height: 40px;"
            "   margin-top: 20px;"            
            "}"
            "QPushButton::hover{"
            "   background-color: qlineargradient(spread:pad, x1:0.006, y1:0, x2:0, y2:1, stop:0 rgba(212, 56, 106, 255), stop:1 rgba(255, 131, 129, 255));"
            "}"
            "QPushButton::pressed{"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.955, stop:0 rgba(89, 156, 208, 255), stop:1 rgba(65, 118, 184, 255));"
            "}")

def getRegisterAccountButtonStyle():
    return ("QPushButton{"
            "   color:#fff;"
            "   background: none;"
            "   border:none;"
            "   border-radius:19px;"
            "   background-color: qlineargradient(spread:pad, x1:0.006, y1:0, x2:0, y2:1, stop:0 rgba(212, 46, 96, 255), stop:1 rgba(255, 121, 119, 255));"            
            "   font-size:16px;"
            "   max-width: 300px;"
            "   height: 40px;"            
            "}"
            "QPushButton::hover{"
            "   background-color: qlineargradient(spread:pad, x1:0.006, y1:0, x2:0, y2:1, stop:0 rgba(212, 56, 106, 255), stop:1 rgba(255, 131, 129, 255));"
            "}"
            "QPushButton::pressed{"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.955, stop:0 rgba(89, 156, 208, 255), stop:1 rgba(65, 118, 184, 255));"
            "}")

def getLabelStyle():
    return ("QLabel{"            
            "   font-size: 15px;"
            "   font-style: italic;"
            "   color: #363535;"
           "}")    

def getLabelErrorStyle():
    return ("QLabel{"            
            "   font-size: 15px;"
            "   font-style: italic;"
            "   color: #f22929;"
           "}")
        
def getLabelSuccessStyle():
    return ("QLabel{"            
            "   font-size: 15px;"
            "   font-style: italic;"
            "   color: #06bd24;"
           "}")        
    
def getEditStyle():
    return ("QLineEdit{"
            "   max-width: 300px;"
            "   height: 30px;"
            "   border: none;"            
            "}")
    
def getLabelDrawsStyle():
    return ("QLabel{"            
            "   font-size: 15px;"
            "   font-style: italic;"
            "   color: #f07918;"
           "}")
   
def getLabelWinsStyle():
    return ("QLabel{"            
            "   font-size: 15px;"
            "   font-style: italic;"
            "   color: #06bd24;"
           "}")
    
def getLabelLossesStyle():
    return ("QLabel{"            
            "   font-size: 15px;"
            "   font-style: italic;"
            "   color: #f22929;"
           "}")  
    
def getTabWidgetStyle():
    return ("QTabWidget::pane{"            
            "   border: none;"            
            "}")
