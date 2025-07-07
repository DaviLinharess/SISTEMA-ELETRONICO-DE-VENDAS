import streamlit as st
from View import View
import time

class MinhasComprasUI:
    def main():
        st.header("Meu Histórico de Compras")

        id_cliente = st.session_state.get("cliente_id")
        if id_cliente is None:
            st.error("Faça login pra ver seu histórico de compras")
            return

        minhas_vendas = View.Venda_Listar_Cliente(id_cliente)

        if len(minhas_vendas) == 0:
            st.info("Não tem compras finalizadas")
        else:
            vendas_ordenadas = sorted(minhas_vendas, key=lambda v: v.get_data(), reverse=True)
            
            for venda in vendas_ordenadas:
                st.subheader(f"Pedido #{venda.get_id()} - Realizado em: {venda.get_data().strftime('%d/%m/%Y')}")
                
                itens_da_venda = View.Venda_Itens_Listar(venda.get_id())
                
                if not itens_da_venda:
                    st.write("Nao tem itens no pedido")
                else:
                    for item in itens_da_venda:
                        produto = View.Produto_Listar_id(item.get_id_produto())
                        if produto:
                            # colunas para alinhar o nome do produto e o botão
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                st.text(f"- {produto.get_descricao()}")
                                st.caption(f"  Quantidade: {item.get_qtd()} | Preço: R$ {item.get_preco():.2f}")
                            with col2:
                                # chave única para cada botão para evitar conflitos
                                key_button = f"buy_again_{venda.get_id()}_{item.get_id()}"
                                
                                if st.button("Comprar novamente", key=key_button):
                                    try:
                                        # adiciona 1 unidade do produto ao carrinho
                                        View.carrinho_adicionar(id_cliente, produto.get_id(), 1)
                                        st.success(f'"{produto.get_descricao()}" foi adicionado ao seu carrinho!')
                                        time.sleep(2) # pausa pra ler a mensagem
                                    except Exception as e:
                                        st.error(f"Erro ao adicionar ao carrinho: {e}")
                
                st.write(f"Total do Pedido: R$ {venda.get_total():.2f}")
                st.markdown("---")