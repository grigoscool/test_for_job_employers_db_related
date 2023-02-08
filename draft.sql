CREATE TABLE work_site_electric as SELECT


insert into work_site_electric select
(now() — interval '1 day' * round(random() * 100))::timestamp(0) as employment_date,
generate_series(2,40000) as id,
md5(random()::text)::char(10) as fio,
(array['electric', 'monter', 'operative'])[ceil(random()*3)] as job,
(floor(random()*35000+55000))::int as salary,
(floor(random()*1+999)):: int as leader_id;
