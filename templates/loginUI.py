import streamlit as st
from View.View import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Entrar"):
            usuario = View.autenticar_usuario(email, senha)
            if usuario is None: 
                st.write("E-mail ou senha inválidos")
            else:    
                st.session_state["cliente_id"] = usuario["id"]
                st.session_state["cliente_nome"] = usuario["nome"]
                st.session_state["e_admin"] = usuario["e_admin"]
                st.session_state["e_entregador"] = usuario["e_entregador"] 
                st.rerun()