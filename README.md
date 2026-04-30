# Projeto de Reconhecimento e Scripts de Exemplo

Este projeto reúne uma página web de reconhecimento de imagem usando Teachable Machine e exemplos em Python com foco em lógica e refatoração.

## Estrutura do projeto

- `index.html` — interface web que usa câmera e um modelo do Teachable Machine para predizer classes via TensorFlow.js.
- `test-assistent-programing/num_primo.py` — script Python que verifica se um número é primo.
- `test-assistent-programing/refatoracao.py` — script Python refatorado que calcula estatísticas básicas de uma lista de números.
- `test-assistent-programing/explicacao-refatoracao` — explicação em texto da refatoração aplicada em `refatoracao.py`.
- `test-assistent-programing/esplicacao_num_primo` — arquivo atualmente vazio, possivelmente destinado a conter explicação sobre `num_primo.py`.
- `test-assistent-programing/debug.py` — arquivo vazio atualmente.

## Descrição geral

### `index.html`

Esta página implementa uma interface de reconhecimento de imagem com webcam:

- utiliza `@tensorflow/tfjs` e `@teachablemachine/image`
- carrega um modelo remoto do Teachable Machine
- mostra as predições em tempo real com barras de progresso
- exibe o estado da câmera e o status de conexão

### `test-assistent-programing/num_primo.py`

Contém a função `is_prime(n)`:

- valida se um número inteiro é primo
- trata casos especiais para números pequenos
- usa otimização com checagem até a raiz quadrada e passo de 6 em 6
- pode ser executado via linha de comando ou com prompt interativo

### `test-assistent-programing/refatoracao.py`

Apresenta uma versão refatorada de um código original que calcula total, média, máximo e mínimo:

- usa nomes de variáveis descritivos
- inclui docstrings e type hints
- separamos a lógica em funções reutilizáveis
- usa funções built-in Python (`sum`, `max`, `min`)

### `test-assistent-programing/explicacao-refatoracao`

Contém a explicação da refatoração feita em `refatoracao.py`, listando problemas do código original e as melhorias aplicadas.

## Como executar

### Rodar a página web

1. Abra o arquivo `index.html` em um navegador moderno.
2. Permita o acesso à câmera quando solicitado.
3. Clique em "Ativar câmera".

> O modelo é carregado de um URL remoto; portanto, é necessária conexão com a internet.

### Executar os scripts Python

É recomendado usar Python 3.8+.

```bash
python test-assistent-programing/num_primo.py 17
python test-assistent-programing/refatoracao.py
```

Se nenhum argumento for passado para `num_primo.py`, o script pedirá que o usuário digite um número.

## Observações

- `debug.py` ainda não contém código.
- `test-assistent-programing/esplicacao_num_primo` está vazio e pode ser usado para documentar a lógica da função de primo.
- A página `index.html` parece ser um protótipo de interface de reconhecimento de imagem com classes dinâmicas carregadas de um modelo Teachable Machine.

## Recomendações

- Adicionar um arquivo de documentação ou README específico para `test-assistent-programing` se desejar detalhar os exemplos Python.
- Completar `esplicacao_num_primo` com explicações sobre o algoritmo de primo.
- Caso queira versão local do modelo, substitua o URL remoto no `index.html` por um caminho local.
