from apify_client import ApifyClient
import os 
from dotenv import load_dotenv
load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Fetch LinkedIn jobs based on search query and location
def fetch_linkedin_jobs(search_query, location="india", rows=60):
    search_query_encoded = search_query.replace(" ", "%20")
    location_encoded = location.replace(" ", "%20")
    
    linkedin_url = f"https://www.linkedin.com/jobs/search/?keywords={search_query_encoded}&location={location_encoded}&count={rows}"
    
    run_input = {
        "urls": [linkedin_url],
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        }
    }
    run = apify_client.actor("hKByXkMQaC5Qt9UMN").call(run_input=run_input)
    jobs = list(apify_client.dataset(run.default_dataset_id).iterate_items())  # ← dot notation
    return jobs


def fetch_naukri_jobs(search_query, location="india", rows=60):
    run_input = {
        "keyword": search_query,
        "maxJobs": 60,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }
    run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
    jobs = list(apify_client.dataset(run.default_dataset_id).iterate_items())  # ← dot notation
    return jobs
