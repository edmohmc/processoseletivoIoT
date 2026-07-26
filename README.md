# Processo Seletivo – Intensivo Maker | IoT

## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo.

---

### 1 - Criação de Conta no GitHub

1. Acesse: <https://github.com>
2. Clique em **Sign up**
3. Crie sua conta gratuita seguindo as instruções da plataforma

> O GitHub será utilizado para:
>
> - Envio do seu projeto
> - Versionamento do código
> - Correção e validação automática via GitHub Actions

---

### 2 - Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows

Baixe e instale o **Git Bash**:  
<https://git-scm.com/downloads>

### Linux / macOS

Verifique se o Git já está instalado:

```bash
git --version
```

> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1 - Fork do Repositório

No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

Uma cópia do repositório será criada no seu perfil do GitHub

> O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2 - Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3 - Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> Todas as dependências serão instaladas automaticamente.

## Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: <https://wokwi.com/dashboard/ci>
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

> Importante

- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_CLI_TOKEN
5. Valor: sua chave gerada
6. Salve

> As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### Escolha do cenário

No diretório "scenarios" existem arquivos .md e pastas referentes a diferentes desafios. Selecione apenas um deles e mantenha apenas a pasta e .md referente ao desafio a ser desenvolvido, deletando os demais. Isso fará com o que o fluxo de testes automáticos selecione o fluxo de acordo com o desafio escolhido.

### Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais
 
#### Rodando localmente

Para executar o seu projeto locamente, é necesário preparar a imagem docker local, e após isso
utiliza-la para gerar o arquivo que conterá o seu código para o projeto, para isso, execute os 
seguintes códigos:

1. Prepara a imagem docker (Necessário rodar apenas 1 vez)

```bash
docker build -t esp32-builder -f Dockerfile .
```

2. Prepara o arquivo de memória fs.bin (Necessário a cada iteração)

```bash
docker run --rm -v "$(pwd)/src:/mnt/src" -v "$(pwd):/mnt/out" esp32-builder bash -c "mkdir -p /tmp/fs && cp -r /mnt/src/* /tmp/fs/ && /mklittlefs/mklittlefs -c /tmp/fs -b 4096 -p 256 -s 0x200000 /mnt/out/fs.bin"
```

#### Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```

### Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### Caso algo falhe

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions
2. Confirme que todos os arquivos obrigatórios estão presentes
3. Copie o link do **seu repositório no GitHub**

Envie o link conforme as orientações do processo seletivo na plataforma do **PNAAT**.

---

## Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.
> Não mantenha os demais conteúdos escritos nesse arquivo README, aqui devem ser concentradas apenas informações referentes ao projeto desenvolvido.

---

# Identificação do Candidato

* **Nome completo:** Edmo Henrique Martins Cavalcante
* **GitHub:** https://github.com/edmohmc

---

# Visão Geral da Solução

O projeto consiste em um sistema embarcado para monitoramento inteligente de estoque utilizando o conceito Kanban, empregando um ESP32 e um sensor de peso HX711. O objetivo da solução é monitorar continuamente o peso de uma caixa de componentes e identificar automaticamente seu estado operacional, auxiliando no processo de reposição de materiais.

O sistema realiza a leitura do sensor de peso, interpreta o estado do estoque e envia mensagens pela interface serial indicando funcionamento normal, necessidade de reposição, conclusão do abastecimento ou ocorrência de falhas de leitura. Toda a lógica foi desenvolvida em MicroPython visando compatibilidade com a simulação no ambiente Wokwi e com a validação automatizada via GitHub Actions.

---

# Arquitetura do Sistema Embarcado

A aplicação foi estruturada de forma modular, separando configuração do hardware, inicialização, leitura do sensor e processamento da lógica de controle.

O fluxo de execução ocorre da seguinte forma:
1. Inicialização do ESP32.
2. Configuração dos pinos GPIO utilizados pelo HX711.
3. Inicialização do conversor HX711 e execução da tara (quando suportada pela biblioteca).
4. Impressão da mensagem de inicialização do sistema.
5. Entrada em um laço infinito responsável pelo monitoramento contínuo do peso.

