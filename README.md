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

O projeto tem como objetivo desenvolver um sistema embarcado para monitoramento inteligente de estoque utilizando o conceito Kanban, por meio da leitura contínua do peso de uma caixa de componentes.

A solução utiliza um ESP32 em conjunto com um sensor de peso HX711 para identificar automaticamente o estado do estoque. Com base na leitura do peso, o sistema classifica a situação em quatro estados: funcionamento normal, estoque crítico, caixa reabastecida e falha de leitura do sensor.

A interação com o usuário ocorre através do monitor serial, onde são exibidas mensagens informando o status do estoque, alertas de reposição e possíveis falhas de operação.

---

# Arquitetura do Sistema Embarcado

O firmware foi desenvolvido em MicroPython utilizando uma arquitetura simples, baseada em inicialização do hardware seguida por um laço principal de monitoramento contínuo.

## Fluxo principal

1. Inicialização do ESP32.
2. Configuração dos pinos GPIO do sensor HX711.
3. Tentativa de execução da tara do sensor.
4. Exibição da mensagem de inicialização.
5. Entrada em um loop infinito para monitoramento do peso.

Durante cada iteração do loop:

* é realizada uma leitura do sensor HX711;
* o valor recebido é validado;
* o peso é comparado com os limites definidos;
* o estado do estoque é atualizado;
* uma mensagem é enviada ao monitor serial quando ocorre mudança de estado.

Foi utilizado um pequeno atraso de 100 ms entre as leituras para reduzir o uso da CPU sem comprometer a resposta do sistema.

### Fluxo lógico

```text
Inicialização
      │
      ▼
Configuração do HX711
      │
      ▼
Leitura do Peso
      │
      ▼
┌──────── Peso = 0 ? ─────────┐
│            Sim              │
│      Alerta de erro         │
└────────────┬────────────────┘
             │Não
             ▼
 Peso ≤ 150 g ?
      │
 ┌────┴────┐
 │   Sim   │
 │Repor caixa
 └────┬────┘
      │Não
      ▼
 Peso ≥ 5000 g
 e reposição ativa?
      │
 ┌────┴────┐
 │   Sim   │
 │Abastecimento
 └────┬────┘
      │Não
      ▼
Estoque Regular
      │
      ▼
Nova leitura
```

---

# Componentes Utilizados na Simulação

O circuito desenvolvido no Wokwi é composto pelos seguintes componentes:

* **ESP32 DevKit C v4**

  * Microcontrolador responsável pela execução do firmware.

* **Sensor de peso HX711**

  * Responsável pela leitura da carga aplicada à célula de carga simulada.

* **Monitor Serial**

  * Utilizado para exibição das mensagens de status e validação automática pela esteira de testes.

### Conexões principais

| Componente | GPIO ESP32 |
| ---------- | ---------- |
| HX711 DT   | GPIO 5     |
| HX711 SCK  | GPIO 18    |
| HX711 VCC  | 3.3 V      |
| HX711 GND  | GND        |

---

# Decisões Técnicas Relevantes

Durante o desenvolvimento foram adotadas algumas decisões visando simplicidade, robustez e facilidade de manutenção.

* Organização do código em blocos bem definidos (configuração, inicialização, funções e loop principal).
* Utilização de constantes para todos os limites de peso, facilitando futuras alterações.
* Implementação da função `ler_peso()` para encapsular a leitura do HX711 e tratar possíveis exceções.
* Tratamento de valores negativos retornando zero, evitando leituras inválidas.
* Utilização de uma variável de controle (`reposicao_disparada`) para impedir múltiplos disparos consecutivos do evento de reposição.
* Uso da variável `ultima_mensagem` para evitar repetição contínua das mesmas mensagens no monitor serial.
* Adoção de um pequeno atraso (`time.sleep_ms(100)`) para reduzir o consumo de processamento mantendo o sistema responsivo.

---

# Resultados Obtidos

O sistema desenvolvido atende aos requisitos propostos para o desafio.

Na simulação foi possível observar corretamente:

* inicialização do sistema;
* monitoramento contínuo do peso;
* identificação do estado de estoque regular;
* detecção automática de estoque crítico;
* disparo único do evento de reposição;
* reconhecimento do reabastecimento da caixa;
* identificação de falha de leitura ou ausência da caixa quando o peso é igual a zero.

As mensagens enviadas ao monitor serial seguem exatamente o formato especificado pelo desafio, permitindo compatibilidade com a validação automática da esteira de integração contínua (Wokwi CI).

---

# Comentários Adicionais

O desenvolvimento deste projeto permitiu aplicar conceitos de sistemas embarcados utilizando MicroPython, sensores digitais e simulação em ambiente Wokwi.

Como melhoria futura, seria interessante implementar:

* indicadores visuais utilizando LEDs;
* sinalização sonora através de buzzer;
* envio dos dados para uma plataforma IoT via Wi-Fi (MQTT ou HTTP);
* registro histórico das medições;
* interface web para acompanhamento remoto do estoque.

O projeto demonstrou a importância da organização do firmware, do tratamento adequado de exceções e da implementação de lógica não bloqueante para garantir compatibilidade com testes automatizados.


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
