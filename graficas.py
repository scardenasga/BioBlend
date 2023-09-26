import flet as ft
from read import leer_datos_desde_csv

archivo_csv = 'assets/Datos/variables.csv'

# Llamar a la función para leer el archivo CSV y obtener las listas
masa, temperatura, ph, agua, consumo_corriente = leer_datos_desde_csv(archivo_csv)


def line_chart():
    class State:
        toggle = True

    s = State()
    
    def get_masa():
        data_points = []
        for i in range(30):
            data_points.append(ft.LineChartDataPoint(i+1,masa[i]))
        return data_points
    def get_agua():
        data_points = []
        for i in range(30):
            data_points.append(ft.LineChartDataPoint(i+1,agua[i]))
        return data_points
    def get_ph():
        data_points = []
        for i in range(30):
            data_points.append(ft.LineChartDataPoint(i+1,ph[i]))
        return data_points

    data_1 = [
        ft.LineChartData(
            data_points=get_masa(),
            stroke_width=8,
            color=ft.colors.LIGHT_GREEN,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=get_agua(),
            color=ft.colors.PINK,
            below_line_bgcolor=ft.colors.with_opacity(0, ft.colors.PINK),
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=get_ph(),
            color=ft.colors.CYAN,
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
        ),
    ]

    data_2 = [
        ft.LineChartData(
            data_points=get_masa(),
            stroke_width=8,
            color=ft.colors.with_opacity(0.5, ft.colors.LIGHT_GREEN),
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=get_agua,
            color=ft.colors.with_opacity(0.5, ft.colors.PINK),
            below_line_bgcolor=ft.colors.with_opacity(0.2, ft.colors.PINK),
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=get_ph(),
            color=ft.colors.with_opacity(0.5, ft.colors.CYAN),
            stroke_width=8,
            stroke_cap_round=True,
        ),
    ]

    def get_chart_axis_labels(start_value, end_value):
        labels = []
        for value in range(start_value, end_value + 1):
            label = ft.ChartAxisLabel(
                value=value,
                label=ft.Container(
                    ft.Text(
                        str(value),
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                    ),
                    margin=ft.margin.only(top=10),
                )
            )
            labels.append(label)
        return labels

    def get_chart_axis_labels_left(start_value, end_value):
        labels = []
        for value in range(start_value, end_value + 1):
            label = ft.ChartAxisLabel(
                value=value,
                label=ft.Text(
                    str(value),
                    size=14,
                    weight=ft.FontWeight.BOLD,
                )
            )
            labels.append(label)
        return labels


    chart = ft.LineChart(
        data_series=data_1,
        border=ft.Border(
            bottom=ft.BorderSide(6, ft.colors.with_opacity(0.4, ft.colors.ON_SURFACE))
        ),
        left_axis=ft.ChartAxis(
            labels=get_chart_axis_labels_left(1,20),
            labels_size=60
        ),
        bottom_axis=ft.ChartAxis(
            labels=get_chart_axis_labels(1,30),
            labels_size=31,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=22,
        min_x=0,
        max_x=31,
        animate=5000,
        # expand=True,
        width=700,
        height=400,
    )


    return ft.Column(
        controls=[chart]
    )


def bar_chart():
    chart = ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(
                x=0,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=40,
                        width=40,
                        color=ft.colors.AMBER,
                        tooltip="Apple",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=100,
                        width=40,
                        color=ft.colors.BLUE,
                        tooltip="Blueberry",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=30,
                        width=40,
                        color=ft.colors.RED,
                        tooltip="Cherry",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=3,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=60,
                        width=40,
                        color=ft.colors.ORANGE,
                        tooltip="Orange",
                        border_radius=0,
                    ),
                ],
            ),
        ],
        border=ft.border.all(1, ft.colors.GREY_400),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Fruit supply"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0, label=ft.Container(ft.Text("Apple"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=1, label=ft.Container(ft.Text("Blueberry"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=2, label=ft.Container(ft.Text("Cherry"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=3, label=ft.Container(ft.Text("Orange"), padding=10)
                ),
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=110,
        interactive=True,
        # expand=True,
        # width=700,
        # height=500,
        aspect_ratio=1,
    )

    # return chart
    return ft.Column(
        controls=[ft.Container(content=chart, padding=10)],
    )


