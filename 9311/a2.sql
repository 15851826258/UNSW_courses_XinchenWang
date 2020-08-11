--Q1 ok 55
create or replace view Q1(name) as
  select name
  from person per join proceeding p on per.personid = p.editorid group by name;

--Q2 ok 39
create or replace view Q2(name) as
  (select name
  from relationpersoninproceeding r join  person per on per.personid = r.personid group by name )
  intersect
  (select name
  from proceeding p join person p2 on p.editorid = p2.personid group by name);

--Q3 ok 19
create or replace view q3(name) as
select distinct p.name
  from proceeding pro join person p on pro.editorid = p.personid
  join inproceeding i on pro.proceedingid = i.proceedingid
  join relationpersoninproceeding r on i.inproceedingid = r.inproceedingid
  where r.personid=pro.editorid;

--Q4 ok 31
create or replace view Q4(Title) as
  select ip.title
  from relationpersoninproceeding r,person per,proceeding p,inproceeding ip
  where r.personid=per.personid
  and per.personid=p.editorid
  and r.inproceedingid=ip.inproceedingid
  and ip.proceedingid=p.proceedingid;

--Q5 ok 2
create or replace view Q5(Title) as
  select distinct ip.title
  from relationpersoninproceeding r,person per,inproceeding ip
  where r.personid=per.personid
  and r.inproceedingid=ip.inproceedingid
  and per.name ~ '.*Clark$';

--Q6 ok 18
create or replace view Q6(Year, Total) as
  select p.year,count(*)
  from inproceeding ip,proceeding p
  where ip.proceedingid=p.proceedingid
  group by p.year
  order by p.year;

--Q7 ok 1 Springer
create or replace view Q7_publisher_inprocessing as
  select pub.name,count(*)
  from publisher pub,inproceeding ip,proceeding p
  where pub.publisherid=p.publisherid
  and p.proceedingid=ip.proceedingid
  group by name;
  --先从publish表中找到name

create or replace view Q7 as
  select max(Q7_publisher_inprocessing.name) as Name
  from Q7_publisher_inprocessing;
  --前面找到表中出现次数最多的

--Q8 ok 2 Toby Walsh,Eugene C. Freuder
create or replace view Q8_co_work as
 select r.inproceedingid,count(r.inproceedingid) as num
  from relationpersoninproceeding r
  group by r.inproceedingid
  having count(r.inproceedingid)>=2;
  --先找到具有合作的作品

create or replace view Q8_co_author as
  select per.name,per.personid
  from Q8_co_work,person per,relationpersoninproceeding r
  where Q8_co_work.inproceedingid=r.inproceedingid
  and r.personid=per.personid;
  --找到合作的作者

create or replace view Q8_name_num as
  select name,count(name) as num
  from Q8_co_author
  group by name;
  --找到合作的姓名和数字的个数

create or replace view Q8(Name) as
  select name
  from Q8_name_num
  where num=(select max(num)
              from Q8_name_num);

--Q9 ok 435
create or replace view co_works as
  select r.inproceedingid,count(inproceedingid) as num
  from relationpersoninproceeding r
  group by r.inproceedingid
  having count(r.inproceedingid)=1;
  --找出合作过的paper编号 因为人名可能重复

create or replace view co_author as
  select distinct r.personid
  from relationpersoninproceeding r
  where r.inproceedingid in (select inproceedingid from co_works);
  --找出合作者的id

create or replace view Q9_co_author as
  select per.name,per.personid
  from Q8_co_work,person per,relationpersoninproceeding r
  where Q8_co_work.inproceedingid=r.inproceedingid
  and r.personid=per.personid;
  --找到合作的作者

create or replace view Q9(Name) as
  select name
  from  person
  where personid in (select * from co_author)
  and personid not in (select q9_co_author.personid
                       from q9_co_author);
  --排除掉已经合作过的（Q8中找到的）

--Q10 ok 3358
create or replace view Q10(Name, Total) as
select per.name,count(distinct(r2.personid))-1 as Total
  from relationpersoninproceeding r1,relationpersoninproceeding r2,person per
  where per.personid=r1.personid
  and r1.inproceedingid=r2.inproceedingid
  group by per.name,r1.personid
  order by  Total desc,per.name asc;

--Q11 ok 3289
create or replace view authors as
  select  per.personid,per.name,r.inproceedingid
  from relationpersoninproceeding r,person per
  where per.personid=r.personid
  and inproceedingid is not null ;
  --所有的作者 4487

create or replace view richards_id as
  select distinct personid from authors
  where name like 'Richard%';
  --Richard作者的个数

