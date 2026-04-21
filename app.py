import streamlit as st
from docxtpl import DocxTemplate
from datetime import datetime
import io
import random

# --- 1. SUPER DICIONÁRIO ESTRUTURADO (COMPLETO) ---
DICIONARIO_ULTRA = {
    # NÚCLEO FAMILIAR E COMPLEXOS
    "pai": "instância paterna, representante da Lei e do Ideal do Eu",
    "mãe": "figura materna, suporte das relações primordiais e do desejo do Outro",
    "irmão": "relação fraternal, campo da rivalidade imaginária e do semelhante",
    "filho": "investimento pulsional no objeto narcísico descendente",
    "família": "constelação familiar e seus atravessamentos simbólicos",
    "infância": "período de constituição subjetiva e fixações libidinais",
    
    # AFETOS, ANGÚSTIA E HUMOR
    "medo": "angústia manifesta que sinaliza o encontro com o Real",
    "triste": "afeto melancólico associado a uma perda do objeto libidinal",
    "raiva": "afeto agressivo e tensão narcísica frente ao Outro",
    "culpa": "tensão ética entre o Eu e a severidade do Superego",
    "ansiedade": "fenômeno da angústia como sinal do desamparo subjetivo",
    "desespero": "ponto de basta subjetivo frente ao desamparo (Hilflosigkeit)",
    "vazio": "sentimento de falta constitutiva e desinvestimento objetal",
    
    # SINTOMAS E MANIFESTAÇÕES DO CORPO
    "insônia": "distúrbio do sono como resistência ao relaxamento do controle do Eu",
    "não dorme": "manifestação sintomática de agitação psíquica e excesso pulsional",
    "comer": "relação com a oralidade e a demanda de preenchimento do vazio",
    "corpo": "o soma como palco de conversões histéricas e manifestações pulsionais",
    "dor": "sofrimento psíquico manifestado via via somática",
    "pânico": "crise de angústia aguda sem mediação simbólica",
    
    # SEXUALIDADE E DESEJO
    "sexo": "economia libidinosa e a relação do sujeito com o gozo",
    "traição": "ruptura do contrato simbólico e ferida no narcisismo",
    "ciúme": "triangulação do desejo e angústia de castração",
    "namorado": "objeto de investimento amoroso e projeções imaginárias",
    "casamento": "laço conjugal e as repetições de padrões parentais",
    
    # MUNDO EXTERNO E LABORAL
    "trabalho": "ambiente laboral enquanto campo de repetição de impasses subjetivos",
    "chefe": "figura de autoridade que reatualiza a relação com o pai primordial",
    "dinheiro": "significante do valor fálico e do poder simbólico",
    "carreira": "realização profissional vinculada às exigências do Superego",
    
    # FORMAÇÕES DO INCONSCIENTE
    "esqueceu": "ato falho que denuncia uma interrupção pelo recalque",
    "sonho": "produção onírica, via régia para o acesso ao inconsciente",
    "silêncio": "resistência que marca a proximidade de um conteúdo recalcado",
    "erro": "lapso ou formação substitutiva que revela o desejo",
    "repetição": "compulsão à repetição e insistência do sintoma"
}

