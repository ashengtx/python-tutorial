class Employee(object) :
    """所有employee的基类"""

    empCount = 0 # 类变量(class variable)，被所有实例共享，可以从类的内部和外部通过Employee.empCount访问，不如实例变量常用

    """
    类内部定义的函数叫做类的方法（Method）
    """
    def __init__(self, name, salary):
        """
        实例化一个类的时候会被调用的初始化方法
        """
        self.name = name # 实例变量（instance vairable），定义在方法内，只属于这个实例
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)


# 类的实例化，实例叫做这个类的对象
# This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

# 对象属性用点操作符访问'.'
emp1.displayEmployee()
emp2.displayEmployee()
# 类变量的访问
print("Total Employee %d" % Employee.empCount)

# 对象属性可以随时添加，删除，修改
emp1.age = 27  # Add an 'age' attribute.
print(emp1.age)
emp1.age = 28  # Modify 'age' attribute.
print(emp1.age)
del emp1.age  # Delete 'age' attribute.

# print(emp1.age) # 这个会报错，因为已经删除属性了

name = 'James'
age = 33
print("%s is %d years old." % (name, age))
