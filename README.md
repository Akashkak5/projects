Lead Scoring Backend
Setup Steps

Clone the repository

git clone <your-repo-url>
cd lead-scoring-backend


Create virtual environment

python -m venv .venv
# Activate
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Set OpenAI API key

# Windows (PowerShell)
setx OPENAI_API_KEY "YOUR_API_KEY"
# Linux/Mac
export OPENAI_API_KEY="YOUR_API_KEY"


Run the server

uvicorn app.main:app --reload


Open Swagger UI

http://127.0.0.1:8000/docs

API Usage Examples
POST /offer

Upload product/offer information:

{
  "name": "AI Outreach Automation",
  "value_props": ["24/7 outreach", "6x more meetings"],
  "ideal_use_cases": ["B2B SaaS mid-market"]
}

POST /leads/upload

Upload CSV file with columns:

name,role,company,industry,location,linkedin_bio

POST /score

Generate lead scores.

GET /results

View scored leads with intent and reasoning.

Example cURL:

# Upload offer
curl -X POST "http://127.0.0.1:8000/offer" \
-H "Content-Type: application/json" \
-d "{\"name\":\"AI Outreach Automation\",\"value_props\":[\"24/7 outreach\",\"6x more meetings\"],\"ideal_use_cases\":[\"B2B SaaS mid-market\"]}"

# Upload leads CSV
curl -X POST "http://127.0.0.1:8000/leads/upload" -F "file=@leads.csv"

# Score leads
curl -X POST "http://127.0.0.1:8000/score"

# Get results
curl -X GET "http://127.0.0.1:8000/results"

Rule Logic & AI Prompts
Rule-Based Scoring (0–50 points)

Role relevance: decision maker (+20), influencer (+10), else 0

Industry match: exact ICP (+20), adjacent (+10), else 0

Data completeness: all fields present (+10)

AI Layer (0–50 points)

Uses OpenAI GPT to classify lead intent: High / Medium / Low

Mapping: High = 50, Medium = 30, Low = 10

Final Score: rule_score + AI points

Sample AI Prompt:

Product: AI Outreach Automation
Value Props: 24/7 outreach, 6x more meetings
Ideal Use Cases: B2B SaaS mid-market

Lead Info:
Name: Ava Patel
Role: Head of Growth
Company: FlowMetrics
Industry: SaaS
Location: Bengaluru
LinkedIn Bio: Experienced growth manager in SaaS

Classify intent: High/Medium/Low. Explain in 1-2 sentences.


This version includes only setup steps, API examples, and rule + AI explanation as requested.

I can also make it even more compact for GitHub submission if you want. Do you want me to do that?

You said:
i want all in one 
ChatGPT said:

Got it! Here's a single compact README.md combining Setup Steps, API usage examples, and Rule/AI explanation in one clean document for your submission:

Lead Scoring Backend
Setup Steps

Clone the repository

git clone <your-repo-url>
cd lead-scoring-backend


Create virtual environment

python -m venv .venv
# Activate
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Set OpenAI API key

# Windows (PowerShell)
setx OPENAI_API_KEY "YOUR_API_KEY"
# Linux/Mac
export OPENAI_API_KEY="YOUR_API_KEY"


Run the server

uvicorn app.main:app --reload


Open Swagger UI

http://127.0.0.1:8000/docs

API Usage Examples
1. POST /offer

Upload product/offer information:

{
  "name": "AI Outreach Automation",
  "value_props": ["24/7 outreach", "6x more meetings"],
  "ideal_use_cases": ["B2B SaaS mid-market"]
}

2. POST /leads/upload

Upload CSV file with columns:

name,role,company,industry,location,linkedin_bio

3. POST /score

Generate lead scores.

4. GET /results

View scored leads with intent and reasoning.

cURL Example:

# Upload offer
curl -X POST "http://127.0.0.1:8000/offer" \
-H "Content-Type: application/json" \
-d "{\"name\":\"AI Outreach Automation\",\"value_props\":[\"24/7 outreach\",\"6x more meetings\"],\"ideal_use_cases\":[\"B2B SaaS mid-market\"]}"

# Upload leads CSV
curl -X POST "http://127.0.0.1:8000/leads/upload" -F "file=@leads.csv"

# Score leads
curl -X POST "http://127.0.0.1:8000/score"

# Get results
curl -X GET "http://127.0.0.1:8000/results"

Rule Logic & AI Prompts
Rule-Based Scoring (0–50 points)

Role relevance: decision maker (+20), influencer (+10), else 0

Industry match: exact ICP (+20), adjacent (+10), else 0

Data completeness: all fields present (+10)

AI Layer (0–50 points)

Uses OpenAI GPT to classify lead intent: High / Medium / Low

Mapping: High = 50, Medium = 30, Low = 10

Final Score: rule_score + AI points

Sample AI Prompt:

Product: AI Outreach Automation
Value Props: 24/7 outreach, 6x more meetings
Ideal Use Cases: B2B SaaS mid-market

Lead Info:
Name: Ava Patel
Role: Head of Growth
Company: FlowMetrics
Industry: SaaS
Location: Bengaluru
LinkedIn Bio: Experienced growth manager in SaaS

Classify intent: High/Medium/Low. Explain in 1-2 sentences.
