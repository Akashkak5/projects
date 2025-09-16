from fastapi import FastAPI, UploadFile, File
from app.models import Offer
from app.utils import save_upload_file, read_csv
from app.scoring import calculate_rule_score, get_ai_intent
import pandas as pd

app = FastAPI()

uploaded_leads_df = pd.DataFrame()
offer_data = None
results = []

@app.post("/offer")
def create_offer(offer: Offer):
    global offer_data
    offer_data = offer
    return {"message": "Offer received", "offer": offer.dict()}

@app.post("/leads/upload")
def upload_leads(file: UploadFile = File(...)):
    global uploaded_leads_df
    file_path = save_upload_file(file)
    uploaded_leads_df = read_csv(file_path)
    return {"message": f"{file.filename} uploaded successfully"}

@app.post("/score")
def score_leads():
    global uploaded_leads_df, offer_data, results
    results = []
    if uploaded_leads_df.empty or offer_data is None:
        return {"error": "Upload leads and offer first"}
    
    for _, lead_row in uploaded_leads_df.iterrows():
        lead = lead_row.to_dict()
        rule_score = calculate_rule_score(lead, offer_data)
        ai_points, intent, reasoning = get_ai_intent(lead, offer_data)
        final_score = rule_score + ai_points
        results.append({
            "name": lead["name"],
            "role": lead["role"],
            "company": lead["company"],
            "intent": intent,
            "score": final_score,
            "reasoning": reasoning
        })
    return {"message": "Leads scored successfully"}

@app.get("/results")
def get_results():
    return results
