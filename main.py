import httpx
from typing import Any

URL = "https://reqres.in/api/users?page=1"
TIMEOUT = 10.0


def buscar_usuarios(client: httpx.Client) -> list[dict[str, Any]]:
    try:
        resposta = client.get(URL)
        resposta.raise_for_status()

        dados: dict[str, Any] = resposta.json()
        usuarios = dados.get("data", [])

        if not isinstance(usuarios, list):
            return []

        return usuarios

    except (httpx.HTTPError, ValueError):
        return []


def exibir_usuarios(usuarios: list[dict[str, Any]]) -> None:
    for usuario in usuarios:
        primeiro_nome = usuario.get("first_name", "Nome")
        sobrenome = usuario.get("last_name", "não informado")
        email = usuario.get("email", "E-mail não informado")

        nome = f"{primeiro_nome} {sobrenome}"

        print(f"Usuário: {nome} | Email: {email}")


def main() -> None:
    with httpx.Client(timeout=TIMEOUT) as client:
        usuarios = buscar_usuarios(client)
        exibir_usuarios(usuarios)


if __name__ == "__main__":
    main()
