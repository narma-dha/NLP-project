                                                                                         # NLP-project

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                             
#  NLP Document Classification System

## Project Overview

The **NLP Document Classification System** is a Python-based project that automatically classifies text documents into predefined categories such as **Invoice**, **Resume**, **Medical Report**, or **Prescription**. The system uses **Natural Language Processing (NLP)** and **Machine Learning** techniques to analyze document content and predict its type along with a confidence score.

This project demonstrates the practical application of NLP in **document automation** and is suitable for **academic mini-projects or final-year projects**.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##  Objectives

* Automatically classify documents based on their text content
* Reduce manual effort in document sorting
* Apply NLP preprocessing techniques on real-world data
* Build a basic machine learning text classification model
* Display prediction results with confidence percentage

--------------------------------------------------------------------------------------------------------------------------------------

## Technologies Used

* **Programming Language:** Python
* **Libraries & Frameworks:**

  * NLTK (Text preprocessing)
  * scikit-learn (Machine Learning models)
  * PyPDF2 (PDF text extraction)
  * pandas & numpy (Data handling)
* **IDE:** VS Code / PyCharm
* **Model Used:** Naive Bayes Classifier

--------------------------------------------------------------------------------------------------------------------------------------

## ⚙️ System Workflow

1. Input document (PDF or text)
2. Extract text from document
3. Text preprocessing (tokenization, stopword removal)
4. Feature extraction using TF-IDF Vectorizer
5. Document classification using ML model
6. Output predicted document type and confidence score

---------------------------------------------------------------------------------------------------------------

##  How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install nltk scikit-learn PyPDF2 pandas numpy
```

### Step 2: Download NLTK Data

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### Step 3: Prepare Dataset

* Ensure the dataset contains document text and labels
* Example labels: Invoice, Resume, Medical, Prescription

### Step 4: Run the Project

```bash
python main.py
```

---

## Sample Output

```
Document Type: Invoice
Confidence: 54.58%
```

----------------------------------------------------------------------------------------------------------------

##  Model Evaluation

* Accuracy depends on dataset size and quality
* Confidence score is calculated based on prediction probability
* Can be improved by increasing training data

--------------------------------------------------------------------------------------------------------------

##  Advantages

* Automates document classification
* Saves time and manual effort
* Easy to extend with new categories
* Good introduction to NLP and ML

--------------------------------------------------------------------------------------------------------------

## Limitations

* Accuracy may be low with small datasets
* Cannot handle unseen document formats well
* Not suitable for production-level use without improvements

--------------------------------------------------------------------------------------------------------------------

##  Future Enhancements

* Use advanced models (SVM, Deep Learning, BERT)
* Improve preprocessing techniques
* Add a web interface (Flask/Django)
* Increase dataset size for better accuracy

--------------------------------------------------------------------------------------------------------------------

##  Author

**Narmadhadevi D**
B.Tech – Information Technology
St. Joseph’s College of Engineering

----------------------------------------------------------------------------------------------------------------

##  Disclaimer

This project is developed **for educational purposes only** and should not be used for real-world document verification or legal dec

                                        -------------------------------------------------------X X X X X X ----------------------------------------------------------------
