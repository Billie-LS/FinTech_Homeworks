# Columbia University Engineering, New York FinTech BootCamp 
# August 2022 Cohort
## Module 2, Challenge

This is a command line interface (CLI) data processing application for bank loan pre-qualification screening.  This application matches loan applicants with banks and associated bank loans for which they may qualify.

The screening application is processed via applicant query for applicant specific data.  The user will input applicant's credit score, current debt level, income, the size of the loan desired, and the value of the applicant's collateral (i.e. current home value).  These data points are compared against the loan criteria of various lenders contained within a comma separated values (CSV) file, `daily_rate_sheet`.  

Through processing the loan applicant provided data and comparing it to the loan criteria of various lenders, the loan applicant's eligibility for the loan they are seeking is determined.  The program will output for the applicant their calculated monthly debt to income (DTI) ratio, loan to value (LTV) ratio, and, if they qualify, the number of banks with a list of those banks to which they are pre-qualified will be outputted.  The program will then offer to save the list of banks and loan data.  Upon selcting to save the data, the list of banks and loan data within a comma separated values (CSV) file, `bank_loan_list`.

The command line interface operator/user will input
    file path for the `daily_rate_sheet`
    applicant's
        credit score
        monthly debt
        monthly income
        desired loan size
        current home value
    if qualified, file path to save list of banks and associated loan data

Just after the title, introduce your project by describing attractively what the project is about and what is the main problem that inspires you to create this project or what is the main contribution for the potential user of your project.

---
## Technologies
## Development Hardware used
macOS Monterey version 12.5.1
    MacBook Pro (16-inch, 2021)
    Chip Appple M1 Max

## Development Software

Homebrew 3.5.10
    Homebrew/homebrew-core (git revision 0b6b6d9004e; last commit 2022-08-30)
    Homebrew/homebrew-cask (git revision 63ae652861; last commit 2022-08-30)

conda 4.13.0
Python 3.7.13

pip 22.1.2 from /opt/anaconda3/envs/dev/lib/python3.7/site-packages/pip (python 3.7)
    fire 0.4.0
    questionary 1.10.0

git version 2.37.2

Visual Studio Code version: 1.71.0 (Universal)

---

## Installation Guide

In this section, you should include detailed installation notes containing code blocks and screenshots.

---

## Usage

This section should include screenshots, code blocks, or animations explaining how to use your project.

---

## Contributors
Author
    Loki 'billie' Skylizard
    https://www.linkedin.com/in/l-s-6a0316244/

BootCamp lead instructor
    Vinicio De Sola
BootCamp teaching assistants
    Corey Recai
    Santiago Pedemonte
BootCamp classmates
    Dinesh Mandal
    Will Conyea
Slack application, student support services via 'askBCS'
    Laanu Adeyeye
    Tristen Ortiz

In this section, list all the people who contribute to this project. You might want recruiters or potential collaborators to reach you, so include your contact email and, optionally, your LinkedIn or Twitter profile.

---

## License

When you share a project on a repository, especially a public one, it's important to choose the right license to specify what others can and can't with your source code and files. Use this section to include the license you want to use.
