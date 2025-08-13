select english_title, artist
from views
where artist = 'Hokusai'
order by brightness desc
limit 1;
