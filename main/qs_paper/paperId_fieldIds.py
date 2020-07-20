"""
# @author Lucas
# @date 2020/7/20 15:00
"""
import pymysql
import json


def connection():
    conn = pymysql.connect(host="202.120.36.29", port=13307, user="mobilenet", password="mobilenet",
                            database="am_paper", charset="utf8")
    curs = conn.cursor(cursor=pymysql.cursors.DictCursor)
    curs.execute("select paper_id, field_id from am_paper_field")
    result = curs.fetchall()
    paperId_fieldIds = {}
    fieldId_paperIds = {}
    for ele in result:
        paper_id = ele["paper_id"]
        field_id = ele["field_id"]
        # 统计paper及其所属的field，dict形式存储成txt，{"499999992": [2046656743, 2032156429, 2043523143, 2018782504]}
        if paper_id in paperId_fieldIds:
            paperId_fieldIds[paper_id].append(field_id)
        else:
            paperId_fieldIds[paper_id] = [field_id]
            print(paper_id)
        # 统计field及其包含的paper，dict形式存储成txt，{"2046656743": [499999992, 192518076, 257431162, 449153379]}
        if field_id in fieldId_paperIds:
            fieldId_paperIds[field_id].append(paper_id)
        else:
            fieldId_paperIds[field_id] = [paper_id]
            print(field_id)
    with open("paperId_fieldIds.txt", "w") as fd:
        fd.write(json.dumps(paperId_fieldIds))
    with open("fieldId_paperIds.txt", "w") as fd:
        fd.write(json.dumps(fieldId_paperIds))

    curs.close()
    conn.close()


if __name__ == '__main__':
    connection()




