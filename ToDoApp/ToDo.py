from flet import *
import sqlite3


class ToDo:
    def __init__(self, pagina):
        self.pagina = pagina
        self.pagina.window_width= 380
        self.pagina.window_height = 550
        self.pagina.title="Aplicativo ToDo Python"
        self.pagina.window_always_on_top=True
        self.pagina.window_resizable = False
        self.db_execute("CREATE TABLE IF NOT EXISTS tarefas (nome, status)")
        self.result = self.db_execute("SELECT * FROM tarefas")
        self.view = "todos"
        self.pagina.update()
        self.main_page()
        
    def lista_tarefas(self):
        return Container(
            height= self.pagina.height*0.8,
            content= Column(
                controls=[
                    Checkbox(label=res[0], 
                                on_change = self.verifica_lista, 
                                value=True if res[1] == "completo" else False)
                    for res in self.result if res
                ]
            )
        )
    
    def db_execute(self, query, params = []):
        with sqlite3.connect("database.db") as con:
         cur = con.cursor()
         cur.execute(query,params)
         con.commit()
         return cur.fetchall()
    
    def set_input(self,e):
        self.input_value = e.control.value
        
    def verifica_lista(self,e):
        verifica = e.control.value
        label = e.control.label
        
        if verifica:
            self.db_execute("UPDATE tarefas SET status ='completo' WHERE nome = ?", params=[label])
        else:
            self.db_execute("UPDATE tarefas SET status ='incompleto' WHERE nome = ?", params=[label])
            
        if self.view == "todos":
            self.result = self.db_execute("SELECT * FROM tarefas")
        else:
            self.result = self.db_execute("SELECT * FROM tarefas WHERE status = ?", params=[self.view])  
              
        self.update_lista_tarefas()
        self.pagina.update()
        
    def tabs_selecionado(self,e):
        if e.control.selected_index == 0:
            self.result = self.db_execute("SELECT * FROM tarefas")
            self.view = "todos"
        elif e.control.selected_index == 1:
            self.result = self.db_execute("SELECT * FROM tarefas WHERE status = 'incompleto'")
            self.view = "incompleto"
        elif e.control.selected_index == 2:
            self.result = self.db_execute("SELECT * FROM tarefas WHERE status = 'completo'")
            self.view = "completo"  
            
        self.update_lista_tarefas()
        self.pagina.update() 
            
    def add_tarefa(self,e, input_tarefa):
        tarefa = self.input_value
        status = "incompleto"
        
        if tarefa:
           self.db_execute(query="INSERT INTO tarefas VALUES (?,?)", params=[tarefa, status])
           input_tarefa.value = ""
           self.pagina.update()
           self.result = self.db_execute("SELECT * FROM tarefas")
           self.update_lista_tarefas()
           
    def update_lista_tarefas(self):
        update_tarefas = self.lista_tarefas()
        self.pagina.controls.pop()
        self.pagina.add(update_tarefas)
        self.pagina.update()
        
    def main_page(self):
        
        input_tarefa = TextField(hint_text="Digite sua Tarefa", 
                                    expand=True, text_size=20,
                                    on_change= self.set_input
                                    )
        
        input_menu = Row(
            controls=[
            input_tarefa,
            FloatingActionButton(icon=icons.ADD,
                                    bgcolor="#1E90FF",
                                    on_click=lambda e:self.add_tarefa(e,input_tarefa)
                                    )
            ]
        )
        input_tabs = Row(
            controls=[
                Tabs(
                    selected_index=0,
                    on_change= self.tabs_selecionado,
                    tabs=[Tab(text="Todos"),
                          Tab(text="Em Andamento"),
                          Tab(text="Finalizados")]
                )
            ]
        )
    
        tarefas = self.lista_tarefas()
        
        self.pagina.add(input_menu, input_tabs,tarefas)
    
             
        
app(target=ToDo)   
    