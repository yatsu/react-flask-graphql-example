from collections import namedtuple, OrderedDict
from graphql import (
    GraphQLField, GraphQLNonNull, GraphQLArgument,
    GraphQLObjectType, GraphQLList, GraphQLBoolean, GraphQLString,
    GraphQLSchema
)


Todo = namedtuple('Todo', 'id text completed')

TodoList = namedtuple('TodoList', 'todos')

TodoType = GraphQLObjectType(
    name='Todo',
    fields=lambda: {
        'id': GraphQLField(
            GraphQLNonNull(GraphQLString),
        ),
        'text': GraphQLField(
            GraphQLString
        ),
        'completed': GraphQLField(
            GraphQLBoolean
        )
    }
)

TodoListType = GraphQLObjectType(
    name='TodoList',
    fields=lambda: {
        'todos': GraphQLField(
            GraphQLList(TodoType),
            resolver=lambda todo_list, *_: get_todos(todo_list),
        )
    }
)


todo_data = OrderedDict({
    '1': Todo(id='1', text='Make America Great Again', completed=False),
    '2': Todo(id='2', text='Quit TPP', completed=False)
})


def get_todo_list():
    return TodoList(todos=todo_data.keys())


def get_todo(id):
    return todo_data.get(id)


def get_todos(todo_list):
    return map(get_todo, todo_list.todos)


def get_todo_single():
    return Todo(id=1, text='Make America Great Again', completed=False)


def add_todo(text):
    todo = Todo(id=str(len(todo_data) + 1), text=text, completed=False)
    todo_data[todo.id] = todo
    return todo


def toggle_todo(id):
    cur_todo = todo_data[id]
    todo = Todo(id=id, text=cur_todo.text, completed=not cur_todo.completed)
    todo_data[id] = todo
    return todo


QueryRootType = GraphQLObjectType(
    name='Query',
    fields=lambda: {
        'test': GraphQLField(
            GraphQLString,
            args={
                'who': GraphQLArgument(GraphQLString)
            },
            resolver=lambda root, args, *_:
                'Hello %s' % (args.get('who') or 'World')
        ),
        'todo': GraphQLField(
            TodoType,
            resolver=lambda root, args, *_: get_todo_single(),
        ),
        'todoList': GraphQLField(
            TodoListType,
            resolver=lambda root, args, *_: get_todo_list(),
        )
    }
)


MutationRootType = GraphQLObjectType(
    name='Mutation',
    fields=lambda: {
        'addTodo': GraphQLField(
            TodoType,
            args={
                'text': GraphQLArgument(GraphQLString)
            },
            resolver=lambda root, args, *_: add_todo(args.get('text'))
        ),
        'toggleTodo': GraphQLField(
            TodoType,
            args={
                'id': GraphQLArgument(GraphQLString)
            },
            resolver=lambda root, args, *_: toggle_todo(args.get('id'))
        )
    }
)

Schema = GraphQLSchema(QueryRootType, MutationRootType)
