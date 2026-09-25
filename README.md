# atividade01_teep

Atividade 01 - Tópicos Especiais em Programação

## 🛠️ Parte 3: Diagnóstico e Refatoração de Código Legado

Esta implementação corresponde à **Parte 3 — Diagnóstico e Refatoração de Código Legado** da atividade de Automação Web com Python.

A questão propõe analisar um script legado que utiliza `requests` e identificar **5 falhas de arquitetura, qualidade ou segurança**, além de refatorá-lo aplicando:

- `httpx.Client()` com gerenciador de contexto;
- timeout explícito;
- tratamento de exceções;
- `raise_for_status()`;
- extração defensiva com `.get()` e fallbacks;
- Type Hints;
- bloco seguro `if __name__ == "__main__":`.

A solução refatorada está disponível em [`main.py`](./main.py).

## O que o código faz

O script consulta a API pública `https://reqres.in/api/users?page=1`, obtém uma lista de usuários e imprime no terminal o nome completo e o e-mail de cada pessoa.

## Como o código funciona

1. Define constantes para a URL da API e timeout (`URL` e `TIMEOUT`).
2. Na função `main()`, cria um cliente HTTP com `httpx.Client(timeout=TIMEOUT)` dentro de `with`, garantindo fechamento seguro da conexão.
3. Chama `buscar_usuarios(client)`, que:
   - faz a requisição `GET`;
   - usa `raise_for_status()` para tratar respostas HTTP com erro;
   - converte o JSON com segurança;
   - extrai o campo `data` com `.get(..., [])`;
   - valida se o resultado é realmente uma lista.
4. Se ocorrer erro de rede, HTTP ou JSON inválido, retorna lista vazia sem quebrar o programa.
5. Chama `exibir_usuarios(usuarios)`, que imprime os dados com valores padrão (fallbacks) caso algum campo venha ausente.
6. Usa `if __name__ == "__main__":` para executar `main()` apenas quando o arquivo é executado diretamente.

## Por que essa solução resolve o problema

A solução resolve a atividade porque elimina os riscos comuns do código legado e aplica as práticas pedidas no enunciado:

- aumenta a confiabilidade com timeout explícito e tratamento de exceções;
- evita falhas por estrutura inesperada de resposta usando extração defensiva;
- trata erros HTTP corretamente com `raise_for_status()`;
- melhora legibilidade e manutenção com funções separadas e type hints;
- garante execução segura e previsível com ponto de entrada explícito (`main`).

### Questão original

[Parte 3: Diagnóstico e Refatoração de Código Legado](https://maykolsampaio.github.io/cursos-maykol/cursos/automacao-web-python/unidade-1/atividade-1/#parte-3-diagnostico-e-refatoracao-de-codigo-legado)
