DROP TABLE IF EXISTS staging;
DROP TABLE IF EXISTS air_traffic;

.import --csv air_traffic.csv staging

create table air_traffic (
    "Year" INTEGER,
    "Month" INTEGER,
    dom_pax NUMBER,
    int_pax NUMBER,
    pax NUMBER,
    dom_flt NUMBER,
    int_flt NUMBER,
    flt NUMBER,
    dom_rpm NUMBER,
    int_rpm NUMBER,
    rpm NUMBER,
    dom_asm NUMBER,
    int_asm NUMBER,
    asm NUMBER,
    dom_lf NUMBER,
    int_lf NUMBER,
    lf NUMBER
);

update staging SET
    dom_pax = replace(dom_pax, ",", ""),
    int_pax = replace(int_pax, ",", ""),
    pax = replace(pax, ",", ""),
    dom_flt = replace(dom_flt, ",", ""),
    int_flt = replace(int_flt, ",", ""),
    flt = replace(flt, ",", ""),
    dom_rpm = replace(dom_rpm, ",", ""),
    int_rpm = replace(int_rpm, ",", ""),
    rpm = replace(rpm, ",", ""),
    dom_asm = replace(dom_asm, ",", ""),
    int_asm = replace(int_asm, ",", ""),
    asm = replace(asm, ",", ""),
    dom_lf = replace(dom_lf, ",", ""),
    int_lf = replace(int_lf, ",", ""),
    lf = replace(lf, ",", "");

Insert into air_traffic (
    Year,
    Month,
    dom_pax,
    int_pax,
    pax,
    dom_flt,
    int_flt,
    flt,
    dom_rpm,
    int_rpm,
    rpm,
    dom_asm,
    int_asm,
    asm,
    dom_lf,
    int_lf,
    lf
)
select
    Year,
    Month,
    CAST(dom_pax AS NUMBER),
    CAST(int_pax AS NUMBER),
    CAST(pax AS NUMBER),
    CAST(dom_flt AS NUMBER),
    CAST(int_flt AS NUMBER),
    CAST(flt AS NUMBER),
    CAST(dom_rpm AS NUMBER),
    CAST(int_rpm AS NUMBER),
    CAST(rpm AS NUMBER),
    CAST(dom_asm AS NUMBER),
    CAST(int_asm AS NUMBER),
    CAST(asm AS NUMBER),
    CAST(dom_lf AS NUMBER),
    CAST(int_lf AS NUMBER),
    CAST(lf AS NUMBER)
from staging;
