import os
from dotenv import load_dotenv
from google import genai

# Load API Key securely
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ============ TOOLS (Agent Skills) ============

def search_jobs(keyword: str) -> str:
    """Tool: Search for job listings based on keyword"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Generate 2 realistic job listings for: {keyword}. Include title, company, and requirements."
    )
    return response.text

def analyze_resume(job_description: str) -> str:
    """Tool: Analyze resume match against job description"""
    resume = "Skills: Python, AI Agents, Machine Learning, REST APIs"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Score this resume (0-100) against this job:\nResume: {resume}\nJob: {job_description}\nGive score and reason."
    )
    return response.text

def generate_cover_letter(job_title: str, company: str) -> str:
    """Tool: Generate personalized cover letter"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Write a short professional cover letter for {job_title} at {company}."
    )
    return response.text

# ============ AGENTS ============

class JobHunterAgent:
    def run(self, keyword):
        print("\n[Agent 1: Job Hunter] Searching for jobs...")
        result = search_jobs(keyword)
        print(result)
        return result

class MatchmakerAgent:
    def run(self, job_description):
        print("\n[Agent 2: Matchmaker] Analyzing resume match...")
        result = analyze_resume(job_description)
        print(result)
        return result

class ApplierAgent:
    def run(self, job_title, company):
        print("\n[Agent 3: Applier] Generating cover letter...")
        result = generate_cover_letter(job_title, company)
        print(result)
        return result

# ============ MAIN PIPELINE ============

def run_pipeline():
    print("=" * 60)
    print("   AUTO-APPLY AI AGENT - Powered by Google Gemini   ")
    print("=" * 60)

    hunter = JobHunterAgent()
    matchmaker = MatchmakerAgent()
    applier = ApplierAgent()

    jobs = hunter.run("AI Engineer")
    matchmaker.run(jobs)
    applier.run("AI Engineer", "Google DeepMind")

    print("\n[Pipeline Complete] Application package ready!")

if __name__ == "__main__":
    run_pipeline()
