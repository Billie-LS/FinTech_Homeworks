# **Columbia University Engineering, New York FinTech BootCamp** 
# **August 2022 Cohort**
## *Module 3, Challenge*

This is a financial analysis application. This analysis utilizes a web-based interactive development environment (IDE) interface to run a data processing application which retrospectively examines the arbitrage trade opportunities for Bitcoin using bitstamp and coinbase exchanges over a three month period in 2018.

This application script is run through Jupyter Lab web-based interactive development environment to perform the analysis.  The analysis employs a three phase financial analysis approach (data collection, preparation, and analysis) to identify potentially profitable arbitrage opportunities that may have existed between bitstamp and coinbase exchanges over a three month period in 2018.  For the purpose of this analysis, a profitable arbitrage trade was defined as one in which the return was equal to or greater than 1%.  This would thus take into account 1/2% cost to buy in conjunction with 1/2% cost to sell.  

The Bitcoin trading data for the time period analyzed was collected and processed from `bitstamp.csv` and `coinbase.csv` data files.  From this data, three one day periods were identified for potential arbitrage trade opportunity comparisons, 'early', 'middle', and 'late'.  These three days utilized for this analysis do not represent the only opportunities available.  Rather, they represent the greatest opportunities for the time period of the data from which each was chosen.

Beyond the scope of the assignment, the author sought to conduct additional processing of the data obtained through processing and provide further visualization with combined data plots of the three one-day time periods examined.  The image included below is a rough example that is more thoroughly explained within the body of the analysis.

![combined overlay of arbitrage plots]images/cumulative_prof_overlay.png

---
## **Methods**

The command line interface operator/user will input

    file path for the `daily_rate_sheet`
    applicant's

        credit score
        monthly debt
        monthly income
        desired loan size
        current home value

    * the app will output as to available matches found or none found,
    * if no matches are found, the user / operator will be be prompted as to desire to save,
    * if no matches are identified, but user / operator indicates desire to save, output message will indicate there is none to save,
    * if matches are found and user / operator indicates desire to save,
    * the user / operator will be be prompted for a file path to where the list should be saved,
    * the user / operator will be be notified that the file has been saved to the specified path that has been in putted by the user / operator 

![Loan Qualifier Prompts](images/gen_methods.png)

---
## **Technologies**
---
### **Dependencies**

This project leverages Jupyter Lab v3.4.4 and python v3.7 with the following packages:

* [Path](https://docs.python.org/3/library/pathlib.html?highlight=path#module-pathlib) - From 'pathlib', Object-oriented filesystem paths, used to identify a file

* [pandas](https://pandas.pydata.org/docs/) - Software library written for the Python programming language for data manipulation and analysis.

* [read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html?highlight=read_csv#) - From 'pandas', read a comma-separated values (csv) file into DataFrame

For additional and / or supplemental processing and visulaization this project also makes use of the following packages:

* [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame) - From 'pandas', to construct a dataframe, i.e. a two-dimensional, size-mutable, potentially heterogeneous tabular data

* [MinMaxScaler](https://pandas.pydata.org/docs/) - from sklearn, preprocessing package provides several common utility functions and transformer classes to change raw feature vectors into a representation that is more suitable for the downstream estimators, transforms features by scaling each feature to a given range.


### **Hardware used for development**

MacBook Pro (16-inch, 2021)

    Chip Appple M1 Max
    macOS Monterey version 12.5.1

### **Development Software**

Homebrew 3.5.10

    Homebrew/homebrew-core (git revision 0b6b6d9004e; last commit 2022-08-30)
    Homebrew/homebrew-cask (git revision 63ae652861; last commit 2022-08-30)

anaconda Command line client 1.10.0

    conda 4.13.0
    Python 3.7.13

pip 22.1.2 from /opt/anaconda3/envs/dev/lib/python3.7/site-packages/pip (python 3.7)

    fire 0.4.0
    questionary 1.10.0

git version 2.37.2

Visual Studio Code version: 1.71.0 (Universal)

---
## *Installation of application (i.e. github clone)*

 In the terminal, navigate to directory where you want to install this application from the repository and enter the following command

```python
git clone git@github.com:Billie-LS/FinTech_Homeworks.git
```

---
## **Usage**

From terminal, the installed application is run from the installed directory by typing at prompt:

```python
  jupyter lab
```
![Loan Qualifier Prompts](images/app_on.png)

the following images will display sequential steps and prompts under four example protypical applicant scenarios.

###    scenario 1 - typical good candidate
        credit score 750, 
        monthly debt $1200, 
        monthly income $7500, 
        desired loan size $100000,
        current home value $140000

![Loan Qualifier Prompts](images/perfect_app1.png)
![Loan Qualifier Prompts](images/perfect_app2.png)
![Loan Qualifier Prompts](images/perfect_app_complete.png)

###    scenario 2 - good candidate, mistakenly enterred wrong / inadequate credit score
![Loan Qualifier Prompts](images/perfect_mistake1.png)
![Loan Qualifier Prompts](images/perfect_mistake_complete.png)

###    scenario 3 - candidate with inadequate credit score 
![Loan Qualifier Prompts](images/too_low1.png)
![Loan Qualifier Prompts](images/too_low2.png)
![Loan Qualifier Prompts](images/too_low_complete.png)

###    scenario 4 - good candidate seeking too large a loan
![Loan Qualifier Prompts](images/too_much.png)
![Loan Qualifier Prompts](images/too_much_complete.png)

---
## **Requirements**
### user stories and acceptance criteria

    Provided in directory `y_stories`

---
## **Version control**

This project was transferred to its current / new repository location.  For current / post-transfer GitHub repository version control history information please follow hyperlink.

[post-transfer-repository](https://github.com/Billie-LS/loan_prequal_qualifier_app)

For earlier / pre-transfer GitHub repository version control history information please follow hyperlink.

[pre-transfer-repository](https://github.com/Billie-LS/FinTech_Homeworks/commits/main/Challenge2)

---
## **Contributors**

### **Author**

Loki 'billie' Skylizard
[LinkedIn](https://www.linkedin.com/in/l-s-6a0316244)



### **BootCamp lead instructor**

Vinicio De Sola



### **BootCamp teaching assistants**

Corey Recai

Santiago Pedemonte



### **BootCamp classmates**

Stratis Gavnoudias

Will Conyea
[@GitHub](https://github.com/willkanye)


### **Slack application, student support services via 'askBCS'**

Roberto Salazar

Mark S.

---
## **License**

MIT License

Copyright (c) [2022] [Loki 'billie' Skylizard]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

