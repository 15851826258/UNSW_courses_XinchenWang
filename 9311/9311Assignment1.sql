-- COMP9311 18s2 Assignment 1
-- Schema for the myPhotos.net photo-sharing site
--
-- Written by:
--    Name:  XINCHEN WANG
--    Student ID:  Z5197409
--    Date:  01/09/2018
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

--photos
create domain visibility as
  varchar(20) check (value in ('private', 'friends', 'family', 'friends+family', 'public'));

create domain SafetyLevel as
  varchar(20) check (value in ('safe', 'moderate', 'restricted'));

--rates
create domain RateStar as
  varchar (10) check (value ~ '[1-5]{1}');


-- Tables (you must add more)

create table People (
	id             serial,
	family_name    NameValue,
	given_names    NameValue not null,
	display_name   LongNameValue,
	email_address  EmailValue unique not null,
	primary key (id)
);--pass

create table Users (
  id                 integer references People(id),
	website            URLValue unique,
	date_registered    date,
	gender             GenderValue,
	birthday           date,
	password           text not null,
  portrait_photo_id  integer,
	primary key (id)
);--pass

create table Groups (
	id              serial ,
	owner_of_group  integer not null references Users(id),
	title           text not null,
	mode            GroupModeValue not null,
	primary key (id)
);--pass

create table User_member_Group (
  user_in_group       integer references Groups(id),
  groups_have_users   integer references Users(id),
  primary key (user_in_group,groups_have_users)
);--pass

create table Contact_Lists (
  id                serial,
	user_id           integer references Users(id),
	type              ContactListTypeValue,
	title             text not null,
	primary key (id)
);--pass

create table Person_member_Contactlists (
  person_in_contactlists    integer references contact_lists(id),
  contactlist_have_people   integer references People(id),
  primary key (person_in_contactlists,contactlist_have_people)
);--pass

create table Discussions(
  id                serial,
  title             varchar(50),
  primary key (id)
);--pass

create table Comments(
  id                           serial,
  when_posted                  timestamp,
  content                      text,
  user_make_comment            integer references Users(id),
  discussion_contains_comment  integer references Discussions(id),
  comment_to_comment           integer references Comments(id),
  primary key  (id)
);--pass

create table Photos(
  id                    serial,
	date_taken            date,
	title                 varchar(50) not null,
	date_uploaded         date not null,
	description           text,
  technical_details     text,
  safety_level          SafetyLevel,
  visibility            visibility ,
  file_size             integer check (file_size>0) not null,
  user_has_photo        integer references Users(id),
  discussion_of_photo   integer references Discussions(id),
	primary key (id)
);--pass
--protrait
--alter table Users add constraint FK_constraint foreign key (portrait_photo_id) references Photos(id);
alter table Users add foreign key (portrait_photo_id) references Photos(id) deferrable;

create table Tags(
  id                serial,
  name              NameValue,
  freq              integer,
  primary key (id)
);--pass

create table Photos_have_Tags(
  photo_of_user_tags            integer references Photos(id),
  tag_of_user_photos            integer references Tags(id),
  user_of_tags_photos           integer references Users(id),
  when_tagged       timestamp,
  primary key (photo_of_user_tags,tag_of_user_photos,user_of_tags_photos)---???
);--pass

create table Users_rate_Photos (
  user_rate_photo           integer references Users(id) not null ,
  photo_ratedby_users       integer references Photos(id) not null,
  rating                    RateStar not null ,
  when_rated                timestamp,
  primary key (user_rate_photo,photo_ratedby_users)
);--pass  not null

create table Groups_have_Discussions(
  discussion_of_groups         integer references Discussions(id),
  group_has_discussion         integer references Groups(id),
  primary key (discussion_of_groups,group_has_discussion)
);--pass

create table Collections (
  id                 serial,
  title              varchar(50) not null,
  description        text,
  photo_id           integer references Photos(id),
  primary key (id)
);--pass

create table Photo_in_Collections(
  rank_order        integer check (rank_order>0),
  collection_id     integer references Collections(id),
  photo_id          integer references Photos(id),
  collection_type   varchar(50) check(collection_type in ('User_Collections', 'Group_Collection')) not null,--new
  primary key (collection_id,photo_id)
);--pass


create table User_Collections(
  collection_id     integer references Collections(id),
  user_id           integer references Users(id),
  primary key (collection_id,user_id)
);--pass

create table Group_Collection(
  collection_id     integer references Collections(id),
  group_id          integer references Users(id),
  primary key (collection_id,group_id)
);--pass

