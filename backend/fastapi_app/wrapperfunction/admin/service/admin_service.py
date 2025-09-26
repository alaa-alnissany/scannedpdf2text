from admin.model import admin_models

def reply(query:admin_models.UserQuery):
    return {f"User id {query.admin_id} has the query: {query.query}"}