# 💼 **Automated Job Searching on LinkedIn**

Python project for searching for job openings on LinkedIn and email me a summary

## 🎯 Objective

- Go through LinkedIn Job posts using Selenium
- Save the post’s information I'm interested in and URL into a dictionary
- Filter and format the data
- Send me the data by a HTML formatted email

### **Automated email example**
![emailExample_automatedJobSearchingLinkedIn](https://github.com/vcardui/automatedJobSearchingLinkedIn/assets/145515264/ec266ef1-79be-46e7-92a1-555c2a6c85c5)

## Selenium **Automated Job Searching on LinkedIn example**
![seleniumAutomatization_automatedJobSearchingLinkedIn](https://github.com/vcardui/automatedJobSearchingLinkedIn/assets/145515264/a1c3bc3d-0539-4759-a2c7-cd76c64cae9b)

### Working project demo
https://github.com/vcardui/automatedJobSearchingLinkedIn/assets/145515264/3cdcbc42-318d-4681-9f95-4ab889ee20af

## 🙌 Project Personal Milestones

- Web Scraping using **Selenium** (automated web testing tool). Learned how to use it’s classes and methods.
- Gained an understanding of Xpaths and HTML tags, IDs and classes for finding elements in website
- **Handled** Selenium **exceptions** that involved not finding and element (which resulted into program crashing)
- **Formatted data in HTML** in order to add emojis, bullets and colors for highlighting important information in email aided by **MIMEMultipart** library
- Send automated email aided by **Smtplib**

## 💡 Inspiration for creating this project

I’m currently enrolled in 100 Days of Code: The Complete Python Pro Bootcamp (Udemy) and this is the course’s #49th project. The original project only involved saving the post or applying to it, but I went a bit further and decided to filter the data and email me a summary of it.

## 👀 About the project

My criteria for filtering and formatting the job offers were based on:

- Mentioned programming languages description: Looked for languages I was familiar with and saved those who were found in text. Colored Python in turquese for outstanding in email
- Work Modality: Since I'm main interested in remote positions or nerby me, I added a computer emoji to text when found a Remote position and and office emoji when not.
- Level, Location and Published Date: Outstanded each job detail into a bulled list in email
- Link: Added link to job offer for further reference and avoiding adding full job description into email
