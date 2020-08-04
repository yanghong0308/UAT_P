import win32gui, win32api, win32con
import  win32com.client
import pythoncom


def gaozhibaocun(): ###稿纸保存
    #pythoncom.CoInitialize()  # 声明 doc 之前要加入的代码
    word = win32com.client.Dispatch('Word.application')

    word.Visible = 0  # 后台运行
    word.DisplayAlerts = 0  # 不显示，不警告

    docume = word.Documents.count#获取已经打开的文档的数目，
    print(docume)
    doc = word.Documents[0]  #想要获取第一个文档的句柄，我们使用Documents集合


    # 在文档开头添加内容
    myRange1 = doc.Range(0, 0)
    myRange1.InsertBefore('caoni ge  Dj')

    doc.Save()  # 保存
    doc.Close()  # 关闭 word 文档
    word.Quit()#控制Word一定要注意退出

    #pythoncom.CoUninitialize()# 关闭 doc 之后加入的代码
gaozhibaocun()

#http://www.bathome.net/thread-8155-1-5.html