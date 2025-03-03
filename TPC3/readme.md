# TPC3

## Extração de dados textuais para criação de template HTML

### Objetivo

Este TPC3 tem como objetivo processar um ficheiro de texto de conceitos médicos e as suas respetivas definições, gerando um ficheiro HTML para visualização formatada dos conteúdos.

### Descrição do Problema

O ficheiro de entrada está estruturado com conceitos médicos seguidos das suas definições, separados por quebras de linha. Cada par conceito-definição é delimitado por uma dupla quebra de linha. No entanto, o ficheiro contém casos em que os conceitos e definições são separados por quebras de página, o que introduz quebras de linha adicionais.

O método de marcar conceitos com o caractere `@` sempre que eram precedidos por duas quebras de linha, falhava em alguns casos, identificando incorretamente partes das definições como conceitos (no conceito aberrante, por exemplo)

### Solução Proposta

Para resolver este problema, a solução proposta modifica a abordagem inicial de marcação de conceitos. Em vez de simplesmente adicionar o caractere `@` após cada dupla quebra de linha, é utilizada uma expressão regular mais robusta.

texto = re.sub(r"(\n\n)(.*)\n{1,}", r"\1@\2\n", texto)

### Explicação da expressão regular:
(\n\n): Captura exatamente duas quebras de linha.

(.*): Captura qualquer texto na linha seguinte (presumivelmente o nome do conceito).

\n{1,}: Garante que uma ou mais quebras de linha subsequentes são consideradas, permitindo acomodar os casos onde há quebras extras de página.

r"\1@\2\n": Reinsere as duas quebras de linha originais, adiciona @ antes do conceito e mantém uma única quebra de linha após ele.

Este método garante que apenas as linhas que representam conceitos sejam corretamente identificadas, evitando marcações erradas dentro das definições.

### Extração dos Conceitos
Após a marcação adequada dos conceitos, utilizamos outra expressão regular para extrair corretamente os pares conceito-definição:

conceitos_raw = re.findall(r'@(.*?)\n(.*?)(?=\n@|\Z)', texto)

### Explicação da expressão regular:
@: Indica o início de um conceito.

(.*?)\n: Captura o nome do conceito até à primeira quebra de linha.

(.*?): Captura a definição do conceito.

(?=\n@|\Z): Utiliza uma lookahead assertion (conceito aprendido e utilizado no último TPC)  para definir onde a captura deve parar:

\n@: Se houver um @ após uma quebra de linha, significa que um novo conceito começa.

\Z: Garante que a última definição também seja capturada corretamente no final do ficheiro, ao contrário do $, o \Z define o final de uma string ou texto para lá dos \n.

Com este método, os conceitos e suas definições são extraídos corretamente, prontos para serem formatados em HTML (tpc3.html)


