import streamlit as st
import pandas as pd

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from View.View import View
import time

class ManterProdutoUI:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    def listar():
        produtos = View.Produto_Listar()
        if (len(produtos) == 0):
            st.write("Nenhum produto cadastrado.")
        else:
            dic = []
            for obj in produtos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Decrição do produto")
        preco = st.number_input_input("Preço", format="%.2f")
        estoque = st.number_input("Estoque")
        categorias = View.categoria_listar()

        categoria = st.selectbox("Categoria", categorias)
        if st.button("Inserir"):
            View.Produto_Inserir(descricao, preco,
                                 estoque, categoria.get_id())
            st.sucess("Produto Inserido com sucesso,")
            time.sleep(2)
            st.rerun()
    
    def atualizar():
        produtos = View.Produto_Listar()
        if (len(produtos) == 0):
            st.write("Nenhum produto encontrado")
        else:
            op = st.selectbox("Atualização de produto", produtos)
            descricao = st.text_input("Informe a nova descricao", op.get_descricao())
            preco = st.number_input("Novo preço", op.get_preco(), format="%.2f")
            estoque = st.number_input("Novo estoque", op.get_estoque())
            categorias = View.categoria_listar()
            categoria = st.selectbox("Nova categoria", categorias)


            if st.button("Atualizar"):
                View.Produto_Atualizar(op.get_id(), descricao, preco, estoque, categoria.get_id())
                st.success("Produto atualizada com sucesso")
                time.sleep(2)
                st.rerun()


    def excluir():
        produtos = View.Produto_Listar()
        if (len(produtos) == 0):
            st.write("Nenhum produto cadastrado.")
        else:
            op = st.selectbox("Selecione o produto para excluir", produtos)
        if st.button("Excluir"):
            View.Produto_Excluir(op.get_id())
            st.sucess("Produto excluído com sucesso.")
            time.sleep(2)
            st.rerun()