def pie_chart():
    normal_radius = 100
    hover_radius = 110
    normal_title_style = ft.TextStyle(
        size=12, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
    )
    hover_title_style = ft.TextStyle(
        size=16,
        color=ft.colors.WHITE,
        weight=ft.FontWeight.BOLD,
        shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
    )
    normal_badge_size = 40
    hover_badge_size = 50

    def badge(icon, size):
        return ft.Container(
            ft.Icon(icon),
            width=size,
            height=size,
            border=ft.border.all(1, ft.colors.BROWN),
            border_radius=size / 2,
            bgcolor=ft.colors.WHITE,
        )

    def on_chart_event(e: ft.PieChartEvent):
        for idx, section in enumerate(chart.sections):
            if idx == e.section_index:
                section.radius = hover_radius
                section.title_style = hover_title_style
            else:
                section.radius = normal_radius
                section.title_style = normal_title_style
        chart.update()

    chart = ft.PieChart(
        sections=[
            ft.PieChartSection(
                40,
                title="40%",
                title_style=normal_title_style,
                color=ft.colors.BLUE,
                radius=normal_radius,
                badge=badge(ft.icons.AC_UNIT, normal_badge_size),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                30,
                title="30%",
                title_style=normal_title_style,
                color=ft.colors.YELLOW,
                radius=normal_radius,
                badge=badge(ft.icons.ACCESS_ALARM, normal_badge_size),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                15,
                title="15%",
                title_style=normal_title_style,
                color=ft.colors.PURPLE,
                radius=normal_radius,
                badge=badge(ft.icons.APPLE, normal_badge_size),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                15,
                title="15%",
                title_style=normal_title_style,
                color=ft.colors.GREEN,
                radius=normal_radius,
                badge=badge(ft.icons.PEDAL_BIKE, normal_badge_size),
                badge_position=0.98,
            ),
        ],
        sections_space=0,
        center_space_radius=0,
        on_chart_event=on_chart_event,
        expand=True,
    )

    # return chart
    return ft.Column(
        controls=[ft.Container(content=chart, padding=10)],
    )


def example(page):

    def on_new_page_click(event):
        page.go("/")

    def tabs_changed(e):
        print(f"Tabs changed to{e.control.selected_index}")

    charts = ft.Tabs(
        selected_index=0,
        scrollable=False,
        expand=True,
        on_change=tabs_changed,
        tabs=[
            ft.Tab(text="Lineas", content=line_chart()),
            # ft.Tab(text="BarChart", content=bar_chart()),
            # ft.Tab(text="PieChart", content=pie_chart()),
        ],
    )

    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[charts,
                  ft.Container(
                      ft.Row([
                          ft.Text("Masa", color=ft.colors.LIGHT_GREEN),
                          ft.Text("Agua", color=ft.colors.PINK),
                          ft.Text("pH", color=ft.colors.CYAN)
                      ]),
                      alignment=ft.alignment.center_right
                  ),
                  ft.ElevatedButton(
                      "Inicio",
                      color=ft.colors.GREEN,
                      on_click= on_new_page_click
                  )],
    )


activo = False



def principal(page):
    def on_estadistics_click(event):
        page.go("/estadistics")

    def on_values_click(event):
        page.go("/values")




    def on_button_click(event, page):
        # Change the button color to red.
        if activo is not True:
            boton_principal.bgcolor = ft.colors.RED_ACCENT_700
            boton_principal.text= "Stop"
            palabra.value = "El compostador esta encendido"
        else:
            boton_principal.bgcolor = ft.colors.GREEN_ACCENT_700
            boton_principal.text = "Start"
            palabra.value = "El comopostador esta apagado"
            
        page.update()

    boton_principal = ft.ElevatedButton(
                text= "Start",
                color=ft.colors.WHITE,
                bgcolor=ft.colors.GREEN_ACCENT_700,
                on_click=lambda event: on_button_click(event, page),
                width=200,
                height=60,
            )
    palabra = ft.Text(
        value="El condensador esta apagado",
        size=15

    )

    return ft.Column(
        
        spacing=15,
        expand= True,
        controls=[
# Esta es la barra del que tien el titulo
            ft.Container(
                # bgcolor="yellow",
                content=ft.Row([
                    ft.Text("BioBlend",
                            size=50,
                            color=ft.colors.CYAN_ACCENT_700,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD
                            ),
                    ft.Container(
                        # bgcolor="green",
                        content=ft.Row([
                            ft.IconButton(
                                icon=ft.icons.ANALYTICS,
                                icon_color=ft.colors.DEEP_PURPLE_400,
                                icon_size=20,
                                tooltip="Delete record",
                                on_click=on_estadistics_click
                            ),
                            ft.IconButton(
                                icon=ft.icons.TRENDING_UP_ROUNDED,
                                icon_color=ft.colors.AMBER_400,
                                icon_size=20,
                                tooltip="Delete record",
                                on_click=on_values_click
                            ),

                            ],
                            alignment=ft.alignment.center
                            
                        )
                        
                        )
                    ],
                    alignment=ft.MainAxisAlignment,
                    spacing="10%",
                    ),
                    border=ft.Border(
                         bottom=ft. BorderSide(color=ft.colors.GREEN_300, width=1.0)
                    )
            ),
# Este es el cuerpo contiene la imagen y el boton
            ft.Container(
                content=ft.Column([
                        ft.Image(
                            src=f"/Imagen1.png",
                            width="200%",
                            height="30%",
                            fit=ft.ImageFit.CONTAIN
                            ),
                        ft.Container(
                            content=ft.Column([
                            boton_principal,
                            palabra
                            ]),
                            alignment=ft.alignment.bottom_center

                        )
                            


                    ],
                    horizontal_alignment=ft.CrossAxisAlignment),
                    alignment=ft.alignment.bottom_center


                )
        ]


    )

    
