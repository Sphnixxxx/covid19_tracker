import requests
#for global stat
def get_global_data():
    url = "https://disease.sh/v3/covid-19/all"
    response = requests.get(url)
    data = response.json()
    
    print("\n   GLOBAL COVID-19 STATS   ")
    print(f"Total Cases: {data['cases']:,}")
    print(f"Total Deaths: {data['deaths']:,}")
    print(f"Total Recovered: {data['recovered']:,}")
    print(f"Active Cases: {data['active']:,}")
    print(f"Today Cases: {data['todayCases']:,}")
    print(f"Today Deaths: {data['todayDeaths']:,}")

#for country stat
def get_country_data():
    country = input("Enter country name: ").strip()
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)
    if response.status_code == 404:
        print("Country not found! ")
        return
    data = response.json()
    
    print(f"\n  COVID-19 STATS FOR {data['country'].upper()}")
    print(f"Total Cases: {data['cases']:,}")
    print(f"Total Deaths: {data['deaths']:,}")
    print(f"Total Recovered: {data['recovered']:,}")
    print(f"Active Cases: {data['active']:,}")
    print(f"Today Cases: {data['todayCases']:,}")
    print(f"Today Deaths: {data['todayDeaths']:,}")
    print(f"Population: {data['population']:,}")

def compare_countries():
    country1 = input("Enter first country: ").strip()
    country2 = input("Enter second country: ").strip()
    url1 = f"https://disease.sh/v3/covid-19/countries/{country1}"
    url2 = f"https://disease.sh/v3/covid-19/countries/{country2}"
    data1 = requests.get(url1).json()
    data2 = requests.get(url2).json()
    
    print(f"\n  COMPARISON  ")
    print(f"\n{data1['country']}:")
    print(f"    Total Cases: {data1['cases']:,}")
    print(f"    Total Deaths: {data1['deaths']:,}")
    print(f"    Total Recovered: {data1['recovered']:,}")
    print(f"    Active Cases: {data1['active']:,}")
    
    print(f"\n{data2['country']}:")
    print(f"    Total Cases: {data2['cases']:,}")
    print(f"    Total Deaths: {data2['deaths']:,}")
    print(f"    Total Recovered: {data2['recovered']:,}")
    print(f"    Active Cases: {data2['active']:,}")
    

while True:
    print("\n1. Global Stats")
    print("2. Country Stats")
    print("3. Compare Countries")
    print("4. Exit")
    
    choice = input("\nChoose option (1-4): ").strip()
    if choice == '1':
        get_global_data()
    elif choice == '2':
        get_country_data()
    elif choice == '3':
        compare_countries()
    elif choice == '4':
        print("Thanks for using the tracker")
        break
    else:
        print("Invalid !")
