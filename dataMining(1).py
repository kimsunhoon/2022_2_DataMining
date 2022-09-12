#!/usr/bin/env python
# coding: utf-8

# <h1>Datamining</h1>
# <h3>강의 1. Numpy 함수 기초 학습</h3>
# <ol>
#     <li>numpy 함수 불러오기</li>
#     <li>rank,shape,array</li>
#     <li>arange</li>
#     <li>zeros,ones</li>
#     <li>index</li>
#     <li>full,eye,range</li>
#     <li>numpy 사칙연산</li>
#     <li>행렬의 곱</li>
#     <li>broadcast,sum,prod</li>
#     <li>reshape</li>
#     <li>numpy 다차원 배열에서 요소의 최대 최소값 반환</li>
#     <li>numpy 슬라이싱</li>
# </ol>

# 1

# In[19]:


#numpy를 np이름으로 불러 들인다.
import numpy as np 
# np.array()는 python list를 인수로 받아서 numpy라이브러리 형태의 배열로 반환한다. 
Y1=np.array([1, 2, 3, 4])
print(Y1)


# 2

# In[20]:


import numpy as np
list1 = [1, 2, 3, 4]
a = np.array(list1)
print(a.shape) # (4, )


# In[21]:


b = np.array([[1,2,3],[4,5,6]])
print("b=\n",b)
print(b.shape) # (2, 3)
print(b[0,0])  # 1 


# In[22]:


V1=np.array([1, 2, 3, 4])   
print(V1)


# 3

# In[23]:


V1=np.arange(1, 10, 2)**2  
print(V1)


# In[24]:


V2=np.arange(3, 10, 2, dtype=int)  
V3=np.arange(3.5, 10.5, 2, dtype=float)
print(V2)
print(V3)


# 4

# In[25]:


import numpy as np
a = np.zeros((2,2))
print(a)


# In[26]:


a = np.ones((2,3))
print(a)


# 5

# In[30]:


lst1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
a = np.array(lst1)
a[[1,2]]


# In[31]:


lst1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
a = np.array(lst1)
a[[-1,-2]]


# In[32]:


lst1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
a = np.array(lst1)
a[[1,2],[-1,-2]]


# 6

# In[34]:


a=np.full((2,3),5)
print(a)


# In[36]:


a=np.eye(3)
print(a)


# In[37]:


a=np.array(range(20)).reshape((4,5))
print(a)


# 7

# In[42]:


ex1=np.array([1,2,3])
ex2=np.array([4,5,6])
result1=np.add(ex1,ex2)
print(result1)


# In[46]:


result2=np.subtract(ex1,ex2)
print(result2)


# In[49]:


result3=np.multiply(ex1,ex2)
print(result3)


# In[50]:


result4=np.divide(ex1,ex2)
print(result4)


# 8

# In[52]:


ex_lst1=[[1,2,3],
         [3,4,5]]
ex_lst2=[[5,6],
         [7,8],
         [9,10]]
a1=np.array(ex_lst1)
b1=np.array(ex_lst2)

c1=np.dot(a1,b1)
print(c1)


# 9

# <h5>numpy broadcast</h5>
# <p>행렬 사칙연산은 기본적으로 두 개의 행렬 크기가 같아야만 수행 가능. numpy 에서는 크기가 다른 두 행렬 간에도 사칙 연산 가능하게 하는 것이 broad cast 기능. 차원이 작은 행렬을 큰 행렬에 행 단위로 반복해서 크기를 맞춘 후에 연산
# <br> broadcast 수행 시 column 위주로 복사하여 큰 행렬에 사이즈를 맞춘다.
# <br> broadcast 수행 후 행렬의 크기는 입력 행렬의 행의 최대 크기, 열의 최대 크기로 결정된다.</p>

# In[53]:


ex3=[[0],[10],[20],[30]]
ex4=[[0,1,2]]
result5=np.add(ex3,ex4)
print(result5)


# In[57]:


ex5=np.array([[1,2],[3,4]])
#각 배열 요소들을 더하는 sum() 함수
ex6=np.sum(ex5)
print(ex6)


# In[59]:


#sum() 함수에 axis를 지정가능. axis=1 이면 row끼리 더하고 
#axis=0이면 column끼리 더한다.
s=np.sum(ex5,axis=0)
print(s)
s=np.sum(ex5,axis=1)
print(s)
s=np.prod(ex5)
print(s)


# 10

# <p>np.reshape(행렬수,행,열,order='C'or'F')
# <br>order='C' : 값을 row부터 채움(기본값,생략가능)
# <br>order='F' : 값을 column부터 채움</p>

# In[66]:


y1=np.arange(12)
print(y1)

#2차원의 변환
y2=y1.reshape(2,3,2,order='C')
print(y2)


# In[68]:


y1=np.arange(12)
print(y1)
y2=y1.reshape(3,2,2,order='F')
print(y2)


# 11

# In[74]:


y3=np.arange(3.5,10.5,2, dtype=float)
print(y3)
print(np.amax(y3))


# In[78]:


y6=np.arange(1,5)
y7=y6.reshape(2,2)
print(y6)
print(y7)
print(np.amin(y7))


# 12

# In[80]:


lst= [[1,2,3],
      [4,5,6],
      [7,8,9]]
arr = np.array(lst)
a = arr[0:1,0:3]
print(a)


# In[81]:


a=arr[0:2,0:2]
print(a)


# In[82]:


a=arr[2:,1:]
print(a)


# In[83]:


a=arr[1:,1:]
print(a)

