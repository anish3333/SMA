# %%
import pandas as pd

# File paths
public_path = "data/stack-overflow-developer-survey-2025/survey_results_public.csv"
schema_path = "data/stack-overflow-developer-survey-2025/survey_results_schema.csv"

# Load CSVs
public_df = pd.read_csv(public_path)
schema_df = pd.read_csv(schema_path)

print("=== Public Survey Dataset Schema ===")
print(public_df.info())

print("\n=== First few columns ===")
print(public_df.columns.tolist())

print("\n=== Schema Dataset (Question Mapping) ===")
print(schema_df.head(20))

# %%
ai_cols = [
    "AISent",
    "AIAcc",
    "AIThreat",
    "AIFrustration",
    "AIExplain"
]

ai_df = public_df[ai_cols]

ai_df.head()

# %%
for col in ai_cols:
    print(f"\n===== {col} =====")
    print(public_df[col].value_counts())

# %%
import matplotlib.pyplot as plt

public_df["AISent"].value_counts().plot(kind="bar")

plt.title("Developer Sentiment Towards AI")
plt.ylabel("Number of Developers")
plt.xlabel("Sentiment")
plt.show()

# %%
from collections import Counter

text_data = public_df["TechEndorse_13_TEXT"].dropna()

words = " ".join(text_data).lower().split()

common_words = Counter(words).most_common(20)

print(common_words)

# %%


# %%
public_df["Country"].value_counts().head(10)

# %%
ai_country = public_df.groupby("Country")["AISent"].value_counts().unstack()

ai_country.head()

# %%
top_countries = public_df["Country"].value_counts().head(10).index

country_ai = public_df[public_df["Country"].isin(top_countries)]

country_ai.groupby("Country")["AISent"].value_counts().unstack().plot(kind="bar", stacked=True)

plt.title("AI Sentiment by Country")
plt.ylabel("Number of Developers")
plt.show()

# %%


# %%
salary_ai = public_df.groupby("AISent")["ConvertedCompYearly"].mean()

salary_ai

# %%
salary_ai.plot(kind="bar")

plt.title("Average Salary vs AI Sentiment")
plt.ylabel("Average Salary")
plt.show()

# %%


# %%
public_df["SOVisitFreq"].value_counts()

# %%
public_df["SOPartFreq"].value_counts()

# %%
public_df["SOVisitFreq"].value_counts().plot(kind="bar")

plt.title("StackOverflow Visit Frequency")
plt.ylabel("Number of Users")
plt.show()

# %%


# %%
!pip install wordcloud

# %%
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text_data = public_df["TechEndorse_13_TEXT"].dropna()

text = " ".join(text_data.astype(str))

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color="white",
    colormap="viridis"
).generate(text)

plt.figure(figsize=(14,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Common Words in Technology Endorsement Responses")
plt.show()

# %%
public_df["AISent"].value_counts().plot(
    kind="pie",
    autopct='%1.1f%%',
    figsize=(6,6)
)

plt.title("Developer Sentiment Towards AI")
plt.ylabel("")
plt.show()

# %%



