#!/usr/bin/env python
# coding: utf-8

# In[7]:


# !pip install selenium
# !pip install webdriver-manager


# In[102]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

# Function to safely find and extract text
def safe_find_text(wait, by, selector):
    try:
        element = wait.until(EC.presence_of_element_located((by, selector)))
        return element.text.strip()
    except TimeoutException:
        print(f"Element with selector {selector} not found after waiting.")
        return None

# Set up the WebDriver
driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

# Navigate to the initial page
driver.get('https://maharerait.mahaonline.gov.in/SearchList/Search')


# In[103]:


# Wait for the table to load
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody tr')))

# Find all rows in the table of agents
rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')

agents_info = []


for row in rows:
    # Get agent information from the main page
    agent_name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
#     print(agent_name)
    certificate_no = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
#     print(certificate_no)
    view_details_link = row.find_element(By.CSS_SELECTOR, '.grid-cell a')
    view_details_url = view_details_link.get_attribute('href')
#     print(view_details_url)

    # Open view link in a new tab
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(view_details_url)

    # Use the function to get additional information on the new page
    house_number_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualHouseNo"]) + div'
    house_number = safe_find_text(wait, By.CSS_SELECTOR, house_number_selector)
#     print(house_number)

    building_name_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualBuilding"]) + div'
    building_name = safe_find_text(wait, By.CSS_SELECTOR, building_name_selector)

    street_name_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualStreet"]) + div'
    street_name = safe_find_text(wait, By.CSS_SELECTOR, street_name_selector)

    locality_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualLocality"]) + div'
    locality_name = safe_find_text(wait, By.CSS_SELECTOR, locality_selector)

    landmark_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualLandmark"]) + div'
    landmark_name = safe_find_text(wait, By.CSS_SELECTOR, landmark_selector)

    landmark_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualLandmark"]) + div'
    landmark_name = safe_find_text(wait, By.CSS_SELECTOR, landmark_selector)

    state_ut_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualState"]) + div'
    state_ut_name = safe_find_text(wait, By.CSS_SELECTOR, state_ut_selector)

    division_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualDivisionValue"]) + div'
    division_name = safe_find_text(wait, By.CSS_SELECTOR, division_selector)

    district_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualDistrictValue"]) + div'
    district_name = safe_find_text(wait, By.CSS_SELECTOR, district_selector)

    taluka_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualTalukaValue"]) + div'
    taluka_name = safe_find_text(wait, By.CSS_SELECTOR, taluka_selector)

    village_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualVillageValue"]) + div'
    village_name = safe_find_text(wait, By.CSS_SELECTOR, village_selector)

    pin_code_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualPinCode"]) + div'
    pin_code = safe_find_text(wait, By.CSS_SELECTOR, pin_code_selector)

    office_number_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_IndivisualOfficeNo"]) + div'
    office_number = safe_find_text(wait, By.CSS_SELECTOR, office_number_selector)
#     print(office_number)
    website_url_selector = 'div.col-md-3.col-sm-3:has(> label[for="PersonalInfoModel_WebsiteURL"]) + div'
    website_url = safe_find_text(wait, By.CSS_SELECTOR, website_url_selector)
    

    
    
    
    agents_info.append({
        'Agent Name':agent_name,
        'Certificate No.':certificate_no,
        'House Number':house_number,
        'Building Name':building_name,
        "street Name":street_name,
        "landmark_Name":landmark_name,
        "State_ut Name":state_ut_name,
        "Division Name":division_name,
        "District Name":district_name,
        "Taluka Name":taluka_name,
        "Village Name":village_name,
        "Pincode":pin_code,
        "Office Number":office_number,
        "WebSite URl":website_url
               
        
    })
    
        # Close the current tab
    driver.close()

    # Switch back to the main tab
    driver.switch_to.window(driver.window_handles[0])


# Convert the list to a DataFrame
agents_df = pd.DataFrame(agents_info)


# Close the WebDriver
driver.quit()


# In[106]:


agents_df = pd.DataFrame(agents_info)


# In[107]:


agents_df


# In[109]:


agents_df.shape


# In[111]:


filepath = r'C:\Users\Aditya\Downloads\output_images\agents_info2.csv'
agents_df.to_csv(filepath) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




