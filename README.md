# Profiling--Buscador
O objetivo deste código é realizar uma análise de desempenho de um método de busca sequencial em diferentes tamanhos de arquivos. Especificamente, estamos realizando uma busca numérica em arquivos com um milhão, um bilhão e um trilhão de linhas. A estrutura do arquivo é um número por linha. Durante o processo, monitoraremos o uso de CPU, memória RAM e tempo de execução dedicados exclusivamente ao momento da busca nos arquivos.

**Observação:** A criação do terceiro arquivo excedeu 200 GB e, mesmo assim, a execução não foi concluída. Realizei modificações para otimizá-lo, porém não foram suficientes para efetuar a busca por um trilhão de linhas. Mesmo usando uma lógica diferente, criando vários arquivos menores e descartando-os quando a busca era finalizada sem sucesso, o resultado permaneceu inconclusivo nesse escopo.

Segue o PDF com todos os dados que consegui, com graficos e tabelas de comparação.
[Profiling - Buscador.pdf](https://github.com/user-attachments/files/16698186/Profiling.-.Buscador.pdf)
