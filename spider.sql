create table if not exists topic.topic
(
    id int auto_increment
        primary key,
    topic_name varchar(200) not null,
    count bigint not null,
    insert_datetime datetime default CURRENT_TIMESTAMP null,
    update_datetime datetime default CURRENT_TIMESTAMP null
);