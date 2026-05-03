import streamlit as st
import pandas as pd
import json
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="FITMIND",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .header {
        text-align: center;
        padding: 2rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Base de dados de alimentos com restrições
ALIMENTOS_DATABASE = {
    "Proteínas": {
        "Frango grelhado": {
            "calorias": 165, "proteina": 31, "carboidrato": 0, "gordura": 3.6,
            "alergias": ["aves"], "restricoes": [],
            "beneficios": ["Ganho muscular", "Baixo em gordura"]
        },
        "Ovos cozidos": {
            "calorias": 155, "proteina": 13, "carboidrato": 1.1, "gordura": 11,
            "alergias": ["ovos"], "restricoes": [],
            "beneficios": ["Colina", "Ganho muscular"]
        },
        "Peixe branco": {
            "calorias": 82, "proteina": 17.4, "carboidrato": 0, "gordura": 0.8,
            "alergias": ["peixe", "frutos_do_mar"], "restricoes": [],
            "beneficios": ["Omega-3", "Baixo em gordura"]
        },
        "Carne magra": {
            "calorias": 250, "proteina": 26, "carboidrato": 0, "gordura": 15,
            "alergias": ["carne_vermelha"], "restricoes": [],
            "beneficios": ["Ferro", "Ganho muscular"]
        },
        "Tofu": {
            "calorias": 76, "proteina": 8, "carboidrato": 2, "gordura": 5,
            "alergias": ["soja"], "restricoes": [],
            "beneficios": ["Vegetariano", "Baixo em gordura"]
        },
        "Iogurte natural": {
            "calorias": 59, "proteina": 10, "carboidrato": 3.2, "gordura": 0.2,
            "alergias": ["lactose", "leite"], "restricoes": [],
            "beneficios": ["Probióticos", "Cálcio"]
        },
        "Feijão": {
            "calorias": 127, "proteina": 8.7, "carboidrato": 23, "gordura": 0.5,
            "alergias": [], "restricoes": [],
            "beneficios": ["Fibra", "Vegetariano"]
        },
        "Lentilha": {
            "calorias": 116, "proteina": 9, "carboidrato": 20, "gordura": 0.4,
            "alergias": [], "restricoes": [],
            "beneficios": ["Fibra", "Vegetariano"]
        }
    },
    "Carboidratos": {
        "Arroz integral": {
            "calorias": 112, "proteina": 2.6, "carboidrato": 24, "gordura": 0.9,
            "alergias": ["glúten"], "restricoes": [],
            "beneficios": ["Fibra", "Energia sustentável"]
        },
        "Batata-doce": {
            "calorias": 86, "proteina": 1.6, "carboidrato": 20, "gordura": 0.1,
            "alergias": [], "restricoes": [],
            "beneficios": ["Vitamina A", "Fibra"]
        },
        "Pão integral": {
            "calorias": 265, "proteina": 9, "carboidrato": 49, "gordura": 3.3,
            "alergias": ["glúten", "trigo"], "restricoes": [],
            "beneficios": ["Fibra", "Energia"]
        },
        "Aveia": {
            "calorias": 389, "proteina": 17, "carboidrato": 66, "gordura": 6.9,
            "alergias": ["glúten"], "restricoes": [],
            "beneficios": ["Fibra solúvel", "Colesterol"]
        },
        "Macarrão integral": {
            "calorias": 124, "proteina": 5.3, "carboidrato": 25, "gordura": 1.1,
            "alergias": ["glúten", "trigo"], "restricoes": [],
            "beneficios": ["Fibra", "Energia"]
        },
        "Batata comum": {
            "calorias": 77, "proteina": 2, "carboidrato": 17, "gordura": 0.1,
            "alergias": [], "restricoes": [],
            "beneficios": ["Potássio", "Energia"]
        },
        "Mel": {
            "calorias": 304, "proteina": 0.3, "carboidrato": 82, "gordura": 0,
            "alergias": [], "restricoes": ["diabetes"],
            "beneficios": ["Energia rápida"]
        },
        "Pão sem glúten": {
            "calorias": 250, "proteina": 6, "carboidrato": 48, "gordura": 2,
            "alergias": [], "restricoes": [],
            "beneficios": ["Sem glúten", "Energia"]
        }
    },
    "Vegetais": {
        "Brócolis": {
            "calorias": 34, "proteina": 2.8, "carboidrato": 7, "gordura": 0.4,
            "alergias": [], "restricoes": [],
            "beneficios": ["Vitamina C", "Antioxidantes"]
        },
        "Cenoura": {
            "calorias": 41, "proteina": 0.9, "carboidrato": 10, "gordura": 0.2,
            "alergias": [], "restricoes": [],
            "beneficios": ["Vitamina A", "Visão"]
        },
        "Espinafre": {
            "calorias": 23, "proteina": 2.7, "carboidrato": 3.6, "gordura": 0.4,
            "alergias": [], "restricoes": [],
            "beneficios": ["Ferro", "Antioxidantes"]
        },
        "Alface": {
            "calorias": 15, "proteina": 1.4, "carboidrato": 2.9, "gordura": 0.2,
            "alergias": [], "restricoes": [],
            "beneficios": ["Baixa caloria", "Fibra"]
        },
        "Tomate": {
            "calorias": 18, "proteina": 0.9, "carboidrato": 3.9, "gordura": 0.2,
            "alergias": [], "restricoes": [],
            "beneficios": ["Licopeno", "Antioxidantes"]
        },
        "Abóbora": {
            "calorias": 26, "proteina": 1, "carboidrato": 6.5, "gordura": 0.1,
            "alergias": [], "restricoes": [],
            "beneficios": ["Vitamina A", "Fibra"]
        },
        "Couve-flor": {
            "calorias": 25, "proteina": 1.9, "carboidrato": 5, "gordura": 0.3,
            "alergias": [], "restricoes": [],
            "beneficios": ["Vitamina C", "Baixa caloria"]
        },
        "Beterraba": {
            "calorias": 43, "proteina": 1.6, "carboidrato": 10, "gordura": 0.2,
            "alergias": [], "restricoes": ["hipertensao"],
            "beneficios": ["Nitrato", "Energia"]
        }
    },
    "Frutas": {
        "Banana": {
            "calorias": 89, "proteina": 1.1, "carboidrato": 23, "gordura": 0.3,
            "alergias": [], "restricoes": [],
            "beneficios": ["Potássio", "Energia"]
        },
        "Maçã": {
            "calorias": 52, "proteina": 0.3, "carboidrato": 14, "gordura": 0.2,
            "alergias": [], "restricoes": [],
            "beneficios": ["Fibra", "Antioxidantes"]
        },
        "Laranja": {
            "calorias": 47, "proteina": 0.9, "carboidrato": 12, "gordura": 0.1,
            "alergias": ["citrinos"], "restricoes": [],
            "beneficios": ["Vitamina C", "Imunidade"]
        },
        "Morango": {
            "calorias": 32, "proteina": 0.8, "carboidrato": 8, "gordura": 0.3,
            "alergias": [], "restricoes": [],
            "beneficios": ["Vitamina C", "Antioxidantes"]
        },
        "Blueberry": {
            "calorias": 57, "proteina": 0.7, "carboidrato": 14, "gordura": 0.3,
            "alergias": [], "restricoes": [],
            "beneficios": ["Antioxidantes", "Memória"]
        },
        "Abacate": {
            "calorias": 160, "proteina": 2, "carboidrato": 9, "gordura": 15,
            "alergias": ["latex"], "restricoes": [],
            "beneficios": ["Gordura saudável", "Potássio"]
        },
        "Melancia": {
            "calorias": 30, "proteina": 0.6, "carboidrato": 7.6, "gordura": 0.2,
            "alergias": [], "restricoes": [],
            "beneficios": ["Hidratação", "Licopeno"]
        },
        "Pêra": {
            "calorias": 57, "proteina": 0.4, "carboidrato": 15, "gordura": 0.1,
            "alergias": [], "restricoes": [],
            "beneficios": ["Fibra", "Digestão"]
        }
    },
    "Gorduras Saudáveis": {
        "Azeite de oliva": {
            "calorias": 884, "proteina": 0, "carboidrato": 0, "gordura": 100,
            "alergias": [], "restricoes": [],
            "beneficios": ["Gordura mono", "Coração"]
        },
        "Amendoim": {
            "calorias": 567, "proteina": 26, "carboidrato": 16, "gordura": 49,
            "alergias": ["amendoim"], "restricoes": [],
            "beneficios": ["Proteína", "Gordura saudável"]
        },
        "Castanha": {
            "calorias": 687, "proteina": 14, "carboidrato": 27, "gordura": 68,
            "alergias": ["nozes"], "restricoes": [],
            "beneficios": ["Selênio", "Antioxidantes"]
        },
        "Sementes de girassol": {
            "calorias": 584, "proteina": 20, "carboidrato": 20, "gordura": 51,
            "alergias": [], "restricoes": [],
            "beneficios": ["Vitamina E", "Selênio"]
        },
        "Abóbora com sementes": {
            "calorias": 151, "proteina": 5.2, "carboidrato": 5.5, "gordura": 13,
            "alergias": [], "restricoes": [],
            "beneficios": ["Magnésio", "Zinco"]
        }
    }
}

# Condições de saúde
CONDICOES_SAUDE = {
    "diabetes": {
        "nome": "Diabetes",
        "alimentos_evitar": ["mel", "bebidas_açucaradas"],
        "recomendacoes": "Preferir alimentos com baixo índice glicêmico"
    },
    "hipertensao": {
        "nome": "Hipertensão",
        "alimentos_evitar": ["sal_em_excesso"],
        "recomendacoes": "Reduzir sódio, aumentar potássio e magnesio"
    },
    "colesterol": {
        "nome": "Colesterol Alto",
        "alimentos_evitar": ["saturadas"],
        "recomendacoes": "Preferir gorduras insaturadas e aumentar fibra"
    },
    "gastrite": {
        "nome": "Gastrite",
        "alimentos_evitar": ["pimenta", "café", "álcool"],
        "recomendacoes": "Alimentos suaves e fácil digestão"
    },
    "intolerancia_lactose": {
        "nome": "Intolerância à Lactose",
        "alimentos_evitar": ["leite", "queijo"],
        "recomendacoes": "Usar alternativas sem lactose"
    }
}

# Funções auxiliares
def calcular_imc(peso, altura):
    """Calcula o IMC"""
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)
    
    if imc < 18.5:
        categoria = "Abaixo do peso"
        cor = "#3498db"
    elif imc < 25:
        categoria = "Peso normal"
        cor = "#2ecc71"
    elif imc < 30:
        categoria = "Sobrepeso"
        cor = "#f39c12"
    else:
        categoria = "Obeso"
        cor = "#e74c3c"
    
    return imc, categoria, cor

