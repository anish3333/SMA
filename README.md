Great idea — having a clean README will strengthen your submission 👍
Below is a **complete README.txt content** you can copy and save as:

```
README.txt
```

---

# 📘 README.txt — Social Media Analytics Dataset Ingestion Project

---

## Project Title

Stack Overflow Developer Survey Data Ingestion for Social Media Analytics

---

## Problem Statement

This project aims to analyze how software developers perceive and respond to the growing influence of Artificial Intelligence in software development. By ingesting and storing large-scale developer survey data into a NoSQL database, the project enables future social media analytics, sentiment analysis, and cognitive dissonance detection based on developers’ opinions, experiences, and attitudes.

---

## Dataset Description

The dataset contains structured survey responses collected from software developers worldwide. It includes demographic details, professional background, programming languages used, tools and platforms, and opinions about emerging technologies. The dataset is originally provided in CSV format and is converted into JSON documents for database storage.

---

## Technologies Used

* Node.js
* MongoDB Atlas (Cloud NoSQL Database)
* Mongoose
* csvtojson
* dotenv

---

## Project Folder Structure

```
SMA/
 ├─ data/
 │   └─ survey_results_public.csv
 ├─ import_csv.js
 ├─ .env
 ├─ package.json
 └─ README.txt
```

---

## Setup Instructions

1. Install Node.js
2. Create a MongoDB Atlas account and cluster
3. Clone or download this project folder
4. Install dependencies:

```
npm install
```

5. Create a `.env` file and add:

```
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/sma_database?retryWrites=true&w=majority&authSource=admin
```

6. Place the CSV dataset inside the `data` folder

7. Run the ingestion script:

```
node import_csv.js
```

---

## Data Storage Approach

Each row of the CSV file is converted into a JSON document and stored inside a MongoDB collection. All columns are preserved without modification to maintain raw data integrity.

---

## Sample Document Structure

```
{
  "_id": "ObjectId",

  "ResponseId": "string",
  "MainBranch": "string",
  "Age": "string",
  "EdLevel": "string",
  "Employment": "string",
  "EmploymentAddl": "string",

  "WorkExp": "string",
  "YearsCode": "string",

  "DevType": "string",
  "OrgSize": "string",
  "ICorPM": "string",
  "RemoteWork": "string",

  "Country": "string",
  "Currency": "string",
  "Industry": "string",

  "CompTotal": "string",
  "ConvertedCompYearly": "string",
  "JobSat": "string",

  "LearnCodeChoose": "string",
  "LearnCode": "string",
  "LearnCodeAI": "string",
  "AILearnHow": "string",

  "LanguageChoice": "string",
  "LanguageHaveWorkedWith": "string",
  "LanguageWantToWorkWith": "string",
  "LanguageAdmired": "string",

  "DatabaseChoice": "string",
  "DatabaseHaveWorkedWith": "string",
  "DatabaseWantToWorkWith": "string",
  "DatabaseAdmired": "string",

  "PlatformChoice": "string",
  "PlatformHaveWorkedWith": "string",
  "PlatformWantToWorkWith": "string",
  "PlatformAdmired": "string",

  "WebframeChoice": "string",
  "WebframeHaveWorkedWith": "string",
  "WebframeWantToWorkWith": "string",
  "WebframeAdmired": "string",

  "DevEnvsChoice": "string",
  "DevEnvsHaveWorkedWith": "string",
  "DevEnvsWantToWorkWith": "string",
  "DevEnvsAdmired": "string",

  "OfficeStackAsyncHaveWorkedWith": "string",
  "OfficeStackAsyncWantToWorkWith": "string",
  "OfficeStackAsyncAdmired": "string",

  "CommPlatformHaveWorkedWith": "string",
  "CommPlatformWantToWorkWith": "string",
  "CommPlatformAdmired": "string",

  "AIModelsChoice": "string",
  "AIModelsHaveWorkedWith": "string",
  "AIModelsWantToWorkWith": "string",
  "AIModelsAdmired": "string",

  "AISelect": "string",
  "AISent": "string",
  "AIAcc": "string",
  "AIComplex": "string",

  "AIToolCurrentlyPartiallyAI": "string",
  "AIToolPlanToPartiallyUseAI": "string",

  "AIFrustration": "string",
  "AIExplain": "string",

  "AIAgents": "string",
  "AIAgent_Uses": "string",
  "AIAgentOrchestration": "string",
  "AIAgentExternal": "string",

  "AIHuman": "string",
  "AIOpen": "string"
}

```

---

## Data Cleaning and Preprocessing

* Removal of duplicate records
* Handling missing values
* Conversion from CSV to JSON
* Basic text normalization

---

## Output

After successful execution, the entire dataset is available in MongoDB Atlas and can be used for:

* Social Media Analytics
* Sentiment Analysis
* Topic Modeling
* Cognitive Dissonance Detection

---

## Author

Soham Aversekar
Anish Awasthi
Mayuresh Chavan
Ajinkya Chitre