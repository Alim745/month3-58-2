import flet as ft 
import datetime as dt

def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    greeting_text = ft.Text("Hello world")
    name_input = ft.TextField(label="Введите имя:")
    hour = dt.datetime.now().hour 

    def get_greeting_time():
        if 5 <= hour < 12:
            return "Доброе утро"
        elif 12<= hour < 18:
            return "Добрый день"
        elif 18 <= hour < 23:
            return "Добрый вечер"
        else:
            return "Доброй ночи"

    def on_button_click(_):
        name = name_input.value.strip()
        greeting_time = get_greeting_time()
        print(name)
        
        if name:
            greeting_text.value = f"{greeting_time}, {name}!"
            name_input.value = ""
        else:
            print("User ничего не ввел")
            greeting_text.value = 'Пожалуйста, введите имя!'

        page.update()

    def theme_mode_change(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    name_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    theme_mode_button = ft.ElevatedButton('Сменить тему', icon=ft.Icons.BRIGHTNESS_7, on_click=theme_mode_change)

    page.add(greeting_text, name_input, name_button, theme_mode_button)


ft.app(target=main)