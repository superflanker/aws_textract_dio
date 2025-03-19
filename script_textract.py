import json
from pathlib import Path
import boto3
from botocore.exceptions import ClientError
from mypy_boto3_textract.type_defs import DetectDocumentTextResponseTypeDef

def processar_imagem_textract() -> None:
    """
    Processa uma imagem utilizando o Amazon Textract para detectar texto.
    O resultado da extração é salvo em um arquivo JSON chamado 'resultado_textract.json'.
    """
    client = boto3.client("textract")

    caminho_arquivo = str(Path(__file__).parent / "images" / "lista-material-escolar.jpeg")
    with open(caminho_arquivo, "rb") as f:
        bytes_documento = f.read()

    try:
        resposta = client.detect_document_text(Document={"Bytes": bytes_documento})
        with open("resultado_textract.json", "w") as arquivo_resposta:
            json.dump(resposta, arquivo_resposta)
    except ClientError as erro:
        print(f"Erro ao processar o documento: {erro}")

def extrair_linhas_texto() -> list[str]:
    """
    Extrai as linhas de texto do arquivo 'resultado_textract.json'.
    Se o arquivo não existir, ele será gerado chamando `processar_imagem_textract()`.
    
    Retorna:
        list[str]: Lista de linhas de texto extraídas do documento.
    """
    try:
        with open("resultado_textract.json", "r") as f:
            dados: DetectDocumentTextResponseTypeDef = json.load(f)
            blocos = dados["Blocks"]
        return [bloco["Text"] for bloco in blocos if bloco["BlockType"] == "LINE"]  # type: ignore
    except IOError:
        processar_imagem_textract()
    return []

if __name__ == "__main__":
    for linha in extrair_linhas_texto():
        print(linha)

