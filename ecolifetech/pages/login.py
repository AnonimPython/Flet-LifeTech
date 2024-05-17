import flet as ft
import sqlite3


# ! скрыть символы в пароле



def view(page):
    login = ft.TextField(label="Логин")
    password = ft.TextField(label="Пароль")
        
    user_inputs = ft.Column(
        [
            login,
            password,
        ]
    )
    
    def log_in(e):

        # Подключаемся к базе данных
        con = sqlite3.connect("users.db")
        cur = con.cursor()

        # Проверяем существование пользователя с данным логином и паролем
        cur.execute("SELECT * FROM users WHERE login = ? AND password1 = ?", (login.value, password.value))
        user = cur.fetchone()

        if user:
            # Авторизация успешна, перенаправляем на страницу статистики или другую нужную страницу
            username = user[2]
            page.session.set("username", username)
            value = page.session.get("username")
            print(f"Пользователь из сесии {value} успешно авторизован")
            
            # e.page.go("/stats")
            e.page.go("/hello_screen")
            
        else:
            # Пользователь с данным логином и паролем не найден, выводим сообщение об ошибке
            page.snack_bar = ft.SnackBar(
                bgcolor="red",
                content=ft.Text(f"Неправильный логин или пароль")
                )
            page.snack_bar.open = True
            login.value = ""
            password.value = ""
            page.update()
            

        con.close()
    

        
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                            # left (inputs)
                            ft.Column(
                                    [
                                        ft.Text(
                                            "Авторизация",
                                            weight=ft.FontWeight.BOLD,
                                            size=35,
                                        ),
                                        user_inputs,
                                        ft.ElevatedButton(
                                            "Авторизироваться",
                                            width=300,
                                            height=40,
                                            bgcolor=ft.colors.BLUE_900,
                                            color="white",
                                            on_click=log_in,

                                        ),
                                        ft.ElevatedButton(
                                            "Зарегистрироваться",
                                            width=300,
                                            height=40,
                                            color="black",
                                            on_click=lambda e: e.page.go("/register"),
                                            style=ft.ButtonStyle(
                                                side={
                                                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE_900),
                                                },
                                            )
                                            
                                        )
                                        
                                    ]
                                ),
                            # ! потом сделать Stack с лого компании
                            # right (img) 3264 × 5824
                            ft.Image(
                                src="log1.jpg",
                                # 900 
                                width=700,
                                height=650,
                                fit=ft.ImageFit.FIT_WIDTH,
                                border_radius=ft.border_radius.all(10),
                            ),

                            ],alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            
                        ) # end Row
                    ]
                )
            )
        ]
    )