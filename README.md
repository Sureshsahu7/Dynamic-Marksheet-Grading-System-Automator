# Dynamic-Marksheet-Grading-System-Automator
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#run">Run</a></li>
      </ul>
    </li>
    <li><a href="#Output-Data-Acquired">Output Data Acquired</a></li>
   
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

![portfolio3](https://user-images.githubusercontent.com/85033183/187027874-7b526d1a-02e3-4351-97fc-05e2846fe9b6.png)

Using Flask,designed a grading module for generating marksheet via Google quiz with Dynamic negative marking, and sending marksheets via mail to respective students.
With a given .csv file that contains marks for each roll number and the individual options marked by each students  this  Grading module generates
an individual marksheet for each student and a concise Marksheet of whole batch of students 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![HTML][html.com]][html-url]
* [![CSS][css.com]][css-url]
* [![Javascript][Js.com]][Js-url]
* [![Python][python.com]][python-url]
* [![Flask][flask.com]][flask-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

 
 <!-- GETTING STARTED -->
## Getting Started
  When the quiz is conducted on Google Form, Google does not provide an option for computing -ve marking. It gives 0
marks for wrong answer. It just gives a csv file as output for post processing.So I made a web
based interface that will have such an option.

we'll get a .csv file from Google Form that contains marks for each roll number and the individual options marked by each student.
Timestamp: At what time student submitted their question paper.
Email address: Email address to which student login.
Score: Total calculated score.
Name: Name of the student.
IITP webmail: IITP webmail address.
Phone number: Phone number of the student
Roll Number: Roll number of the student.

### Prerequisites

Install python and edit its path in environmental variable

Activate env and Install Flask
* Flask
  ```sh
  venv\Scripts\activate
  ```
  ```sh
  pip install Flask
  ```
  

### Run

1. Clone the repo
   ```sh
   git clone https://github.com/Sureshsahu7/Dynamic-Marksheet-Grading-System-Automator.git
   ```
2. Open terminal and Enable env
   ```sh
   C:\Users\user_name\Documents\GitHub\Dynamic-Marksheet-Grading-System-Automator/env/scripts/Activate.ps1
   ```
3. Run The  app in flask Server
   ```js
   python .\app.py
   ```
4. Download the master roll and responses (.csv) Dataset

5. First button is to upload a master roll.csv file. It contains the names and roll number of all the students of the class 

6. Next is for the response sheet csv obtained from google both will be Uploaded in sample_input folder.

6. The user will be asked to enter the +ve and -ve marks for right and Wrong answers respectively of each question Dynamically.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Output Data Acquired

   🔳 Generate Roll Number wise marksheet 🔳 

1. Click the button it generates a marksheet for every roll number present in the master roll. If a roll number is present in the master file but not in the response.csv that means that student was absent, so a blank marksheet will be generated having all answers as blank.
2. This option also will generate a marksheet of individual roll number and save as ”.xlsx”.The number of right answers, number of wrong answers, not attempted questions and the marks associated with right, wrong answers are displayed after being calculated automatically.
3. Master Key answers will be in Blue, Student’s correct answer is in Green and wrong answer are in red.The file also have the IITP logo.

  🔳 Generate conscise marksheet 🔳 

The generate concise marksheet option is given that generate all the marked options as well as marks before and after -ve computation

All the output files will be Generated in the sample_output folder.

  🔳 send email 🔳 
  
 Email address is located from the response sheet csv file of Google Form.when you click on Send Email button, it will send a marksheet to respective roll_no's email
 address with the marksheet of that roll number.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



 video link: https://www.youtube.com/watch?v=wYvzRWSkY_s



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[css.com]:https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white
[css-url]: https://css.com
[html.com]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[html-url]:	https://html.com
[Js.com]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[Js-url]: https://javascript.com
[python.com]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.com
[flask.com]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.com





