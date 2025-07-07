import streamlit as st
from View.View import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir uma Nova Conta")

        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        fone = st.text_input("Informe o telefone")

        if st.button("Cadastrar"):
            try:
                View.Cliente_Inserir(email=email, senha=senha, nome=nome, fone=fone)
                st.success("Conta criada, Você já pode fazer o login")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao criar conta: {e}")