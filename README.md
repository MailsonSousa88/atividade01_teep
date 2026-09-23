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

### Questão original

[Parte 3: Diagnóstico e Refatoração de Código Legado](https://maykolsampaio.github.io/cursos-maykol/cursos/automacao-web-python/unidade-1/atividade-1/#parte-3-diagnostico-e-refatoracao-de-codigo-legado)
