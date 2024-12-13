# Script Video Dark Generator

Este script permite criar vídeos únicos combinando áudio e imagens retirados de vídeos do YouTube. O resultado é um vídeo final com cortes personalizados, ideal para criadores de conteúdo. Este guia detalhado orienta você passo a passo desde a clonagem do repositório até a execução do script.

---

## Pré-requisitos

Antes de começar, certifique-se de que o seu computador atende aos seguintes requisitos:

1. **Python** instalado (versão 3.8 ou superior).
   - [Baixe Python](https://www.python.org/downloads/).
   - Durante a instalação, marque a opção **Add Python to PATH**.

2. **Git** instalado para clonar o repositório.
   - [Baixe Git](https://git-scm.com/).

3. **Conexão com a Internet** para baixar dependências e arquivos do YouTube.

4. **FFmpeg** instalado para processar áudio e vídeo.
   - FFmpeg é uma ferramenta de código aberto essencial para o funcionamento deste script. **Não é um vírus.** Ela é amplamente usada para edição e manipulação de mídia.
   - **Recomendado:** Instale o FFmpeg usando o Conda, pois é a maneira mais fácil:
     ```bash
     conda install -c conda-forge ffmpeg
     ```
     - Para instalar o Conda, acesse o [Miniconda](https://docs.conda.io/en/latest/miniconda.html) e siga as instruções do site.
   - **Alternativa Manual:** [Baixe FFmpeg](https://www.gyan.dev/ffmpeg/builds/):
     1. Escolha a versão mais recente na seção "Release builds".
     2. Baixe o arquivo ZIP.
     3. Extraia o conteúdo para uma pasta, por exemplo: `C:\ffmpeg`.
     4. Adicione o caminho da pasta `bin` do FFmpeg ao PATH do sistema:
        - No Windows, pesquise por **Editar variáveis de ambiente do sistema**.
        - Edite a variável `Path` e adicione o caminho completo até a pasta `bin` (ex.: `C:\ffmpeg\bin`).

---

## Passo a Passo

### 1. Clone o repositório
Abra o terminal ou prompt de comando e execute o seguinte comando para clonar o repositório:
```bash
git clone https://github.com/lukeguima/script-video-dark-generator.git
```

### 2. Navegue até o diretório do projeto
Entre no diretório do projeto clonado:
```bash
cd script-video-dark-generator
```

### 3. Crie um ambiente virtual
Crie um ambiente virtual para instalar as dependências do projeto de forma isolada:
```bash
python -m venv venv
```

### 4. Ative o ambiente virtual
- **No Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **No Linux/MacOS:**
  ```bash
  source venv/bin/activate
  ```

### 5. Instale as dependências
Baixe e instale todas as bibliotecas necessárias listadas no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 6. Configure as variáveis de entrada
Abra o arquivo `video_generator.py` no editor de texto de sua preferência e configure as seguintes variáveis de entrada:

- **`link_audio_youtube`**: URL do vídeo no YouTube de onde será extraído o áudio.
- **`start_audio_clip` e `final_audio_clip`**: Ponto inicial e final do áudio que será cortado (em formato `[minutos:segundos]`).
- **`link_image_youtube`**: URL do vídeo no YouTube de onde será extraído o fundo (imagem em movimento).
- **`start_background_clip`**: Ponto inicial do fundo que será cortado (em formato `[minutos:segundos]`).
- **`video_name`**: Nome do arquivo de vídeo final (sem extensão).

#### Exemplo:
```python
link_audio_youtube = 'https://www.youtube.com/watch?v=AW36rKr2yxs'
start_audio_clip = '[0:40]'
final_audio_clip = '[1:49]'

link_image_youtube = 'https://www.youtube.com/watch?v=Tp6HQCb70yM'
start_background_clip = '[0:00]'

video_name = 'verdadeira_transformacao'
```

- **Descrição das variáveis:**
  - `link_audio_youtube`: URL do vídeo de onde será retirado o áudio.
  - `start_audio_clip`: Ponto inicial do áudio em minutos e segundos.
  - `final_audio_clip`: Ponto final do áudio em minutos e segundos.
  - `link_image_youtube`: URL do vídeo de onde será retirada a imagem de fundo.
  - `start_background_clip`: Ponto inicial do fundo em minutos e segundos.
  - `video_name`: Nome do vídeo gerado.

### 7. Execute o script
No terminal, execute o seguinte comando para rodar o script:
```bash
python video_generator.py
```

### 8. Verifique a saída
O vídeo final será salvo na pasta `output` com o nome definido na variável `video_name`.

---

## Resolução de Problemas

- **Erro: `ModuleNotFoundError`**
  Certifique-se de ter instalado todas as dependências usando:
  ```bash
  pip install -r requirements.txt
  ```

- **Erro ao rodar o script**
  Certifique-se de que o ambiente virtual está ativado antes de rodar o comando:
  ```bash
  python video_generator.py
  ```

- **Problemas com links do YouTube**
  Verifique se os links inseridos são válidos e acessíveis.

- **FFmpeg não encontrado:**
  Certifique-se de que o FFmpeg está instalado e configurado corretamente no PATH do sistema. Reinicie o terminal após a configuração.

---

## Estrutura do Projeto

```plaintext
script-video-dark-generator/
├── src/
│   ├── utils/
│   │   ├── clean_temp_files.py
│   │   ├── create_folder.py
│   ├── generator/
│       ├── cortes/
│           ├── create_audio_clip.py
│           ├── create_background_clip.py
│           ├── compile_video.py
│           ├── video_generator.py
├── temp/           # Pasta temporária para arquivos intermediários
├── output/         # Pasta onde o vídeo final será salvo
├── requirements.txt
├── main.py         # Script principal
```

---

## Versão Beta

Este script está em versão beta e receberá atualizações futuras, incluindo:

1. **Interface para o usuário:** Uma interface amigável para facilitar a utilização do script.
2. **Integração com WhatsApp e OneDrive:** Para envio e armazenamento automático do vídeo gerado.
3. **Opção 2 de cortes:** Uma funcionalidade voltada para criadores de conteúdo dark de podcasts.

---

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request no repositório.

---

## Contato
Acompanhe nosso conteúdo no TikTok: [@projetosdev](https://www.tiktok.com/@projetosdev)

---

## Licença
Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

