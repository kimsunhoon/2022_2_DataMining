#!/usr/bin/env python
# coding: utf-8

# <h1>Datamining</h1>
# <h3>강의 3. Numpy 함수 기초 학습 & Matplotlib</h3>
# <ol>
#     <li>Nditer 객체를 이용한 행렬 iterate</li>
#     <li>Matplotlib</li>
# </ol>

# 1

# In[1]:


import numpy as np


# In[3]:


a=np.array([[10,20,30,40],[50,60,70,80]])
it=np.nditer(a,flags=['f_index'])
while not it.finished:
    print("%d(%d)"%(it[0],it.index),end='')
    it.iternext()


# In[6]:


it=np.nditer(a,flags=['c_index'])
while not it.finished:
    print("%d(%d)"%(it[0],it.index),end='')
    it.iternext()


# In[8]:


it=np.nditer(a,flags=['multi_index'])
while not it.finished:
    print("%d%s"%(it[0],it.multi_index),end='')
    it.iternext()


# 2

# <h4>Matplotlib</h4>
# <p>Matplotlib를 이용하여 그래프 그리기, 데이터 시각화 가능
# <br>데이터의 분포, 머신러닝의 결과를 시각적으로 표시하여 이해와 해석을 용이하게 할 수 있다.</p>

# In[9]:


import matplotlib.pyplot as plt


# In[23]:


import numpy as np
import matplotlib.pyplot as plt
x1=np.arange(1.0, 6.5, 0.2, dtype=float)
#1부터 0.2 간격으로 6.5를 넘지않게 데이터를 생성하여 변수 x1에 할당
y1= np.sin(x1) 
#x1의 각원소에 numpy의 sin함수를 적용하여 결과를 y1에 할당

plt.plot(x1,y1) # x1,y1의 인수값에 따라 plot 메소드를 호출하여 그래프를 그린다
plt.show()   # 그래프를 출력


# In[24]:


import numpy as np
import matplotlib.pyplot as plt
x1=np.arange(1.0, 6.5, 0.2, dtype=float)
y1= np.sin(x1)
y2= np.cos(x1)
plt.plot(x1, y1, label="sin")  
plt.plot(x1, y2, linestyle="--", label="cos") #cos함수는 점선으로 

plt.xlabel("X-value") #X축 이름
plt.ylabel("Y-value") #Y축 이름
plt.title('SIN-COS Graph') # 제목
plt.legend() # 범례를 작성
plt.show()  # 그래프를 출력

