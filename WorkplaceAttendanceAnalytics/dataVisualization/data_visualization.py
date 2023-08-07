from matplotlib import pyplot as plt
from database.database_operations import DatabaseOperations


class VisualizeData:
    def __init__(self):
        self.db = DatabaseOperations()

    def visualize_location_day_wise_data(self, date):
        # get location wise data
        get_loc_wise_data_query = f"""select Location, count(*)
                                     from employee_data
                                     where Date='{date}'
                                     group by Location;"""
        loc_wise_data = self.db.read_database(get_loc_wise_data_query, 'msys')
        locations, count_loc = zip(*loc_wise_data)
        index_of_max_loc = count_loc.index(max(count_loc))
        point_out_max_loc = [0]*len(locations)
        point_out_max_loc[index_of_max_loc] = 0.2

        plt.figure(figsize=[15, 5])
        plt.title("Location")
        plt.pie(count_loc, labels=locations, explode=point_out_max_loc,
                autopct="%.2f")
        plt.legend(loc="lower left", shadow=True, fontsize='8')
        plt.show()

    def visualize_department_day_wise_data(self, date):
        # get Department wise data
        get_dept_wise_data_query = f"""select Department, count(*)
                                     from employee_data
                                     where Date='{date}'
                                     group by Department;"""
        dept_wise_data = self.db.read_database(get_dept_wise_data_query, 'msys')
        departments, count_dept = zip(*dept_wise_data)
        highlight_index = count_dept.index(max(count_dept))
        main_color = '#007acc'
        highlight_color = '#ff7f00'

        plt.title("Department")
        plt.barh(departments, count_dept, color=main_color)

        plt.barh(departments[highlight_index], count_dept[highlight_index], color=highlight_color)

        f = {'family': 'Arial', "size":10, "color":"blue"}
        plt.xlabel("Number of Employee", fontdict=f)
        plt.ylabel("Department Name", fontdict=f)
        plt.show()

    def visualize_designation_day_wise_data(self, date):
        # get Designation wise data
        get_des_wise_data_query = f"""select Designation, count(*)
                                     from employee_data
                                     where Date='{date}'
                                     group by Designation;"""
        des_wise_data = self.db.read_database(get_des_wise_data_query, 'msys')
        designations, count_des = zip(*des_wise_data)
        highlight_index = count_des.index(max(count_des))
        main_color = '#ffa24c'
        highlight_color = '#007acc'

        plt.title("Designation")
        plt.barh(designations, count_des, color=main_color)

        plt.barh(designations[highlight_index], count_des[highlight_index], color=highlight_color)

        f = {'family': 'Arial', "size":10, "color":"blue"}
        plt.xlabel("Number of Employee", fontdict=f)
        plt.ylabel("Department Name", fontdict=f)
        plt.show()

    def visualize_reporting_day_wise_data(self, date):
        # get reporting wise data
        get_repo_wise_data_query = f"""select Reporting_manager, count(*)
                                     from employee_data
                                     where Date='{date}'
                                     group by Reporting_manager;"""
        repo_wise_data = self.db.read_database(get_repo_wise_data_query, 'msys')
        reporting, count_repo = zip(*repo_wise_data)
        highlight_index = count_repo.index(max(count_repo))
        main_color = '#1c9099'
        highlight_color = '#fc8d59'

        plt.title("Designation")
        plt.barh(reporting, count_repo, color=main_color)

        plt.barh(reporting[highlight_index], count_repo[highlight_index], color=highlight_color)

        f = {'family': 'Arial', "size": 10, "color": "blue"}
        plt.xlabel("Number of Employee", fontdict=f)
        plt.ylabel("Department Name", fontdict=f)
        plt.show()


if __name__ == "__main__":
    dv = VisualizeData()
    dv.visualize_reporting_day_wise_data('2023-08-02')
