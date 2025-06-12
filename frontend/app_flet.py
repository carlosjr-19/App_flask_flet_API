import flet as ft
import requests
from components.config import obtener_config_colores, obtener_config_formulario 
from components.formulario import build_formulario
from components.menu import crear_menu
from components.info import crear_info_panel
from components.utils import crear_dropdown

def main(page: ft.Page):

    # Variables de estado para archivos seleccionados
    archivo_1_path = ""
    archivo_2_path = ""

    def archivo_finanzas_seleccionado(e: ft.FilePickerResultEvent):
        nonlocal archivo_1_path
        if e.files:
            archivo_1_path = e.files[0].path
            info_textfield.value += (f"\n📑Archivo 1: {archivo_1_path}")
            page.update()

    def archivo_general_seleccionado(e: ft.FilePickerResultEvent):
        nonlocal archivo_2_path
        if e.files:
            archivo_2_path = e.files[0].path
            info_textfield.value += (f"\n📑Archivo 2: {archivo_2_path}")
            page.update()
    
    def procesar_archivos(e):
        if not archivo_1_path or not archivo_2_path:
            info_textfield.value += "\nDebes seleccionar ambos archivos"
            page.update()
            return

        try:
            loader.visible = True 
            page.update()

            #df1 = pd.read_csv(archivo_1_path)
            #df2 = pd.read_excel(archivo_2_path)

            comision = input_comision.value
            sales_p = select_pago_sales.value
            marca = select_marca.value
            proceso = select_proceso.value
            fecha = input_fecha.value

            print(comision, sales_p, marca, proceso, fecha)

            # Empaquetar archivos para enviar al backend
            files = {
                'archivo_1': open(archivo_1_path, 'rb'),
                'archivo_2': open(archivo_2_path, 'rb')
            }

            response = requests.post("http://127.0.0.1:5000/upload", files=files)

            if response.status_code == 200:
                data = response.json()
                info_textfield.value += f"\n✅ {data["message"]}\n"
                info_textfield.value += f"Archivo 1 filas: {data["archivo_1_filas"]}\n"
                info_textfield.value += f"Archivo 2 filas: {data["archivo_2_filas"]}\n"
            else:
                info_textfield.value += f"\n❌ Error: {response.text}"

            page.update()
            
        
        except Exception as ex:
                info_textfield.value += f"❌ Error al procesar los archivos: {ex}\n"
                print(ex)
                page.update()

        finally:
            loader.visible = False
            page.update()



    # Obtener configuraciones desde API
    # Config API
    colores_config = obtener_config_colores()
    formulario_config = obtener_config_formulario()

    bgcolor = colores_config['themes']['bgcolor']
    dark_white = colores_config['themes']['dark_white']
    grey_color = colores_config['themes']['grey_color']
    yellow_color = colores_config['themes']['yellow_color']
    dark_page = colores_config['themes']['dark_page']
    page.bgcolor = bgcolor

    # Configuración de menú desde la API
    menu = crear_menu(colores_config["menu"])

    select_marca = crear_dropdown("Marca", formulario_config["dropdowns"]["marca"])
    select_pago_sales = crear_dropdown("Recibe comisión adelantada por sales", formulario_config["dropdowns"]["sales"])
    select_proceso = crear_dropdown("Proceso", formulario_config["dropdowns"]["proceso"])
    input_comision = crear_dropdown("Comisión %", formulario_config["dropdowns"]["comision"])
    input_fecha = ft.TextField(
        label="Introduce fecha dd-mm-aaaa",
        value=formulario_config["fecha_default"],
        width=350
    )

    loader = ft.ProgressBar(visible=formulario_config["loader_visible"])

    picker_finanzas = ft.FilePicker(on_result=archivo_finanzas_seleccionado)
    picker_general = ft.FilePicker(on_result=archivo_general_seleccionado)

    page.overlay.append(picker_finanzas)
    page.overlay.append(picker_general)

    formulario = build_formulario(
        formulario_config, picker_finanzas, picker_general,
        select_marca, select_pago_sales, select_proceso,
        input_comision, input_fecha, procesar_archivos, loader
    )

    info_textfield = ft.TextField(
        value="", read_only=True, multiline=True, height=500, width=680,
        border_radius=5, border_color=dark_page, text_style=ft.TextStyle(size=14)
    )


    info = crear_info_panel({
        "dark_page": dark_page,
        "yellow_color": yellow_color,
        "width": 800,
        "margin": 5,
        "border_radius": 10,
        "content_width": 700,
        "title": "Información del Proceso",
        "description": "Resultados de la carga de archivos y procesamiento:"
    }, info_textfield)


    page.add(
            ft.Column(
                expand=True,
                controls=[
                    menu,
                    ft.Row(
                        expand=True,
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            formulario,
                            info
                        ]
                    )
                ]
            )
        )                                    

    page.window_width = 14000
    page.window_height = 20000
    page.min_width = 400
    page.min_height = 300
    page.expand = True
    page.window_resizable = True
    page.update() 

ft.app(target=main,)
