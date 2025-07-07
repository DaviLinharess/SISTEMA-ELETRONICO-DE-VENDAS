import streamlit as st
import pandas as pd
from View.View import View
import time

class ManterEntregadorUI:
    def main():
        st.header("Cadastro de Entregadores")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterEntregadorUI.listar()
        with tab2:
            ManterEntregadorUI.inserir()
        with tab3:
            ManterEntregadorUI.atualizar()
        with tab4:
            ManterEntregadorUI.excluir()
    
    def listar():
        entregadores = View.Entregador_listar()
        if len(entregadores) == 0:
            st.write("Nenhum entregador cadastrado.")
        else:
            dicionario = []
            for obj in entregadores:
                dicionario.append({
                    "ID": obj.get_id(),
                    "Nome": obj.get_nome(),
                    "Email": obj.get_email(),
                    "Fone": obj.get_fone()
                })

            df = pd.DataFrame(dicionario)
            st.dataframe(df, hide_index=True)
    
    def inserir():
        nome = st.text_input("Informe o nome do entregador")
        email = st.text_input("Informe o email")
        senha = st.text_input("Informe a senha", type="password")
        fone = st.text_input("Informe o telefone")

        if st.button("Inserir Entregador"):
            try:
                View.Entregador_Inserir(nome, email, senha, fone)
                st.success("Entregador inserido com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")
    
    def atualizar():
        entregadores = View.Entregador_Listar()
        if len(entregadores) == 0:
            st.write("Nenhum entregador pra atualizar")
            return
        
        entregador_selecionado = st.selectbox(
            "Selecione o entregador para atualizar",
            entregadores,
            format_func=lambda e: f"{e.get_id()} - {e.get_nome()}")

        if entregador_selecionado:

            nome_atual = entregador_selecionado.get_nome()
            email_atual = entregador_selecionado.get_email()
            fone_atual = entregador_selecionado.get_fone()


            novo_nome = st.text_input("Novo nome", nome_atual)
            novo_email = st.text_input("Novo e-mail", email_atual)
            novo_fone = st.text_input("Novo fone", fone_atual)

        if st.button("Atualizar Entregador"):
            try:
                View.Entregador_Atualizar(entregador_selecionado.get_id(), novo_nome, novo_email, novo_fone)
                st.success("Entregador atualizado")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")
            
    def excluir():
        entregadores = View.Entregador_Listar()
        if len(entregadores) == 0:
            st.write("Nenhum entregador para excluir.")
            return
            
        entregador_selecionado = st.selectbox(
            "Selecione o entregador para excluir",
             entregadores,
             format_func=lambda e: f"{e.get_id()} - {e.get_nome()}")

        if st.button("Excluir Entregador"):
            try:
                View.Entregador_Excluir(entregador_selecionado.get_id())
                st.success("Entregador excluído com sucesso!")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")
