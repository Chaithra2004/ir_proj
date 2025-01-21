import json
from datetime import datetime, timedelta
import random

# Categories with their typical headlines and descriptions
categories = {
    "TECHNOLOGY": {
        "headlines": [
            "New AI Model Breaks Performance Records in {task}",
            "Tech Giant Launches Revolutionary {product}",
            "Breakthrough in Quantum Computing Achieves {achievement}",
            "Startup Raises ${amount}M for {technology} Development",
            "Scientists Develop {technology} for {application}"
        ],
        "desc_templates": [
            "Researchers have achieved significant progress in {field}, promising to revolutionize {application}.",
            "The new technology demonstrates unprecedented accuracy in {task}, marking a major milestone.",
            "Industry experts predict this development could transform {industry} within the next few years.",
            "Early tests show promising results in {application}, with potential applications in {field}.",
            "The innovation addresses long-standing challenges in {field}, offering new possibilities."
        ]
    },
    "BUSINESS": {
        "headlines": [
            "Market Surge: {company} Stock Rises {percent}% After {event}",
            "Global Investment in {sector} Reaches ${amount}B",
            "{company} Announces Merger with {other_company}",
            "Economic Report Shows {trend} in {sector} Growth",
            "{company} Expands Operations to {region}"
        ],
        "desc_templates": [
            "Analysts predict significant market impact following the announcement of {event}.",
            "The deal is expected to create new opportunities in {sector} and boost market competition.",
            "Industry experts view this development as a positive sign for {sector} growth.",
            "The move is part of a larger strategy to expand presence in {region} markets.",
            "Investors respond positively to news of {event}, driving stock prices up."
        ]
    },
    "SCIENCE": {
        "headlines": [
            "Scientists Discover New {discovery} in {location}",
            "Research Reveals Unexpected Link Between {thing1} and {thing2}",
            "Breakthrough Study Shows Promise for {condition} Treatment",
            "New Evidence Suggests {theory} About {subject}",
            "International Team Maps {subject} for First Time"
        ],
        "desc_templates": [
            "The discovery could lead to new understanding of {subject} and its role in {field}.",
            "Researchers say this finding could revolutionize our approach to {field}.",
            "The study provides new insights into {subject}, challenging previous theories.",
            "This breakthrough could have significant implications for {field} research.",
            "The findings open new possibilities for applications in {field}."
        ]
    },
    "HEALTH": {
        "headlines": [
            "New Study Links {factor} to Improved {health_outcome}",
            "Breakthrough Treatment Shows Promise for {condition}",
            "Research Reveals Benefits of {activity} for {health_aspect}",
            "Medical Trial Reports Success in {treatment} Development",
            "Health Experts Recommend New Guidelines for {health_aspect}"
        ],
        "desc_templates": [
            "The research suggests significant benefits for patients suffering from {condition}.",
            "Clinical trials show promising results in treating {condition} with new approach.",
            "Experts recommend lifestyle changes including {activity} for better health outcomes.",
            "The study highlights the importance of {factor} in maintaining good health.",
            "New guidelines aim to improve treatment outcomes for {condition} patients."
        ]
    },
    "WORLD NEWS": {
        "headlines": [
            "{country} Announces Major Policy Shift on {issue}",
            "International Summit Addresses {global_issue}",
            "Historic Agreement Reached Between {country1} and {country2}",
            "Global Initiative Launches to Combat {problem}",
            "Report Shows Impact of {issue} on {region}"
        ],
        "desc_templates": [
            "The decision is expected to have significant implications for {issue} globally.",
            "Leaders from multiple nations gathered to address growing concerns about {issue}.",
            "The agreement marks a historic step forward in addressing {issue}.",
            "Experts say this development could reshape international relations in {region}.",
            "The initiative aims to address challenges related to {issue} across borders."
        ]
    }
}

