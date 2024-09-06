# Week 3

## CodeLab

### Questions

- [x] Create a new environment and import the Test Files into the Project. You will need to download the file as a .xlsx file.
- [x] Generate the email addresses of all the students in the format below. 
  - [x] Student Name: John, Doe Hussein - Email address: jhussein@ gmail.com
  Points to Note
    - [x] Email addresses should be unique
    - [x] If the student has two names then you need to use what is available
    - [x] Email addresses should not have special characters (regex - `^\w\s`)
    
- [x] This project should be pushed into GitHub for collaboration.
  - [x] This project must have a proper readme file
  - [x] All output files must be labeled properly ('student_emails.csv' & 'student_emails.tsv')
    - [x] Files with all functions - functions.py
    - [x] Files with constraints - constraints.py
    - [x] Main program file - main.py
  - [x] Use log files to save all the computations
  
- [x] Save the files as TSV and CSV respectively
  - [x] For all information formatting 
  
- [x] Generate separate lists of Male and Female students
  - [x] In the logs, you need to show the number of all male students and female students
  - [x] List the names of students with special characters for example Orony, Charis Ng'wono - regex solution

- [ ] It is common that some names are similar, using LaBSE, run a similarity matrix on all male names vs female names and show the results in a json file. Pick the results that have at least 50% similarity. - stretch

- [ ] Merge all the documents into one file then:
  - [ ] Using Pandas, run a one time shuffle of the names and save the file as a json file.
  - [ ] Save another copy as a Jsonl file with the format below





### Miscellaneous
#### Pull Requests
- `git remote add upstream git://github.com/some-url`
- `git fetch upstream`
- `git rebase upstream/master`
