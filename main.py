import requests
import json
import csv
import os

def get_one_user():
    response = requests.get("https://randomuser.me/api/")
    user = response.json()['results'][0]

    data = {
        "first_name": user['name']['first'],
        "last_name": user['name']['last'],
        "gender": user['gender'],
        "email": user['email'],
        "phone": user['phone'],
        "address": {
            "street": user['location']['street']['name'],
            "city": user['location']['city'],
            "country": user['location']['country']
        }
    }

    with open("user.json", "w") as f:
        json.dump(data, f, indent=2)
    print("user.json fayli yaratildi.")

def get_10_users():
    response = requests.get("https://randomuser.me/api/?results=10")
    users = response.json()['results']

    data = []
    for user in users:
        data.append({
            "full_name": f"{user['name']['first']} {user['name']['last']}",
            "email": user['email'],
            "gender": user['gender'],
            "country": user['location']['country']
        })

    with open("users.json", "w") as f:
        json.dump(data, f, indent=2)
    print("users.json fayli yaratildi.")

def get_females():
    response = requests.get("https://randomuser.me/api/?results=10&gender=female")
    users = response.json()['results']

    data = []
    for user in users:
        data.append({
            "name": f"{user['name']['first']} {user['name']['last']}",
            "email": user['email'],
            "phone": user['phone'],
            "country": user['location']['country']
        })

    with open("females.json", "w") as f:
        json.dump(data, f, indent=2)
    print("females.json fayli yaratildi.")

def users_with_images():
    response = requests.get("https://randomuser.me/api/?results=10")
    users = response.json()['results']

    data = []
    for user in users:
        data.append({
            "name": f"{user['name']['first']} {user['name']['last']}",
            "email": user['email'],
            "image_url": user['picture']['large']
        })

    with open("users_with_images.json", "w") as f:
        json.dump(data, f, indent=2)
    print("users_with_images.json fayli yaratildi.")

def young_users():
    response = requests.get("https://randomuser.me/api/?results=20")
    users = response.json()['results']

    data = []
    for user in users:
        birth_year = int(user['dob']['date'][:4])
        if birth_year > 1990:
            data.append({
                "name": f"{user['name']['first']} {user['name']['last']}",
                "birth_year": birth_year,
                "email": user['email']
            })

    with open("young_users.json", "w") as f:
        json.dump(data, f, indent=2)
    print("young_users.json fayli yaratildi.")

def users_to_csv():
    response = requests.get("https://randomuser.me/api/?results=10")
    users = response.json()['results']

    with open("users.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Full Name", "Gender", "Email", "Phone", "Country"])

        for user in users:
            writer.writerow([
                f"{user['name']['first']} {user['name']['last']}",
                user['gender'],
                user['email'],
                user['phone'],
                user['location']['country']
            ])
    print("users.csv fayli yaratildi.")

def download_images():
    response = requests.get("https://randomuser.me/api/?results=5")
    users = response.json()['results']

    os.makedirs("images", exist_ok=True)

    for i, user in enumerate(users, 1):
        img_url = user['picture']['large']
        img_data = requests.get(img_url).content
        with open(f"images/user{i}.jpg", "wb") as f:
            f.write(img_data)

    print("5 ta rasm images/ papkaga saqlandi.")

def main():
    while True:
        print("Uyga Vazifalar Menyusi ---")
        print("1. Bitta foydalanuvchini user.json ga yozish")
        print("2. 10 ta foydalanuvchini users.json ga yozish")
        print("3. Faqat ayollarni females.json ga yozish")
        print("4. Rasm bilan users_with_images.json")
        print("5. 1990-yildan keyin tug'ilganlar → young_users.json")
        print("6. users.csv faylga yozish")
        print("7. Rasmlarni yuklab olish (images/user1.jpg...)")
        print("0. Chiqish")
        tanlov = input("Tanlang (0-7): ")

        if tanlov == "1":
            get_one_user()
        elif tanlov == "2":
            get_10_users()
        elif tanlov == "3":
            get_females()
        elif tanlov == "4":
            users_with_images()
        elif tanlov == "5":
            young_users()
        elif tanlov == "6":
            users_to_csv()
        elif tanlov == "7":
            download_images()
        elif tanlov == "0":
            print("Dastur yakunlandi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")

if __name__ == "__main__":
    main()
