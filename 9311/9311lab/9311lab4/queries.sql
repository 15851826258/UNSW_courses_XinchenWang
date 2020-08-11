-- COMP9311 18s2 Lab 04 Exercises

-- Q1. What beers are made by Toohey's?
create or replace view beer_and_brewer as
select b.name as beer,r.name as brewer
from beers b join brewers r on (b.brewer=r.id);

create or replace view Q1 as
select beer
from  beer_and_brewer
where  brewer ='Toohey''s'
;

select * from q1;

-- Q2. Show beers with headings "Beer", "Brewer".

create or replace view Q2 as
select beer as "Beer", brewer as "Brewer"
from   beer_and_brewer
;
select * from q2;

-- Q3. Find the brewers whose beers John likes.

create or replace view Q3 as
select distinct (r.name) as brewer
from   drinkers d
join likes l on d.id=l.drinker
join beers b on l.beer = b.id
join brewers r on b.brewer = r.id
where d.name='John'
;
select * from q3;
-- Q4. How many different beers are there?

create or replace view Q4 as
select count(*) as "#beers"
from   beers
;
select * from q4;

-- Q5. How many different brewers are there?
create or replace view Q5 as
select count(*) as "#brewers"
from   brewers
;
select * from q5;


-- Q6. Find pairs of beers by the same manufacturer
--     (but no pairs like (a,b) and (b,a), and no (a,a))
drop view q6
create or replace view Q6 as
select b1.name as beer1, b2.name as beer2
from   beers b1 join beers b2 on (b1.brewer=b2.brewer)
where  b1.name < b2.name
;
select * from q6;

-- Q7. How many beers does each brewer make?

create or replace view Q7 as
select r.name as brewer,count (*) as nbeers
from   brewers r join beers b on (r.id=b.brewer)
group by r.name
;
select * from q7;

-- Q8. Which brewer makes the most beers?

create or replace view Q8 as
select brewer
from   Q7
where  nbeers=(select max(nbeers) from q7)
;
select * from q8;

-- Q9. Beers that are the only one by their brewer.

create or replace view Q9 as
select beer
from   beer_and_brewer
where  brewer in (select brewer from q7 where nbeers=1)
;
select * from q9;

-- Q10. Beers sold at bars where John drinks.

create or replace view Q10 as
select distinct (b.name) as beer
from   frequents f
join drinkers d on f.drinker = d.id
join sells s on s.bar=f.bar
join beers b on s.beer = b.id
where  d.name='John'
;
select * from q10;

-- Q11. Bars where either Gernot or John drink.

create or replace view bar_and_drinker as
select b.name as bar ,d.name as drinker
from bars b
join frequents f on b.id = f.bar
join drinkers d on f.drinker = d.id;
select * from bar_and_drinker;

create or replace view Q11 as
select bar
from   bar_and_drinker
where  drinker='John' or drinker ='Gernot'
;
select * from q11;

-- Q12. Bars where both Gernot and John drink.

create or replace view Q12 as
(select bar from bar_and_drinker where drinker='John')
intersect
(select bar from bar_and_drinker where drinker='Gernot')
;
select * from q12;

-- Q13. Bars where John drinks but Gernot doesn't

create or replace view Q13 as
(select bar from bar_and_drinker where drinker='John')
except
(select bar from bar_and_drinker where drinker='Gernot')
;
select * from q13;

-- Q14. What is the most expensive beer?
create or replace view beer_bar_price as
select b.name as beer,r.name as bar,s.price
from beers b
join sells s on (s.beer=b.id)
join bars r on (s.bar=r.id);

create or replace view Q14 as
select beer
from   beer_bar_price
where  price=(select max (price) from beer_bar_price)
;
select * from q14;

-- Q15. Find bars that serve New at the same price
--      as the Coogee Bay Hotel charges for VB.

create or replace view cbh_vb_price as
select price from beer_bar_price
where bar='Coogee Bay Hotel' and beer='Victoria Bitter';
select * from cbh_vb_price;

create or replace view Q15 as
select bar
from   beer_bar_price
where  beer='New' and price=(select price from cbh_vb_price)
;
select * from q15;

-- Q16. Find the average price of common beers
--      ("common" = served in more than two hotels).

create or replace view Q16 as
select beer,avg(price)::numeric (5,2) as "AvgPrice"
from   beer_bar_price
group by beer
having count(bar)>2
;
select * from q16;

-- Q17. Which bar sells 'New' cheapest?

create or replace view Q17 as
select ...
from   ...
where  ...
;

-- Q18. Which bar is most popular? (Most drinkers)

create or replace view Q18 as
select ...
from   ...
where  ...
;

-- Q19. Which bar is least popular? (May have no drinkers)

create or replace view Q19 as
select ...
from   ...
where  ...
;

-- Q20. Which bar is most expensive? (Highest average price)

create or replace view Q20 as
select ...
from   ...
where  ...
;

-- Q21. Which beers are sold at all bars?

create or replace view Q21 as
select ...
from   ...
where  ...
;

-- Q22. Price of cheapest beer at each bar?

create or replace view Q22 as
select ...
from   ...
where  ...
;

-- Q23. Name of cheapest beer at each bar?

create or replace view Q23 as
select ...
from   ...
where  ...
;

-- Q24. How many drinkers are in each suburb?

create or replace view Q24 as
select ...
from   ...
where  ...
;

-- Q25. How many bars in suburbs where drinkers live?
--      (Must include suburbs with no bars)

create or replace view Q25 as
select ...
from   ...
where  ...
;
