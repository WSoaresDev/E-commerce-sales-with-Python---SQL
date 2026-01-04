CREATE DATABASE analise_vendas;
USE analise_vendas;

-- Tabela de Produtos
CREATE TABLE produtos (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR(100),
    categoria VARCHAR(50),
    preco_custo DECIMAL(10,2),
    preco_venda DECIMAL(10,2)
);

-- Tabela de Vendas (Relacional)
CREATE TABLE vendas (
    id_venda INT PRIMARY KEY AUTO_INCREMENT,
    id_produto INT,
    quantidade INT,
    data_venda DATE,
    canal_venda VARCHAR(50), -- Ex: Online, Loja Física
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

-- Inserindo dados para análise
INSERT INTO produtos (nome_produto, categoria, preco_custo, preco_venda) VALUES 
('iPhone 15', 'Eletrônicos', 4000.00, 7000.00),
('Cadeira Gamer', 'Móveis', 500.00, 1200.00),
('Teclado Mecânico', 'Acessórios', 150.00, 450.00);

INSERT INTO vendas (id_produto, quantidade, data_venda, canal_venda) VALUES 
(1, 2, '2023-11-01', 'Online'),
(2, 5, '2023-11-02', 'Loja Física'),
(1, 1, '2023-11-03', 'Online'),
(3, 10, '2023-11-04', 'Online');