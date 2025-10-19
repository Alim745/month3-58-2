import flet as ft 


def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world")
    name_input = ft.TextField(label="Введите имя:")

    def on_button_click(_):
        name = name_input.value.strip()
        print(name)
        
        if name:
            greeting_text.value = f"Hello {name}"
            name_input.value = ""   
        else:
            print("User ничего не ввел")
            greeting_text.value = 'Пожалуйста, введите имя!'

        page.update()


    name_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
     
    page.add(greeting_text, name_input, name_button)


ft.app(target=main)