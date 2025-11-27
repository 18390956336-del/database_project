# data-structure-a2
！！！不要随便修改代码！！！

所有功能（顺序与代码一致）：
  department:
    1, 添加一个department
    2, 查询这个department负责的project
    3, 员工数量
    4, 显示基本信息

  dependent:（一个员工只能有一个）
    1, 加一个dependent
    2, 输入员工ssn显示其对应的dependent

  employee:
    1, 加一个
    2, 设置此员工管理输入的dep
    3, 移除这个员工
    4，设置minit
    5, 设置salary
    6, 设置supervisor
    7, 显示基本信息
    8，显示此员工所有负责的project（在最下面）

  project:
    1, 加一个
    2, 所有负责这个project的dep
    3, 添加员工负责此项目（！！！此举会自动将员工所属的dep设置为负责此项目！！！）
    4, 所有负责这个project的员工
    5, 显示基本信息
    6, 设置此员工在这个项目上花的时间

tips: 运行setup_database即可创建新的数据库，另外文件里的test是用来调试的测试文件
    
  
  
更新1.0：
  1，修复了setup_database可能无法正常运行的bug
  2，为所有类型添加了remove和all（显示这个类型下的所有实例）
  3，美化了所有方法的output
  4，department的num_of_employee中去掉了print，改成了return。添加了managed_by（可以查看谁在管理这个dep）
  5，employee中添加了supervising（查看这个supervisor在监视那些employee）
  6，添加了employee_assists_project（不会自动设置其dep负责此项目），department_charge_project（单独设置一个dep负责一个project）


  
更行2.0：
  1，添加了location，功能：
    a. 加一个location
    b. 显示所有地址
    c. 显示在这个building下的所有project
    d. 显示在这个date下发生的所有project
    e. 移除
    f. 设置对应project发生的时间（所有pj_id是这个project的地址的date全部设置为此日期）
    g. 输入pj_id，输出其所有的location

  2，为project加入了type（harmful chemical, weather-related等多种类型）

  3，为project加入了contractor，并支持一键查询所有已外包项目(all_contracted_project)

  4，修改了部分project的输出（其它部分的输出未变）
    
