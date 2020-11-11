#%%
root=[1,2,3]
root.insert(3,3)



# %%
class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj 
        self.leftChild=None
        self.rightChild=None 

    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t 

    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t 
        
    def getRightChild(self):
        return self.rightChild 
    
    def getLeftChild(self):
        return self.leftChild 

    def setRootVal(self,obj):
        self.key=obj

    def getRootVal(self):
        return self.key 


r = BinaryTree('a')


# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd 


# %%
Stock=pd.read_excel("G:/Valuation/上市公司.xlsx")
StockList=Stock["股票代码"].to_list()
report=pd.DataFrame()


#%%
for i in range(len(StockList)):
    try:
        PreUrl="http://stock.finance.sina.com.cn/stock/go.php/vReport_List/kind/search/index.phtml?t1=2&symbol="
        StockCode=StockList[i][0:6]
        r=pd.DataFrame()
        for j in range(10):  # 页数
            try:
                res = requests.get(PreUrl+StockCode+"&p="+str(j)) #模拟get请求获取链接返回的内容
                # res.encoding = 'utf-8'#设置编码格式为utf-8
                soup = BeautifulSoup(res.text, 'html.parser')#前面已经介绍将html文档格式化为一个树形结构，每个节点都是一个对python对象，方便获取节点内容        
    
                table=soup.select(".main")[0].find_all("table")[0] # 解析为上下两个表，上表为研报数据，下表为页码
                trList=table.find_all("tr")  # 解析为每行记录的列表

                href=[]
                title=[]
                date=[]
                company=[]
                author=[]

                for i in range(2,len(trList)):  #前两行为表头
                    tr=trList[i]
                    href.append(tr.find("a")["href"])
                    title.append(tr.find("a")["title"])
                    tdList=tr.find_all("td")
                    # 第一个td是行号，
                    # 第二个td是文章标题和链接，
                    # 第三个td是类型，这里都是公司
                    # 第四个td是日期
                    # 第五个td是本页链接及研报公司名称
                    # 第六个td是作者
                    date.append(tdList[3].get_text())
                    company.append(tdList[4].find("span").get_text())
                    author.append(tdList[5].find("span").get_text())


                rp=pd.DataFrame({"href":href,"title":title,"date":date,"company":company,"author":author})
                rp["Stock"]=StockList[i]
                r=r.append(rp)
            except:
                pass
        report=report.append(r)
    except:
        pass 



# %%  BinarySearch
class BinarySearchTree:
    def __init__(self):
        self.root=None 
        self.size=0 
    
    def length(self):
        return self.size 
    
    def __len__(self):
        return self.size 
    
    def __iter__(self):
        return self.root.__iter__()


# %%
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
# %%
