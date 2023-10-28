from flet import *
from time import sleep
import requests



class App:
    def __init__(self, page:Page):
        self.page = page
        self.page.window_width = 390
        self.page.window_height = 650
        self.page.title = "Consulta CEP Python"
        self.page.window_always_on_top = True
        self.page.window_center()
        self.page.window_maximizable = False
        self.page.bgcolor = colors.AMBER
        self.page.fonts = {"Roboto-Regular": "./assets/fonts/Roboto-Regular.ttf"}
        self.page.theme = Theme(font_family="Roboto-Regular")
        self.page.horizontal_alignment = MainAxisAlignment.CENTER
        self.cep_digitado = ""
        self.constructor()
        self.page.update()

    def atualiza_cep(self, e):
        self.cep_digitado = e.control.value
        self.page.update() 
    
    def nova_consulta(self):
        self.page.controls.pop(-1)
        self.page.controls.pop(-1)
        self.page.controls.pop(-1)
        self.constructor()     

    def buscar_cep(self,e,text_field):
        
        text_field.value = ""
        self.page.update()
        
        if self.cep_digitado == "":
            self.page.update()
            
        if len(self.cep_digitado)==8:
            try:
                cep = int(self.cep_digitado)
                link1 = f"https://viacep.com.br/ws/{cep}/json/"
                requisicao = requests.get(link1)
                response = requisicao.json()

                try:
                    erro_cep = response["erro"]
                    self.cep_digitado = ""
                    self.page.snack_bar = SnackBar(Text("[X] Error: CEP Inexistente, ou erro ao digitar."), bgcolor=colors.RED)
                    self.page.snack_bar.open = True 
                    self.page.update()
                except KeyError:
                    self.cep_digitado = ""
                    self.page.controls.pop()
                    header_result = Container(
                        margin=margin.only(top=70),
                        alignment=alignment.center,
                        content=Text(value=f"Resultado da Busca [{cep}]", size=18, weight=FontWeight.W_700, color=colors.WHITE70, font_family="Roboto-Regular")
            
                    )
                    body_result = Container(
                        margin=margin.only(left=25,top=25),
                        alignment=alignment.center_left,
                        padding=padding.all(20),
                        bgcolor= colors.WHITE38,
                        border_radius=10,
                        width=300,
                        content=ListView(
                         controls=[ 
                         Text(value=f"CAIXA POSTAL: {response['cep']}", size=15, color="#05469D"),
                         Text(value=f"ENDEREÇO: {response['logradouro']}", size=15, color="#05469D"),
                            Text(value=f"COMPLEMENTO: {response['complemento']}", size=15, color="#05469D"),
                            Text(value=f"BAIRRO: {response['bairro']} ", size=15, color="#05469D"),
                            Text(value=f"CIDADE: {response['localidade']} - {response['uf']}", size=15, color="#05469D"),
                            ]
                        ) 
                    )
                    bnt_nova_consulta = Container(
                        margin=margin.only(left=10,top=35),
                        alignment=alignment.center,
                        content= ElevatedButton(text="Nova Consulta",
                                                bgcolor="#05469D",
                                                color= colors.WHITE,
                                                on_click= lambda e: self.nova_consulta(),
                                                style=ButtonStyle(shape=RoundedRectangleBorder(radius=8))
                                                )
                    )
                    self.page.update()
                    return self.page.add(header_result,body_result,bnt_nova_consulta)
                
            except ValueError:
                 self.cep_digitado = ""
                 self.page.snack_bar = SnackBar(Text("[X] Error: Digite apenas NUMEROS!"), bgcolor=colors.RED)
                 self.page.snack_bar.open = True 
                 self.page.update()
                 
        elif len(self.cep_digitado) >=1 :
            self.cep_digitado =""
            self.page.update()
            self.page.snack_bar = SnackBar(Text("[X] Error: Digite 8 caracteres do tipo NUMERO!"), bgcolor=colors.RED)
            self.page.snack_bar.open = True 
            self.page.update()
              
       
    def constructor(self):
        header = Container(
            content=Row(
                spacing=2,
                alignment="center", 
                controls=[
                    Text(value="Consulta CEP", color=colors.WHITE70, size=25, weight=FontWeight.W_900),
                    Icon(name=icons.MANAGE_SEARCH_SHARP, color=colors.WHITE70, size=48),
                ]
            ),
            margin=margin.only(top=10, bottom=10),
            alignment=alignment.center,
            width=390

        )
        image = Container(
            content=Image(src=f"./assets/images/logo.png",
                          width=100, height=100, fit=ImageFit.CONTAIN),
            margin=margin.only(top=100),
        )
        text_field = TextField(hint_text="Digite o CEP", 
                                value="",
                                width=180,
                                height=50,
                                border_color=colors.WHITE70,
                                border_radius=10,
                                border_width=1,
                                text_align="center",
                                content_padding = padding.all(0),
                                color="#05469D",
                                text_size=20,
                                on_change=self.atualiza_cep
        )

        input_cep = Row(
            controls=[
                      text_field, 
                      ElevatedButton(
                " ",
                icon="SEARCH_OUTLINED",
                bgcolor = "#05469D",
                icon_color=colors.WHITE,
                style=ButtonStyle(
                    shape=RoundedRectangleBorder(radius=8),
                    elevation=100,

                ),
                height=50,
                width =60,
                on_click=lambda e:self.buscar_cep(e,text_field)
            ),
            ],
            spacing=5,
            alignment="center",
            width=390
        )
        
        


        body = Container(
            content=ListView(
                controls=[
                    image,
                    header,
                    input_cep
                ]
            ),
            width=390,
            margin=margin.all(-10),
            gradient=LinearGradient(begin=alignment.bottom_center, end=alignment.top_center, colors=[
                                    colors.AMBER, colors.AMBER_ACCENT_700])
        )

        self.page.update()
        self.page.add(body)


app(target=App)
