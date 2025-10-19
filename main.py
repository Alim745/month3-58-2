import flet as ft 
import datetime as dt

def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world") 

    greeting_history = []
    history_text = ft.Text("История приветствий:")


    def get_greeting_time():
        hour = dt.datetime.now().hour
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

            timestamp = dt.datetime.now().strftime("%H:%M:%S")
            greeting_history.append(f"{timestamp} {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history) 
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

    def clear_hitory(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()
    
    def sort_history(_):
        greeting_history.sort(key=lambda x: x.split()[1].lower()) 
        history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        page.update()

    name_input = ft.TextField(label="Введите имя:", on_submit=on_button_click, expand=True)
    name_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    theme_mode_button = ft.ElevatedButton('Сменить тему', icon=ft.Icons.BRIGHTNESS_7, on_click=theme_mode_change)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_hitory)
    sort_button = ft.ElevatedButton("Сортировать", icon=ft.Icons.SORT_BY_ALPHA, on_click=sort_history)

    page.add(greeting_text,
             ft.Row([name_input, name_button, theme_mode_button, clear_button, sort_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,),
             history_text
             )


ft.app(target=main)