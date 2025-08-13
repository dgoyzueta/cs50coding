
select
round((select max(entropy) from views where artist = 'Hokusai') - entropy, 2) AS Diffence_from_Max_Entropy
from views
where artist = 'Hokusai'
order by entropy;
