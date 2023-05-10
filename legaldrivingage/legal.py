legal_age_driving = {
    'Africa': {'Eswatini': '18', 'Ethiopia': '18', 'Ghana': '18', 'Kenya': '18', 'Lesotho': '18',
                             'Libya': '18', 'Mali': '18', 'Mauritania': '18', 'Mauritius': '18', 'Mayotte': '18',
                             'Morocco': '18', 'Mozambique': '17', 'Namibia': '18', 'Niger': '23', 'Nigeria': '18',
                             'Réunion (France)': '18', 'Rwanda': '18', 'Senegal': '18', 'South Africa': '17',
                             'Tanzania': '18', 'Tunisia': '18', 'Zambia': '16', 'Zimbabwe': '16'},
    'Americas': {'Canada': '16', 'Mexico': '18', 'United States': '17', 'Costa Rica': '18',
                               'El Salvador': '18', 'Guatemala': '18', 'Honduras': '18', 'Nicaragua': '18',
                               'Panama': '18', 'Argentina': '18', 'Bolivia': '18', 'Brazil': '18', 'Chile': '18',
                               'Colombia': '18', 'Ecuador': '18', 'Falkland Islands': '17', 'French Guiana': '18',
                               'Guyana': '17', 'Paraguay': '18', 'Peru': '18', 'Suriname': '18', 'Uruguay': '18',
                               'Venezuela': '18', 'Anguilla': '18', 'Bahamas': '17', 'Cuba': '18',
                               'Cayman Islands': '17', 'Dominican Republic': '16', 'Guadeloupe': '18', 'Jamaica': '18',
                               'Martinique': '18', 'Netherlands Antilles': '18', 'Puerto Rico': '18',
                               'Saint Barthélemy': '18', 'Saint Martin': '18', 'Trinidad and Tobago': '17',
                               'St. Kitts and Nevis': '18', 'US Virgin Islands': '18'},
    'Asia': {'Bahrain': '18', 'Iran': '18', 'Iraq': '18', 'Israel': '17', 'Jordan': '18', 'Kuwait': '18',
                           'Lebanon': '18', 'Oman': '18', 'Qatar': '18', 'Saudi Arabia': '18', 'Syria': '18',
                           'United Arab Emirates': '18', 'Yemen': '18', 'Afghanistan': '18', 'Bangladesh': '18',
                           'India': '18', 'Nepal': '18', 'Pakistan': '18', 'SriLanka': '17', 'Maldives': '18',
                           'China': '18', 'HongKong': '18', 'Japan': '18', 'Macau': '18', 'SouthKorea': '18',
                           'Taiwan': '18', 'Brunei': '18', 'Myanmar': '18', 'Cambodia': '18', 'Indonesia': '17',
                           'Laos': '18', 'Malaysia': '17', 'Philippines': '17', 'Singapore': '18', 'Thailand': '18',
                           'Vietnam': '18'},
    'Europe': {'Austria': '17', 'Belgium': '18', 'Bulgaria': '18', 'Croatia': '18', 'Cyprus': '18', 'Czech Republic': '18',
                           'Denmark': '17', 'Estonia': '18', 'Finland': '18', 'France': '18', 'Germany': '18', 'Gibraltar': '17',
                           'Greece': '18', 'Hungary': '18', 'Iceland': '17', 'Ireland': '17', 'Italy': '18', 'Latvia': '18',
                           'Liechtenstein': '18', 'Lithuania': '18', 'Luxembourg': '18', 'Malta': '18', 'Netherlands': '18',
                           'Norway': '18', 'Poland': '18', 'Portugal': '18', 'Romania': '18', 'Slovakia': '18', 'Slovenia': '18',
                           'Spain': '18', 'Sweden': '18', 'Switzerland': '18', 'United Kingdom': '18', 'Albania': '18', 'Andorra': '18',
                           'Armenia': '18', 'Azerbaijan': '18', 'Belarus': '18', 'Bosnia and Herzegovina': '18', 'Georgia': '17',
                           'Guernsey': '17', 'Isle of Man': '16', 'Jersey': '17', 'Kosovo': '18', 'Moldova': '18', 'Monaco': '18',
                           'Montenegro': '18', 'Northern Cyprus': '18', 'North Macedonia': '18', 'Russia': '18', 'San Marino': '18',
                           'Turkey': '18', 'Ukraine': '18'},
    'Oceania': {'Australia': '18', 'Fiji': '17', 'Marshall Islands': '18', 'New Zealand': '16', 'Papua New Guinea': '18', 'Tonga': '18'}}

try:
    age_of_user = int(input("What is your age? "))
    assert age_of_user > 0
except (ValueError, AssertionError):
    print("The input is not valid. Please enter valid number.")
else:
    for continent in legal_age_driving:
        print(continent, ":")
        country = []
        for key, value in legal_age_driving[continent].items():
            if age_of_user >= int(value):
                country.append(key)
        if len(country) == 0:
            print(f"You are not allowed to drive anywhere at the age of {age_of_user}")
        else:
            print(", ".join(country))
        print()
    # if legal_age_driving > age_of_user:
    #     print("You are not old enough to legally drive.")
    # else:
    #     print("You are old enough to legally drive.")

