select english_title as "Hiroshige Average Entropy"
from views
where artist = 'Hiroshige'
order by brightness desc
limit 5;
