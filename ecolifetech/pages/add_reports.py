import flet as ft
import json

from datetime import datetime
from time import sleep


def view(page):
    
    page.window_height = 400
    page.window_width = 500
    
    page.window_left = 500
    page.window_top = 100
    
    page.update()
    
    
    def alert():
        dlg = ft.AlertDialog(
            title=ft.Text("Не все поля заполнены!",weight=ft.FontWeight.BOLD),
            content_padding=3,
            bgcolor=ft.colors.WHITE,
        )
        page.dialog = dlg
        dlg.open = True
        page.update()
        sleep(1)
        dlg.open = False
        page.update()
        
        
    def add_reports(e):
        if not (select_months.value and set_year.value and set_require.value):
            return alert()
            
            
            
        now = datetime.now()

        new_data = {
            "month": select_months.value,
            "year": set_year.value,
            "date": "",
            "time": now.strftime("%H:%M"),
            "amount": set_require.value
        }
            
        with open('/Users/evgenijlevin/Desktop/провекты flet/Диплом Эмилька/emil_diplom/assets/json/months.json', 'r+',encoding='utf8') as file:
            data = json.load(file)
            data["reports"].append(new_data)
            file.seek(0)
            json.dump(data, file, indent=4,ensure_ascii=False)
                
        select_months.value = ""
        set_year.value = ""
        set_require.value = ""
        
        page.go("/stats")
        
        page.update()
    
    page.update()
    
    select_months = ft.Dropdown(
        width=130,
        options=[
            ft.dropdown.Option("Январь"),
            ft.dropdown.Option("Февраль"),
            ft.dropdown.Option("Март"),
            ft.dropdown.Option("Апрель"),
            ft.dropdown.Option("Май"),
            ft.dropdown.Option("Июнь"),
            ft.dropdown.Option("Июль"),
            ft.dropdown.Option("Август"),
            ft.dropdown.Option("Сентябрь"),
            ft.dropdown.Option("Октябрь"),
            ft.dropdown.Option("Ноябрь"),
            ft.dropdown.Option("Декабрь"),
        ],
    )
    
    set_require = ft.TextField(label="Сумма")
    set_year = ft.TextField(label="Год",hint_text="2024",multiline=False,max_length=4,width=90)
    
    
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.IconButton(
                            icon=ft.icons.ARROW_CIRCLE_LEFT_OUTLINED,
                            icon_color=ft.colors.BLACK,
                            icon_size=30,
                            on_click=lambda e: e.page.go("/stats")
                        ),
                        ft.Row(
                            [
                                set_require,
                                select_months 
                            ]
                        ),
                        
                        ft.Row(
                            [   
                                # year
                                set_year
                            ]
                        ),
                        
                        ft.ElevatedButton("Создать", on_click=add_reports),
                        
                    ]
                    )
                )
            ]
        )