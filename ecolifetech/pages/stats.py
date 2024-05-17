import flet as ft
import json



from flet.plotly_chart import PlotlyChart
import plotly.graph_objects as go


def read_tours_data():
    with open('assets/json/months.json', 'r') as file:
        data = json.load(file)
    return data['reports']




def process_data(reports):
    # Group data by month and sum amounts
    monthly_data = {}
    for report in reports:
        month = report['month']
        amount = report['amount']
        if month not in monthly_data:
            monthly_data[month] = 0
        monthly_data[month] += amount

    # Create a list of months and a list of corresponding total amounts
    months = list(monthly_data.keys())
    amounts = list(monthly_data.values())

    return months, amounts


def view(page):

    page.window_height = 820
    page.window_width = 1300
    
    page.window_left = 300
    page.window_top = 50
    username = page.session.get("username")
    
    reports = read_tours_data()

    
    page.theme_mode = ft.ThemeMode.LIGHT
    

    months = []
    amounts = []

    for item in reports:
        months.append(item['month'])
        amounts.append(item['amount'])

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=months, y=amounts, 
                                name='Amounts',
                                line=dict(color='green', width=3)))
        fig.update_layout(title='График выбросов 2023-2024',
                    xaxis_title='Месяца', 
                    yaxis_title='Процент выбросов')
    
    

    
    list_reports = ft.ListView(spacing=10,auto_scroll=False,horizontal=True,reverse=True)

    
    
    

    
    for report in reports:
        list_reports.controls.append(
            ft.Container(
                # margin=ft.margin.only(top=50),
                width=300,
                padding=ft.padding.all(10),
                border=ft.border.all(1, ft.colors.GREY),
                border_radius=5,
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text(f"{report["month"]}",
                                        size=15,
                                        weight=ft.FontWeight.BOLD
                                ),
                                ft.Text(f"{report["year"]}"),
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Text(f"{report["amount"]}%" ,
                                        size=30,
                                        weight=ft.FontWeight.BOLD
                                ),
                                ft.Text(f"{report["time"]}"),
                            ]
                        )
                        
                    ]
                )
        )
        )
    
    
    
    

    
    page.update()
    
    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        theme_change.label = (
            "Светлая тема" if page.theme_mode == ft.ThemeMode.LIGHT else "Темная тема"
        )
        page.update()
        
    
    theme_change = ft.Switch(label="Светлая тема", on_change=theme_changed)
    

       

    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        # Top Bar 
                        ft.Container(
                            height=90,
                            alignment=ft.alignment.center,
                            content=ft.Row(
                                [
                                    theme_change,
                                    ft.Row(
                                        [
                                            ft.Image(src="logo.png", width=50, height=50),
                                            ft.Text("ЭкоLifeTech", color="green",size=40),
                                        ]
                                    ),
                                    ft.CircleAvatar(
                                        foreground_image_url=f"https://thispersondoesnotexist.com/",
                                        content=ft.Text("USR"),
                                        radius=30,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),  # Top Bar
                        ft.Divider(),

                        # Menu
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Row(
                                [
                                    ft.Text(
                                        "Панель статистики",
                                        size=35,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.ElevatedButton(
                                        "Месячный отчет",
                                        on_click=lambda e: e.page.go("/add"),
                                        # on_click=open_dlg_modal,
                                        bgcolor=ft.colors.BLUE_900,
                                        color="white",
                                        style=ft.ButtonStyle(
                                            padding={ft.MaterialState.DEFAULT: 20},
                                            shape={
                                                ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                                                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
                                            },
                                        ),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                        ),  # end Menu
                        ft.Divider(),
                        
                    

                        # график
                        ft.Container(
                            alignment=ft.alignment.center,
                            height=400,
                            width=1200,
                            content=PlotlyChart(fig, expand=True,original_size=True)
                        ),
                        ft.Divider(),
                        ft.Container(
                            height=100,
                            content=list_reports
                        ),
                        ft.Divider(),
                        
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Text("ЭкоLifeTech CO by EVG", text_align=ft.TextAlign.CENTER,size=5)
                        )
                        
                    ]
                )
            ),
        ],horizontal_alignment=ft.MainAxisAlignment.CENTER,
    )
