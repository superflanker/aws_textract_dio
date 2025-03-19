# Extração de Texto com Amazon Textract

## Descrição
Este script utiliza o serviço **Amazon Textract** para extrair texto de uma imagem contendo um documento. O processamento gera um arquivo JSON contendo a resposta da API da AWS, e as linhas de texto extraídas são exibidas no console.

## Pré-requisitos
Antes de executar o script, certifique-se de ter os seguintes requisitos atendidos:

- **Python 3.7+** instalado
- **Conta AWS** com permissões para utilizar o Amazon Textract
- **AWS CLI** configurado com credenciais válidas
- **Pacotes necessários** instalados (listados abaixo)

## Instalação
1. Clone este repositório ou baixe os arquivos.
2. Instale as dependências do projeto executando:
   ```sh
   uv install
   ```
3. Configure suas credenciais AWS caso ainda não tenha feito:
   ```bash
   aws configure
   ```

## Estrutura do Projeto
```
📂 projeto-textract
 ├── 📂 imagens
 │   └── documento-escolar.jpeg  # Imagem a ser processada
 ├── script_textract.py           # Script principal
 ├── script_textract.py           # Script principal
 ├── pyproject.toml               # Dependências
 ├── uv.lock                      #
 ├── resultado_textract.json      # Resultado da extração (gerado automaticamente)
 ├── README.md                    # Este arquivo
```

## Como Usar
1. Certifique-se de que a imagem a ser analisada está na pasta `imagens/`.
2. Execute o script:
   ```sh
   uv run script_textract.py
   ```
3. O texto extraído será exibido no console e salvo no arquivo `resultado_textract.json`.

## Explicação do Código
- `processar_imagem_textract()`: Envia a imagem para o Amazon Textract e salva a resposta no arquivo JSON.
- `extrair_linhas_texto()`: Lê o JSON e retorna as linhas de texto extraídas.
- O script imprime as linhas de texto extraídas no console.

## Erros Comuns
- **Erro de Credenciais AWS**: Verifique se as credenciais estão configuradas corretamente.
- **Arquivo de Imagem Não Encontrado**: Certifique-se de que a imagem está no caminho correto.
- **Permissão Negada**: Confirme que sua conta AWS tem permissão para usar o Textract.

## Insights e Melhorias

### **1. Aplicações Práticas**
#### **1.1 Processamento de Documentos**
- Automação da extração de dados de **notas fiscais**, **contratos**, **faturas** e **relatórios**.
- Conversão de documentos físicos para texto digital para arquivamento e busca eficiente.
- Processamento de **formulários padronizados** para entrada de dados automatizada.

#### **1.2 Análise de Textos Escaneados**
- **Reconhecimento de texto** em imagens escaneadas para facilitar pesquisas e indexação.
- Extração de **listas**, como **inventários**, **listas de materiais escolares**, **pedidos de compras**.

#### **1.3 Integração com Outros Serviços**
- **Processamento de Currículos** para triagem automática em processos seletivos.
- **Análise de textos jurídicos** para pesquisa e automação de contratos.
- **Digitalização de receitas médicas** para facilitar a interpretação e o armazenamento.

### **2. Melhorias e Expansões**
#### **2.1 Melhoria na Extração de Texto**
- **Uso de NLP (Processamento de Linguagem Natural)** para refinar e classificar o texto extraído.
- **Correção ortográfica automática** para melhorar a precisão dos resultados.
- **Detecção de palavras-chave** para categorizar documentos de forma inteligente.

#### **2.2 Suporte para Diferentes Formatos de Arquivos**
- Atualmente o sistema processa **JPEG**, mas pode ser expandido para **PNG, PDF** e outros formatos.
- Uso de **Amazon Textract StartDocumentAnalysis** para processamento assíncrono de PDFs maiores.

#### **2.3 Integração com Bancos de Dados e APIs**
- **Armazenamento dos textos extraídos** em bancos de dados (PostgreSQL, MongoDB).
- **Envio automático dos resultados** para um sistema de gestão documental.
- **Geração de relatórios automáticos** a partir das informações extraídas.

### **3. Redução de Custos e Otimização**
- Uso de **OCR alternativo (Tesseract)** para processamentos locais sem custo na AWS.
- **Armazenamento de respostas em cache** para evitar requisições repetitivas ao Textract.
- **Compressão das imagens antes do processamento** para reduzir custos e tempo de execução.

### **4. Segurança e Compliance**
- Implementação de **criptografia** para proteger os arquivos enviados e processados.
- Uso de **logs detalhados** para auditoria e rastreabilidade das informações.
- Conformidade com normas como **LGPD, GDPR** para garantir a privacidade dos dados extraídos.

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário!

---
💡 **Dúvidas ou sugestões?** Fique à vontade para abrir um issue ou contribuir! 🚀