# Fill-in content for templates
content_fillers = {
    "task": ["image recognition", "natural language processing", "predictive analytics", "speech recognition", "pattern detection"],
    "product": ["smartphone", "AI assistant", "wearable device", "smart home system", "autonomous vehicle system"],
    "achievement": ["quantum supremacy", "processing speed record", "efficiency milestone", "accuracy benchmark", "scalability breakthrough"],
    "technology": ["neural network", "blockchain system", "quantum processor", "machine learning algorithm", "AI model"],
    "application": ["healthcare", "autonomous vehicles", "space exploration", "climate monitoring", "cybersecurity"],
    "field": ["artificial intelligence", "renewable energy", "biotechnology", "quantum computing", "robotics"],
    "industry": ["healthcare", "finance", "transportation", "manufacturing", "education"],
    "company": ["TechCorp", "InnovateX", "FutureWorks", "GlobalTech", "NextGen Solutions"],
    "other_company": ["DataFlow", "SmartSys", "TechVision", "InnovateCo", "FutureTech"],
    "sector": ["renewable energy", "artificial intelligence", "biotechnology", "digital payments", "cloud computing"],
    "region": ["Asia Pacific", "European Union", "Latin America", "Middle East", "African markets"],
    "percent": [15, 20, 25, 30, 35],
    "amount": [100, 250, 500, 750, 1000],
    "event": ["quarterly earnings", "product launch", "strategic partnership", "market expansion", "technology acquisition"],
    "trend": ["positive", "unexpected", "significant", "steady", "rapid"],
    "discovery": ["species", "planetary system", "particle", "compound", "phenomenon"],
    "location": ["deep ocean", "distant galaxy", "Arctic region", "rainforest", "ancient ruins"],
    "thing1": ["diet", "exercise", "sleep", "stress", "genetics"],
    "thing2": ["mental health", "longevity", "cognitive function", "immune response", "physical performance"],
    "theory": ["new theory", "alternative hypothesis", "revolutionary concept", "updated model", "novel explanation"],
    "subject": ["human evolution", "climate patterns", "brain function", "universe expansion", "genetic variation"],
    "condition": ["cancer", "heart disease", "diabetes", "alzheimer's", "chronic pain"],
    "health_outcome": ["heart health", "mental clarity", "immune function", "longevity", "cognitive performance"],
    "activity": ["meditation", "exercise", "diet changes", "sleep habits", "stress management"],
    "health_aspect": ["mental health", "cardiovascular health", "immune system", "cognitive function", "physical fitness"],
    "treatment": ["cancer therapy", "gene therapy", "immunotherapy", "regenerative medicine", "targeted treatment"],
    "factor": ["diet", "exercise", "sleep", "stress management", "social connections"],
    "country": ["United States", "China", "European Union", "India", "Japan"],
    "country1": ["United States", "China", "Russia", "European Union", "India"],
    "country2": ["Japan", "South Korea", "Australia", "Brazil", "Canada"],
    "global_issue": ["climate change", "cybersecurity", "public health", "economic cooperation", "renewable energy"],
    "issue": ["climate policy", "trade relations", "technology regulation", "public health", "economic cooperation"],
    "problem": ["climate change", "cybercrime", "food security", "energy crisis", "public health challenges"]
}

def fill_template(template):
    """Fill in a template with random content from the fillers."""
    while '{' in template:
        for key in content_fillers:
            placeholder = '{' + key + '}'
            if placeholder in template:
                template = template.replace(placeholder, str(random.choice(content_fillers[key])))
    return template

def generate_article(category, date):
    """Generate a single article with the given category and date."""
    templates = categories[category]
    headline = fill_template(random.choice(templates["headlines"]))
    description = fill_template(random.choice(templates["desc_templates"]))
    
    # Generate a unique link based on the headline
    link_text = headline.lower().replace(" ", "-").replace(":", "").replace("'", "")
    link = f"https://news-sample.com/article/{link_text}"
    
    return {
        "link": link,
        "headline": headline,
        "category": category,
        "short_description": description,
        "authors": f"{random.choice(['John', 'Jane', 'Michael', 'Sarah', 'David', 'Emma'])} {random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia'])}",
        "date": date.strftime("%Y-%m-%d")
    }

# Generate 100 articles
articles = []
end_date = datetime.now()
current_date = end_date - timedelta(days=100)

for _ in range(100):
    category = random.choice(list(categories.keys()))
    article = generate_article(category, current_date)
    articles.append(article)
    current_date += timedelta(days=1)

# Save to JSON file
with open('Data/news_articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, indent=2, ensure_ascii=False)

print("Generated 100 sample articles and saved to news_articles.json")