def valoresActuales(page):
    def on_estadistics_click(event):
        page.go("/estadistics")
    
    def regresar(event):
        page.go("/")


    def actualizar(event):
        electricidad_dato.value = round(electricidad_dato.value + 0.1,3)
        temperatura_dato.value = round(temperatura_dato.value + 0.1,3)
        produccion_dato.value = round(produccion_dato.value + 0.1,3)
        agua_dato.value = round(agua_dato.value + 0.05,4)
        page.update()

    agua_dato = ft.Text(
        value=agua[0],
        size=20,
        width=ft.FontWeight.BOLD
    )
    temperatura_dato = ft.Text(
        value=temperatura[0],
        size=20,
        width=ft.FontWeight.BOLD
    )
    electricidad_dato = ft.Text(
        value=consumo_corriente[0],
        size=20,
        width=ft.FontWeight.BOLD
    )
    produccion_dato = ft.Text(
        value=masa[0],
        size=20,
        width=ft.FontWeight.BOLD
    )

    return ft.Column(
        controls=[
             ft.Container(
                ft.Row([
                    ft.IconButton(
                        icon=ft.icons.HOME,
                        icon_color=ft.colors.AMBER_400,
                        icon_size=30,
                        tooltip="Delete record",
                        on_click=on_estadistics_click
                    ),
                    ft.Text("Datos", size=30, width=ft.FontWeight.BOLD)

                ],
                spacing="200%"
                ),
                # bgcolor="red",
                border=ft.Border(
                    bottom=ft. BorderSide(color=ft.colors.GREEN_300, width=1.0)
                    ),
                alignment=ft.alignment.center,
                width=70
            ),
            ft.Container(
                ft.Row([
                    ft.Text("Mililitros de agua producido:"),
                    agua_dato

                ]),
                bgcolor=ft.colors.LIGHT_BLUE,
                border=ft.Border(
                    bottom=ft. BorderSide(color=ft.colors.WHITE70, width=3.0)
                    ),
                height=60
            ),
            ft.Container(
                ft.Row([
                     ft.Text("Temperatura:"),
                    temperatura_dato

                ]),
                bgcolor=ft.colors.RED_ACCENT_700,
                border=ft.Border(
                    bottom=ft. BorderSide(color=ft.colors.WHITE70, width=3.0)
                    ),
                height=60
            ),
            ft.Container(
                ft.Row([
                    ft.Text("Consumo electrico:"),
                    electricidad_dato

                ]),
                bgcolor=ft.colors.AMBER_ACCENT_700,
                border=ft.Border(
                    bottom=ft. BorderSide(color=ft.colors.WHITE70, width=3.0)
                    ),
                height=60
            ),
            ft.Container(
                ft.Row([
                    ft.Text("Produccion de compost:"),
                    produccion_dato

                ]),
                bgcolor=ft.colors.GREEN_ACCENT_700,
                border=ft.Border(
                    bottom=ft. BorderSide(color=ft.colors.WHITE70, width=3.0)
                    ),
                height=60
            ),
            ft.Container(
                ft.Row([
                    ft.ElevatedButton("Actualizar",
                                      color=ft.colors.WHITE70,
                                      bgcolor=ft.colors.PURPLE_ACCENT_700,
                                      on_click=actualizar
                                      )
                ]),
                # bgcolor="yellow",
                border=ft.Border(
                    bottom=ft. BorderSide(color=ft.colors.WHITE70, width=1.0)
                    ),
                height=60
            ),
            ft.Container(
                ft.Row([
                    ft.ElevatedButton(
                        text="Regresar",
                        color=ft.colors.WHITE70,
                        bgcolor=ft.colors.TEAL_ACCENT_700,
                        on_click=regresar
                    )
                ]),
                # bgcolor="purpule",
                border=ft.Border(
                    bottom=ft. BorderSide(color=ft.colors.WHITE70, width=1.0)
                    ),
                height=60
            ),

        ],
        alignment=ft.alignment.center,
        spacing=15

    )
    
    


def views_handler(page):

    return {
        '/':ft.View(
            route='/',
            controls=[
                principal(page),
            ]
        ),
        '/estadistics':ft.View(
            route='/estadistics',
            controls=[
              example(page)
              

            ]
        ),
        '/values': ft.View(
            route='/values',
            controls=[
                valoresActuales(page)
            ]
        )
    }


def main(page: ft.Page):
 
    page.title = "BioBlend"
    page.window_width = 350
    page.window_height = 650

    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]

        )

    page.on_route_change = route_change
    page.update()
    page.go("/")
    


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets/Datos")