def filtrar_alimentos(alergias, restricoes_saude):
    """Filtra alimentos baseado em alergias e restrições de saúde"""
    alimentos_recomendados = {}
    alimentos_evitar = []
    
    for categoria, alimentos in ALIMENTOS_DATABASE.items():
        alimentos_recomendados[categoria] = {}
        
        for alimento, info in alimentos.items():
            # Verificar alergias
            tem_alergia = any(alergia in info["alergias"] for alergia in alergias)
            
            # Verificar restrições de saúde
            tem_restricao = any(restricao in info["restricoes"] for restricao in restricoes_saude)
            
            if not tem_alergia and not tem_restricao:
                alimentos_recomendados[categoria][alimento] = info
            else:
                alimentos_evitar.append(alimento)
    
    return alimentos_recomendados, alimentos_evitar

def gerar_plano_diario(alimentos_disponiveis, peso):
    """Gera um plano de refeições diário"""
    plano = {
        "Café da Manhã": [],
        "Almoço": [],
        "Lanche": [],
        "Jantar": []
    }
    
    # Lógica simples de recomendação
    if "Proteínas" in alimentos_disponiveis and alimentos_disponiveis["Proteínas"]:
        proteina = list(alimentos_disponiveis["Proteínas"].items())[0]
        plano["Almoço"].append(proteina)
    
    if "Carboidratos" in alimentos_disponiveis and alimentos_disponiveis["Carboidratos"]:
        carbo = list(alimentos_disponiveis["Carboidratos"].items())[0]
        plano["Almoço"].append(carbo)
    
    if "Vegetais" in alimentos_disponiveis and alimentos_disponiveis["Vegetais"]:
        veg = list(alimentos_disponiveis["Vegetais"].items())[0]
        plano["Almoço"].append(veg)
    
    if "Frutas" in alimentos_disponiveis and alimentos_disponiveis["Frutas"]:
        fruta = list(alimentos_disponiveis["Frutas"].items())[0]
        plano["Café da Manhã"].append(fruta)
    
    if "Proteínas" in alimentos_disponiveis and len(alimentos_disponiveis["Proteínas"]) > 1:
        proteina2 = list(alimentos_disponiveis["Proteínas"].items())[1]
        plano["Jantar"].append(proteina2)
    
    return plano

# Interface principal
def main():
    st.markdown("""
        <div class="header">
            <h1>🥗 FITMIND</h1>
            <p>Descubra alimentos saudáveis adaptados ao seu perfil e restrições</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Sidebar para entrada de dados
    with st.sidebar:
        st.header("👤 Seu Perfil")
        
        # Dados biométricos
        col1, col2 = st.columns(2)
        with col1:
            peso = st.number_input("Peso (kg)", min_value=30, max_value=200, value=70)
        with col2:
            altura = st.number_input("Altura (cm)", min_value=100, max_value=250, value=170)
        
        idade = st.number_input("Idade (anos)", min_value=1, max_value=120, value=30)
        
        genero = st.radio("Gênero", ["Masculino", "Feminino"])
        
        # Alergias
        st.subheader("🚫 Alergias")
        alergias = []
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.checkbox("Leite/Lactose"):
                alergias.append("lactose")
                alergias.append("leite")
        with col2:
            if st.checkbox("Ovos"):
                alergias.append("ovos")
        with col3:
            if st.checkbox("Glúten"):
                alergias.append("glúten")
                alergias.append("trigo")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.checkbox("Amendoim"):
                alergias.append("amendoim")
        with col2:
            if st.checkbox("Nozes/Castanhas"):
                alergias.append("nozes")
        with col3:
            if st.checkbox("Peixe/Frutos do Mar"):
                alergias.append("peixe")
                alergias.append("frutos_do_mar")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.checkbox("Aves"):
                alergias.append("aves")
        with col2:
            if st.checkbox("Carne Vermelha"):
                alergias.append("carne_vermelha")
        
        if st.checkbox("Citrinos"):
            alergias.append("citrinos")
        
        if st.checkbox("Soja"):
            alergias.append("soja")
        
        if st.checkbox("Latex"):
            alergias.append("latex")
        
        # Condições de saúde
        st.subheader("⚕️ Condições de Saúde")
        restricoes_saude = []
        
        col1, col2 = st.columns(2)
        with col1:
            if st.checkbox("Diabetes"):
                restricoes_saude.append("diabetes")
        with col2:
            if st.checkbox("Hipertensão"):
                restricoes_saude.append("hipertensao")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.checkbox("Colesterol Alto"):
                restricoes_saude.append("colesterol")
        with col2:
            if st.checkbox("Gastrite"):
                restricoes_saude.append("gastrite")
        
        if st.checkbox("Intolerância à Lactose"):
            restricoes_saude.append("intolerancia_lactose")
    
    # Conteúdo principal
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Perfil", "🍎 Recomendações", "📋 Plano Diário", "📚 Informações"])
    
    # Aba 1: Perfil
    with tab1:
        col1, col2, col3 = st.columns(3)
        
        imc, categoria_imc, cor = calcular_imc(peso, altura)
        
        with col1:
            st.metric("IMC", f"{imc:.1f}", categoria_imc)
        with col2:
            st.metric("Peso", f"{peso} kg")
        with col3:
            st.metric("Altura", f"{altura} cm")
        
        st.divider()
        
        # Resumo de restrições
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🚫 Alergias Identificadas")
            if alergias:
                for alergia in set(alergias):
                    st.write(f"• {alergia.upper()}")
            else:
                st.info("Nenhuma alergia registrada")
        
        with col2:
            st.subheader("⚕️ Restrições de Saúde")
            if restricoes_saude:
                for restricao in restricoes_saude:
                    st.write(f"• {CONDICOES_SAUDE[restricao]['nome']}")
            else:
                st.info("Sem restrições de saúde registradas")
    
    # Aba 2: Recomendações
    with tab2:
        alimentos_recomendados, alimentos_evitar = filtrar_alimentos(alergias, restricoes_saude)
        
        st.subheader("✅ Alimentos Recomendados")
        
        for categoria, alimentos in alimentos_recomendados.items():
            if alimentos:
                with st.expander(f"{categoria} ({len(alimentos)} opções)"):
                    cols = st.columns(2)
                    for idx, (alimento, info) in enumerate(alimentos.items()):
                        col = cols[idx % 2]
                        with col:
                            st.write(f"**{alimento}**")
                            col1, col2, col3, col4 = st.columns(4)
                            col1.metric("Cal", f"{info['calorias']:.0f}", "kcal")
                            col2.metric("Prot", f"{info['proteina']:.1f}", "g")
                            col3.metric("Carb", f"{info['carboidrato']:.1f}", "g")
                            col4.metric("Gord", f"{info['gordura']:.1f}", "g")
                            
                            if info["beneficios"]:
                                st.caption("💡 " + ", ".join(info["beneficios"]))
        
        if alimentos_evitar:
            st.divider()
            st.subheader("❌ Alimentos a Evitar")
            with st.expander(f"Ver {len(alimentos_evitar)} alimentos a evitar"):
                for alimento in alimentos_evitar:
                    st.write(f"• {alimento}")
    
    # Aba 3: Plano Diário
    with tab3:
        plano = gerar_plano_diario(alimentos_recomendados, peso)
        
        st.subheader("Seu Plano de Refeições")
        
        for refeicao, alimentos in plano.items():
            st.write(f"### {refeicao}")
            if alimentos:
                for nome, info in alimentos:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"**{nome}**")
                        st.caption(f"Calorias: {info['calorias']:.0f} | Proteína: {info['proteina']:.1f}g | Carbs: {info['carboidrato']:.1f}g | Gordura: {info['gordura']:.1f}g")
                    with col2:
                        st.write(f"100g")
            else:
                st.info("Nenhum alimento disponível para esta refeição")
            st.divider()
    
    # Aba 4: Informações
    with tab4:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📖 Como Funciona")
            st.write("""
            Este sistema analisa seu perfil para fornecer recomendações personalizadas:
            
            1. **Coleta de dados**: Peso, altura, idade e gênero
            2. **Alergias**: Alimentos que você não pode consumir
            3. **Condições de saúde**: Restrições médicas específicas
            4. **Recomendações**: Alimentos adequados ao seu perfil
            5. **Plano diário**: Sugestões de refeições balanceadas
            """)
        
        with col2:
            st.subheader("⚠️ Aviso Importante")
            st.warning("""
            Este sistema é uma ferramenta educacional e **NÃO substitui** 
            aconselhamento profissional de um nutricionista ou médico.
            
            Para um plano personalizado de qualidade, consulte um especialista.
            """)
        
        st.divider()
        st.subheader("🔬 Dados Nutricionais")
        st.info("Todos os valores são baseados em porções de 100g e retirados de bases de dados nutricionais públicas.")

if __name__ == "__main__":
    main()
