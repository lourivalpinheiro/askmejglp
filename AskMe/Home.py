# BIBLIOTECAS


# FUNÇÃO PRINCIPAL

def boasvindas():
    n = str(input('Qual é o seu nome?'))
    print('É um prazer lhe conhecer, {}!'.format(n))
    print('''
        1. Conhecimento;
        2. Saúde;
        3. Financeiro;
        4. Dicas úteis.
''')
    escolha = int(input('Escolha uma das opções acima: '))
    if escolha == 1:
        print(conhecimento())
    elif escolha == 2:
        print()


# OPÇÕES


def conhecimento():
    print('''\n
          1. Primeiros socorros;
          2. Livros para desenvolvimento infantil na perspectiva científica e cristã;
          3. Livros sobre criação Bílingue;
          4. Criação sem telas;
          5. Gentle Parenting.
    ''')
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        print('O curso de primeiros socorros é extremamente importante.')
    elif escolha == 2:
        print('''
            PERSPECTIVA CIENTÍFICA
              
            1. O Cérebro da Criança: Desvendando os Mistérios do Desenvolvimento Infantil por Bruce Perry e Lia Schuman

            Este livro explora as últimas descobertas da neurociência sobre como o cérebro da criança se desenvolve e como isso molda seu aprendizado, comportamento e emoções. Os autores fornecem insights práticos para pais, educadores e outros cuidadores sobre como criar ambientes que promovam o desenvolvimento cerebral saudável.
            
            2. A Criança e Seu Mundo por  Winnicott D.W.
            
             Este clássico da psicologia infantil oferece uma visão abrangente do desenvolvimento emocional e social das crianças. Winnicott explora a importância dos relacionamentos primários, do brincar e do espaço transicional no desenvolvimento da personalidade saudável.
            
            3. Desenvolvimento Humano por  Papalia, Diane E.; Feldman, Ruth S.
            
            Este abrangente livro-texto fornece uma introdução completa ao desenvolvimento humano, desde a concepção até a velhice. Os autores cobrem todos os aspectos do desenvolvimento, incluindo físico, cognitivo, social e emocional.
            
            PERSPECTIVA CRISTÃ

            1. Pais e Filhos: Construindo Um Relacionamento de Amor e Fé por  Josh McDowell.
            
             Este livro oferece orientação bíblica para pais sobre como criar filhos em um mundo secular. McDowell aborda tópicos como disciplina, comunicação e educação sexual, de uma perspectiva cristã.
              
            2. Educar com Amor: Princípios Bíblicos para a Educação dos Filhos por  Evelyn Whitaker.
              
            Este livro oferece um guia prático para pais cristãos sobre como educar seus filhos de acordo com os princípios bíblicos. Whitaker fornece conselhos sobre como criar um ambiente familiar amoroso e disciplinado, e como ensinar seus filhos sobre fé e valores.
            
            3. Crescendo em Graça: Uma Jornada de Fé para Pais e Filhos por  Gary Chapman e  Carol Streck.
              
             Este livro explora como os pais podem usar os cinco princípios da linguagem do amor para criar relacionamentos fortes com seus filhos e ajudá-los a desenvolver uma fé autêntica.
              
            Observação: Esta lista é apenas um ponto de partida. Existem muitos outros livros excelentes sobre desenvolvimento infantil disponíveis na perspectiva científica e cristã. É importante escolher livros que sejam relevantes para seus próprios valores e necessidades.


            ''')
    elif escolha == 3:
        print('''
              1. Criando Filhos Bilíngues: Um Olhar Sobre Bilinguismo, Mitos, Práticas e Relatos Reais por Aline Silva e Juliana Cunha de Melo;

               Este livro é um guia completo para pais que desejam criar filhos bilíngues. As autoras abordam os mitos comuns sobre o bilinguismo, oferecem dicas práticas para criar um ambiente bilíngue em casa e compartilham histórias de famílias bilíngues reais.
              
              2. O Caminho para Criação Bilíngue por Aline Jaeger.
              
              Este e-book oferece um plano passo a passo para criar filhos bilíngues. A autora fornece conselhos sobre como escolher o método de bilinguismo certo para sua família, como criar oportunidades para seus filhos praticarem o segundo idioma e como lidar com os desafios da criação bilíngue.
              
              3. Meu Bebê Bilíngue: 10 Dicas Para Criar Filhos Apaixonados por Leitura por  Isabella Fernandes.
              
              Este livro oferece 10 dicas para criar filhos bilíngues que amam ler. A autora fornece sugestões para escolher livros bilíngues adequados à idade, criar um ambiente de leitura acolhedor e tornar a leitura uma experiência divertida para seus filhos.
              
              4. Desmistificando o Bilinguismo: Um Guia para Criar Filhos Bilíngues por Louise Machado.
              
              Este livro desmistifica os mitos comuns sobre o bilinguismo e oferece um guia prático para pais que desejam criar filhos bilíngues. A autora fornece informações sobre os benefícios do bilinguismo, como escolher o método de bilinguismo certo para sua família e como lidar com os desafios da criação bilíngue.
              
              5. Bilinguismo Infantil: Guia Básico para Promoção do Bilinguismo Precoce por Aline Montiel.
              
              Este livro oferece um guia básico para pais que desejam criar filhos bilíngues desde cedo. A autora fornece informações sobre os benefícios do bilinguismo precoce, como escolher o método de bilinguismo certo para sua família e como criar oportunidades para seus filhos praticarem o segundo idioma.
              
              Observação: Esta lista é apenas um ponto de partida. Existem muitos outros livros excelentes sobre criação bilíngue disponíveis. É importante escolher livros que sejam relevantes para seus próprios valores e necessidades.''')
    elif escolha == 4:
        print('''
A era digital apresenta desafios e oportunidades para os pais de hoje. A ubiquidade das telas pode ser um recurso valioso para educação e entretenimento, mas também pode ter um impacto negativo no desenvolvimento infantil.

Por que Limitar o Tempo de Tela?

Desenvolvimento Cerebral: O uso excessivo de telas pode prejudicar o desenvolvimento de habilidades cognitivas importantes, como linguagem, memória e atenção.
Saúde Física: O tempo excessivo em frente às telas pode levar à obesidade, problemas de sono e problemas de visão.
Saúde Mental: O uso de telas pode aumentar o risco de ansiedade, depressão e problemas de interação social.
Habilidades Sociais: As crianças aprendem a interagir com outras pessoas através da brincadeira e da conversa cara a cara. O tempo excessivo de tela pode limitar essas oportunidades.
Dicas para Criar Filhos Sem Telas:

Defina Limites Claros: Determine quanto tempo de tela seus filhos são permitidos por dia e cumpra essas regras.
Seja um Bom Exemplo: Limite seu próprio tempo de tela e mostre aos seus filhos que existem outras atividades divertidas que podem fazer.
Ofereça Alternativas: Incentive seus filhos a se envolverem em atividades físicas, brincadeiras criativas e leitura.
Crie um Espaço Livre de Telas: Designe um espaço em sua casa onde as telas não sejam permitidas, como o quarto ou a mesa de jantar.
Use a Tecnologia de Forma Positiva: Existem aplicativos e programas educativos que podem ser usados ​​para complementar o aprendizado e a brincadeira.
Seja Flexível: Haverá momentos em que seus filhos precisarão usar telas, como para fazer videochamadas com familiares ou amigos. Seja flexível, mas mantenha seus limites gerais.
Converse com Seus Filhos: Explique aos seus filhos por que você está limitando o tempo de tela e os incentive a compartilhar seus pensamentos e sentimentos sobre isso.
Lembre-se:

Cada criança é diferente e o que funciona para uma criança pode não funcionar para outra.
É importante encontrar um equilíbrio entre o uso de telas e outras atividades.
O objetivo é criar um ambiente onde seus filhos possam se desenvolver de forma saudável e feliz.''')
    elif escolha == 5:
        print('''Imagine que você está brincando com seus bloquinhos e, de repente, sem querer, derruba a torre que você estava construindo com tanto cuidado. Fica triste, né? É normal se sentir assim! A gente também fica triste quando as coisas não saem como a gente quer.

Gentle Parenting ou **parentalidade gentil**, também chamada de **parentalidade positiva**, entende que as crianças também têm sentimentos e que, às vezes, erram porque ainda estão aprendendo. Em vez de brigar ou punir, essa maneira de educar busca ensinar as crianças de um jeito mais legal, com amor e respeito. 

É como se fosse um jogo de cooperação, onde pais e filhos trabalham juntos para resolver problemas e aprender coisas novas. Na parentalidade gentil, a gente conversa bastante com as crianças, explica as coisas com calma e tenta entender o que elas estão pensando e sentindo. 

Em vez de dizer "não" o tempo todo, a gente tenta encontrar soluções criativas que funcionem para todos. Por exemplo, se a criança não quer escovar os dentes, a gente pode cantar uma música divertida enquanto escova os dentes dela também, ou inventar uma história sobre um bichinho que adora escovar os dentes.

A parentalidade gentil também ensina as crianças a serem responsáveis e a fazerem suas próprias escolhas. A gente dá opções para as crianças, dentro do que é seguro e bom para elas, e deixa que elas escolham o que querem fazer. Assim, as crianças se sentem mais confiantes e aprendem a tomar decisões por conta própria.

Essa maneira de educar pode ser um desafio no começo, mas com um pouco de prática e paciência, você e seus filhos vão se adaptar e colher muitos benefícios. As crianças que são criadas com gentileza tendem a ser mais felizes, mais confiantes e mais bem-comportadas. 

Lembre-se: a parentalidade gentil é um caminho, não um destino. O importante é ter amor, respeito e paciência com seus filhos, e sempre buscar o melhor para eles.

Aqui estão algumas dicas para você começar a praticar a parentalidade gentil em casa:

1. **Converse bastante com seus filhos.** Pergunte sobre o dia deles, como eles estão se sentindo e o que eles estão pensando.
2. **Escute com atenção o que seus filhos têm a dizer.** Mostre que você está realmente interessado no que eles estão falando.
3. **Seja paciente.** As crianças aprendem em ritmos diferentes. Não desista se seu filho não entender algo na primeira vez.
4. **Celebre as conquistas dos seus filhos.** Reconheça o esforço deles e diga o quanto você está orgulhoso deles.
5. **Seja um bom exemplo para seus filhos.** Mostre como você lida com suas próprias emoções e com os desafios da vida.

Com essas dicas, você estará no caminho certo para criar filhos felizes, confiantes e bem-sucedidos!''')

# CÓDIGO

import streamlit as st

st.set_page_config("ASK ME", page_icon='askme.ico', layout='wide')
ico = "askme.ico"
st.image('askme.png')
menu = st.sidebar.selectbox("MENU", options=["CONHECIMENTO"], index=0)
st.header("BEM-VINDOS AO ASK ME!")
st.divider()
st.write(
    '''
Pesquise sobre temas extramamente relevantes ao período de gravidez e que exigem atenção dos pais.
'''
)