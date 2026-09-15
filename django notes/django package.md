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