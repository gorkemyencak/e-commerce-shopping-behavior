
# E-Commerce Shopper Behavior Analysis & Segmentation

## Project Overview
This project explores e-commerce shopper behavior and lifestyle patterns using a large-scale dataset derived from Amazon / Shopify–style platforms. The goal is to understand how lifestyle, engagement, and behavioral signals translate into shopping behavior, and to build interpretable customer segments that can inform marketing and business decisions.

The project follows an end-to-end data science workflow: data ingestion, exploratory analysis, feature engineering, baseline modeling, and unsupervised customer segmentation.

## Dataset
The dataset contains 1M shoppers, and includes information about:
- Monthly spend
- Browsing & shopping habits
- Lifestyle & wellbeing indicators
- Impulse vs planned purchase behavior
- Funnel activity (cart, wishlist, checkout)

## Project Objectives
1. **Analyze** relationships between lifestyle, behavioral patterns, and spending behavior  
2. **Engineer** composite behavioral scores to improve interpretability and insight  
3. **Develop and evaluate** baseline predictive models for customer behavior  
4. **Perform** robust customer segmentation using unsupervised learning techniques  
5. **Translate** identified clusters into actionable shopper personas for business decision-making

## Workflow Overview

### 1. **Data Loading**
- Custom KaggleCSVLoader downloads raw CSV directly from Kaggle

### 2. **Dataset Investigation**
- Column walkthrough
- Data types & missing value analysis
- Target variable identification (monthly_spend)

### 3. **Exploratory Data Analysis (EDA)**
- Correlation analysis
- Distribution analysis
- Spend vs behavioral feature exploration

**Key Insight:** Linear correlations are weak $\Rightarrow$ shopper behavior is **nonlinear** & **multi-dimensional**

### 4. **Feature Engineering**
#### Composite Behavioral Scores
To improve interpretability and reduce dimensionality, several **composite behavioral scores** were engineered:

- **Wellbeing Score**
- **Shopping Engagement Score**
- **Price Awareness Score**
- **Impulse Purchase Score**
- **Review Influence Score**
- **Shopping Funnel Score**

Each composite score aggregates multiple raw behavioral signals into a single, interpretable metric.

The processed dataset is saved as a **compressed Parquet file** for efficient storage and loading.

## 5. **Modeling & Baselines**

Two problem formulations were explored:

- **Regression:** Predicting monthly spend  
- **Classification:** Spend tiers (*Low / Medium / High*)

### Baseline Models
- Majority class predictor  
- Logistic Regression  
- Decision Tree  

**Result:**  
Predictive performance is intentionally modest, highlighting the greater value of **customer segmentation** over pure prediction for this problem.

## 6. **Customer Segmentation Analysis**
### Methodology

- **Features:** Composite behavioral scores  
- **Scaling:** StandardScaler  
- **Algorithm:** KMeans (with subsampling for computational efficiency)  
- **Model Selection:** Silhouette score  
- **Selected Number of Clusters:** $\( K = 3 \)$

### Cluster Stability Validation
- **Adjusted Rand Index (ARI)** across subsamples

## **Key Insights**

- Shopper behavior is not well explained by linear relationships alone
- Composite behavioral features improve interpretability
- Customer segmentation reveals distinct shopping archetypes with clear business relevance
- High wellbeing & impulsivity strongly align with funnel progression