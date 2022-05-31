import os

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class DialogContent(BoxLayout):
    pass


class InputDialogContent(DialogContent):
    pass


class FilterDialogContent(DialogContent):
    pass


class DeleteDialogContent(DialogContent):
    pass


class UploadDialogContent(DialogContent):
    pass


class SaveDialogContent(DialogContent):
    pass


class DialogWindow(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(
            title=kwargs["title"],
            type="custom",
            content_cls=kwargs["content_cls"],
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    on_release=self.close
                ),
            ],
        )
        self.mode = kwargs["mode"]
        self.controller = kwargs["controller"]
        self.model = kwargs["model"]

    def close(self, obj):
        self.dismiss()


class InputWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="New student: ",
            content_cls=InputDialogContent(),
            mode="input",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            [
                self.content_cls.ids.input_fio.text,
                self.content_cls.ids.input_line_up.text,
                self.content_cls.ids.input_position.text,
                self.content_cls.ids.input_titles.text,
                self.content_cls.ids.input_sport_type.text,
                self.content_cls.ids.input_rank.text
            ]
        )


class CustomDropDown(DropDown):
    pass


class FilterWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Filter students: ",
            content_cls=FilterDialogContent(),
            mode="filter",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )


        dropdown = DropDown();
        sport = 'football'
        btn = Button(text=sport, pos=(200, 200), size_hint_y=None, height=30)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
        mainButton = Button(text="Choose sporttype", size_hint=(0.3, 0.3))
        mainButton.pos_hint = ()
        mainButton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.content_cls.ids['filter_sport_type'], 'text', x))
        self.add_widget(mainButton)

        dropdown = DropDown();
        for rank in ['1st', '2nd', '3d', 'CMS', 'master']:
            btn = Button(text=rank, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        mainButton1 = Button(text="Choose rank", size_hint=(0.3, 0.3))
        mainButton1.pos_hint = ()
        mainButton1.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.content_cls.ids['filter_rank'], 'text', x))
        self.add_widget(mainButton1)

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            [
                self.content_cls.ids.filter_fio.text,
                self.content_cls.ids.filter_line_up.text,
                self.content_cls.ids.filter_position.text,
                self.content_cls.ids.filter_titles.text,
                self.content_cls.ids.filter_sport_type.text,
                self.content_cls.ids.filter_rank.text
            ]
        )


class DeleteWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Delete students: ",
            content_cls=DeleteDialogContent(),
            mode="delete",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            [
                self.content_cls.ids.delete_fio.text,
                self.content_cls.ids.delete_line_up.text,
                self.content_cls.ids.delete_position.text,
                self.content_cls.ids.delete_titles.text,
                self.content_cls.ids.delete_sport_type.text,
                self.content_cls.ids.delete_rank.text
            ]
        )


class SaveWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Saving: ",
            content_cls=SaveDialogContent(),
            mode="save",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(self.content_cls.ids.save_path.text)


class UploadWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Upload: ",
            content_cls=UploadDialogContent(),
            mode="upload",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(self.content_cls.ids.upload_path.text)


Builder.load_file(os.path.join(os.path.dirname(__file__), "dialog_windows.kv"))
