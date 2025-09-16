import openai
from app.config import OPENAI_API_KEY

# Points mapping
ROLE_SCORES = {"decision maker": 20, "influencer": 10}
INDUSTRY_SCORES = {"exact": 20, "adjacent": 10}
AI_POINTS = {"High": 50, "Medium": 30, "Low": 10}

def calculate_rule_score(lead, offer):
    """Simple rule-based score"""
    score = 0
    role = lead["role"].lower()
    if "head" in role or "manager" in role or "director" in role:
        score += ROLE_SCORES["decision maker"]
    elif "executive" in role or "specialist" in role:
        score += ROLE_SCORES["influencer"]

    if lead["industry"].lower() in [u.lower() for u in offer.ideal_use_cases]:
        score += INDUSTRY_SCORES["exact"]
    else:
        score += INDUSTRY_SCORES["adjacent"]

    if all(lead.get(k) for k in ["name","role","company","industry","location","linkedin_bio"]):
        score += 10

    return score

def get_ai_intent(lead, offer):
    """Call OpenAI to classify lead intent"""
    openai.api_key = OPENAI_API_KEY
    prompt = f"""
    Product: {offer.name}
    Value Props: {', '.join(offer.value_props)}
    Ideal Use Cases: {', '.join(offer.ideal_use_cases)}

    Lead Info:
    Name: {lead['name']}
    Role: {lead['role']}
    Company: {lead['company']}
    Industry: {lead['industry']}
    Location: {lead['location']}
    LinkedIn Bio: {lead['linkedin_bio']}

    Classify intent: High/Medium/Low. Explain in 1-2 sentences.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":prompt}],
            temperature=0
        )
        text = response.choices[0].message.content.strip()
        intent = "Low"
        reasoning = ""
        for line in text.split("\n"):
            if line.lower().startswith("intent"):
                intent = line.split(":")[1].strip()
            elif line.lower().startswith("reasoning"):
                reasoning = line.split(":",1)[1].strip()
        return AI_POINTS.get(intent, 10), intent, reasoning
    except:
        return 10, "Low", "AI error"
