"""
@author Lucas
@date 2018/12/3 10:15

"""
import re


def cheackPhone(str):
    # pattern = r"^1[34578]\d{9}$"
    # result = re.match(pattern, str)
    pattern = r"1[34578]\d{9}"
    result = re.findall(pattern, str)
    return result


if __name__ == '__main__':
    # print(re.match("www", "Www.baidu.com", flags=re.I))
    # print(re.search("www", "baidu.wwW.com", flags=re.I))
    # print(re.findall("www", "baidu.wwW.com.www", flags=re.I))
    # print(re.search(".", "\nbaidu.wwW.com", flags=re.I))
    # print(re.search("[023456b]", "1baidu.wwW.com", flags=re.I))
    # print(re.search("[0-9]", "1baidu.wwW.com", flags=re.I))
    # print(re.search("[a-z]", "baidu.wwW.com", flags=re.I))
    # print(re.search(" ", " baidu.wwW.com", flags=re.I))
    # print(re.search("_", "_baidu.wwW.com", flags=re.I))
    # print(re.search("[^b]", "baidu.wwW.com", flags=re.I))
    # print(re.findall("\d", "baidu9.wwW.com", flags=re.I))
    # print(re.search("com$", "baidu.wwW.com", flags=re.I))
    # print(re.search("com$", "baidu.wwW.com.com", flags=re.I))
    # print(re.findall("^baidu", "1baidu.wwW.com\nbaidu", flags=re.M))
    # print(re.search(r"er\b", "erveraer", flags=re.I))
    # print(re.search(r"er\B", "asdvasdaer", flags=re.I))
    # print(re.search(r"(erver)", "erveraer", flags=re.I))
    # print(re.findall(r"a*", "asdasdasdaa", flags=re.I))
    # print(re.findall(r"a?", "asdasdasdaa", flags=re.I))
    # print(re.findall(r"a+", "asdasdasdaa", flags=re.I))
    # print(re.findall(r"((s|S)ock)", "sock-Sock", flags=re.I))
    # print(re.findall(r"x{4}", "xxxxxx", flags=re.I))
    # print(re.findall("(word)", "asdwordasd", flags=re.I))
    #
    str = "Lucas is a good man \nLucas is        a good man Lucas is a good man"
    print(re.findall(r"Lucas.*?man", str))
    print(re.findall(r"Lucas.*man", str))
    print(re.findall(r"^Lucas is", str, re.M))

    # print(cheackPhone("18201712787"))
    print(cheackPhone("asdadas18201712787asdasdff13515756066asd"))
