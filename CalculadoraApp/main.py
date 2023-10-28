import flet as ft
from flet import colors

class App:
    def __init__(self, page: ft.Page):
        self.page = page 
        self.page.window_width= 370
        self.page.window_height = 600
        self.page.title="Calculadora Python"
        self.page.fonts = {"Roboto-Regular": "./assets/fonts/Roboto-Regular.ttf"}
        self.page.bgcolor = ft.colors.BLACK12
        self.page.window_always_on_top = True
        self.page.window_resizable = False
        self.page.window_maximizable = False
        self.page.horizontal_alignment.CENTER
        self.operacao = ""
        self.cont = False
        self.res = False
        self.var = False
        self.textDisplay = ft.Text(value="0", color= colors.BLUE_500, size=50, weight=ft.FontWeight.BOLD)
        self.inforDisplay = ft.Text(value="",color=colors.WHITE, size=15)
        self.page.update()
        self.construtor()
        
    def formNum(self, num, sep='.'):
       return num if len(num) <= 3 else self.formNum(num[:-3], sep) + sep + num[-3:]
       #return num if len(num) <= 3 else  num = "{}.{},{}".format(num[1:3], num[3:5])
  
    def select(self,e): 
       self.display = self.textDisplay.value if self.textDisplay.value !="0" else "" 
       self.digitado = e.control.content.value 
       self.digitado = self.digitado if self.digitado !="x" else "*"
       
       if self.res == True:
           self.display =""
           self.inforDisplay.value = ""
           self.res=False
       
       if self.digitado == "AC":
           self.display = "0"
           self.inforDisplay.value = ""
           self.digitado=""
        
       if self.digitado == "C":
           self.display = self.textDisplay.value[:-1]
           self.digitado=""  
           
       if self.digitado in ("/","x","*","%","-","+","="):
           if self.cont == False and self.var == False and self.digitado != "=":
              self.cont = True
              self.inforDisplay.value = self.inforDisplay.value+self.textDisplay.value+self.digitado 
              self.digitado =""
              self.textDisplay.value = "0"
           elif self.var == False:
              self.operacao = self.inforDisplay.value+self.textDisplay.value   
              self.inforDisplay.value = self.inforDisplay.value+self.textDisplay.value+"="   
              self.calcular_valor(operador=self.digitado)
              self.cont = False
           elif self.var == True: self.textDisplay.value = "0"
       else:
           self.textDisplay.value = self.display+self.digitado
           self.textDisplay.value = "0" if self.textDisplay.value == "" else self.display+self.digitado
           self.digitado=""
           self.var = False    
       self.page.update()
    
    def calcular_valor(self,operador):
        if operador in ("/","*","%","-","+","="):
           self.textDisplay.value = eval(self.operacao)
           self.res = True
           self.var = True
           self.digitado=""    
        
        self.page.update()   
         

    def construtor(self):

       display1 = ft.Row(
           controls=[self.inforDisplay],
           alignment="end",
           width=310
       )
       display2 = ft.Row(
           controls=[self.textDisplay],
           alignment="end",
           width=320
        )
       
       bAC = ft.Container(
           content= ft.Text(value="AC",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_300,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       bC = ft.Container(
           content= ft.Text(value="C",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_300,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       bPO = ft.Container(
           content= ft.Text(value="%",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_300,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       bDIV = ft.Container(
           content= ft.Text(value="/",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_500,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       b01 = ft.Container(
           content= ft.Text(value="1",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_100,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       b02 = ft.Container(
           content= ft.Text(value="2",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_100,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       b03 = ft.Container(
           content= ft.Text(value="3",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_100,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       bMU = ft.Container(
           content= ft.Text(value="x",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_500,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       b04 = ft.Container(
           content= ft.Text(value="4",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_100,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       b05 = ft.Container(
           content= ft.Text(value="5",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_100,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       b06 = ft.Container(
           content= ft.Text(value="6",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_100,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       bMI = ft.Container(
           content= ft.Text(value="-",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_500,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       b07 = ft.Container(
           content= ft.Text(value="7",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_100,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       b08 = ft.Container(
           content= ft.Text(value="8",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_100,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       b09 = ft.Container(
           content= ft.Text(value="9",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_100,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       bSO = ft.Container(
           content= ft.Text(value="+",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_500,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       b0P = ft.Container(
           content= ft.Text(value=",",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_300,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       b00 = ft.Container(
           content= ft.Text(value="0",size=25, font_family="Roboto-Regular"),
           bgcolor= colors.BLUE_GREY_100,
           width=70,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
       bRE = ft.Container(
           content= ft.Text(value="=",size=30, font_family="Roboto-Black"),
           bgcolor= colors.BLUE_500,
           width=150,
           height=70,
           border_radius=100,
           alignment=ft.alignment.center,
           on_click=self.select
       )
      
       
       keyboard = ft.Row(
          controls= [ bAC, bC, bPO, bDIV,
                      b01, b02, b03, bMU,
                      b04, b05, b06, bMI,
                      b07, b08, b09, bSO,
                      b0P, b00, bRE
                     ],
          wrap=True,
          width=400,
          alignment="center"
       )
        
       
       self.page.add(display1,display2,keyboard)
       
ft.app(target=App, assets_dir="assets")