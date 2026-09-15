## Django Project

→ Collection of applications.

## Application

→ Specific functionality/module of a project.

## Model

→ Represents database/table.

## View

→ Handles request and response.

## Inheritance

→ Child class gets properties/methods from parent class.

class Manager(Employee):
    pass

Manager → inherits Employee

class QuestionListCreateView(View):
    pass

QuestionListCreateView → inherits View


┌──────────────────────────────────────┐
│              /questions/             │
├──────────────────────────────────────┤
│ class QuestionListCreateView:        │
│                                      │
│     def get(self, request)           │
│     def post(self, request)          │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│           /questions/{pk}/           │
├──────────────────────────────────────┤
│ class QuestionRetrieveUpdateDeleteView:
│                                      │
│     def get(self, request, id)       │
│     def put(self, request, id)       │
│     def delete(self, request, id)    │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│          Model – Question            │
├──────────────────────────────────────┤
│ id                                   │
│ title                                │
│ description                          │
│ score                                │
│ difficulty_level                     │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│               /answers/              │
├──────────────────────────────────────┤
│ class AnswerListCreateView:          │
│                                      │
│     def get(self, request)           │
│     def post(self, request)          │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│            /answers/{pk}/            │
├──────────────────────────────────────┤
│ class AnswerRetrieveUpdateDeleteView:│
│                                      │
│     def get(self, request, id)       │
│     def put(self, request, id)       │
│     def delete(self, request, id)    │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│            Model – Answer            │
├──────────────────────────────────────┤
│ id                                   │
│ solution                             │
│ marks                                │
│ question                             │
│ submitted_by                         │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│                 Apps                 │
├──────────────────────────────────────┤
│ question_app                         │
│ answer_app                           │
└──────────────────────────────────────┘
