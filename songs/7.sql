select avg(energy) avg_enery from songs
where artist_id = (select id from artists where name = 'Drake');
