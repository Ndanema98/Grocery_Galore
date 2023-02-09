# Milestone project 3
# Grocery Galore Survey Data Analysis

["Grocery Galore Survey Data Analysis"](https://grocerygalore.herokuapp.com/) is a programme designed to manage the data of a fruit store using a ["Google spreadsheet"](https://docs.google.com/spreadsheets/d/1RSS3h2Ib16TlZVCldceVdtXsgKBAxrh0M2AchVnSSQQ/edit?usp=sharing).

This programme was built for a company which sells fruits. It will allow the user to input the daily sales data and the daily waste data of a specific fruit and add it to a google spreadsheet. The programme will also calculate the new stock levels of the fruits and calculate restock recommendations. Different validation methods are also present throughtout this programme to check whether the data being inputted is valid.

Spreadsheets are a great way to store data for companies because it allows them to organise and perform calculations on the data. This enables them to make important predictions and decisions, which on a whole will benefit them. 

This programme was built using knowledge gained from Python modules, for the purpose of completing my third Milestone Project for the Code Institute's full stack developer course. This programme is easy to navigate and easy to read, with a clear goal and aim. 

 # User Experience/User Interface (UX/UI)

 - ## User Stories
   ### First Time User Goals
   As a first time user I want: 
   - To be able to understand the aim of the programme and how it works. 
   - To be able to use the programme in relation to my business. 
   - The programme to function correctly. 

   ### Frequent User Goals
   As a frequent user I want:
   - The programme to be fluent and easy to use. 
   - The programme to positively affect my business.
   - The programme to function correctly. 

   ### Developer's Goals.
   As the developer I want:
   - To provide a useful programme that fufills it's aims. 
   - To have the programme run smoothly without crashing. 
   
 
 - ## Design 
   ### Data Model 
    The data model for this code would be a Google Sheets document called "Grocery_Galore" with four worksheets: "Dailysales", "Dailywastechart", "Stocklevels", and "Dailyrestock". The worksheets contain data on daily sales, daily waste, stock levels, and daily restock levels for 7 different types of grocery items: Apples, Oranges, Bananas, Avocado, Pears, Grapes, Mangos. The data is updated through user inputs and calculations done in the code.

   ### Flowchart
   ![A screenshot of my flowchart](/assets/flowchart.jpeg)


 # Features
 - ## Input Sales Data 
   ![A screenshot of the input for the sales data.](/assets/sales_entry.png)


   - This feature allows the user to input data that they have for the weekly sales of the different fruits. 


 - ## Validate Sales Data
   ![A screenshot of my validation for the input of sales data.](/assets/sales_validate.png)


   - This feature allows the code to validate the data that has been inputted for the weekly sales. The validation makes sure that only seven numerical entries are inputed.
  

 - ## Update Sales Worksheet 
   ![A screenshot of the input of sales data in to the worksheet.](/assets/sales_update.png)


   - This feature allows the code to update the sales worksheet with the inputted sales data.


 - ## Input Waste Data
   ![A screenshot of the input for the waste data.](/assets/waste_entry.png)


   - This feature allows the user to input data that they have for the weekly waste of the different fruits. 


 - ## Validate Waste Data
   ![A screenshot of my validation for the input of waste data.](/assets/waste_validate.png)


   - This feature allows the code to validate the data that has been inputted for the weekly waste figures. The validation makes sure that only seven numerical entries are inputed.

   
 - ## Update Waste Worksheet 
   ![A screenshot of the input of the waste data in to the worksheet.](/assets/waste_validate.png)


   - This feature allows the code to update the waste worksheet with the inputted waste data.

  
 - ## Calculate Restock Ammount 
   ![A screenshot of the restock being calculated and printed.](/assets/restock_calculate.png)


   - This feature allows the code to calculate a suitable restock ammount and then print that ammount to the terminal. Thhis restock aamount is found by calculating the average over seven days and then multiplying that figure by 110%.
   
   
 - ## Update Restock Worksheet 
   ![A screenshot of the input of the Restock data in to the worksheet.](/assets/restock_update.png)


   - This feature allows the code to update the restock worksheet with the calculated restock data.

 - ## Calculate New Stock Ammount 
   ![A screenshot of the new stock ammount being calculated and printed.](/assets/newstock_calculate.png)


   - This feature allows the code to calculate a the new stock level ammount by subtracting the sales and waste data from the stock ammount from the day before and then adding the restock data. This ammount is then printed to the terminal. 
  
   
 - ## Update Stock Worksheet 
   ![A screenshot of the input of the new stock data in to the worksheet.](/assets/newstock_update.png)


   - This feature allows the code to update the stock level worksheet with the new stock data.
   
    
 # Testing 
 - ## Manual 
   - I have manually tested the code by doing the following: 
      - Passed the code through a Pep8 Validator. 
      - Given invalid inputs, to test the validation. 
      - Tested code in local terminal and the Code Institute Heroku terminal. 


   ![A screenshot of the testing done for less than 7 figures.](/assets/validation_lessthan7.png)


   - This test was done to make sure that no less than 7 values can be inputted. 


   ![A screenshot of the testing done for more than 7 figures.](/assets/validation_morethan7.png)


   - This test was done to make sure that no more than 7 values can be inputted. 


   ![A screenshot of the testing done for none numerical figures.](/assets/validation_nonenumerical.png)


   - This test was done to make sure that only numerical values were inputted.  


 - ## Validator 
   - ### Python
     - A ["Pep8 python checker"](https://pep8ci.herokuapp.com/#) from code institute was used to validate my code and no errors were returned. 
  
- ## Bugs 
   - ### Solved 
     - When trying to write the function to calculate the restock data, I had to add the sales column to the waste column. When trying to do this it didnt do the addition of the two columns properly as they were strings. Therefore I had to convert the columns from strings into integers before the addition was done. 

   - ### Unsolved
   No remaining bugs left in the code.   
     
 # Technologies Used 
   - Git 
     - Allowed me to add commit and push my code to github for version control. 
   - Gitpod 
     - The programme used to code my website.
   - Github 
     - Allowed me to store my repository and files pushed from Gitpod. 
   - Chrome developer tools 
     - Allowed me to troubleshoot and edit my code.
   
 # Deployment
  - This code was deployed using Code Institute's mock terminal for Heroku. 

  - ## Steps for deployment:
   1. In the top right corner of the page click on the fork button. 
   2. The next page will show a forked version of my project.
   3. Create a new Heroku app.
   4. Set the buildbacks to Python and NodeJS in that order.
   5. Link the Heroku app to the repository. 
   6. Click on deploy. 

 # Credits
 ## Acknowledgement 
    - The online tutors that Code Institute provides. 
    - Code institute for the deployment terminal. 
    - My mentor Ben Kav for helping me when I was stuck. 
    - Everybody on slack, for their advice. 