create or replace view richards_pro as
  select r.inproceedingid
  from authors r
  where r.personid in (select * from richards_id);
  --Richard作品数34

create or replace view co_richard_id as
  select distinct r.personid
  from authors r
  where r.inproceedingid in (select * from richards_pro);
  --根据里查德的作品id查里查德的合作者id 54

create or replace view co_richard_pro as
  select distinct r.inproceedingid
  from authors r
  where r.personid in (select * from co_richard_id);
  --找出richard合作者写过的文章

create or replace view co_author_of_co_authors_id as
  select distinct r.personid
  from authors r
  where r.inproceedingid in (select * from co_richard_pro);

create or replace view co_author_of_co_authors_pro as
  select distinct r.inproceedingid
  from authors r
  where r.personid in (select * from co_author_of_co_authors_id);

create or replace view Q11 as
  select name
  from person per
  where personid in (select personid from authors
                       where personid not in (select * from co_author_of_co_authors_id))
  and name not like 'Richard%';

--Q12
create or replace view Q12_co_author(id,name,coauthor_id,coauthor_name) as
  select distinct per1.personid,per1.name,per2.personid,per2.name
  from person per1
  inner join relationpersoninproceeding r1 on per1.personid = r1.personid
  inner join relationpersoninproceeding r2 on r1.inproceedingid=r2.inproceedingid
  inner join person per2 on r2.personid = per2.personid
  where r1.personid<>r2.personid;

create or replace view Q12(Name) as with recursive Q12_func(id) as(
  select per.personid
  from person per,relationpersoninproceeding r
  where r.personid=per.personid
  and per.name ilike 'Richard%'
  union
  select coauthor_id
  from Q12_func join Q12_co_author
      on Q12_co_author.coauthor_id=Q12_func.id)
  select name from Q12_func,person per
  where per.personid=Q12_func.id
  and per.name not like 'Richard%';

--Q13 ok 3385
create or replace view parper_pro_person as
  select per.personid,per.name,p.year,i.inproceedingid,p.proceedingid
  from person per join relationpersoninproceeding r on per.personid = r.personid
  join inproceeding i on r.inproceedingid = i.inproceedingid
  left outer join  proceeding p on i.proceedingid = p.proceedingid
  order by per.personid;

create or replace view classify_by_year as
  select personid,name,count(proceedingid) as Total,
    coalesce(min(year),'unknown') as min_year,coalesce(max(year),'unknown') as max_year
  from parper_pro_person
  group by personid,name;

create or replace view Q13(Author, Total, FirstYear, LastYear) as
  select name,Total,min_year as FirstYear,max_year as LastYear
  from classify_by_year
  order by total desc,name asc;

--Q14 ok 288
create or replace view proceeding_contain_data as
  select p.proceedingid
  from proceeding p
  where title ilike '%data%';
   --找到包含data的期刊
create or replace view paper_contain_data as
  select ip.inproceedingid
  from inproceeding ip
  where ip.title ilike '%data%';
  --找到包含data的文章
create or replace view paper_pro_contain_data as
  select ip.inproceedingid
  from inproceeding ip
  where ip.proceedingid in (select * from proceeding_contain_data);
  --找出带有data的期刊中的文章
create or replace view data_pro as
  (select distinct personid
  from relationpersoninproceeding r
  where r.inproceedingid in (select * from paper_contain_data))
  union
  (select distinct personid
  from relationpersoninproceeding r
  where r.inproceedingid in (select * from paper_pro_contain_data));
  --将两种的作者入表
create or replace view Q14(Total) as
  select count(*) from data_pro;

--Q15 ok 59
create or replace view Q15(EditorName, Title, PublisherName, Year, Total) as
  select per.name as EditorName,p.title as Title,pub.name as PublisherName,p.year as Year,count(ip.inproceedingid) as Total
  from person per,proceeding p,publisher pub,inproceeding ip
  where per.personid=p.editorid
  and pub.publisherid=p.publisherid
  and p.proceedingid=ip.proceedingid
  group by per.name,p.title,pub.name,p.year
  order by Total desc,year asc ,title asc;

--Q16 ok 427
Create or replace view never_edit_id as
  select per.personid
  from person per,proceeding p
  where per.personid=p.editorid;
  --找出从来没有编辑过的人的ID
create or replace view never_edit_name as
  select per.name
  from person per
  where personid in (select * from never_edit_id);
  --找出从来没有编辑过的人的姓名
create or replace view Q16(Name) as
  select Q9.name
  from Q9
  except (select * from never_edit_name);


