import streamlit as st
from View.View import View
from templates.mantercategoriaUI import ManterCategoriaUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterprodutoUI import ManterProdutoUI
from templates.mantervendaUI import ManterVendaUI
from templates.loginUI import LoginUI
from templates.abrircontaUI import AbrirContaUI
from templates.manterentregadorUI import ManterEntregadorUI 
from templates.manterentregaUI import ManterEntregaUI
from templates.minhascomprasUI import MinhasComprasUI
from templates.listarprodutosUI import ListarProdutosUI
from templates.vercarrinhoUI import VerCarrinhoUI


class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()


    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Categorias", "Cadastro de Clientes", "Cadastro de Produtos", "Cadastro de Entregadores", "Listagem de Vendas"])
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Cadastro de Entregadores": ManterEntregadorUI.main()
        if op == "Listagem de Vendas": ManterVendaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Ver Produtos", "Meu Carrinho", "Meus Pedidos"])
        if op == "Ver Produtos": ListarProdutosUI.main()
        if op == "Meu Carrinho": VerCarrinhoUI.main()
        if op == "Meus Pedidos": MinhasComprasUI.main()

        
    def menu_entregador():
        ManterEntregaUI.main()
        

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    def sidebar():
        if "cliente_id" not in st.session_state:
            # usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # usuário logou
            st.sidebar.write(f"Bem-vindo(a), {st.session_state['cliente_nome']}")
            
            # verifica o tipo de usuario
            if st.session_state.get("e_admin"): #verificação pro admin
                IndexUI.menu_admin()
            elif st.session_state.get("e_entregador"): # verificação para o entregador
                IndexUI.menu_entregador()
            else:
                IndexUI.menu_cliente()
                
            IndexUI.sair_do_sistema()
    
    def main():
        # verifica a existe o usuário admin
        View.cadastrar_admin()

        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()