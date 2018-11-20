from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window

#classes

class MainWidget(Widget):
    pass

class AcousticRecognitionSystem(App):
    #set window title
    App.title = "Acoustic Recognition System - Proof of Concept"
    
    #Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
    #Config.set('graphics', 'width', '1000')
    #Config.set('graphics', 'height', '800')
    
    def build(self):
        #Window.clearcolor = (1,1,1,1)
        return MainWidget()
    
#main functions

#main
if __name__ == "__main__":
    #instantiate and run app
    AcousticRecognitionSystem().run()
