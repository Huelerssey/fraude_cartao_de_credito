import streamlit as st
from streamlit_extras.colored_header import colored_header


# constroi a pagina 4
def apresentacao():
    st.markdown("<h1 style='text-align: center;'>🎉 Seja Bem-Vindo à Apresentação do Projeto! 🎉</h1>", unsafe_allow_html=True)

    # header azul
    colored_header(
    label="",
    description="",
    color_name="light-blue-70"
    )
    
    # cria 3 colunas
    col1, col2, col3 = st.columns(3)

    # Criar um botão
    if col2.button('💻Vídeo da Apresentação💻'):
        # video incorporado do youtube
        st.markdown('<iframe width="700" height="500" src="https://www.youtube.com/embed/enphZoeAkjw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>', unsafe_allow_html=True)

    st.subheader("📝 - Introdução")
    st.write("Através desta apresentação, espero demonstrar minhas habilidades relevantes para a área como estatística, machine learning, visualização de dados e, claro, a comunicação eficaz dos resultados. Acredito que a combinação de tecnologia e pensamento crítico pode levar a soluções inovadoras, e estou aqui para provar que também posso ser #Fera 🚀")
    st.write("")

    st.subheader("📖 - Conhecendo a Problemática")
    st.write("As fraudes em cartões de crédito são um problema crescente que afeta bancos, comerciantes e consumidores. A detecção rápida e precisa de transações fraudulentas é crucial para minimizar perdas financeiras e manter a confiança do cliente. Esta solução propõe um sistema integrado que utiliza tecnologias modernas de processamento de dados e aprendizado de máquina para detectar fraudes em tempo real. Vou ilustrar o processo a baixo através de um fluxograma:")
    st.image("imagens/infografico.png")
    st.write("Agora que já conhecemos o processo, podemos explicar separadamente cada etapa desta pepline.")
    st.write("")

    st.subheader("1️⃣ - Coleta de Dados de Transações em Tempo Real (Lambda e Kinesis Stream)")
    st.write("Os dados de transações são coletados em tempo real através do Lambda, que captura detalhes essenciais de cada transação. Esses dados são então transmitidos pelo Kinesis Stream, um serviço de streaming em tempo real que permite o processamento contínuo de grandes volumes de dados.")
    st.write("")

    st.subheader("2️⃣ - Pré-processamento e Limpeza de Dados (Firehose)")
    st.write("Como os dados brutos podem conter erros, valores ausentes e inconsistências. Utilizando o Firehose, os dados são pré-processados e limpos, garantindo que estejam no formato correto e prontos para análise. Essa etapa é vital para a qualidade e precisão dos modelos subsequentes.")
    st.write("")

    st.subheader("3️⃣ - Armazenamento de Dados (S3 Bucket e Redis Cluster)")
    st.write("Os dados limpos são armazenados no S3 Bucket para análise histórica e treinamento de modelos de aprendizado de máquina. O Redis Cluster é usado para análise em tempo real, fornecendo acesso rápido a novos dados de entrada onde o modelo já treinado com dados históricos irá prever se essa nova compra é ou não fraudulenta. Combinando essas tecnologias, a solução pode automatizar modelos robustos capazes de detectar padrões de fraude.")
    st.write("")

    st.subheader("4️⃣ - Desenvolver Modelos de Machine Learning")
    st.write("Os modelos de aprendizado de máquina avaliam cada transação em tempo real, classificando-as como fraude ou não fraude. Se uma fraude é detectada, ações imediatas são tomadas, como bloquear a transação ou alertar o cliente. A detecção rápida reduz perdas financeiras e protege a reputação do banco. Além disso, os dados de feedback, como confirmações de fraude ou contatos com o call center, são usados para ajustar continuamente o modelo, tornando-o cada vez mais preciso.")
    st.write("")

    st.subheader("5️⃣ - Avaliação em Tempo Real e Geração de Relatórios")
    st.write("Com base nos resultados gerados pela avaliação em tempo real, são produzidos relatórios de análise profunda que se tornam ferramentas indispensáveis na tomada de decisões estratégicas. Esses relatórios fornecem insights valiosos que podem ser transformados em ações direcionadas.")
    st.write("")

    st.write("---")
    st.subheader("🌟 - Entregando Soluções (o que você esperava ler)")
    st.write("**✅ - Problema Principal: Modelagem em Tempo Real e Personalização**")
    st.write("Esta abordagem inovadora para a detecção de fraudes em cartões de crédito não se limita a uma única solução. Reconhecemos a diversidade e complexidade do comportamento do consumidor e, portanto, implementamos uma estratégia multi-modelo. Utilizando técnicas de clusterização, segmentamos os clientes de acordo com o nível de consumo e adaptamos os modelos de classificação para cada grupo.")
    st.write("➡️ **Clientes de Baixo Consumo:** Para transações menores, um modelo flexível é implementado, permitindo bloqueios e liberações rápidas através do aplicativo.")
    st.write("➡️ **Clientes de Alto Consumo:** Compras de valores mais elevados exigem uma abordagem mais conservadora. Neste caso, um modelo rigoroso é utilizado para prevenir perdas substanciais por fraudes.")

    st.write("---")
    st.write("**✅ - Grandes Oportunidades: Insights para Marketing e Incentivo à Segurança**")
    st.write("A nossa solução vai além da detecção de fraudes, transformando dados e insights em oportunidades de negócios. Através da análise de clusters e do comportamento de segurança dos clientes, geramos informações valiosas para a equipe de marketing. Esses insights são a base para campanhas direcionadas que incentivam boas práticas de segurança.")
    st.write("➡️ **Recompensas e Incentivos:** Oferecemos recompensas como descontos ou cashback em parceria com empresas, incentivando os clientes a manter suas contas seguras.")
    st.write("➡️ **Engajamento e Educação:** Campanhas educativas fortalecem a consciência sobre segurança, criando uma cultura de responsabilidade e confiança.")

    st.write("---")
    st.write("**✅ - Quem Será o Usuário/Beneficiado Desta Aplicação**")
    st.write("A nossa solução é projetada para servir várias partes interessadas, tanto dentro quanto fora da empresa:")
    st.write("➡️ **Product Manager:** Utiliza a solução para orientar o desenvolvimento do produto, garantindo que ele atenda às necessidades do mercado.")
    st.write("➡️ **Equipe de Marketing:** Aproveita os insights gerados para criar campanhas eficazes e direcionadas.")
    st.write("➡️ **Setor de Contact Center:** Fornece suporte essencial para resolver problemas relacionados a fraudes e outros desafios.")
    st.write("➡️ **Clientes:** No centro de tudo, os clientes beneficiam-se de uma experiência segura e personalizada, reforçada por incentivos e recompensas.")

    st.write("---")
    st.subheader("📜 - Conclusão")
    st.write("Ao apresentar esta solução, espero ter demonstrado minha proficiência nas habilidades exigidas, incluindo estatística, machine learning, visualização de dados e comunicação eficaz de resultados. Estou confiante de que esta proposta representa não apenas uma resposta robusta ao case técnico, mas também uma visão inovadora de como a ciência de dados pode ser aplicada para criar valor real e sustentável.")

    # header azul
    colored_header(
    label="",
    description="",
    color_name="light-blue-70"
    )

    # cria 3 colunas
    col1, col2, col3 = st.columns(3)

    with col2:    
        #footer
        st.write("Developed By: [@Huelerssey](https://huelerssey-portfolio.website)")
        st.markdown("<h6 style='text-align: center;'>#QueroSerFera</h6>", unsafe_allow_html=True)
