# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def dmg_conversion(lst):
  return_list = []
  for i in damages:
    if i == "Damages not recorded":
      return_list.append(i)
    else:
      suffix = i[-1:]
      prefix = i[:-1]
      value = float(prefix) * conversion[suffix]
      return_list.append(value)
  
  return return_list
# test function by updating damages

updated_damages = dmg_conversion(damages)
#print(updated_damages)

# 2 
# Create a Table
def create_dictionary(names, months, years, max_wind, area_affected, damages, deaths):
  ret_dict = {}
  for i in range(len(names)):
    ret_dict[names[i]] = {
      "Name": names[i],
      "Month": months[i],
      "Year": years[i],
      "Max Sustained Wind": max_sustained_winds[i],
      "Areas Affected": areas_affected[i],
      "Damage": updated_damages[i],
      "Deaths": deaths[i]
    }
  
  return ret_dict
# Create and view the hurricanes dictionary

hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)



# 3
# Organizing by Year

def organise_by_year(mydict):
  ret_dict = {}
  for i in hurricanes:
    if hurricanes[i]["Year"]:
      ret_dict[hurricanes[i]["Year"]] = hurricanes[i]
    else:
      print(f"Unable to add {i}")
  return ret_dict

# create a new dictionary of hurricanes with year and key
hurricanes_by_year = organise_by_year(hurricanes)

#for i in hurricanes_by_year:
  #print(hurricanes_by_year[i])

# 4
# Counting Damaged Areas

def counting_areas(hurricanes):
  ret_dict = {}
  for i in hurricanes:
    for j in hurricanes[i]["Areas Affected"]:
      if j in ret_dict:
        ret_dict[j] += 1
      else:
        ret_dict[j] = 1
  return ret_dict

# create dictionary of areas to store the number of hurricanes involved in

areas_aff = counting_areas(hurricanes)
#print(areas_aff)

# 5 
# Calculating Maximum Hurricane Count
def most_affected(areas):
  highest_name = ""
  highest_count = 0
  for i in areas:
    if areas[i] > highest_count:
      highest_count = areas[i]
      highest_name = i
  print(f"The highest area hit was {highest_name} which was hit {highest_count} time(s).")
  return highest_name, highest_count

# find most frequently affected area and the number of hurricanes involved in
highest_place, highest_count = most_affected(areas_aff)


# 6
# Calculating the Deadliest Hurricane
def most_deaths(hurricanes):
  destination = ""
  total = 0

  for i in hurricanes:
    if hurricanes[i]["Deaths"] > total:
      total = hurricanes[i]["Deaths"]
      destination = i
  print(f"The highest number of deaths was caused by {destination} which total'd {total}.")
  return destination, total

# find highest mortality hurricane and the number of deaths
highest_deaths, total_lost = most_deaths(hurricanes)
print(highest_deaths, total_lost)

# 7
# Rating Hurricanes by Mortality

def mortality_calc(hurricanes):
  mort_dict = {0: [],
              1: [],
              2: [],
              3: [],
              4: [],
              5: []}
  for i in hurricanes:
    x = hurricanes[i]["Deaths"]
    rating = 0
    if x == 0:
      mort_dict[0].append(i)
    elif x <= 100:
      mort_dict[1].append(i)
    elif x <= 500:
      mort_dict[2].append(i)
    elif x <= 1000:
      mort_dict[3].append(i)
    elif x <= 10000:
      mort_dict[4].append(i)
    else:
      mort_dict[5].append(i)
  return mort_dict

# categorize hurricanes in new dictionary with mortality severity as key
mortality = mortality_calc(hurricanes)
# 8 Calculating Hurricane Maximum Damage

def most_damages(hurricanes):
  most = ""
  damage = 0.0
  for i in hurricanes:
    if type(hurricanes[i]["Damage"]) != float:
      continue
    elif hurricanes[i]["Damage"] > damage:
      damage = hurricanes[i]["Damage"]
      most = i
  return most, damage


# find highest damage inducing hurricane and its total cost
highest_damages, total_damage = most_damages(hurricanes)
print(f"The highest damage costs were by {highest_damages} costing ${total_damage}0.")

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_calc(hurricanes):
  dam_dict = {"Damages not recorded": [],
              0: [],
              1: [],
              2: [],
              3: [],
              4: [],
              5: []}
  for i in hurricanes:
    x = hurricanes[i]["Damage"]
    rating = 0
    if type(hurricanes[i]["Damage"]) != float:
      dam_dict["Damages not recorded"].append(i)
    elif x == 0:
      dam_dict[0].append(i)
    elif x <= 100000000.0:
      dam_dict[1].append(i)
    elif x <= 1000000000.0:
      dam_dict[2].append(i)
    elif x <= 10000000000.0:
      dam_dict[3].append(i)
    elif x <= 50000000000.0:
      dam_dict[4].append(i)
    else:
      dam_dict[5].append(i)
  return dam_dict
# categorize hurricanes in new dictionary with damage severity as key

damages_cat = damage_calc(hurricanes)
print(damages_cat)
