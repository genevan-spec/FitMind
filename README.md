# 🥗 FITMIND

Um aplicativo web inteligente para obter recomendações de alimentos personalizadas baseadas no seu perfil, alergias e condições de saúde.

## ✨ Funcionalidades

- **Perfil Personalizado**: Coleta dados biométricos (peso, altura, idade, gênero)
- **Gestão de Alergias**: Identifica e exclui alimentos com as quais você tem alergia
- **Condições de Saúde**: Adapta recomendações para:
  - Diabetes
  - Hipertensão
  - Colesterol Alto
  - Gastrite
  - Intolerância à Lactose
- **Base de Dados Ampla**: Mais de 40 alimentos com informações nutricionais completas
- **Plano Diário**: Sugestões de refeições balanceadas
- **Cálculo de IMC**: Avaliação do seu índice de massa corporal
- **Interface Intuitiva**: Dashboard responsivo com múltiplas abas

## 📋 Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

## 🚀 Como Instalar e Executar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Execute o aplicativo

```bash
streamlit run Dieta.py
```

O navegador abrirá automaticamente em `http://localhost:8501`

## 📖 Como Usar

### Passo 1: Inserir Dados Biométricos
- Digite seu peso (kg), altura (cm) e idade
- Selecione seu gênero (Masculino/Feminino)

### Passo 2: Indicar Alergias
Marque as caixas das alergias que você tem:
- Leite/Lactose
- Ovos
- Glúten
- Amendoim
- Nozes/Castanhas
- Peixe/Frutos do Mar
- Aves
- Carne Vermelha
- Citrinos
- Soja
- Látex

### Passo 3: Selecionar Condições de Saúde
Se aplicável, indique:
- Diabetes
- Hipertensão
- Colesterol Alto
- Gastrite
- Intolerância à Lactose

### Passo 4: Visualizar Recomendações
O sistema filtrará automaticamente:
- ✅ Alimentos recomendados
- ❌ Alimentos a evitar
- 📋 Plano de refeições diárias
- 📊 Informações nutricionais

## 🍎 Base de Dados de Alimentos

### Categorias

**Proteínas** (8 opções)
- Frango, peixe, carne, ovos, tofu, iogurte, feijão, lentilha

**Carboidratos** (8 opções)
- Arroz, batata, pão, aveia, macarrão, batata-doce, mel, pão sem glúten

**Vegetais** (8 opções)
- Brócolis, cenoura, espinafre, alface, tomate, abóbora, couve-flor, beterraba

**Frutas** (8 opções)
- Banana, maçã, laranja, morango, blueberry, abacate, melancia, pêra

**Gorduras Saudáveis** (5 opções)
- Azeite, amendoim, castanha, sementes, abóbora com sementes

## 📊 Cálculo de IMC

O sistema calcula automaticamente seu IMC:

| IMC | Categoria |
|-----|-----------|
| < 18.5 | Abaixo do peso |
| 18.5 - 24.9 | Peso normal |
| 25 - 29.9 | Sobrepeso |
| ≥ 30 | Obeso |

## 🔬 Informações Nutricionais

Todos os valores são por porção de **100g** e incluem:
- Calorias (kcal)
- Proteína (g)
- Carboidratos (g)
- Gordura (g)
- Alergias associadas
- Restrições de saúde
- Benefícios à saúde

## 📁 Estrutura do Projeto

```
Dieta/
├── Dieta.py                 # Aplicação Streamlit
├── requirements.txt         # Dependências
├── executar.bat            # Script para Windows
└── README.md               # Este arquivo
```

## ⚙️ Tecnologias Utilizadas

- **Streamlit**: Framework para criar aplicações web em Python
- **Pandas**: Manipulação de dados
- **Plotly**: Visualizações interativas
- **Python 3**: Linguagem de programação

## 💡 Exemplos de Uso

### Exemplo 1: Pessoa com Alergia a Glúten
Se marcar "Glúten":
- Será automaticamente excluído: Pão integral, aveia, macarrão
- Será recomendado: Pão sem glúten e alternativas

### Exemplo 2: Pessoa com Diabetes
Se selecionar "Diabetes":
- O mel será excluído das recomendações
- Serão priorizados alimentos com baixo índice glicêmico
- Recomendação especial para controle de glicose

### Exemplo 3: Pessoa Vegetariana
- Pode desativar aves e carne vermelha
- Sistema recomendará: tofu, feijão, lentilha, ovos, etc.

## ⚠️ Aviso Importante

**Este aplicativo é uma ferramenta educacional e NÃO substitui:**
- Consulta com nutricionista profissional
- Acompanhamento médico
- Diagnóstico ou tratamento médico

**Para um plano de dieta personalizado de qualidade profissional, sempre consulte:**
- Um nutricionista qualificado
- Seu médico de família
- Um especialista em saúde

## 🔄 Fluxo da Aplicação

```
1. Entrada de Dados
   ├─ Biometria (peso, altura, idade, sexo)
   ├─ Alergias
   └─ Condições de saúde

2. Processamento
   ├─ Cálculo de IMC
   ├─ Filtragem de alimentos
   └─ Geração de plano

3. Apresentação
   ├─ Perfil resumido
   ├─ Alimentos recomendados
   ├─ Alimentos a evitar
   ├─ Plano de refeições
   └─ Informações nutricionais
```

## 🎯 Objetivos Futuros

- [ ] Suporte a mais alergias
- [ ] Cálculo de calorias diárias personalizadas
- [ ] Gerador de planos semanais
- [ ] Integração com apps de fitness
- [ ] Histórico de refeições
- [ ] Sistema de avaliação de refeições
- [ ] Exportar plano em PDF

## 📞 Suporte

Para reportar problemas ou sugerir melhorias, você pode:
- Criar uma issue
- Entrar em contato via email
- Deixar feedback na aplicação

---

**Criado com ❤️ para sua saúde e bem-estar**

*Versão 2.0 - Sistema Streamlit de Recomendação Personalizada*
