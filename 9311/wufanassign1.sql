
create domain EmailValue as
	varchar(100) check (value like '%@%.%');

create domain NameValue as
	varchar(50);

create domain LongNameValue as
	varchar(100);

--user
create domain URLValue as
	varchar(100) check (value like 'http://%');

create domain GenderValue as
	varchar(6) check (value in ('male','female'));

--Phote
create domain Title as
	varchar(50);

create domain Photo_safety_level as
	varchar check(value in ('safe', 'moderate', 'restricted'));

create domain Photo_visibility as
	varchar check (value in('private', 'friends', 'family', 'friends+family', 'public'));

--contact list
create domain GroupModeValue as
	varchar(15) check (value in ('private','by-invitation','by-request'));

create domain ContactListTypeValue as
	varchar(10) check (value in ('friends','family'));

create domain RateStar as char(1) check (value ~ '[1-5]{1}');

create table People(
	id       serial,
	family_name     NameValue,
	given_names     NameValue not null,
	displayed_name  LongNameValue,
	email_address   EmailValue not null,
	primary key(id)
);--wxc


create table Users(
	user_id        integer not null references People(id),
	website          URLValue,
	date_registered  date,
	gender           GenderValue,
	birthday		 date,
	password         text     not null, --password ?????????
	user_photo_id 	 integer ,
	primary key(user_id)

);--wxc
create table Discussions(
	discussion_id  sinteger,
	discussion_title  Title,
	primary key(discussion_id)
);--wxc

create table Photos(
	photo_id            integer unique not null,
	date_taken          date,
	photo_title         Title not null,
	date_uploaded	    date,
	description		    text,
	technical_details   text,
	safety_level		Photo_safety_level,
	visibility			Photo_visibility,
	file_size           integer,
	photo_user_id       integer references Users(user_id),
	photo_discussion_id  integer references Discussions(discussion_id),
	primary key(photo_id)

);--wxc
alter table Users add constraint FK_constraint
	foreign key (user_photo_id) REFERENCES Photos(photo_id);

create table Groups(
	group_id     integer primary key,
	group_title  text,
	mode          GroupModeValue not null,
	group_user_id integer not null references Users(user_id)

);--wxc


create table Comments(
	comment_id   integer primary key,
	when_posted	 timestamp,
	content      text ,
	comment_discussion_id integer,
	comment_user_id  integer,
	comment_comment_id integer references Comments(comment_id),
	foreign key (comment_discussion_id) references Discussions(discussion_id),
	foreign key (comment_user_id) references Users(user_id)
);--wxc

create table ContactLists(
	contactlist_id   integer primary key,
	type             ContactListTypeValue,
	contactlist_title text not null,------conjunction with the first?????
	contactlist_user_id integer references Users(user_id)
);--wxc

create table Tags(
	tag_id  integer not null,
	freq	integer,--??????????
	name    NameValue,
	primary key(tag_id)
);--wxc
/*relation ??*/
create table User_rates_photo(
	rates_user_id   integer,
	rates_photo_id  integer,
	when_rated      timestamp,
	rating           RateStar ,-----?????????5???????????
	primary key(rates_user_id,rates_photo_id),
	foreign key(rates_user_id) references Users (user_id),
	foreign key (rates_photo_id) references Photos (photo_id)
);--wxc
create table Photo_user_has_tag(
	when_tagged	 timestamp,
	has_tig_id   integer ,
	has_photo_id  integer,
	has_user_id   integer references Users(user_id),
	primary key(has_tig_id,has_user_id,has_photo_id),
	foreign key(has_photo_id) references Photos(photo_id),
	foreign key (has_tig_id) references Tags(tag_id)
);--wxc
create table Groups_has_discussion(
	Groups_has_discussion_discussion_id integer references Discussions(discussion_id),
	Groups_has_discussion_group_id integer references Groups(group_id),
	primary key(Groups_has_discussion_discussion_id,Groups_has_discussion_group_id )
);--wxc
create  table Person_Member_Contact(--?person?contactlist?? ?user?group?umember??
	Person_Member_Contact_person_id     integer not null,
	Person_Member_Contact_contactlist_id integer,
	primary key(Person_Member_Contact_person_id,Person_Member_Contact_contactlist_id),
	foreign key(Person_Member_Contact_person_id)references People(id),
	foreign key(Person_Member_Contact_contactlist_id )references ContactLists(contactlist_id)
);--wxc
create table User_Member_Group(
	User_Member_Group_user_id integer,
	User_Member_Group_group_id integer,
	primary key(User_Member_Group_user_id,User_Member_Group_group_id),
	foreign key(User_Member_Group_user_id) references Users(user_id),
	foreign key (User_Member_Group_group_id) references Groups(group_id)
);--wxc


/* ??collection??????*/
 create table Collections(
 	collection_id  integer primary key,
 	collection_title Title not null,
 	description      text,
 	collection_photo_id  integer references Photos(photo_id),
 	usercollection_user_id integer references Users (user_id),
 	groupcollection_group_id integer references Groups(group_id),
 	constraint DisjointTotal check
 	((usercollection_user_id is not null and groupcollection_group_id is null)
 	 or
 	 (usercollection_user_id is null and groupcollection_group_id is not null)
     )
 );
 create table Photo_in_collection (
	"order"           integer check("order">0),
	in_photo_id      integer references Photos (photo_id),
	in_collection_id integer references Collections(collection_id),
	primary key (in_photo_id,in_collection_id)
);--wxc
