CREATE TABLE public."CNPJ_utilizados_2023_2024" AS
SELECT 
    REGEXP_REPLACE(CNPJ_CPF, '[^0-9]', '', 'g') AS CNPJ_CPF
FROM 
    cotas_ano_2023
UNION
SELECT 
    REGEXP_REPLACE(CNPJ_CPF, '[^0-9]', '', 'g') AS CNPJ_CPF
FROM 
    cotas_ano_2024;


ALTER TABLE IF EXISTS public."CNPJ_utilizados_2023_2024"
    OWNER to postgres;
