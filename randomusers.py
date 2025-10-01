from dataset import randomuser_data
from pprint import pprint


def get_full_names(data: dict) -> list[str]:
    """
    Returns a list of users' full names in 'First Last' format.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[str]: List of full names.
    """
    names = []
    for user in data['results']:
        GetName = user["name"]
        fullName = f"{GetName['first']} {GetName['last']}"
        names.append(fullName)
    return names

# pprint(get_full_names(randomuser_data))


def get_users_by_country(data: dict, country: str) -> list[dict]:
    """
    Filters and returns users who live in a specific country.

    Args:
        data (dict): JSON data containing user records.
        country (str): Country name to filter by.

    Returns:
        list[dict]: List of dictionaries containing full name and email of matching users.
    """
    result = []
    for user in data['results']:
        GetName = user["name"]
        fullName = f"{GetName['first']} {GetName['last']}"

        if country in user['location']['country']:result.append({'name': fullName, 'email': user['email'], 'country': user['location']['country']})
    return result

# pprint(get_users_by_country(randomuser_data, 'Ireland'))


def count_users_by_gender(data: dict) -> dict:
    """
    Counts the number of users by gender.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with gender as keys and count as values.
    """
    result = {'male': 0, 'female': 0}
    for user in data['results']:
        if user['gender'] == 'male':result['male'] += 1
        elif user['gender'] == 'female':result['female'] += 1
    return result

# print(count_users_by_gender(randomuser_data))


def get_emails_of_older_than(data: dict, age: int) -> list[str]:
    """
    Returns a list of emails of users older than the given age.

    Args:
        data (dict): JSON data containing user records.
        age (int): Age threshold.

    Returns:
        list[str]: List of email addresses.
    """
    result = []
    for user in data['results']:
        if user['dob']['age'] > age: result.append(user['email'])
    return result

# print(get_emails_of_older_than(randomuser_data, 60)) # FIXME: yangi narsa borligi sabab tashlab ketildi


def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:
    """
    Sorts users by age in ascending or descending order.

    Args:
        data (dict): JSON data containing user records.
        descending (bool, optional): Whether to sort in descending order. Defaults to False.

    Returns:
        list[dict]: List of users with name and age sorted accordingly.
    """
    result = []
    for user in data['results']:
        result.append({'name': f"{user['name']['first']} {user['name']['last']}", 'age': user['dob']['age']})
    return 

# pprint(sort_users_by_age(randomuser_data))

    

def get_usernames_starting_with(data: dict, letter: str) -> list[str]:
    """
    Returns a list of usernames starting with a given letter.

    Args:
        data (dict): JSON data containing user records.
        letter (str): The starting letter to filter usernames.

    Returns:
        list[str]: List of matching usernames.
    """
    result = []
    for user in data['results']:
        if letter in user['login']['username'][0]:result.append(user['login']['username'])
    return result

# pprint(get_usernames_starting_with(randomuser_data, 'g'))


def get_average_age(data: dict) -> float:
    """
    Calculates and returns the average age of users.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        float: Average age.
    """
    result = 0
    count = 0
    for user in data['results']:
        result+=user['dob']['age']
        count+=1
    return result / count

# pprint(get_average_age(randomuser_data))


def group_users_by_nationality(data: dict) -> dict:
    """
    Groups and counts users by their nationality.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with nationality as keys and count as values.
    """
    result = {}
    for user in data['results']:
        result.setdefault(user['nat'], 0)
        result[user['nat']] += 1
    return result

# print(group_users_by_nationality(randomuser_data))


def get_all_coordinates(data: dict) -> list[tuple[str, str]]:
    """
    Extracts all users' coordinates as tuples of (latitude, longitude).

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[tuple[str, str]]: List of coordinate tuples.
    """
    result = []
    for user in data['results']:
        result.append((user['location']['coordinates']['latitude'], user['location']['coordinates']['longitude']))
    return result

# print(get_all_coordinates(randomuser_data))


def get_oldest_user(data: dict) -> dict:
    """
    Finds and returns the oldest user's name, age, and email.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary containing 'name', 'age', and 'email' of the oldest user.
    """
    mx = data['results'][0]
    for user in data['results']:
        if user['dob']['age'] > mx['dob']['age']:mx=user
    result = {'name': f"{mx['name']['first']} {mx['name']['last']}", "age": mx['dob']['age'], "email": mx['email'] }
    return result

# print(get_oldest_user(randomuser_data))


def find_users_in_timezone(data: dict, offset: str) -> list[dict]:
    """
    Returns users whose timezone offset matches the given value.

    Args:
        data (dict): JSON data containing user records.
        offset (str): Timezone offset (e.g. '+5:30').

    Returns:
        list[dict]: List of users with full name and city.
    """
    
    result = []

    for user in data['results']:
        if user['location']['timezone']['offset'] == offset:
            result.append({"name": f"{user['name']['first']} {user['name']['last']}", "city": user['location']['city']})
    return result

# print(find_users_in_timezone(randomuser_data, "+5:30"))


def get_registered_before_year(data: dict, year: int) -> list[dict]:
    """
    Returns users who registered before a given year.

    Args:
        data (dict): JSON data containing user records.
        year (int): Year threshold.

    Returns:
        list[dict]: List of users with full name and registration date.
    """
    result = []

    for user in data['results']:
        if int(user['registered']['date'][:4]) < year:
            result.append({"name": f"{user['name']['first']} {user['name']['last']}", "registered": user['registered']['date'][:10]})
    return result

# pprint(get_registered_before_year(randomuser_data, 2010))

