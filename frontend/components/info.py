import flet as ft

def crear_info_panel(info_config, info_textfield):
    dark_page = info_config["dark_page"]
    yellow_color = info_config["yellow_color"]

    info_panel = ft.Container(
        width=info_config["width"],
        margin=info_config["margin"],
        alignment=ft.alignment.top_center,
        bgcolor=yellow_color,
        border_radius=info_config["border_radius"],
        content=ft.Column(
            expand=True,
            width=info_config["content_width"],
            alignment=ft.alignment.top_left,
            controls=[
                ft.Text(info_config["title"], size=20, weight="bold", color=dark_page),
                ft.Text(info_config["description"]),
                info_textfield,
            ]
        )
    )
    return info_panel