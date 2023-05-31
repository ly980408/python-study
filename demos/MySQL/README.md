# MySQL

## 安装与配置

### 安装MySQL

https://dev.mysql.com/downloads/

### 配置MySQL

在安装目录下创建`my.ini`

```ini
[mysqld]

# port
port = 3306

# mysql path
basedir = D:\\mysql

# database path
datadir = D:\\mysql\\data
```

### 连接MySQL

使用MySQL自带工具测试连接

```shell
"D:\mysq\bin\mysql.exe" -h 127.0.0.1 -P 3306 -u root -p
```

连接本机默认端口，可简写为：

```shell
"D:\mysql\bin\mysql.exe" -u root -p
```

添加环境变量后：

```shell
mysql -u root -p
```

初始密码为空，直接回车登录。连接到MySQL后，可输入命令设置密码：

```
set password = password("123456");
```

断开连接：
`quit;` or `exit;`

## MySQL指令

### 数据库(Databases)

- 查看已有数据库：
  `show databases;`
- 创建数据库：
  `create database test_db;`
- 删除数据库：
  `drop database test_db;`
- 进入数据库：
  `use test_db;`
- 查看当前数据库所有表：
  `show tables;`

### 数据表(Tables)

进入数据库：
`use test_db;`

创建表：

```sql
create table 表名称
(
    列名称 类型,
    列名称 类型,
    列名称 类型,
);
```

例如:

```sql
create table user_table
(
    id   int,
    name varchar(16),
    age  int
) default charset=utf8;
```

添加约束：

```sql
create table user_table
(
    id   int primary key not null auto_increment, -- 主键，不允许为空，自增
    name varchar(16)     not null,                -- 不允许为空
    age  int default 18                           -- 默认值
) default charset=utf8;
```

删除表：
`drop table user_table;`

> 常用数据类型：
> - tinyint
> - int
> - bigint
> - float
> - double
> - decimal
> - char
> - varchar
> - text
> - datetime
> - time
>
> 参考:
> - https://dev.mysql.com/doc/refman/5.7/en/data-types.html
> - https://www.runoob.com/mysql/mysql-data-types.html
> - https://www.w3school.com.cn/sql/sql_datatypes.asp

### 数据行(Rows)

- 新增数据：

```sql
insert into 表名(列名1, 列名2, ..., 列名N) values (值1, 值2, ..., 值N);
```

- 删除数据：

```sql
delete from 表名;
delete from 表名 where 条件;
```

- 修改数据：

```sql
update 表名 set 列 = 值;
update 表名 set 列1 = 值1, 列2 = 值2;
update 表名 set 列1 = 值1, 列2 = 值2 where 条件;
```

- 查询数据：

```sql
select * from 表名; -- 查询所有数据
select 列名1, 列名2 from 表名;
select 列名1, 列名2 from 表名 where 条件;
```

## Python操作MySQL

> 用Python代码连接MySQL并发送指令

工具包：

- PyMySQL: `pip install pymysql`
