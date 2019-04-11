import cx_Oracle
# python3.5


def connectOracle(account, sql):
    conn = cx_Oracle.connect(account)
    c = conn.cursor()
    c.execute(sql)
    result1 = c.fetchall()
    # 采用集合存储
    result2 = set()
    for i in range(len(result1)):
        # 不是空值就添加到集合中
        if result1[i][0] is not None:
            result2.add((result1[i][0]))
    return result2


# 遍历输出set1中存在但是在set2中不存在的值
def compare(set1, set2):
    # 集合的交，集合的减
    result = set1 - (set1 & set2)
    return result


if __name__ == '__main__':
    account = 'swzbkstg/swzbkstg123@10.18.2.20:1521/soneorcl'
    sql1 = "select MMSI from swz_vessel_table"
    sql2 = "select VESSEL_MMSI from zhxx.vm_ship_dynamic_2@SWZ_XE "
    result1 = connectOracle(account, sql1)
    result2 = connectOracle(account, sql2)
    # print(result2)
    # print(len(result2))
    # print(result1)
    # print(len(result1))
    finalResult = compare(result1, result2)
    for i in finalResult:
        print(i)

    print(len(finalResult))
