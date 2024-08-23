import flet as ft
import datetime
import multiprocessing


q = multiprocessing.Queue()

class Page2(ft.Page):
    def __init__(self):
        super().__init__()


def popup(page_: Page2):
    page_.title = "CheckBox Pelagem"
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page_.window_width = 400
    page_.window_height = 420
    # page_.window_resizable = False
    page_.theme_mode = ft.ThemeMode.LIGHT
    page_.scroll = True
    
    
    def button_clicked(e):
        list_values = {
            f"{c1.label}": c1.value,
            f"{c2.label}": c2.value,
            f"{c3.label}": c3.value,
            f"{c4.label}": c4.value,
            f"{c5.label}": c5.value,
            f"{c6.label}": c6.value,
            f"{c7.label}": c7.value,
            f"{c8.label}": c8.value,
            f"{c9.label}": c9.value,
            f"{c10.label}": c10.value,
            f"{c11.label}": c11.value,
            f"{c12.label}": c12.value,
            f"{c13.label}": c13.value,
            f"{c14.label}": c14.value,
        }

        pelagens = [chave for chave, valor in list_values.items() if valor]
        q.put(pelagens)

        print(list_values)
        print(pelagens)
        # print(q.get())
        page_.window_destroy()
    
    t = ft.Text(value="Escolha a Palagem do Protegido", size=20, weight=ft.FontWeight.BOLD)
    c1 = ft.Checkbox(label="Preto", value=False)
    c2 = ft.Checkbox(label="Cinza", value=False)
    c3 = ft.Checkbox(label="Bege", value=False)
    c4 = ft.Checkbox(label="Siamês", value=False)
    c5 = ft.Checkbox(label="Branco", value=False)
    c6 = ft.Checkbox(label="Marrom", value=False)
    c7 = ft.Checkbox(label="Amarelo", value=False)
    c8 = ft.Checkbox(label="Laranja", value=False)
    c9 = ft.Checkbox(label="Tigrada", value=False)
    c10 = ft.Checkbox(label="Tigrada Preto ou Cinza", value=False)
    c11 = ft.Checkbox(label="Tigrada Amarelo ou Branco", value=False)
    c12 = ft.Checkbox(label="Sem Pelagem", value=False)
    c13 = ft.Checkbox(label="Escama", value=False)
    c14 = ft.Checkbox(label="Outros", value=False)
    b = ft.ElevatedButton(text="Salvar", on_click=button_clicked)

    page_.add(
        ft.Row([t],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Container(height=2),
        ft.Row([
            ft.Column([c1, c2, c3, c4, c5, c6, c7]),
            ft.Container(width=50),
            ft.Column([c8, c9, c10, c11, c12, c13, c14])
        ]),
        ft.Row([
            ft.Column(
                [ft.Container(
                    content=b,
                    padding=10
                )],
            )
        ],
        alignment=ft.MainAxisAlignment.END
        )
    )


def main(page: ft.Page, estado = None):
    data_field = ft.TextField(
        hint_text='Data',
        read_only=True,
        focused_border_color=ft.colors.BLACK,
        value='',
        width=210,
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE,
        border_radius=10
        )
    def change_date(e):
        data_field.value = date_picker.value.date()
        page.update()
    # Criar date_picker_nasc
    date_picker = ft.DatePicker(
        on_change=change_date
    )
    data_castracao = ft.IconButton(
        icon=ft.icons.CALENDAR_MONTH,
        icon_color=ft.colors.WHITE,
        height=50,
        width=50,
        on_click=lambda _: date_picker.pick_date()  # Criar uma função
        )
    page.overlay.append(date_picker)


    def perfil_picked(e):
        if e.files:
            img_perfil.content.src = e.files[0].path
            img_perfil.update()

    def go_home(e):
        page.clean()
        estado.estado = "Tela Seleção"
        estado.main_page()

    icon_return = ft.Container(
        content=ft.IconButton(
            icon=ft.icons.HOME_OUTLINED,
            height=50,
            width=50,
            icon_color=ft.colors.BLACK
        ),
        alignment=ft.alignment.center_left,
        # on_click=go_home,
    )
    img_perfil = ft.Container(
        ft.Image(
            src="https://picsum.photos/800/800",
            width=120,
            height=120,
            border_radius=200,
        )
    )
    
    file_picker = ft.FilePicker(
        on_result=perfil_picked
    )

    upload_img = ft.Container(
        col=8,
        content=ft.Row(
            controls=[
                ft.ElevatedButton("Escolher Foto", 
                                  on_click=lambda _: file_picker.pick_files(allow_multiple=False),
                                  bgcolor="#D9D9D9",
                                  icon=ft.icons.FOLDER_OPEN_OUTLINED, 
                                  color=ft.colors.BLACK)  
            ],
            alignment=ft.MainAxisAlignment.CENTER  
        ),
        width=126
    )
    
    animal_castrado = ft.Dropdown(
        width=172,
        options=[
            ft.dropdown.Option("Castrado"),
            ft.dropdown.Option("Não castrado"),
        ],
        value="Castrado",
        alignment=ft.alignment.center,
        border_radius=8
    )

    campo_obs_cad = ft.Container(
        ft.TextField(
            value="",
            hint_text="Observações castração",
            width=172, height=143,
        ),
    )

    nome_protegido = ft.TextField(
        col=4,
        label="Nome do protegido", 
        value="",
        width=172,
        height=56,
        border_radius=8,
    )

    genero = ft.Dropdown(
        col=4,
        width=172,
        options=[
            ft.dropdown.Option("Gênero"),
            ft.dropdown.Option("Masc."),
            ft.dropdown.Option("Fem."),
            ft.dropdown.Option("Desc.")
        ],
        value="Gênero",
        border_radius=8
    )

    temperamento = ft.Dropdown(
        col=4,
        width=172,
        options=[
            ft.dropdown.Option("Temperamento"),
            ft.dropdown.Option("Calmo"),
            ft.dropdown.Option("Raivoso"),
            ft.dropdown.Option("Sociável"),
            ft.dropdown.Option("Dócil e não convive com outros"),
            ft.dropdown.Option("Dócil e convive com outros"),
            ft.dropdown.Option("Sem Reação"),
            ft.dropdown.Option("Outro"),
        ],
        value="Temperamento",
        alignment=ft.alignment.center,
        border_radius=8
    )

    especie = ft.TextField(
        col=4,
        label="Especie", 
        value="",
        width=172,
        height=56,
        border_radius=8,
    )

    pelagem = ft.Dropdown(
        col=4,  
        width=172,
        options=[
            ft.dropdown.Option("Pelagem"),
            ft.dropdown.Option("Preto"),
            ft.dropdown.Option("Cinza"),
            ft.dropdown.Option("Bege"),
            ft.dropdown.Option("Siamês"),
            ft.dropdown.Option("Branco"),
            ft.dropdown.Option("Marrom"),
            ft.dropdown.Option("Amarelo"),
            ft.dropdown.Option("Laranja"),
            ft.dropdown.Option("Tigrada Marrom ou Preto"),
            ft.dropdown.Option("Tigrada Preto ou Cinza"),
            ft.dropdown.Option("Tigrada Amarelo ou Branco"),
            ft.dropdown.Option("Sem Pelagem"),
            ft.dropdown.Option("Escama"),
            ft.dropdown.Option("Outros"),
        ],  
        value="Pelagem",  
        border_radius=8, 
    )

    raca =  ft.TextField(
        col=4,
        label="Raça", 
        value="",
        width=172,
        height=56,
        border_radius=8,
    )

    porte = ft.Dropdown(
        col=4,
        width=172,
        options=[
            ft.dropdown.Option("Porte"),
            ft.dropdown.Option("Pequeno"),
            ft.dropdown.Option("Médio"),
            ft.dropdown.Option("Grande")
        ],
        value="Porte",
        border_radius=8
    )

    status_atual = ft.Dropdown(
        col=4,
        width=172,
        options=[
            ft.dropdown.Option("Status Atual"),
            ft.dropdown.Option("Abrigado"),
            ft.dropdown.Option("Adotado"),
            ft.dropdown.Option("Óbito")  # Quando o status é mudado para óbito um campo data de óbito e observações de óbito devem aparecer para serem preenchidos
        ],
        value="Status Atual",
        border_radius=8
    )

    mocrochip = ft.Dropdown(
        col=4,
        width=172,
        options=[
            ft.dropdown.Option("Microchip"),
            ft.dropdown.Option("Sim"),
            ft.dropdown.Option("Não"),
        ],
        value="Microchip",
        border_radius=8
    )

    possui_seq = ft.Dropdown(
        col=4,
        width=172,
        options=[
            ft.dropdown.Option("Possui sequela"),
            ft.dropdown.Option("Sim"),
            ft.dropdown.Option("Não"),
        ],
        value="Possui sequela",
        border_radius=8,
    )

    idade = ft.TextField(
        col=3,
        label="Idade ", 
        value="",
        width=109,
        height=56,
        border_radius=8,
    )

    idade_tipo = ft.Dropdown(
        col=1,
        width=172,
        options=[
            ft.dropdown.Option("Tipo"),
            ft.dropdown.Option("Anos"),
            ft.dropdown.Option("Meses"),
        ],
        value="Tipo",
        border_radius=8
    )
    
    def validate_fields(e):
        def run_popup():
            ft.app(target=popup)
        p2 = multiprocessing.Process(target=run_popup)
        p2.start()
        p2.join()

        errors = []
        if not nome_protegido.value:
            errors.append("Nome do protegido é obrigatório.")
        if not idade.value.isdigit():
            errors.append("Idade deve ser um número válido.")
        if errors:
            error_message.value = "\n".join(errors)
            error_message.update()
        else:
            error_message.value = "Formulário válido!"
            error_message.update()

    error_message = ft.Text(value="", color=ft.colors.RED)
    
    submit_button = ft.ElevatedButton(
        text="Salvar",
        on_click=validate_fields,
        color=ft.colors.BLACK
    )

    basic_info = ft.ResponsiveRow(
        col=3,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
        controls=[
            icon_return,
            img_perfil,
            upload_img,
            animal_castrado,
            ft.Row([
                data_field,
                data_castracao
            ]),
            campo_obs_cad
        ]
    )
    
    info_insert = ft.Container(
        padding=80,
        col=12,
        content=ft.ResponsiveRow(
            controls=[
                nome_protegido,
                genero,
                temperamento,
                especie,
                pelagem,
                raca,
                porte,
                status_atual,
                mocrochip,
                possui_seq,
                idade, idade_tipo
            ]
        )
    )
    
    info_obs = ft.Container(
        col=12,
        content=ft.TextField(
            label="Observações", 
            value="",
        ),
        width=300,
        height=155
    ) 
    
    infos_add = ft.ResponsiveRow(
        col=8,
        controls=[
           info_insert,
           info_obs
        ],
        expand=True
    )
    
    layout = ft.ResponsiveRow(
        spacing=70,
        col=12,
        controls=[
            basic_info,
            infos_add,
            error_message
        ],
        # expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(layout)
    page.overlay.append(file_picker)

    page.add(
        ft.Container(
            content=submit_button,
            alignment=ft.alignment.bottom_right,
            padding=ft.padding.only(right=20, bottom=20)
        )
    )


def run_main():
    ft.app(target=main)


def run_popup():
    ft.app(target=popup)


if __name__ == "__main__":
    # t2 = threading.Thread(target=ft.app(target=main), daemon=True)
    # t2.start()
    # t = threading.Thread(target=ft.app(target=LoginView.main), daemon=True)
    # t.start()
    # Adicione este suporte para evitar problemas no Windows com PyInstaller
    multiprocessing.freeze_support()

    # Crie e inicie os processos
    p1 = multiprocessing.Process(target=run_main)

    p1.start()

    # Opcional: Esperar que os processos terminem antes de sair
    p1.join()
