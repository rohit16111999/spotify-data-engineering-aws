# Spotify Data Engineering Project (AWS)

This repository showcases an end-to-end Data Engineering project that demonstrates the lifecycle of building a data pipeline and analytics dashboard using AWS services. The project is based on a preprocessed version of the [Spotify Dataset 2023 from Kaggle](https://www.kaggle.com/datasets/tonygordonjr/spotify-dataset-2023).


---

## 🧱 Project Architecture

![Project Architecture](architecture/Project%20Architecture.png)

The architecture consists of:

- **S3 (Staging & Datawarehouse)**: For storing raw and processed data.
- **AWS Glue**: For ETL processing using visual jobs and PySpark.
- **Glue Crawler**: For schema inference and catalog creation.
- **Athena**: For querying the data using SQL.
- **QuickSight**: For interactive dashboards and visual analytics.
- **IAM**: For secure access and permissions.

---

## 📁 Project Structure

```bash
spotify-data-engineering-aws/
├── architecture/
│   └── Project Architecture.png
│   └── Visual ETL.png
├── datasets/
│   └── albums.csv
│   └── artists.csv
│   └── track.csv
├── screenshots/
│   └── s3_folders.png
│   └── s3_staging.png
│   └── s3_datawarehouse.png
│   └── glue_etl_job_config.png
│   └── crawler_job_for_table.png
│   └── athena_query_result.png
│   └── quicksight_dataset_import.png
│   └── quicksight_dashboard_view.png
│   └── iam_permissions.png
├── dashboard/
│   └── Spotify Project Dashboard.pdf
├── code/
│   └── spotify_etl_job.py     # AWS Glue ETL script to join and transform Spotify datasets
└── README.md
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?style=flat&logo=amazon-aws&logoColor=white)
![Glue](https://img.shields.io/badge/AWS%20Glue-ETL-blueviolet)
![Athena](https://img.shields.io/badge/Athena-SQL-blue)
![QuickSight](https://img.shields.io/badge/QuickSight-Visualization-yellow)

---

## 🧩 Datasets

Stored in the `datasets/` folder, the three CSVs used are:

- `albums.csv`
- `artists.csv`
- `track.csv`

Each file contains cleaned and preprocessed data extracted from the original Kaggle dataset.

---

## 🔄 ETL Process in AWS Glue

- Loaded data from S3 (CSV files) using AWS Glue
- Joined `artists`, `albums`, and `track` tables using PySpark
- Dropped unnecessary fields and applied data quality rules
- Saved output as Parquet into the `datawarehouse/` folder in S3

ETL script available in: [`code/spotify_etl_job.py`](./code/spotify_etl_job.py)

---

## 🧭 Table Creation Using Glue Crawler

- Created a database called `spotify`
- Ran a crawler on the `datawarehouse/` folder
- Automatically created a table `datawarehouse` in Athena

---

## 🔍 Querying with AWS Athena

```sql
SELECT * FROM datawarehouse LIMIT 10;
```

- Verified data quality and transformations using SQL queries
- Screenshot of sample query: `athena_query_result.png`

---

## 📊 Dashboard with AWS QuickSight

- Connected QuickSight with Athena
- Created visuals:
  - Top 10 Artists by Followers
  - Donut chart: Followers by Genre
  - Bar + Line: Popularity vs Duration
  - Heatmap: Popularity by Genre & Year
  - Tree Map: Genre Distribution by Track Count
  - Stacked Area Line Chart: Track Popularity Trends Over Time
- KPIs:
  - Average Followers
  - Average Track Popularity

Dashboard file: [`Spotify Project Dashboard.pdf`](./dashboard/Spotify%20Project%20Dashboard.pdf)

---

## 📈 KPI Metrics & Graph Insights

### 🎯 Key Metrics (KPIs)

| KPI | Insight |
|-----|---------|
| **Average Track Popularity** | Indicates the general popularity level of tracks on Spotify. A higher value suggests the dataset includes widely played and liked tracks. |
| **Average Followers** | Reflects the overall reach of artists in the dataset. A high average shows strong fan engagement and potential listening audience. |

---

### 📊 Graph Insights

- **Top Artists by Followers (Bar Chart)**  
  → Artists like Taylor Swift, Araia Grande, Drake, Eminem and The Weeknd respectively lead with significantly higher follower counts, reflecting their global dominance on the platform.

- **Followers by Genre (Donut Chart)**  
  → Pop and hip hop are the most followed genres, suggesting higher listener engagement and mainstream appeal.

- **Tracks by Popularity & Duration (Bar + Line Chart)**  
  → Tracks between 95–248 seconds tend to have the highest popularity scores, confirming the ideal track length for listener retention.

- **Popularity by Genre and Year (Heatmap)**  
  → Genres like pop and EDM have shown consistently high popularity across years, while niche genres vary more widely over time.

- **Genre Distribution by Track Count (Tree Map)**  
  → Pop, rap, and dance genres dominate the catalog by track count, revealing content volume concentration in trending categories.

- **Track Popularity Over Time (Stacked Area Line Chart)**  
  → Shows rising cumulative popularity for newer genres, indicating shifting user preferences and increased genre diversification in recent years.

---

## 🖼️ Screenshots

Available in the `screenshots/` folder:
- S3 structure
- Glue ETL config
- Crawler setup
- Athena results
- QuickSight dashboard
- IAM permissions

---

## 🔐 IAM Setup

- Separate IAM user created
- Permissions for: `s3:*`, `glue:*`, `athena:*`, `quicksight:*`, `iam:*`
- QuickSight service role allowed to access S3

---

## 📌 Outcome

- ✅ Cloud-native ETL pipeline from raw to dashboard  
- ✅ Used multiple AWS services in an integrated flow  
- ✅ Developed KPIs and visual insights to analyze Spotify data  
- ✅ Built reusable, production-ready project repo for Data Engineering use cases

---

## 👨‍💼 Author

**Rohit Vaishali Motdhare**  
Master’s in Data Analytics Engineering – George Mason University  
AWS | Python | SQL | Data Engineering | Spotify Dataset

---

## 📫 Connect with Me

- [LinkedIn](https://www.linkedin.com/in/rohitmotdhare)  
- [GitHub](https://github.com/rohitmotdhare)  
- [Email](mailto:rohitrvm@gmail.com)

---

© 2025 Rohit Motdhare. All rights reserved.

