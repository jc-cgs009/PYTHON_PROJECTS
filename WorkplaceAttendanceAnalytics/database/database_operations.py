from database.database_connect import connect_database


class DatabaseOperations:
    def read_database(self, query, database_name=None):
        """
        This method is used to fetch the data from database.
        :param query: 'show databases;'/'select * from table_name;'/....../..../
        :param database_name: You need to specify database name when it required otherwise no need to specify.
        :return: It returns list of data.
        """
        con_obj = connect_database(database_name)
        cur_obj = con_obj.cursor()
        try:
            cur_obj.execute(query)
        except:
            con_obj.rollback()
            print('read_database error!')
        else:
            return list(cur_obj)
        finally:
            cur_obj.close()
            con_obj.close()

    def create_database(self, database_name):
        """
        This method is used to create database.
        :param database_name: You need to specify database name that you want to create. ex: student/ employee/ ..
        :return: None.
        """
        con_obj = connect_database()
        cur_obj = con_obj.cursor()
        query = f"create database {database_name}"
        try:
            cur_obj.execute(query)
        except:
            con_obj.rollback()
            print('create_database error!')
        finally:
            cur_obj.close()
            con_obj.close()

    def create_table(self, database_name, table_name, *column_datatype_constraints):
        """
        This method is used to create table in a specified database.
        :param database_name: You need to specify database name where you want to create your table. ex: student
        :param table_name: You need to specify table name that you want to create. ex: student_details
        :param column_datatype_constraints: You need to specify n number of column name with datatype and constraints.
        ex: create_table('student',
                        'student_details',
                        'column1 datatype constraints','column2 datatype constraints','column3 datatype constraints')

                        (or)

        columns = ('column1 datatype constraints','column2 datatype constraints','column3 datatype constraints')

        create_table('student', 'student_details', *columns)

        :return: None.
        """
        con_obj = connect_database(database_name)
        cur_obj = con_obj.cursor()
        column_definitions = ", ".join(column_datatype_constraints)
        query = f"create table {table_name}({column_definitions});"
        try:
            cur_obj.execute(query)
        except:
            con_obj.rollback()
            print('create_table error!')
        else:
            con_obj.commit()
        finally:
            cur_obj.close()
            con_obj.close()

    def insert_into_table(self, database_name, table_name, column_names, values):
        """
        This method is used to insert a single record in a particular table.
        :param database_name: You need to specify database name where your table locates. ex: student
        :param table_name: You need to specify table name where you want to insert record. ex: student_details
        :param column_names: ex: ('student_id', 'student_name', 'branch')
        :param values: ex: (123, 'xyz', 'cse')
        :return: None
        """
        con_obj = connect_database(database_name)
        cur_obj = con_obj.cursor()
        format_specifier = ', '.join(['%s' for i in column_names])
        column_names = ', '.join([name for name in column_names])
        query = f"insert into {table_name}({column_names}) values ({format_specifier});"
        try:
            cur_obj.execute(query, values)
        except:
            con_obj.rollback()
            print("insert_into_table error!")
        else:
            con_obj.commit()
        finally:
            cur_obj.close()
            con_obj.close()

    def insert_many_into_table(self, database_name, table_name, column_names, values):
        """
        This method is used to insert a multiple record in a particular table.
        :param database_name: You need to specify database name where your table locates. ex: student
        :param table_name: You need to specify table name where you want to insert record. ex: student_details
        :param column_names: ex: ('student_id', 'student_name', 'branch')
        :param values: ex: [(123, 'xyz', 'cse'),(124, 'abc','eee'),(),(),...,()]
        :return: None
        """
        con_obj = connect_database(database_name)
        cur_obj = con_obj.cursor()
        format_specifier = ', '.join(['%s' for i in column_names])
        column_names = ', '.join([name for name in column_names])
        query = f"insert into {table_name}({column_names}) values ({format_specifier});"
        try:
            cur_obj.executemany(query, values)
        except:
            con_obj.rollback()
            print("insert_many_into_table error!")
        else:
            con_obj.commit()
        finally:
            cur_obj.close()
            con_obj.close()

    def add_column_to_table(self, database_name, table_name, column_name_with_datatype_constraints, default=None):
        """
        This method is used to add new column to table.
        :param database_name: You need to specify database name where your table locates. ex: student
        :param table_name: You need to specify table name where you want to insert new column. ex: student_details
        :param column_name_with_datatype_constraints: You need to specify new column name with datatype and
         constraints ('column1 datatype constraints'). ex: 'percentage varchar(3) not null'
        :param default: If you want to add new column with default value then you can use this parameter otherwise don't
        pass value to default parameter.
        ex: default = 000
        :return: None
        """
        con_obj = connect_database(database_name)
        cur_obj = con_obj.cursor()
        if default:
            query = f"alter table {table_name} add {column_name_with_datatype_constraints} default '{default}';"
        else:
            query = f"alter table {table_name} add {column_name_with_datatype_constraints};"
        try:
            cur_obj.execute(query)
        except:
            con_obj.rollback()
            print("add_or_delete_column_in_table error!")
        else:
            con_obj.commit()
        finally:
            cur_obj.close()
            con_obj.close()

    def delete_column_from_table(self, database_name, table_name, column_name):
        """
        This method is used to delete specified column from table.
        :param database_name: You need to specify database name where your table locates. ex: student
        :param table_name: You need to specify table name where you want to delete column. ex: student_details
        :param column_name: You ex: percentage
        :return: None
        """
        con_obj = connect_database(database_name)
        cur_obj = con_obj.cursor()
        query = f"alter table {table_name} drop column {column_name};"
        try:
            cur_obj.execute(query)
        except:
            con_obj.rollback()
            print("delete_column_in_table error!")
        else:
            con_obj.commit()
        finally:
            cur_obj.close()
            con_obj.close()

    def update_record_in_table(self, database_name, update_query):
        """
        This method is used to table record.
        :param database_name: You need to specify database name where your table locates. ex: student
        :param update_query: You need to write your update query.

        ---> update_query : "update table_name set column_name='value' where <filter condition>;"

        :return: None.
        """
        con_obj = connect_database(database_name)
        cur_obj = con_obj.cursor()
        try:
            cur_obj.execute(update_query)
        except:
            con_obj.rollback()
            print("update_record_in_table error!")
        else:
            con_obj.commit()
        finally:
            cur_obj.close()
            con_obj.close()

    def delete_record_in_table(self, database_name, delete_query):
        """
        This method is used to delete record from table.
        :param database_name: You need to specify database name where your table locates. ex: student
        :param delete_query: You need to write your delete query.

        ---> delete_query : "delete from table_name where <filter condition>;"

        :return: None.
        """
        con_obj = connect_database(database_name)
        cur_obj = con_obj.cursor()
        try:
            cur_obj.execute(delete_query)
        except:
            con_obj.rollback()
            print("delete_record_in_table error!")
        else:
            con_obj.commit()
        finally:
            cur_obj.close()
            con_obj.close()

    def delete_table_from_database(self, database_name, table_name):
        """
        This method is used to delete table from database.
        :param database_name: You need to specify database name where your table locates. ex: student
        :param table_name: You need to specify table name that you want to delete. ex: student_details
        :return: None.
        """
        con_obj = connect_database(database_name)
        cur_obj = con_obj.cursor()
        query = f"drop table {table_name}"
        try:
            cur_obj.execute(query)
        except:
            con_obj.rollback()
            print("delete_table_from_database error!")
        else:
            con_obj.commit()
        finally:
            cur_obj.close()
            con_obj.close()

    def delete_database(self, database_name):
        """
        This method is used to delete database.
        :param database_name: You need to specify database name that you want to delete. ex: student
        :return: None
        """
        con_obj = connect_database()
        cur_obj = con_obj.cursor()
        query = f"drop database {database_name}"
        try:
            cur_obj.execute(query)
        except:
            con_obj.rollback()
            print("delete_database error")
        else:
            con_obj.commit()
        finally:
            cur_obj.close()
            con_obj.close()


if __name__ == "__main__":
    db = DatabaseOperations()
    # db.create_database('msys')
    # columns = ['Date date not null', 'Emp_id varchar(10) not null', 'Emp_name varchar(100) not null',
    #            'Department varchar(100) not null', 'Designation varchar(100) not null', 'Location varchar(100) not null',
    #            'Reporting_manager varchar(100) not null', 'Year varchar(15) not null', 'Month varchar(15) not null',
    #            'Day varchar(15) not null']
    # db.create_table('msys', 'employee_data', *columns)
    # db.delete_record_in_table('msys', "delete from employee_data where Date='2023-08-01';")
    # db.add_column_to_table('msys', 'employee_data', 'Day varchar(10) not null')
    # db.delete_column_from_table('msys', 'employee_data', 'day')
    # db.delete_table_from_database('msys', 'employee_data')
