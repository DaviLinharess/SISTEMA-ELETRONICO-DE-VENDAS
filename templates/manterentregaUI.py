import streamlit as st
from View.View import View
import time

class ManterEntregaUI:
    def main():
        st.header("Minhas Entregas")

        id_entregador_logado = st.session_state.get("cliente_id")

        if id_entregador_logado is None:
            st.error("Erro: Não foi possível identificar o entregador logado.")
            return

        minhas_entregas = View.Entrega_Listar_Entregador(id_entregador_logado) # buscar as entregas do entregador logado
        
        # Filtra as entregas pendentes para a aba de confirmação
        entregas_pendentes = [e for e in minhas_entregas if e.get_status() == "Pendente"] # filtra as entregas pendentes na aba de confirmação

        tab1, tab2 = st.tabs(["Entregas Pendentes", "Histórico de Entregas"])

        with tab1:
            ManterEntregaUI.listar_pendentes(entregas_pendentes)
        with tab2:
            ManterEntregaUI.listar_historico(minhas_entregas)

    def listar_pendentes(entregas_pendentes):
        if len(entregas_pendentes) == 0:
            st.write("Você não tem nenhuma entrega pendente no momento.")
            return

        st.subheader("Selecione a entrega para confirmar")
        
        entrega_selecionada = st.selectbox("Entregas a confirmar", entregas_pendentes)

        if st.button("Confirmar Entrega"):
            try:
                View.Confirmar_Entrega(entrega_selecionada.get_id())
                st.success("Entrega confirmada")
                time.sleep(1)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao confirmar: {e}")

    def listar_historico(minhas_entregas):
        if len(minhas_entregas) == 0:
            st.write("Você ainda não realizou nenhuma entrega.")
        else:
            st.subheader("Seu histórico completo de entregas")
            
            # Ordena as entregas da mais recente para a mais antiga
            vendas_ordenadas = sorted(minhas_entregas, key=lambda e: e.get_data(), reverse=True)# ordena as entregas mais recente pras mais antigas


            for entrega in vendas_ordenadas:
                venda = View.Venda_Listar_id(entrega.get_id_venda())
                if venda:
                    cliente = View.Cliente_Listar_id(venda.get_id_cliente())
                    nome_cliente = cliente.get_nome() if cliente else "N/A"
                    
                    st.write(f"**Venda #{entrega.get_id_venda()}** (Cliente: {nome_cliente})")
                    st.text(f"  Data de início: {entrega.get_data().strftime('%d/%m/%Y')}")
                    st.text(f"  Status: {entrega.get_status()}")
                    st.text("------------------------------------") # Linha separadora simples