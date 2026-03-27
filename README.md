# 🔐 Password Generator

A fully-featured command-line password manager built in Python. Generates
cryptographically random passwords with customisable character sets, analyses
their strength visually, and saves them locally with labels for easy reference.

Built as the Month 4 capstone project of a 12-month Python learning roadmap,
this project focuses on modular function architecture, algorithmic generation
logic and JSON persistence.

![demo](assets/demo.gif)

---

## ✨ Features

- Customisable character sets — toggle lowercase, uppercase, digits and symbols independently
- Guaranteed character diversity — at least one character from each selected category
- Visual strength analyser with percentage bar and four-tier rating system
- Save passwords with custom labels and automatic date stamping
- View all saved passwords in a clean numbered list
- View a single saved password by index
- Delete saved passwords with confirmation prompt
- Full input validation on every field — handles letters, empty input and out-of-range values

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- No external dependencies — standard library only

### Installation & Run

```bash
git clone https://github.com/ERYXGF/password-generator.git
cd password-generator
python main.py
```

---

## 🕹 How to Use

Run `python main.py`. The main menu presents five options. Navigate by
entering the corresponding number. Option 1 walks you through generation
settings before displaying your password with its strength analysis.

```
+---------------------------------------------------------------------+
|                          PASSWORD GENERATOR                         |
+---------------------------------------------------------------------+
|     1) Generate a password                                          |
|     2) List all passwords                                           |
|     3) Save a password (with a label)                               |
|     4) View a specific saved password                               |
|     5) Delete a saved password                                      |
+---------------------------------------------------------------------+
```

---

## 🔒 Strength Rating System

Passwords are scored 0–100 based on length and character diversity.
Each tier requires both sufficient length and category variety to reach.

| Rating       | Score | Criteria                                     |
|--------------|-------|----------------------------------------------|
| Faible ❌    | 0–39  | Too short or single category                 |
| Moyen ⚠️    | 40–59 | Moderate length, limited variety             |
| Fort ✅      | 60–79 | Good length and multiple categories          |
| Très fort 💪 | 80–100| Long password with full character diversity  |

The visual bar displays as `[████████░░] 80%` directly beneath each
generated password.

---

## 🗂 Project Structure

```
password-generator/
├── main.py              # Entry point — menu loop and user interaction
├── generator.py         # Character pool building and password generation
├── analyser.py          # Strength scoring, rating and visual bar
├── storage.py           # JSON persistence — load, save, add, delete
├── display.py           # All terminal output functions
├── passwords_example.json
├── .gitignore
├── README.md
└── LICENSE
```

---

## 📁 Data Structure

Passwords are stored in `passwords.json` as a list of dictionaries:

```json
[
    {
        "label": "GitHub",
        "password": "Kx9#mP2$vL8@qR3!",
        "strength": "Très fort 💪",
        "date": "2025-03-20"
    },
    {
        "label": "Gmail",
        "password": "correct7Horse!blue",
        "strength": "Fort ✅",
        "date": "2025-03-20"
    }
]
```

---

## 🛠 Built With

- Python 3.11
- Standard library only — `string`, `random`, `json`, `datetime`, `pathlib`

---

## 📚 What I Learned

- Designing a multi-file project with strict separation of concerns across five files
- Implementing a guaranteed character diversity algorithm using list building and shuffling
- Building a mathematical scoring system with progressive length milestones
- Generating visual progress bars purely through string manipulation
- Full CRUD operations on a JSON list structure with pathlib file handling
- Writing reusable validation loops that never crash on bad input
- Designing a public-facing wrapper function that composes three internal functions

---

## 🗺 Future Improvements

- [ ] Copy password to clipboard automatically using the pyperclip library
- [ ] Add a passphrase generator mode using random words joined by symbols
- [ ] Check generated passwords against a list of the 100 most common passwords
- [ ] Add password expiry warnings for entries older than 90 days
- [ ] Master password protection for the saved passwords file

---

## ⚠️ Security Note

Passwords are saved in plain unencrypted JSON and are accessible to anyone
with access to the file. This project is a Python learning exercise, not a
production security tool. A real password manager uses strong encryption
such as AES-256 to protect stored credentials. Never store real sensitive
passwords using this tool.

---

## 📄 Licence

This project is licensed under the GPL-3.0 Licence.
See the [LICENSE](LICENSE) file for details.

---

*Project 4 of 12 — Python learning roadmap | Built by [Eryx Grammatikas](https://github.com/ERYXGF)*