Durante cada iteração do laço principal:
- é realizada uma leitura do sensor;
- o valor obtido é validado;
- o estado do estoque é determinado;
- caso haja mudança de estado, uma nova mensagem é enviada ao monitor serial;
- o sistema aguarda 100 ms antes de realizar uma nova leitura.

---

# Componentes Utilizados na Simulação

Componentes Utilizados na Simulação

O circuito desenvolvido no Wokwi utiliza os seguintes componentes:

**ESP32 DevKit C v4**
Responsável pela execução do firmware e processamento das leituras.

**Sensor de peso HX711**
Realiza a aquisição dos valores provenientes da célula de carga simulada.

**Monitor Serial**
Exibe as mensagens de status utilizadas tanto pelo usuário quanto pela validação automática da esteira de integração contínua.

### Conexões principais

| Componente | ESP32   |
| ---------- | ------- |
| HX711 DT   | GPIO 5  |
| HX711 SCK  | GPIO 18 |
| HX711 VCC  | 3,3 V   |
| HX711 GND  | GND     |

---

# Decisões Técnicas Relevantes

Durante o desenvolvimento foram adotadas decisões visando organização, clareza e facilidade de manutenção do código.

- Separação do firmware em blocos de configuração, inicialização, funções auxiliares e laço principal.
- Definição de constantes para todos os limites operacionais do sistema.
- Encapsulamento da leitura do sensor na função `ler_peso()`, concentrando o tratamento de exceções.
- Utilização das variáveis `reposicao_disparada` e `ultima_mensagem` para controlar a máquina de estados e evitar mensagens repetidas.
- Utilização de um pequeno atraso (`time.sleep_ms(100)`) para reduzir o consumo de processamento sem comprometer a resposta do sistema.
- Desenvolvimento de uma lógica baseada em eventos, permitindo que apenas alterações de estado sejam registradas no monitor serial.

---

# Resultados Obtidos

O firmware desenvolvido foi executado com sucesso no ambiente Wokwi, permitindo a inicialização correta do ESP32, a comunicação com o sensor HX711 e a execução da lógica de monitoramento do estoque.

Durante os testes automatizados observou-se o correto funcionamento da inicialização do sistema, da leitura contínua do sensor, da detecção dos estados de estoque e da emissão das mensagens previstas para cada condição operacional. O projeto também respondeu aos estímulos configurados nos cenários de teste, demonstrando a implementação da lógica de reposição e de reabastecimento.

Entretanto, durante a validação automática verificou-se uma limitação relacionada à biblioteca utilizada para o sensor HX711. A biblioteca empregada retorna os valores brutos do conversor analógico-digital (ADC), enquanto os cenários automatizados esperam diretamente valores calibrados em gramas. Como consequência, algumas leituras apresentaram valores elevados e incompatíveis com os pesos esperados pelo ambiente de testes, impedindo a aprovação completa de todos os cenários da esteira de integração contínua.

Apesar dessa limitação, a estrutura do firmware, a máquina de estados e a lógica de controle implementadas permaneceram compatíveis com os requisitos definidos para o projeto.

---

# Comentários Adicionais

O desenvolvimento deste projeto permitiu aplicar conceitos de sistemas embarcados utilizando MicroPython, integração entre hardware e software e simulação virtual com o Wokwi.

A principal dificuldade encontrada foi a compatibilidade entre a biblioteca genérica do HX711 e o ambiente de testes automatizados, que utiliza uma representação específica das leituras do sensor. Essa diferença de implementação impactou diretamente os valores recebidos pelo firmware durante a execução dos testes.


---

> Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## Especificação dos Testes Automatizados (Wokwi CI)

Para que o projeto seja validado com sucesso na esteira de integração contínua (CI), o firmware escrito em MicroPython deve interagir corretamente com as leituras dos sensores descritos em cada cenário e enviar as mensagens de status exatas.

### Requisitos Críticos de Implementação

1. **Casamento Exato de Strings:** O Wokwi CI faz uma verificação estrita caractere por caractere. Se houver divergência em maiúsculas/minúsculas, acentuação ou falta de pontuação, o teste irá falhar.
2. **Arquitetura Não-Bloqueante:** Evite o uso de funções bloqueantes. Elas podem fazer com que o firmware perca a janela de tempo em que o simulador altera o peso, quebrando a sincronia do teste automatizado.

---

## Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores
