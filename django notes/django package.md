## package install
pip install django

                         Django
                            │
        ┌───────────────────┼───────────────────┐
        ↓                   ↓                   ↓
      utils                http                urls
        │                   │                   │
   decorators         JsonResponse        path(route, view)
        │
 method_decorator()


                         Django
                            │
                  ┌─────────┴─────────┐
                  ↓                   ↓
                  db                views
                  │                   │
             models.py          ┌────┴─────┐
                  │              ↓          ↓
             class Model      generic    decorators
                                  │          │
                             class View     csrf
                                             │
                                      csrf_exempt()


## CSRF
→ Cross-Site Request Forgery
→ Django security protection.

## csrf_exempt
→ Disables CSRF checking for a view.

@method_decorator(csrf_exempt, name="dispatch")

## method_decorator
→ Applies a function decorator to a class-based view.

## dispatch 
→ Sends the request to the correct method. = json data

GET → get()
POST → post()
PUT → put()
DELETE → delete()

## request.body
→ Gets raw data from the client request.

request.body

## loads()
→ Converts JSON string/data → Python object.

form_data = loads(request.body)

## load()
→ Converts JSON file → Python object.

loads → string
load  → file

## Python Native Type

JSON → loads() → Python Dictionary                                      