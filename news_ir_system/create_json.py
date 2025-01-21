import json

articles = [
    {
        "link": "https://www.huffpost.com/entry/covid-boosters-uptake-us_n_632d719ee4b087fae6feaac9",
        "headline": "Over 4 Million Americans Roll Up Sleeves For Omicron-Targeted COVID Boosters",
        "category": "U.S. NEWS",
        "short_description": "Health experts said it is too early to predict whether demand would match up with the 171 million doses of the new boosters the U.S. ordered for the fall.",
        "authors": "Carla K. Johnson, AP",
        "date": "2022-09-23"
    },
    {
        "link": "https://www.huffpost.com/entry/american-airlines-passenger-banned-flight-attendant-punch-justice-department_n_632e25d3e4b0e247890329fe",
        "headline": "American Airlines Flyer Charged, Banned For Life After Punching Flight Attendant On Video",
        "category": "U.S. NEWS",
        "short_description": "He was subdued by passengers and crew when he fled to the back of the aircraft after the confrontation, according to the U.S. attorney's office in Los Angeles.",
        "authors": "Mary Papenfuss",
        "date": "2022-09-23"
    },
    {
        "link": "https://www.huffpost.com/entry/funniest-tweets-cats-dogs-september-17-23_n_632de332e4b0695c1d81dc02",
        "headline": "23 Of The Funniest Tweets About Cats And Dogs This Week (Sept. 17-23)",
        "category": "COMEDY",
        "short_description": "Until you have a dog you don't understand what could be eaten.",
        "authors": "Elyse Wanshel",
        "date": "2022-09-23"
    }
]

with open('Data/news_articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, indent=2, ensure_ascii=False)
