import flet as ft

def crear_dropdown(label, options, width=350):
    return ft.Dropdown(
        label=label,
        width=width,
        options=[ft.dropdown.Option(o) for o in options]
    )