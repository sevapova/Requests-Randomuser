# 🧾 Uyga vazifalar: `requests` + `randomuser.me` + JSON bilan ishlash

### ✅ 1. Bitta foydalanuvchini olib `user.json` faylga yozing

🔗 API manzili: `https://randomuser.me/api/`

📋 **Vazifa:**

1. `GET` so‘rov yuboring.
2. Quyidagi ma'lumotlarni ajrating:

   * `first name`
   * `last name`
   * `gender`
   * `email`
   * `phone`
   * `address`:

     * `street name`
     * `city`
     * `country`
3. `user.json` faylga quyidagicha formatda saqlang:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "gender": "male",
  "email": "johndoe@example.com",
  "phone": "123-456-7890",
  "address": {
    "street": "123 Main Street",
    "city": "New York",
    "country": "United States"
  }
}
```

---

### ✅ 2. 10 ta foydalanuvchini olib `users.json` faylga yozing

🔗 API manzili: `https://randomuser.me/api/?results=10`

📋 **Vazifa:**

1. 10 ta foydalanuvchi oling.
2. Har biri uchun quyidagilarni tayyorlang:

   * `full_name` (`first` + `last`)
   * `email`
   * `gender`
   * `country`
3. Bularni `users.json` faylga quyidagi tarzda yozing:

```json
[
  {
    "full_name": "Alice Smith",
    "email": "alice@example.com",
    "gender": "female",
    "country": "Canada"
  },
  {
    "full_name": "Bob Johnson",
    "email": "bob@example.com",
    "gender": "male",
    "country": "Germany"
  }
]
```

---

### ✅ 3. Faqat ayol foydalanuvchilarni olib `females.json` faylga yozing

🔗 API manzili: `https://randomuser.me/api/?results=10&gender=female`

📋 **Vazifa:**

1. 10 ta **ayol** foydalanuvchini oling.
2. Quyidagi ma'lumotlarni ajrating:

   * `full name`
   * `email`
   * `phone`
   * `country`
3. Ma’lumotlarni `females.json` faylga quyidagicha saqlang:

```json
[
  {
    "name": "Emma Garcia",
    "email": "emma@example.com",
    "phone": "987-654-3210",
    "country": "Spain"
  },
  ...
]
```

---

### ✅ 4. 10 ta foydalanuvchini `users_with_images.json` faylga yozing

🔗 API: `https://randomuser.me/api/?results=10`

📋 **Vazifa:**

1. Har foydalanuvchi uchun:

   * `full name`
   * `email`
   * `picture.large` rasm manzili
2. `users_with_images.json` faylga quyidagicha yozing:

```json
[
  {
    "name": "Laura White",
    "email": "laura@example.com",
    "image_url": "https://randomuser.me/api/portraits/women/75.jpg"
  }
]
```

---

### ✅ 5. 20 ta foydalanuvchini olib, 1990-yildan keyin tug‘ilganlarni `young_users.json` faylga yozing

🔗 API: `https://randomuser.me/api/?results=20`

📋 **Vazifa:**

1. 1990 yildan keyin tug‘ilganlarni ajrating (`dob.date`)
2. Quyidagilarni yozing:

   * `name`
   * `birth_year`
   * `email`
3. `young_users.json` faylga quyidagicha yozing:

```json
[
  {
    "name": "Daniel Brown",
    "birth_year": 1998,
    "email": "daniel@example.com"
  }
]
```

📌 **Eslatma:** `dob.date` format: `"1998-05-17T10:23:45.123Z"` → `birth_year = 1998`

---

### ✅ 6. Barcha foydalanuvchilarni CSV formatga o‘tkazing

🔗 API: `https://randomuser.me/api/?results=10`

📋 **Vazifa:**

1. Quyidagilarni `users.csv` faylga yozing:

   * `Full Name`
   * `Gender`
   * `Email`
   * `Phone`
   * `Country`

📄 CSV fayl format:

```
Full Name,Gender,Email,Phone,Country
Alice Smith,female,alice@example.com,123-456-7890,USA
Bob Jones,male,bob@example.com,321-987-6543,UK
```

> 💡 `csv` moduli ishlatiladi (`import csv`)

---

### ✅ 7. Bonus: Rasm fayllarini yuklab olish

🔗 API: `https://randomuser.me/api/?results=5`

📋 **Vazifa:**

1. Har bir foydalanuvchining `picture.large` URL’ini oling.
2. Har bir rasmni `images/` papkaga saqlang: `user1.jpg`, `user2.jpg`, ...

💡 `requests.get(image_url).content` yordamida rasm faylini yozing.


