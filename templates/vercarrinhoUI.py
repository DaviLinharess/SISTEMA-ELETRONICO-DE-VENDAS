# templates/vercarrinhoUI.py

import streamlit as st
from View.View import View

class VerCarrinhoUI:
    def main():
        st.header("Meu Carrinho de Compras")

        id_cliente = st.session_state.get("cliente_id")
        if id_cliente is None:
            st.error("Faça o login para ver seu carrinho!")
            return

        itens_carrinho = View.carrinho_listar(id_cliente)

        if not itens_carrinho:
            st.info("Seu carrinho está vazio.")
            return

        total_carrinho = 0
        for item in itens_carrinho:
            produto = View.Produto_Listar_id(item.get_id_produto())
            if produto:
                st.write(f"**Produto:** {produto.get_descricao()}")
                st.write(f"**Quantidade:** {item.get_qtd()}")
                st.write(f"**Preço Unitário:** R$ {item.get_preco():.2f}")
                subtotal = item.get_qtd() * item.get_preco()
                st.write(f"**Subtotal:** R$ {subtotal:.2f}")
                total_carrinho += subtotal
                st.markdown("---")

        st.subheader(f"Total do Carrinho: R$ {total_carrinho:.2f}")

        if st.button("Finalizar Compra"):
            try:
                View.carrinho_finalizar(id_cliente)
                st.success("Compra finalizada com sucesso!")
                # Limpa a lista de itens para não mostrar o carrinho antigo
                itens_carrinho.clear()
                st.rerun()
            except ValueError as e:
                st.error(f"Erro ao finalizar a compra: {e}")