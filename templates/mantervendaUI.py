import streamlit as st
import pandas as pd
from View.View import View

class ManterVendaUI:
    def main():
        st.header("Histórico de Vendas")
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