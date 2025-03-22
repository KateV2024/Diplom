valid_new_task = {
  "title": "Kate1",
  "description": "My first task",
  "completed": True,
  "user_id": 31
}

invalid_new_task = {
  "title": "",
  "description": "",
  "completed": True
}

valid_user = {
  "username": "Kate10",
  "password": "test1"

}

updated_task = {
  "title": "Kate11",
  "description": "My updated task",
  "completed": True
}

headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}