#!/usr/bin/env python
# coding: utf-8

# <h1>Datamining</h1>
# <h3>강의 2. Numpy 함수 기초 학습</h3>
# <ol>
#     <li>numpy 정수 인덱싱</li>
#     <li>numpy boolean indexing</li>
#     <li>논리연산 응용</li>
#     <li>조건에 따라 배열의 요소들 구하기</li>
#     <li>조건에 따라 배열의 요소들 변경</li>
#     <li>numpy 주요 함수</li>
# </ol>

# 1

# In[1]:


import numpy as np
lst = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]]
a=np.array(lst)
#a[0,1],a[2,3]의 배열요소를 갖는다.
s=a[[0,2],[1,3]]
print(s)


# 2

# In[4]:


lst=[[1,2,3],
    [4,5,6],
    [7,8,9]]
a=np.array(lst)
bool_indexing_array=np.array([
    [False,True,False],
    [True,False,True],
    [False,True,False]])
n=a[bool_indexing_array]
print(n)


# In[5]:


a=np.array(lst)
# 배열 a에 대해 짝수면 True, 홀수면 False
bool_indexing = (a%2==0)
print(bool_indexing)


# In[8]:


#boolean indexing 사용하여 True 요소만 출력
print(a[bool_indexing])
print(a[a%2==0])


# In[58]:


import numpy as np
names = np.array(['BTS', 'SongGaIn','HongJo','ChoYongPil','GirlGroup'])
number = np.array(['1', '2', '3', '4'])


# In[59]:


# 아래에서 사용되는 np.random.randn() 함수는 기대값이 0이고, 표준편차가 1인 가우시안 정규 분포를 따르는 난수를 발생시키는 함수이다.
# 이 외에도 0~1의 난수를 발생시키는 np.random.rand() 함수도 존재한다.
data = np.random.randn(4,5)
data


# In[60]:


# 요소가 BTS인 항목에 대한 mask 생성
names_BTS_mask = (names == 'BTS')
names_SongGaIn_mask = (names == 'SongGaIn')
number_4_mask = (number == '4')


# In[61]:


# column요소가 4인 항목에 대한 mask 생성
data[number_4_mask,:]


# In[62]:


# row요소가 BTS인 항목에 대한 mask 생성
data[:, names_BTS_mask]


# 3

# In[63]:


# 논리 연산을 응용하여, 요소가 BTS 또는 GirlGroup인 column의 데이터만 출력하기
data[:,(names == 'BTS') | (names == 'GirlGroup')]


# In[68]:


# number == '4＇이고 names == 'BTS’에 해당하는 요소들을 찾아낸다. 
data[(number == '4'),(names == 'BTS')]


# In[69]:


# number == ‘3’ 에 해당하는 요소들을 찾아낸다. 
data[(number=='3'), :]


# 4

# In[50]:


#위에서 생성한 data에서 모든  row 중에서 0번 column(열)의 값이 0보다 작은 row(행)을 구한다.
data[data[:, 0]<0, : ] 


# In[51]:


# 0번째 열(column)의 값이 0보다 작은 행(row)의 1,2번 열 값
data[data[:,0]<0, 1:3]


# 5

# In[70]:


data[data[:,0]<0,1:3]=1.0
data[data[:,0]<0,:]


# In[71]:


print(data[:,1])
data[:,1]<1

