truncate table db_project.tsk2_selection;

insert into db_project.tsk2_selection select * from db_project.tsk2_tbl1
where ID in (1, 2, 3, 4);

select * from db_project.tsk2_selection;
/*--------------------------------------------*/
truncate table db_project.tsk2_projection;

insert into db_project.tsk2_projection select ID, aaa, bbb from db_project.tsk2_tbl1;

select * from db_project.tsk2_projection;
/*--------------------------------------------*/
truncate table db_project.tsk2_union;

insert into db_project.tsk2_union 
select aaa, bbb, ccc from db_project.tsk2_tbl1
union all
select xxx, zzz, yyy from db_project.tsk2_tbl2;

select * from db_project.tsk2_union;
/*-------------------------------------------*/
truncate table db_project.tsk2_minus;

insert into db_project.tsk2_minus select * from db_project.tsk2_tbl1
where ID not in (select ID from db_project.tsk2_tbl1 where aaa like 'aaaaa1');

select * from db_project.tsk2_minus;
/*---------------------------------------------*/
truncate table db_project.tsk2_cross_product;

insert into db_project.tsk2_cross_product select t1.*, t2.xxx, t2.yyy, t2.zzz from db_project.tsk2_tbl1 t1
cross join db_project.tsk2_tbl2 t2 on t1.ID = t2.ID;

select * from db_project.tsk2_cross_product;
/*---------------------------------------------*/