--Q17 ok 2955
create or replace view author as
  select per.name,per.personid,ip.inproceedingid,ip.proceedingid
  from person per,inproceeding ip,relationpersoninproceeding r
  where ip.inproceedingid=r.inproceedingid
  and r.personid=per.personid
  group by per.personid,ip.inproceedingid
  having count(proceedingid)>=1;

create or replace view author_and_papernum as
  select author.personid,author.name,count(proceedingid) as Total
  from author
  group by author.personid,author.name;

create or replace view Q17(Name, Total) as
  select author_and_papernum.name,author_and_papernum.Total
  from author_and_papernum
  where author_and_papernum.personid in (select personid from author_and_papernum)
  order by Total desc ,personid asc;

--Q18 ok 1 1 14
create or replace view publications as
  select per.personid,p.proceedingid
  from person per,relationpersoninproceeding r,inproceeding ip,proceeding p
  where per.personid=r.personid
  and r.inproceedingid=ip.inproceedingid
  and ip.proceedingid=p.proceedingid
  and ip.proceedingid is not null
  group by per.personid,p.proceedingid;
  --找到每个作者对应的出版物

create or replace view sum_of_publications as
  select publications.personid,count(publications.proceedingid) as sum
  from  publications
  group by publications.personid;
  --每个作者对应出版物的数量

create or replace view Q18(MinPub, AvgPub, MaxPub) as
  select min(total)::int as MinPub,round(avg(total)) as AvgPub,max(total)::int as MaxPub
  from Q17;

--Q19 ok 4 28 94
create or replace view pub_in_p as
  select p.proceedingid,count(ip.inproceedingid) as papernum
  from proceeding p
  left outer join inproceeding ip
  on p.proceedingid=ip.proceedingid
  group by p.proceedingid;
  --先找到符合条件出版物的期刊
create or replace view Q19(MinPub, AvgPub, MaxPub) as
  select min(papernum)::int as MinPub,round(avg(papernum)) as AvgPub,max(papernum)::int as MaxPub
  from pub_in_p;
  --得到最小平均数和最大

--Q1 ok 55
create or replace view Q1(name) as
  select name
  from person per join proceeding p on per.personid = p.editorid group by name;

--Q2 ok 39
create or replace view Q2(name) as
  (select name
  from relationpersoninproceeding r join  person per on per.personid = r.personid group by name )
  intersect
  (select name
  from proceeding p join person p2 on p.editorid = p2.personid group by name);

--Q3 ok 19
create or replace view q3(name) as
select distinct p.name
  from proceeding pro join person p on pro.editorid = p.personid
  join inproceeding i on pro.proceedingid = i.proceedingid
  join relationpersoninproceeding r on i.inproceedingid = r.inproceedingid
  where r.personid=pro.editorid;

--Q4 ok 31
create or replace view Q4(Title) as
  select ip.title
  from relationpersoninproceeding r,person per,proceeding p,inproceeding ip
  where r.personid=per.personid
  and per.personid=p.editorid
  and r.inproceedingid=ip.inproceedingid
  and ip.proceedingid=p.proceedingid;

--Q5 ok 2
create or replace view Q5(Title) as
  select distinct ip.title
  from relationpersoninproceeding r,person per,inproceeding ip
  where r.personid=per.personid
  and r.inproceedingid=ip.inproceedingid
  and per.name ~ '.*Clark$';

--Q6 ok 18
create or replace view Q6(Year, Total) as
  select p.year,count(*)
  from inproceeding ip,proceeding p
  where ip.proceedingid=p.proceedingid
  group by p.year
  order by p.year;

--Q7 ok 1 Springer
create or replace view Q7_publisher_inprocessing as
  select pub.name,count(*)
  from publisher pub,inproceeding ip,proceeding p
  where pub.publisherid=p.publisherid
  and p.proceedingid=ip.proceedingid
  group by name;
  --先从publish表中找到name

create or replace view Q7 as
  select max(Q7_publisher_inprocessing.name) as Name
  from Q7_publisher_inprocessing;
  --前面找到表中出现次数最多的

--Q8 ok 2 Toby Walsh,Eugene C. Freuder
create or replace view Q8_co_work as
 select r.inproceedingid,count(r.inproceedingid) as num
  from relationpersoninproceeding r
  group by r.inproceedingid
  having count(r.inproceedingid)>=2;
  --先找到具有合作的作品

create or replace view Q8_co_author as
  select per.name,per.personid
  from Q8_co_work,person per,relationpersoninproceeding r
  where Q8_co_work.inproceedingid=r.inproceedingid
  and r.personid=per.personid;
  --找到合作的作者

create or replace view Q8_name_num as
  select name,count(name) as num
  from Q8_co_author
  group by name;
  --找到合作的姓名和数字的个数

