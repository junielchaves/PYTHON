from flet import *

def main(janela):
    janela.window_width =350
    janela.window_height=400
    janela.window_maximizable = False
    janela.window_always_on_top = True
    janela.window_resizable = False
    janela.vertical_alignment = MainAxisAlignment.CENTER
    janela.title=" Contador Python"
    janela.update()
    
    numero = TextField (value="0", text_size=50,text_align="center", width=80, border_width="0", color="blue")
    contador = Text(value="0",size=30)
    
    def mais(e):
      numero.value = str(int(numero.value)+1)
      if int(str(numero.value))>=10:
         contador.value=str(int(contador.value)+10)
      janela.update()
    
    def menos(e):
      numero.value = str(int(numero.value)-1)
      janela.update()     


    janela.add(
        Row(
        [
            IconButton( icons.REMOVE,on_click=menos),
            numero,
            IconButton( icons.ADD,on_click=mais)
            
        ],
        alignment= MainAxisAlignment.CENTER
        ),
        Row(
        [
           contador
            
        ],
        alignment= MainAxisAlignment.CENTER
        )
    )

app(target=main)