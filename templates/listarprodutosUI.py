# templates/listarprodutosUI.py

import streamlit as st
from View.View import View
import time

class ListarProdutosUI:
    def main():
        st.header("Nossos Produtos")
        
        id_cliente = st.session_state.get("cliente_id")
        if id_cliente is None:
            st.error("Faça o login para adicionar produtos ao carrinho!")
            return

        produtos = View.Produto_Listar()
        if not produtos:
            st.warning("Nenhum produto cadastrado no momento.")
            return

        for produto in produtos:
            st.subheader(produto.get_descricao())
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"Preço: R$ {produto.get_preco():.2f}")
                st.write(f"Estoque: {produto.get_estoque()}")
            
            with col2:
                # Chave única para cada botão/number_input para evitar conflitos
                key_qtd = f"qtd_{produto.get_id()}"
                key_btn = f"btn_{produto.get_id()}"
                
                qtd = st.number_input("Qtd", min_value=1, value=1, key=key_qtd)
                if st.button("Adicionar ao Carrinho", key=key_btn):
                    try:
                        View.carrinho_adicionar(id_cliente, produto.get_id(), qtd)
                        st.success(f'{qtd}x "{produto.get_descricao()}" adicionado(s) ao carrinho!')
                        time.sleep(1)
                    except ValueError as e:
                        st.error(f"Erro: {e}")

            st.markdown("---")