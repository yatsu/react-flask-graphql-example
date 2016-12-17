import { fromJS } from 'immutable';
import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, IndexRoute, browserHistory } from 'react-router';
import { syncHistoryWithStore } from 'react-router-redux';
import ApolloClient, { createNetworkInterface } from 'apollo-client';
import { ApolloProvider } from 'react-apollo';
import App from './containers/App';
import HomeApp from './containers/Home/HomeApp';
import TodoApp from './containers/Todo/TodoApp';
import RemoteTodoApp from './containers/RemoteTodo/RemoteTodoApp';
import configureStore from './redux/store';
import './index.css';

const initialState = {
  todo: fromJS({
    todos: [
      {id: '0', text: 'hello', completed: true},
      {id: '1', text: 'world', completed: false}
    ]
  })
};

const client = new ApolloClient({
  networkInterface: createNetworkInterface({ uri: 'http://localhost:5000/graphql' })
});
const store = configureStore(initialState, client);
const history = syncHistoryWithStore(browserHistory, store)

ReactDOM.render(
  <ApolloProvider store={store} client={client}>
    <Router history={history}>
      <Route path="/" component={App}>
        <IndexRoute component={HomeApp}/>
        <Route path="todo" component={TodoApp}/>
        <Route path="remote" component={RemoteTodoApp}/>
      </Route>
    </Router>
  </ApolloProvider>,
  document.getElementById('root')
);
