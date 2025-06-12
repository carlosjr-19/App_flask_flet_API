import flet as ft

def crear_menu(menu_config):
    menu = ft.Container(
        width=menu_config["width"],
        height=menu_config["height"],
        bgcolor=menu_config["bgcolor"],
        border_radius=5,
        padding=5,
        alignment=ft.alignment.center_right,
        content=ft.Row(
            controls=[
                ft.ElevatedButton(
                    btn["text"],
                    icon=getattr(ft.Icons, btn["icon"].upper()),
                    width=180
                )
                for btn in menu_config["buttons"]
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10
        )
    )
    return menu