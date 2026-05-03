@echo off
REM Instalar dependências
echo Instalando dependências do Python...
pip install -r requirements.txt

REM Executar o aplicativo
echo.
echo Iniciando o aplicativo Streamlit...
echo.
echo O aplicativo estará disponível em: http://localhost:8501
echo Pressione Ctrl+C para parar o servidor
echo.

streamlit run Dieta.py
pause
