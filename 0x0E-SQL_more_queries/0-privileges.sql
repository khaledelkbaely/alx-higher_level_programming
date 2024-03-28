-- lists all priviliges of the mysql users user_0d_1 user_0d_2
-- Usage: cat 0-priviliges.sql | mysql -hlocalhost -uroot -p
SHOW GRANTS FOR `user_0d_1`@`localhost`;
SHOW GRANTS FOR `user_0d_2`@`localhost`;
