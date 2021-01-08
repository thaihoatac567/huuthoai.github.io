#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

col_names=['Bệnh nhân','Tuổi','Địa điểm','Tình trạng','Quốc tịch','Tháng']
#load dataset
#table
df= pd.read_csv("C://Users/Admin/Desktop/AI/DOAN/covid.csv", header=0,names=col_names)



month = df['Tháng']
pop = df['Bệnh nhân']
plt.figure(figsize=(15,10))
plt.plot(month,pop)
plt.title("Increasing number of infected people in Vietnam",size=20)
plt.xlabel('Month',size=13)
plt.ylabel('Infected People',size=13)
plt.show()


# In[52]:


import pandas as pd
import datetime
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
col_names=['Bệnh nhân','Tuổi','Địa điểm','Tình trạng','Quốc tịch','Tháng']
#load dataset
#table
df= pd.read_csv("C://Users/Admin/Desktop/AI/DOAN/covid.csv", header=0,names=col_names)
sns.set_color_codes()
sns.distplot(df['Tuổi'], kde = False, bins = 20,color = "r")
plt.xlabel("Age", fontsize= 12)
plt.title("Histogram for Infected Age", fontsize= 15)


# In[53]:


import pandas as pd
import datetime
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
col_names=['Bệnh nhân','Tuổi','Địa điểm','Tình trạng','Quốc tịch','Tháng']
#load dataset
#table
df= pd.read_csv("C://Users/Admin/Desktop/AI/DOAN/covid.csv", header=0,names=col_names)


sns.barplot(x='Tình trạng', y='Tuổi', data=df)


# In[7]:


import pandas as pd
import datetime
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
col_names=['Bệnh nhân','Tuổi','Địa điểm','Tình trạng','Quốc tịch','Tháng']
#load dataset
#table
df= pd.read_csv("C://Users/Admin/Desktop/AI/DOAN/covid.csv", header=0,names=col_names)
plt.title("Tổng số lượng người nhiễm bệnh COVID-19 trong năm 2020",size=10)
df['Tháng'].value_counts().plot(kind='bar')
plt.xlabel("Tháng")
plt.ylabel("Số lượng")


# In[59]:


import pandas as pd
import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

col_names=['Bệnh nhân','Tuổi','Địa điểm','Tình trạng','Quốc tịch','Tháng']
#load dataset
#table
df= pd.read_csv("C://Users/Admin/Desktop/AI/DOAN/covid.csv", header=0,names=col_names)



plot_size = plt.rcParams["figure.figsize"] 
print(plot_size[0]) 
print(plot_size[1])
plot_size[0] = 15
plot_size[1] = 15
plt.title("TỈ LỆ NHIỄM BỆNH COVID NĂM 2020 (VIỆT NAM)",size=20)
plt.rcParams["figure.figsize"] = plot_size
df.Tháng.value_counts().plot(kind='pie',autopct='%1.1f%%', startangle=140)


# In[60]:


import pandas as pd
import datetime
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
col_names=['Bệnh nhân','Tuổi','Địa điểm','Tình trạng','Quốc tịch','Tháng']
#load dataset
#table
df= pd.read_csv("C://Users/Admin/Desktop/AI/DOAN/covid.csv", header=0,names=col_names)
ohno=['Khỏi', 'Đang điều trị', 'Tử vong','Chưa có thông tin'] 
x=df['Tình trạng'].value_counts()
cols=['#4C8BE2','#00e061','#fe073a','r'] 
exp = [0.2,0.02,0.02,0.1] 

x=plt.pie(x,
        labels=ohno, 
        textprops=dict(size=25,color='black'), 
        radius=3, 
        colors=cols, 
        autopct='%2.2f%%', 
        explode=exp, 
        shadow=True, 
        startangle=50) 
#plt.title("Tình trạng người nhiễm bệnh covid ở Việt Nam")


# In[62]:


#TAILIEU: http://taimuihongtphcm.vn/19-tinh-thanh-tren-ca-nuoc-ghi-nhan-co-truong-hop-nhiem-covid-19/


import pandas as pd


data = pd.read_csv("C://Users/Admin/Desktop/AI/DOAN/district.csv")
data.head() 
  
ac=data.iloc[:22,2].values 
re=data.iloc[:22,5].values 
de=data.iloc[:22,4].values 
co=data.iloc[:22,3].values 
x=list(data.iloc[:22,0])
  
plt.figure(figsize=(25,10)) 
ax=plt.axes()  
ax.set_facecolor('black') 
ax.grid(linewidth=0.4, color='#8f8f8f') 
  

   
ax.set_xlabel('\nTỉnh',size=25, 
              color='#4bb4f2') 
ax.set_ylabel('Số trường hợp ghi nhận\n',size=25, 
              color='#4bb4f2')    
ax.set_title('Trường hợp ghi nhận nhiễm covid ở các tỉnh thành tháng 3-2020\n', 
             size=30,color='#28a9ff') 
plt.yticks(size='15')
plt.xticks(size='10')

plt.bar(x,co,label='re') 
plt.bar(x,re,label='re',color='green') 
plt.bar(x,de,label='re',color='red') 
  
for i,j in zip(x,ac): 
    ax.annotate(str(int(j)), 
                xy=(i,j+3), 
                color='white', 
                size='15') 
  
plt.legend(['Dương Tính','Đã Điều Trị','Âm Tính'], 
           fontsize=20)


# In[69]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
  

data = pd.read_csv("C://Users/Admin/Desktop/AI/DOAN/date.csv") 

Y = data['Daily Confirmed'].values  
X = data['Date']  
  
plt.figure(figsize=(25,8)) 
  
ax = plt.axes() 
ax.grid(linewidth=0.4, color='#8f8f8f')  
  
ax.set_facecolor("black")  
ax.set_xlabel('\nDate',size=25,color='#4bb4f2') 
ax.set_ylabel('Confirm\n', 
              size=25,color='#4bb4f2') 
ax.set_title('Số ca theo ngày được ghi nhận trong tháng 9\n', 
             size=30,color='#28a9ff') 
ax.plot(X,Y, 
        color='#1F77B4', 
        marker='o', 
        linewidth=4, 
        markersize=15, 
        markeredgecolor='#035E9B')


# In[ ]:




