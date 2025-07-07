# templates/vercarrinhoUI.py
import streamlit as st
from View.View import View

class VerCarrinhoUI:
    def main():
        st.header("Meu Carrinho")

        id_cliente = st.session_state.get("cliente_id")
        if id_cliente is None:
            st.error("Login necessário para ver o carrinho.")
            return

        # Lista os itens do carrinho do cliente logado
        itens_carrinho = View.carrinho_listar(id_cliente)

        if not itens_carrinho:
            st.info("Seu carrinho está vazio.")
            st.markdown("Vá para a tela **Ver Produtos** para adicionar itens!")
            return

        total_carrinho = 0
        for item in itens_carrinho:
            # Busca os detalhes do produto de cada item
            produto = View.Produto_Listar_id(item.get_id_produto())
            if produto:
                subtotal = item.get_qtd() * item.get_preco()
                total_carrinho += subtotal
                
                st.write(f"**Produto:** {produto.get_descricao()}")
                st.write(f"**Quantidade:** {item.get_qtd()} x R$ {item.get_preco():.2f}")
                st.write(f"**Subtotal:** R$ {subtotal:.2f}")
                st.markdown("---")

        st.subheader(f"Valor Total do Pedido: R$ {total_carrinho:.2f}")

        if st.button("Finalizar Compra"):
            try:
                # Chama a função que cria a venda e limpa o carrinho
                View.carrinho_finalizar(id_cliente)
                st.success("Compra finalizada com sucesso!")
                st.balloons()
                # Força a atualização da página para limpar o carrinho visualmente
                st.rerun() 
            except ValueError as e:
                st.error(f"Erro: {e}")