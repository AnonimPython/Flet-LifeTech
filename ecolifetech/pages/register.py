import flet as ft
import sqlite3


# ! сделать защиту на короткие символы и пробелы и скрыть символы в пароле

def view(page):
    
    login = ft.TextField(label="Логин")
    username = ft.TextField(label="Имя в системе")
    password1 = ft.TextField(label="Пароль")
    password2 = ft.TextField(label="Повтор пароля")
        
    user_inputs = ft.Column(
        [
            login,
            username,
            password1,
            password2,
            
        ]
    )
    
    def register(e):
        if not (login.value and username.value and password1.value and password2.value):
            page.snack_bar = ft.SnackBar(
                    bgcolor="red",
                    content=ft.Text(f"Некоторые поля пусты или заполнены неправильно!",size=20)
                )
            page.snack_bar.open = True
            login.value = ""
            username.value = ""
            password1.value = ""
            password2.value = ""
            page.update()
        
        if password1.value != password2.value:
            page.snack_bar = ft.SnackBar(
                dismiss_direction=ft.DismissDirection.UP,
                bgcolor="red",
                content=ft.Text(f"Пароли не совпадают",size=20)
            )
            page.snack_bar.open = True
            login.value = ""
            password1.value = ""
            password2.value = ""
            username.value = ""
            page.update()
        
        
        con = sqlite3.connect("users.db")
        cur = con.cursor()
       
        try:
            cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                login TEXT UNIQUE,
                username TEXT,
                password1 TEXT
            )''')
             
            cur.execute("INSERT INTO users (login, username, password1) VALUES (?, ?, ?)", 
                        (login.value, username.value, password1.value))
            con.commit()
            page.go("/stats")
        except sqlite3.IntegrityError:
            page.snack_bar = ft.SnackBar(
                    bgcolor="red",
                    content=ft.Text(f"Данный логином занят!",size=20)
                    # Некоторые поля пусты или заполнены неправильно!
                )
            page.snack_bar.open = True
            login.value = ""
            username.value = ""
            password1.value = ""
            password2.value = ""
            page.update()
        finally:
            con.close()

        
        
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                            # left (img) 3264 × 5824
                            ft.Image(
                                src="reg1.jpg",
                                # 900 
                                width=700,
                                height=650,
                                fit=ft.ImageFit.FIT_WIDTH,
                                border_radius=ft.border_radius.all(10),
                            ),
                            # right (inputs)
                            ft.Column(
                                    [
                                        ft.Text(
                                            "Регистрация",
                                            weight=ft.FontWeight.BOLD,
                                            size=35,
                                        ),
                                        user_inputs,
                                        ft.ElevatedButton(
                                            "Зарегистрироваться",
                                            width=300,
                                            height=40,
                                            bgcolor=ft.colors.BLUE_900,
                                            color="white",
                                            on_click=register,
                                        ),
                                        ft.ElevatedButton(
                                            "Авторизация",
                                            width=300,
                                            height=40,
                                            color="black",
                                            on_click=lambda e: e.page.go("/login"),
                                            style=ft.ButtonStyle(
                                                side={
                                                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE_900),
                                                },
                                            )
                                            
                                        )
                                        
                                    ]
                                )

                            ],alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            
                        ) # end Row
                    ]
                )
            )
        ]
    )