--- COMP9311 18s2 Assignment 1
-- Schema for the myPhotos.net photo-sharing site
--
-- Written by:
--    Name:  YULIANG WANG
--    Student ID:  z5191313
--    Date:  27/08/2018
--
-- Conventions:
-- * all entity table names are plural
-- * most entities have an artifical primary key called "id"
-- * foreign keys are named after either:
--   * the relationship they represent
--   * the table being referenced

-- Domains (you may add more)


create domain URLValue as
	varchar(100) check (value like 'http://%');

create domain EmailValue as
	varchar(100) check (value like '%@%.%');

create domain GenderValue as
	varchar(6) check (value in ('male','female'));

create domain GroupModeValue as
	varchar(15) check (value in ('private','by-invitation','by-request'));

create domain ContactListTypeValue as
	varchar(10) check (value in ('friends','family'));

create domain NameValue as varchar(50);

create domain LongNameValue as varchar(100);

create domain PhotoSafetyLevel as 
	varchar(15) check (value in ('safe','moderate','restricted'));

	create domain PhotoVisibility as 
	varchar(15) check (value in ('private', 'friends', 'family', 'friends+family', 'public'));

create domain RatingType as
	integer check (value < 6 and value > 0);
-- Tables (you must add more)

create table People (
	id          	serial, --numeric ? integer??
	family_name 	NameValue,
	given_names 	NameValue not null,
	displayed_name 	LongNameValue,
	email_address 	EmailValue not null,
	primary key (id)
);

create table Users (
	id	 integer references People(id) ,
	website 		URLValue,
	date_registered date,
	gender 			GenderValue,
	birthday		 date,
	password 		text not null,
	portrait 	 integer, 
	primary key (id)
);

create table Groups (
	id serial ,
	title text,
	mode GroupModeValue not null,
	"user" integer references Users(id),
	primary key (id)
);

create table User_member_Group(
	"user" integer references Users(id),
	"group" integer references Groups(id),
	primary key ("user","group")
);

create table Contact_lists (
	id serial,
	type ContactListTypeValue,
	title text not null,
	"user" integer references Users(id),
	primary key (id)
);

create table Person_member_ContactList(
	person integer references People(id),
	Contact_list integer references Contact_lists(id),
	primary key (person, Contact_list)
);

create table Photos (
	id serial ,
	date_taken date,
	title varchar(50) not null,
	date_uploaded date,
	description text,
	technical_details text,
	safety_level PhotoSafetyLevel,
	visibility PhotoVisibility,
	file_size integer, 
	discussion integer,
	"user" integer references Users(id),
	primary key (id)
);

alter table Users add constraint FK_constraint
foreign	key (portrait) references Photos(id);

create table User_rates_Photo(
	"user" integer references Users(id),
	photo integer references Photos(id),
	rating RatingType,
	when_rated timestamp,
	primary key("user",photo)
);

create table tags(
	id serial,
	freq integer check (freq >= 0),
 	name varchar(50),
 	primary key (id)
);

create table Photo_has_Tag(
	photo integer references Photos(id),
	Tag   integer references Tags(id),
	"user" integer references Users(id),
	when_tagged timestamp,
	primary key(photo,Tag,"user")
);

create table Collections(
	id serial primary key,
	title varchar(50) not null,
	description text,
	photo integer references Photos(id)
);

create table Photo_in_Collection(
	Collection integer references Collections(id),
	Photo   	integer references Photos(id),
	"order"	integer check ("order" > 0),
	primary key (Collection, Photo)
);

create table User_Collection(
	Collection integer references Collections(id),
	"user" integer references Users(id),
	primary key (Collection)
);

create table Group_Collection(
	Collection integer references Collections(id),
	"group" integer references Groups(id),
	primary key (Collection)
);

create table Discussions(
	id serial primary key,
	title varchar(50)
);

alter table Photos add constraint FK_constraint
foreign	key (discussion) references Discussions(id);

create table Group_has_Discussion(
	group_id integer references groups(id),
	discussion_id integer references Discussions(id),
	primary key (group_id, discussion_id)
);

create table Comments(
	id serial,
	when_posted timestamp,
	content text ,
	authorBy integer references Users(id),
	replyTo integer references Comments(id),
	discussion integer references Discussions(id),
	primary key(id)
);

