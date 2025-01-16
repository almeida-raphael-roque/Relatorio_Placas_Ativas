-- a granularidade é por placas, logo 
SELECT DISTINCT
    coalesce(iv.BOARD,it.BOARD,itt.BOARD) as "placa",
    coalesce(iv.chassi,it.chassi,itt.chassi) as "chassi",
    coalesce(iv.id,it.id,itt.id) as "id_placa",
    cast(coalesce(irsc.date_initial_effect,date_add('day',-364,irsc.date_final_effect)) as date) as "data_ativacao",
    ir.id as "Matricula",
    irs.id as "Conjunto",
    'Segtruck' as empresa
    
from silver.insurance_registration ir
        left outer join silver.insurance_reg_set irs on irs.parent = ir.id
        left outer join silver.INSURANCE_REG_SET_COVERAGE irsc ON irsc.PARENT = irs.ID
        left outer join silver.insurance_vehicle iv ON iv.id = irsc.id_vehicle
        left outer join silver.INSURANCE_REG_SET_COV_TRAILER irsct on irsct.PARENT = irsc.ID
        left outer join silver.INSURANCE_TRAILER it on it.ID = irsct.ID_TRAILER
        left outer join silver.insurance_trailer itt on itt.id = irsc.ID_TRAILER

WHERE
    coalesce(iv.BOARD,it.BOARD,itt.BOARD) is not null
    AND coalesce(iv.chassi,it.chassi,itt.chassi) is not null
 
 ORDER BY  cast(coalesce(irsc.date_initial_effect,date_add('day',-364,irsc.date_final_effect)) as date) DESC 


----------------------------------------------------------------------------------------------------
union all
----------------------------------------------------------------------------------------------------


SELECT DISTINCT
    coalesce(iv.BOARD,it.BOARD,itt.BOARD) as "placa",
    coalesce(iv.chassi,it.chassi,itt.chassi) as "chassi",
    coalesce(iv.id,it.id,itt.id) as "id_placa",
    cast(coalesce(irsc.date_initial_effect,date_add('day',-364,irsc.date_final_effect)) as date) as "data_ativacao",
    ir.id as "Matricula",
    irs.id as "Conjunto",
    'Stcoop' as empresa
    
from stcoop.insurance_registration ir
        left outer join stcoop.insurance_reg_set irs on irs.parent = ir.id
        left outer join stcoop.INSURANCE_REG_SET_COVERAGE irsc ON irsc.PARENT = irs.ID
        left outer join stcoop.insurance_vehicle iv ON iv.id = irsc.id_vehicle 
        left outer join stcoop.INSURANCE_REG_SET_COV_TRAILER irsct on irsct.PARENT = irsc.ID
        left outer join stcoop.INSURANCE_TRAILER it on it.ID = irsct.ID_TRAILER
        left outer join stcoop.insurance_trailer itt on itt.id = irsc.ID_TRAILER

WHERE
    coalesce(iv.BOARD,it.BOARD,itt.BOARD) is not null
    AND coalesce(iv.chassi,it.chassi,itt.chassi) is not null
 
 ORDER BY  cast(coalesce(irsc.date_initial_effect,date_add('day',-364,irsc.date_final_effect)) as date) DESC 


----------------------------------------------------------------------------------------------------
union all
----------------------------------------------------------------------------------------------------


SELECT DISTINCT
    coalesce(iv.BOARD,it.BOARD,itt.BOARD) as "placa",
    coalesce(iv.chassi,it.chassi,itt.chassi) as "chassi",
    coalesce(iv.id,it.id,itt.id) as "id_placa",
    cast(coalesce(irsc.date_initial_effect,date_add('day',-364,irsc.date_final_effect)) as date) as "data_ativacao",
    ir.id as "Matricula",
    irs.id as "Conjunto",
    'Viavante' as empresa
    
from viavante.insurance_registration ir
        left outer join viavante.insurance_reg_set irs on irs.parent = ir.id
        left outer join viavante.INSURANCE_REG_SET_COVERAGE irsc ON irsc.PARENT = irs.ID
        left outer join viavante.insurance_vehicle iv ON iv.id = irsc.id_vehicle 
        left outer join viavante.INSURANCE_REG_SET_COV_TRAILER irsct on irsct.PARENT = irsc.ID
        left outer join viavante.INSURANCE_TRAILER it on it.ID = irsct.ID_TRAILER
        left outer join viavante.insurance_trailer itt on itt.id = irsc.ID_TRAILER

WHERE
    coalesce(iv.BOARD,it.BOARD,itt.BOARD) is not null
    AND coalesce(iv.chassi,it.chassi,itt.chassi) is not null
 
 ORDER BY  cast(coalesce(irsc.date_initial_effect,date_add('day',-364,irsc.date_final_effect)) as date) DESC 
 -- a mudança no order by foi para ele pegar no python (transform) como a empresa anterior em que a placa estava cadastrada
 -- caso tenha ocorrido migração