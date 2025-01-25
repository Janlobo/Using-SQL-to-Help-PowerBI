-- View: public.View_CNPJs_Detalhes

-- DROP VIEW public."View_CNPJs_Detalhes";

CREATE OR REPLACE VIEW public."View_CNPJs_Detalhes"
 AS
 SELECT empresa.cnpj_basico,
    empresa.razao_social,
    estabelecimento.nome_fantasia,
    estabelecimento.uf,
    estabelecimento.data_inicio_atividade,
    concat(estabelecimento.cnpj_basico, '', estabelecimento.cnpj_ordem, '', estabelecimento.cnpj_dv) AS cnpj_full,
    cnae.descricao AS atividade,
    munic.descricao AS municipio,
    natju.descricao,
    quals.descricao AS qualificacao,
    cnpjs2023e2024.cnpj_cpf
   FROM empresa
     JOIN natju ON empresa.natureza_juridica = natju.codigo
     JOIN estabelecimento ON empresa.cnpj_basico = estabelecimento.cnpj_basico
     JOIN quals ON empresa.qualificacao_responsavel = quals.codigo
     JOIN cnae ON estabelecimento.cnae_fiscal_principal::text = cnae.codigo
     JOIN munic ON estabelecimento.municipio = munic.codigo
     JOIN cnpjs2023e2024 ON concat(estabelecimento.cnpj_basico, '', estabelecimento.cnpj_ordem, '', estabelecimento.cnpj_dv) = cnpjs2023e2024.cnpj_cpf
  WHERE estabelecimento.motivo_situacao_cadastral <> ALL (ARRAY[1, 5, 6, 10, 15, 31, 34, 37, 54, 66, 67, 70, 75]);

ALTER TABLE public."View_CNPJs_Detalhes"
    OWNER TO postgres;
