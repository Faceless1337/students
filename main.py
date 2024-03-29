from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from Controller.myscreen import MyScreenController
from Model.myscreen import MyScreenModel
from kivy.core.window import Window
from kivy.metrics import dp


class PassMVC(MDApp):
    def __init__(self):
        super().__init__()
        self.table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.7, 0.7),
            use_pagination=True,
            elevation=2,
            rows_num=7,
            pagination_menu_height=240,
            background_color=(0, 1, 0, .10),
            column_data=[
                ("[color=#125800]FIO[/color]", dp(40)),
                ("[color=#125800]Line-up (if available)[/color]", dp(40)),
                ("[color=#125800]Position[/color]", dp(20)),
                ("[color=#125800]Titles[/color]", dp(20)),
                ("[color=#125800]Sport type[/color]", dp(30)),
                ("[color=#125800]Rank[/color]", dp(25)),
            ],
        )
        self.model = MyScreenModel(table=self.table)
        self.controller = MyScreenController(self.model)

    def build(self):
        Window.size = (1920, 1080)
        return self.controller.get_screen()


PassMVC().run()
