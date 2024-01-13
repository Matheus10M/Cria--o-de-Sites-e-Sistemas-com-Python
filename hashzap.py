#  FrontEnd -> usuario vê/interage 
# Backend -> logica por tras do site
# pip install flet -> no terminal
# Botao  de iniciar no chat
    # Popup
    # Escreva seu nome  
    # Entrar no chat

#  Chat 
    # mat entrou no chat
    #  mensagens  do usuario
# Campo para enviar mensagem
# Botao de enviar
import flet as ft

def main(pagina):
    titulo = ft.Text('Hashzap')    

    nome_usuario = ft.TextField(label='Escreva seu nome')

    chat = ft.Column()
    
    def enviar_mensagem_tunel(informacoes):        
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        #  colocar o nome do usuario na mensagem
        text_campo_mensagem = f"{nome_usuario.value}:  {campo_mensagem.value}"      
        pagina.pubsub.send_all((text_campo_mensagem))
        #  limpar o campo mensagem
        campo_mensagem.value =''
        pagina.update()
    campo_mensagem = ft.TextField(label='Escreva sua mensagem aqui',
                                   on_submit=enviar_mensagem)
    
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    
    def entrar_chat(evento):
        # feche o popup
        popup.open=False
        # tire o botão inicar chat da tela
        pagina.remove(botao_iniciar)
        # adcionar o nosso chat
        pagina.add(chat)
        # criar campo de enviar mensagem       

        linha_mesagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mesagem)
        # botão enviar mensagem    
        pagina.add(botao_enviar)
        # botao enviar mensagem
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        print(nome_usuario.value)
        pagina.update()
        

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text('Bem Vindo ao Hashzap'),
        content=nome_usuario,
        actions=[ft.ElevatedButton('Entrar',on_click=entrar_chat)]         
        )
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)
    

    
    pagina.add(titulo)
    pagina.add(botao_iniciar)



ft.app(main, view=ft.WEB_BROWSER)    