#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('****************************************')


# In[2]:


print("Gigi's cafe")


# In[3]:


print("Number of coffees bought?")


# In[4]:


coffees = int(input("Enter the number of coffees:"))


# In[5]:


print("Number of Cookies bought?")


# In[6]:


cookies = int(input("Enter the number of cookies:"))


# In[7]:


print('**************************************** \n \n****************************************')


# In[10]:


print("Gigi's cafe receipt")


# In[9]:


coffee_price = 3.99


# In[25]:


total_coffee = (coffees * coffee_price)


# In[69]:


cookie_price = 2


# In[68]:


total_cookie = (cookies * cookie_price)


# In[12]:


total_cost_before_tax = (coffees * coffee_price) + (cookies * cookie_price)


# In[16]:


sales_tax = total_cost_before_tax * 0.06


# In[17]:


total_cost_after_tax = total_cost_before_tax + sales_tax


# In[47]:


print(f"{coffees} Coffees at ${coffee_price} each: $ {total_coffee}")


# In[70]:


print(f"{cookies} Cookies at ${cookie_price} each: $ {total_cookie}")


# In[76]:


print(f"6% tax: ${sales_tax}")


# In[78]:


print("------")


# In[80]:


print(f"Total: ${total_cost_after_tax}")


# In[81]:


print('****************************************')


# In[ ]:




