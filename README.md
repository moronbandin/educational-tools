# Gerador de Conteúdo Educacional com OpenAI

## Descrição
Esta aplicação Streamlit permite aos usuários gerar conteúdo educacional interativo utilizando modelos da OpenAI. Projetada para ser intuitiva e fácil de usar, oferece uma variedade de ferramentas educacionais, incluindo debates, jogos e perguntas de verdadeiro ou falso, adaptadas para diferentes níveis educacionais.

## Características
- **Seleção de Matérias e Cursos**: Opções para selecionar entre uma variedade de matérias e níveis educativos.
- **Geração de Conteúdo Personalizado**: Utiliza a API da OpenAI para gerar debates, jogos e perguntas de verdadeiro ou falso.
- **Interface Amigável**: Uma interface de usuário clara e simples, com uma barra lateral para configurações e uma vista principal para resultados.
- **Funcionalidade de Copiar para a Área de Transferência**: Permite que os usuários copiem facilmente o conteúdo gerado.

## Instalação
Para executar esta aplicação no seu ambiente local, siga estes passos:

1. Clone este repositório:
   ```
   git clone https://github.com/moronbandin/educational-tools
   ```
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```
   streamlit run app.py
   ```

## Uso
1. Insira sua chave API da OpenAI na barra lateral.
2. Selecione o modelo da OpenAI que deseja utilizar.
3. Escolha a matéria, o nível educativo e o tema específico.
4. Escolha a ferramenta (Debate, Verdadeiro ou Falso, Jogo).
5. Clique em "Gerar" para obter o conteúdo.
6. Utilize o botão "Copiar para a Área de Transferência" se precisar copiar o resultado.

## Contribuições
Contribuições são bem-vindas. Se desejar contribuir, por favor faça um fork do repositório e use uma branch de feature para propor mudanças.

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).
