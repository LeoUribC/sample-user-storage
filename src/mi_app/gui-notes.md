# Jerarquia

```bash
nombre-del-proyecto/
│
├── data/
│   └── database.json
│
├── src/
│   └── mi_app/
│       ├ __init__.py
│       ├ models/
│       ├ services/
│       ├ storage/
│       └ exceptions.py
│
├── interfaces/
│   ├ cli/
│   │   └ main.py
│   │
│   └ gui/
│       └ streamlit_app.py
│
├── tests/
│
├── docs/
│
├── pyproject.toml
└── README.md
```

Minimal streamlit app:

```python
import streamlit as st

from mi_app.services import UserService
from mi_app.storage import JSONStorage

storage = JSONStorage("data/database.json")
service = UserService(storage)

st.title("User Manager")

name = st.text_input("Name")
email = st.text_input("Email")

if st.button("Create user"):

    user = service.create_user(name, email)

    st.success(f"User created with id {user.id}")
```

Complete minimal app:

```python
import streamlit as st
from mi_app.services import UserService
from mi_app.storage import JSONStorage

storage = JSONStorage("data/database.json")
service = UserService(storage)

st.title("User Manager")

# ----------------------
# Create user
# ----------------------

name = st.text_input("Name")
email = st.text_input("Email")

if st.button("Create user"):
    user = service.create_user(name, email)
    st.success(f"User created with id {user.id}")

# ----------------------
# List users
# ----------------------

users = service.get_all_users()

st.subheader("Users")

st.table([
    {
        "id": u.id,
        "name": u.name,
        "email": u.email
    }
    for u in users
])

# ----------------------
# Deactivate user
# ----------------------

user_id = st.number_input("User ID", min_value=1)

if st.button("Deactivate user"):
    service.deactivate_user(user_id)
    st.success("User deactivated")
```
