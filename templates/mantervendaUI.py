import streamlit as st
import pandas as pd
from View.View import View
import time

class ManterVendaUI:
    def main():
        st.header("Histórico de Vendas e Entregas")

        vendas_pendentes = View.Venda_Listar_Pendentes()
        if len(vendas_pendentes) == 0:
            st.write("Nenhuma venda pendente pra entrega")
            return
        
        entregadores = View.Entregador_Listar() #entregadores disponiveis
        if len (entregadores) == 0:
            st.warning("Nenhum entregador cadastrado")
            return 
        
        for venda in vendas_pendentes: #mostra as vendas pendentes com opção de iniciar entrega
            cliente = View.Cliente_Listar_id(venda.get_id_cliente())
            nome_cliente = cliente.get_nome() if cliente else "Cliente não encontrado"

        st.subheader(f"Venda #{venda.get_id()} - Cliente: {nome_cliente}")

        col1, col2 = st.columns([3,1])
        with col1:
            st.text(f"Data: {venda.get_data().strftime('%d/%m/%Y %H:%M')}")
            st.text(f"Total: R$ {venda.get_total():.2f}")
        with col2: #formulario pra cada venda, evitar conflito de botao
            with st.form(key=f"form_entrega_{venda.get_id()}"): 
                entregador_selecionado = st.selectbox(
                    "Adicionar ao Entregador",
                    options=entregadores,
                    format_func=lambda e: e.get_nome(), #mostra o nome do entregador
                    key=f"select_entregador_{venda.get_id()}"
                )
                submit_button = st.form_submit_button("Iniciar Entrega")
                if submit_button:
                        try:
                            View.Iniciar_Entrega(venda.get_id(), entregador_selecionado.get_id())
                            st.success(f"Entrega da venda #{venda.get_id()} iniciada com sucesso!")
                            time.sleep(1)
                            st.rerun() # Recarrega a página para atualizar a lista
                        except Exception as e:
                            st.error(f"Erro ao iniciar entrega: {e}")
            st.markdown("---")

        ManterVendaUI.listar() 

    def listar():
        vendas = View.Venda_Listar()
        if len(vendas) == 0:
            st.write("Nenhuma venda foi encontrada.")
        else:
            dados_venda = []
            for v in vendas:
                cliente = View.Cliente_Listar_id(v.get_id_cliente())
                nome_cliente = cliente.get_nome() if cliente else "Não encontrado"
                dados_venda.append({
                    "ID da Venda": v.get_id(),
                    "Data": v.get_data().strftime('%d/%m/%Y %H:%M'),
                    "Cliente": nome_cliente,
                    "ID do Cliente": v.get_id_cliente(),
                    "Total (R$)": f"{v.get_total():.2f}"
                })
            
            # Criamos o DataFrame do Pandas e o exibimos com st.dataframe
            df = pd.DataFrame(dados_venda)
            st.dataframe(df)