''' 
Создание системы для мониторинга и анализа данных в области экологической устойчивости в компании "ЭкоLifeTech".

Создатель: EVG
'''


import flet as ft


from pages.stats import view as stats_view
from pages.register import view as register_view
from pages.login import view as login_view
from pages.hello_screen import view as hello_screen_view
from pages.add_reports import view as add_reports_view


def main(page: ft.Page):
    
    
    # page.horizontal_alignment = page.vertical_alignment = "center"
    
    
    page.title = "«ЭкоLifeTech»"
    page.window_control_allow_resize = False
    
    # расположение окна на экране для тестирования
    page.window_left = 300
    page.window_top = 50
    # скрытие вверхней части окна (закрыть, свернуть)
    page.window_frameless = True
    # app theme
    page.theme_mode = "light"
    
    # page width and height
    page.window_width = 1300
    page.window_height = 700
    # page.window_max_height = 1500

    # скрытие ползунка скролла
    page.scroll = ft.ScrollMode.HIDDEN
    
    def route_change(route):
        page.views.clear()
        
        # * window with register panel
        page.views.append(
            ft.View(
                "/register",
                [
                register_view(page),
                ],
            )
        )
        # * main window
        if page.route == "/stats":
            page.views.append(
                ft.View(
                    "/stats",
                    [
                    stats_view(page)
                    ]
                )
            )
            
        # * 
        if page.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    [
                    login_view(page)
                    ]
                )
            )
        if page.route == "/hello_screen":
            page.views.append(
                ft.View(
                    "/hello_screen",
                    [
                    hello_screen_view(page)
                    ]
                )
            )
        if page.route == "/add":
            page.views.append(
                ft.View(
                    "/add",
                    [
                    add_reports_view(page)
                    ]
                )
            )
            
            
            
            
            
        page.update()
        
        
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
    
    main = ft.Container(
        content=ft.Text("PAGE ERROR , CHECK YOUR APP , LIBRARYS AND SRC/LINKS/URL",size=35,color="red")
    )
    
    page.add(main)

if __name__ == '__main__':
    ft.app(
            target=main,
            assets_dir="assets",
    )
    
    
    
    
    
  