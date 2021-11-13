import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class example(GridLayout):
    # Constructor
    def __init__(self,**kwargs):

        super(example, self).__init__() #To invoke super class constructor
        self.cols = 1
        self.add_widget(Label(text="Student Name: "))

        self.s_name = TextInput()
        print(kwargs)
        self.add_widget(self.s_name)

        self.press = Button(text="Press_me_daddy")
        self.press.bind(on_press=self.press_me_daddy)
        self.add_widget(self.press)

    def press_me_daddy(self,instance):
        print('The main name is '+self.s_name.text)



class example_app(App):
    # Created a method
    def build(self):
        #Calling the other call
        return example()


if __name__ == "__main__":
    example_app().run()