create or replace view Q8(Name) as
  select name
  from Q8_name_num
  where num=(select max(num)
              from Q8_name_num);

--Q9 ok 435
create or replace view co_works as
  select r.inproceedingid,count(inproceedingid) as num
  from relationpersoninproceeding r
  group by r.inproceedingid
  having count(r.inproceedingid)=1;
  --找出合作过的paper编号 因为人名可能重复

create or replace view co_author as
  select distinct r.personid
  from relationpersoninproceeding r
  where r.inproceedingid in (select inproceedingid from co_works);
  --找出合作者的id

create or replace view Q9_co_author as
  select per.name,per.personid
  from Q8_co_work,person per,relationpersoninproceeding r
  where Q8_co_work.inproceedingid=r.inproceedingid
  and r.personid=per.personid;
  --找到合作的作者

create or replace view Q9(Name) as
  select name
  from  person
  where personid in (select * from co_author)
  and personid not in (select q9_co_author.personid
                       from q9_co_author);
  --排除掉已经合作过的（Q8中找到的）

--Q10 ok 3358
create or replace view Q10(Name, Total) as
select per.name,count(distinct(r2.personid))-1 as Total
  from relationpersoninproceeding r1,relationpersoninproceeding r2,person per
  where per.personid=r1.personid
  and r1.inproceedingid=r2.inproceedingid
  group by per.name,r1.personid
  order by  Total desc,per.name asc;

--Q11 ok 3289
create or replace view authors as
  select  per.personid,per.name,r.inproceedingid
  from relationpersoninproceeding r,person per
  where per.personid=r.personid
  and inproceedingid is not null ;
  --所有的作者 4487

create or replace view richards_id as
  select distinct personid from authors
  where name like 'Richard%';
  --Richard作者的个数

create or replace view richards_pro as
  select r.inproceedingid
  from authors r
  where r.personid in (select * from richards_id);
  --Richard作品数34

create or replace view co_richard_id as
  select distinct r.personid
  from authors r
  where r.inproceedingid in (select * from richards_pro);
  --根据里查德的作品id查里查德的合作者id 54

create or replace view co_richard_pro as
  select distinct r.inproceedingid
  from authors r
  where r.personid in (select * from co_richard_id);
  --找出richard合作者写过的文章

create or replace view co_author_of_co_authors_id as
  select distinct r.personid
  from authors r
  where r.inproceedingid in (select * from co_richard_pro);

create or replace view co_author_of_co_authors_pro as
  select distinct r.inproceedingid
  from authors r
  where r.personid in (select * from co_author_of_co_authors_id);

create or replace view Q11 as
  select name
  from person per
  where personid in (select personid from authors
                       where personid not in (select * from co_author_of_co_authors_id))
  and name not like 'Richard%';

--Q12
create or replace view Q12_co_author(id,name,coauthor_id,coauthor_name) as
  select distinct per1.personid,per1.name,per2.personid,per2.name
  from person per1
  inner join relationpersoninproceeding r1 on per1.personid = r1.personid
  inner join relationpersoninproceeding r2 on r1.inproceedingid=r2.inproceedingid
  inner join person per2 on r2.personid = per2.personid
  where r1.personid<>r2.personid;

create or replace view Q12(Name) as with recursive Q12_func(id) as(
  select per.personid
  from person per,relationpersoninproceeding r
  where r.personid=per.personid
  and per.name ilike 'Richard%'
  union
  select coauthor_id
  from Q12_func join Q12_co_author
      on Q12_co_author.coauthor_id=Q12_func.id)
  select name from Q12_func,person per
  where per.personid=Q12_func.id
  and per.name not like 'Richard%';

--Q13 ok 3385
create or replace view parper_pro_person as
  select per.personid,per.name,p.year,i.inproceedingid,p.proceedingid
  from person per join relationpersoninproceeding r on per.personid = r.personid
  join inproceeding i on r.inproceedingid = i.inproceedingid
  left outer join  proceeding p on i.proceedingid = p.proceedingid
  order by per.personid;

create or replace view classify_by_year as
  select personid,name,count(proceedingid) as Total,
    coalesce(min(year),'unknown') as min_year,coalesce(max(year),'unknown') as max_year
  from parper_pro_person
  group by personid,name;

create or replace view Q13(Author, Total, FirstYear, LastYear) as
  select name,Total,min_year as FirstYear,max_year as LastYear
  from classify_by_year
  order by total desc,name asc;

--Q14 ok 288
create or replace view proceeding_contain_data as
  select p.proceedingid
  from proceeding p
  where title ilike '%data%';
   --找到包含data的期刊