# --- 2. MOTOR DE MÁSCARAS (EXTREMAMENTE COMPLETO) ---
def aplicar_inteligencia(tipo, texto_bruto):
    if not texto_bruto or len(texto_bruto.strip()) < 3:
        return "Sem intercorrências significativas registradas nesta dimensão clínica."

    # Processamento do Dicionário
    processado = texto_bruto.lower()
    for simples, tecnico in DICIONARIO_ULTRA.items():
        if simples in processado:
            processado = processado.replace(simples, f"**{tecnico}**")
    
    processado = processado.capitalize()

    # Banco de Máscaras (Conforme desenvolvido anteriormente)
    mascaras = {
        "analise": [
            f"No horizonte da clínica, observa-se que o sujeito articulou conteúdos sobre {processado}. Tal material aponta para uma tentativa de elaboração dos impasses subjetivos frente ao desejo.",
            f"Durante a escuta analítica, o analisando produziu um material discursivo focado em {processado}, demandando a sustentação da neutralidade frente às demandas."
        ],
        "resistencias": [
            f"O processo de investigação encontrou obstáculos sob a forma de {processado}. Estas formações defensivas são compreendidas como mecanismos de preservação do Eu frente ao Real.",
            f"Verificou-se que o fluxo associativo apresentou {processado}. Tais pontos de clivagem foram manejados via pontuação analítica para favorecer a retificação subjetiva."
        ],
        "transferencia": [
            f"A dinâmica transferencial estabeleceu-se a partir de {processado}, onde o analista é convocado a ocupar um lugar de suporte para o endereçamento das demandas.",
            f"O vínculo transferencial demonstrou estabilidade ao abordar {processado}, permitindo que o analista operasse no lugar de suposto saber, viabilizando a associação livre."
        ]
    }
    
    return random.choice(mascaras.get(tipo, [processado]))

# --- 3. INTERFACE VISUAL (FORMATO DO SITE - DUAS COLUNAS) ---
st.set_page_config(page_title="Sistema Edivania ULTRA", layout="wide")
st.title("🏥 Registro de Evolução Psicanalítica - Alta Complexidade")

col1, col2 = st.columns(2)

with col1:
    nome = st.text_input("Identificação do Analisando")
    data = st.date_input("Data", datetime.now())

st.divider()

with col1:
    st.markdown("### 🗣️ Dinâmica Discursiva")
    analise_in = st.text_area("O que o paciente trouxe? (Notas brutas)", height=150)
    
    st.markdown("### 🔗 Significantes")
    sig_in = st.text_area("Termos que se repetiram", height=100)

with col2:
    st.markdown("### 🛡️ Resistências e Transferência")
    res_in = st.text_area("Dificuldades e vínculo com analista", height=150)
    
    st.markdown("### 📅 Planejamento")
    pend_in = st.text_area("O que ficou para a próxima?", height=100)

# --- 4. GERAÇÃO DO DOCUMENTO ---
if st.button("GERAR EVOLUÇÃO CLÍNICA DE ALTA COMPLEXIDADE"):
    if nome and analise_in:
        with st.spinner("Construindo narrativa clínica baseada na Matriz Psicanalítica..."):
            
            # Aplicação das Máscaras + Dicionário em cada campo
            final_analise = aplicar_inteligencia("analise", analise_in)
            final_resistencia = aplicar_inteligencia("resistencias", res_in)
            final_transferencia = aplicar_inteligencia("transferencia", res_in)
            
            # Processamento de Significantes e Pendências (Apenas Dicionário)
            final_sig = sig_in.lower()
            for s, t in DICIONARIO_ULTRA.items():
                if s in final_sig: final_sig = final_sig.replace(s, t)
            
            final_pend = pend_in.lower()
            for s, t in DICIONARIO_ULTRA.items():
                if s in final_pend: final_pend = final_pend.replace(s, t)

            contexto = {
                'nome': nome,
                'data': data.strftime('%d/%m/%Y'),
                'analise': final_analise,
                'significantes': f"A análise da cadeia associativa revelou a insistência de: {final_sig.capitalize() if final_sig else 'Análise em curso'}.",
                'resistencias': final_resistencia,
                'transferencia': final_transferencia,
                'pendencia': f"Para o próximo encontro, estabelece-se como diretriz: {final_pend.capitalize() if final_pend else 'Continuidade da associação livre.'}"
            }
            
            try:
                doc = DocxTemplate("modelo.docx")
                doc.render(contexto)
                buffer = io.BytesIO()
                doc.save(buffer)
                buffer.seek(0)
                
                st.success("✅ Relatório estruturado com sucesso!")
                st.download_button(
                    label="📥 BAIXAR PRONTUÁRIO",
                    data=buffer,
                    file_name=f"Evolucao_{nome}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            except Exception as e:
                st.error(f"Erro no Word: {e}")
    else:
        st.warning("Preencha o nome e a dinâmica discursiva!")