import flet as ft
from time import sleep



import asyncio


        
def view(page):
    
    page. vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    
    
    username = page.session.get("username")
    

    
    c = ft.Container(
        alignment=ft.alignment.center,
        width=500,
        height=500,
        border_radius=10,
        content=ft.Text(
            f"Приветствую вас,",
            text_align=ft.TextAlign.CENTER,
            size=40,
            spans=[
                ft.TextSpan(
                    f"{username}",
                    ft.TextStyle(weight=ft.FontWeight.BOLD, size=40, color=ft.colors.BLACK)
                    )
                ]
        ),
        # animations
        scale=ft.transform.Scale(scale=1),
        animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
    )
    
    def animate():
        c.scale = 2  
        page.update()
        sleep(2)
        c.scale = 1
        page.update()

  
    

    return ft.Column(
        controls=[
            ft.Container(
                margin=ft.margin.only(top=280),
                content=ft.Column(
                    [
                    ft.Row(
                        [
                            ft.Text(
                                f"Приветствую вас, ",
                                text_align=ft.TextAlign.CENTER,
                                size=40,
                                spans=[
                                    ft.TextSpan(
                                        f"{username}",
                                        ft.TextStyle(weight=ft.FontWeight.BOLD, size=40, color=ft.colors.BLACK)
                                        )
                                    ]
                            ),
                            ft.IconButton(
                                icon=ft.icons.ARROW_FORWARD_IOS_ROUNDED,
                                icon_color="black",
                                icon_size=90,
                                # tooltip="Начать работу",
                                on_click=lambda e: e.page.go("/stats")
                            )
                        ],alignment=ft.MainAxisAlignment.SPACE_AROUND
                    )
                    ]
                )
            ),
        ]
        
        
    )