create or replace view paper_contain_data as
  select ip.inproceedingid
  from inproceeding ip
  where ip.title ilike '%data%';
  --找到包含data的文章
create or replace view paper_pro_contain_data as
  select ip.inproceedingid
  from inproceeding ip
  where ip.proceedingid in (select * from proceeding_contain_data);
  --找出带有data的期刊中的文章
create or replace view data_pro as
  (select distinct personid
  from relationpersoninproceeding r
  where r.inproceedingid in (select * from paper_contain_data))
  union
  (select distinct personid
  from relationpersoninproceeding r
  where r.inproceedingid in (select * from paper_pro_contain_data));
  --将两种的作者入表
create or replace view Q14(Total) as
  select count(*) from data_pro;

--Q15 ok 59
create or replace view Q15(EditorName, Title, PublisherName, Year, Total) as
  select per.name as EditorName,p.title as Title,pub.name as PublisherName,p.year as Year,count(ip.inproceedingid) as Total
  from person per,proceeding p,publisher pub,inproceeding ip
  where per.personid=p.editorid
  and pub.publisherid=p.publisherid
  and p.proceedingid=ip.proceedingid
  group by per.name,p.title,pub.name,p.year
  order by Total desc,year asc ,title asc;

--Q16 ok 427
Create or replace view never_edit_id as
  select per.personid
  from person per,proceeding p
  where per.personid=p.editorid;
  --找出从来没有编辑过的人的ID
create or replace view never_edit_name as
  select per.name
  from person per
  where personid in (select * from never_edit_id);
  --找出从来没有编辑过的人的姓名
create or replace view Q16(Name) as
  select Q9.name
  from Q9
  except (select * from never_edit_name);


--Q17 ok 2955
create or replace view author as
  select per.name,per.personid,ip.inproceedingid,ip.proceedingid
  from person per,inproceeding ip,relationpersoninproceeding r
  where ip.inproceedingid=r.inproceedingid
  and r.personid=per.personid
  group by per.personid,ip.inproceedingid
  having count(proceedingid)>=1;

create or replace view author_and_papernum as
  select author.personid,author.name,count(proceedingid) as Total
  from author
  group by author.personid,author.name;

create or replace view Q17(Name, Total) as
  select author_and_papernum.name,author_and_papernum.Total
  from author_and_papernum
  where author_and_papernum.personid in (select personid from author_and_papernum)
  order by Total desc ,personid asc;

--Q18 ok 1 1 14
create or replace view publications as
  select per.personid,p.proceedingid
  from person per,relationpersoninproceeding r,inproceeding ip,proceeding p
  where per.personid=r.personid
  and r.inproceedingid=ip.inproceedingid
  and ip.proceedingid=p.proceedingid
  and ip.proceedingid is not null
  group by per.personid,p.proceedingid;
  --找到每个作者对应的出版物

create or replace view sum_of_publications as
  select publications.personid,count(publications.proceedingid) as sum
  from  publications
  group by publications.personid;
  --每个作者对应出版物的数量

create or replace view Q18(MinPub, AvgPub, MaxPub) as
  select min(total)::int as MinPub,round(avg(total)) as AvgPub,max(total)::int as MaxPub
  from Q17;

--Q19 ok 4 28 94
create or replace view pub_in_p as
  select p.proceedingid,count(ip.inproceedingid) as papernum
  from proceeding p
  left outer join inproceeding ip
  on p.proceedingid=ip.proceedingid
  group by p.proceedingid;
  --先找到符合条件出版物的期刊
create or replace view Q19(MinPub, AvgPub, MaxPub) as
  select min(papernum)::int as MinPub,round(avg(papernum)) as AvgPub,max(papernum)::int as MaxPub
  from pub_in_p;
  --得到最小平均数和最大

--20
create or replace view  Q20 as
  (select personid from relationpersoninproceeding r
join inproceeding ip on (r.inproceedingid = ip.inproceedingid)
join proceeding p on (i.proceedingid = p.proceedingid)
where (new.personid = r.personid));

Create or replace function disallow_for_Q20() returns trigger as
$$
begin

if (new.inproceedingid) in
         (select r.inproceedingid from relationpersoninproceeding r
   where r.personid in
         (select personid from relationpersoninproceeding r
join inproceeding ip on (r.inproceedingid = ip.inproceedingid)
join proceeding p on (i.proceedingid = p.proceedingid)
where (new.personid = r.personid)))
then
  raise exception 'Failed!Disallowing!';
  return old;
 end if;
Return new;
End;
$$ language plpgsql;

Create trigger Q20
  before insert or update
  on relationpersoninproceeding
  for each row
execute procedure disallow_for_Q20();


























