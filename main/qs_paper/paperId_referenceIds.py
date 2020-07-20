"""
# @author Lucas
# @date 2020/7/20 13:56
"""
import pymysql
import json


def connection():
    conn = pymysql.connect(host="202.120.36.29", port=13307, user="mobilenet", password="mobilenet",
                            database="am_paper", charset="utf8")
    curs = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 统计paper及其引用的参考文献，dict形式存储成txt，{"41083641": [363456051, 215417760, 444792553, 201861237, 113881920]}
    curs.execute("select paper_id, reference_id from am_paper_reference")
    result = curs.fetchall()
    paperId_referenceIds = {}
    for ele in result:
        paper_id = ele["paper_id"]
        reference_id = ele["reference_id"]
        if paper_id in paperId_referenceIds:
            paperId_referenceIds[paper_id].append(reference_id)
        else:
            paperId_referenceIds[paper_id] = [reference_id]
            print(paper_id)
    with open("paperId_referenceIds.txt", "w") as fd:
        fd.write(json.dumps(paperId_referenceIds))

    curs.close()
    conn.close()


if __name__ == '__main__':
    connection()
