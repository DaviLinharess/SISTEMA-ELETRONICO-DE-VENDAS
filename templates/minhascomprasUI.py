# templates/minhascomprasUI.py
import streamlit as st
from View.View import View
from datetime import datetime

class MinhasComprasUI:
    def main():
        st.header("Meus Pedidos")

        id_cliente = st.session_state.get("cliente_id")
        if id_cliente is None:
            st.error("Faça o login para ver seus pedidos.")
            return

        # Chama a nova função que acabamos de criar na View
        minhas_vendas = View.Venda_Listar_Cliente(id_cliente)

        if not minhas_vendas:
            st.info("Você ainda não realizou nenhuma compra.")
            return

        # Ordena as vendas da mais recente para a mais antiga
        minhas_vendas.sort(key=lambda x: x.get_data(), reverse=True)


        for venda in minhas_vendas:
            # Usamos um expander para cada pedido, fica mais organizado
            with st.expander(f"Pedido de {venda.get_data()} - Total: R$ {venda.get_total():.2f}"):
                
                st.write(f"**Status da Entrega:** {'Entregue' if venda.get_entregue() else 'A caminho'}")
                st.markdown("---")
                
                # Para cada venda, buscamos os itens dela
                itens_da_venda = View.VendaItem_Listar(venda.get_id())
                if not itens_da_venda:
                    st.write("Não foi possível carregar os itens deste pedido.")
                else:
                    for item in itens_da_venda:
                        produto = View.Produto_Listar_id(item.get_id_produto())
                        if produto:
                            st.write(f"- **Produto:** {produto.get_descricao()}")
                            st.write(f"  **Quantidade:** {item.get_qtd()}")
                            st.write(f"  **Preço Unitário:** R$ {item.get_preco():.2f}")