import flet as ft

def build_formulario(config, picker_finanzas, picker_general, select_marca, select_pago_sales,
                    select_proceso, input_comision, input_fecha, procesar_archivos, loader):
    container_conf = config["container"]

    return ft.Container(
        width=container_conf["width"],
        height=container_conf["height"],
        margin=container_conf["margin"],
        alignment=ft.alignment.top_center,
        bgcolor=container_conf["bgcolor"],
        border_radius=container_conf["border_radius"],
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    config["title"]["text"],
                    size=config["title"]["size"],
                    weight=config["title"]["weight"],
                    color=config["title"]["color"]
                ),
                ft.Text(config["labels"]["archivo_finanzas"]),
                ft.ElevatedButton("Seleccionar CSV 1", icon=ft.Icons.UPLOAD_FILE, on_click=lambda _: picker_finanzas.pick_files(allow_multiple=False)),
                ft.Text(config["labels"]["archivo_general"]),
                ft.ElevatedButton("Seleccionar Excel General", icon=ft.Icons.UPLOAD_FILE, on_click=lambda _: picker_general.pick_files(allow_multiple=False)),
                select_marca,
                select_pago_sales,
                select_proceso,
                input_comision,
                input_fecha,
                ft.ElevatedButton(
                    text=config["procesar_button"]["text"],
                    bgcolor=config["procesar_button"]["bgcolor"],
                    width=config["procesar_button"]["width"],
                    color=config["procesar_button"]["color"],
                    icon=getattr(ft.Icons, config["procesar_button"]["icon"].upper()),
                    on_click=procesar_archivos,
                ),
                loader,
            ]
        )
    )