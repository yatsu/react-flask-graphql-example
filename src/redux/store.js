import { createStore, applyMiddleware, compose } from 'redux';
import { browserHistory } from 'react-router';
import { routerMiddleware } from 'react-router-redux';
import configureRootReducer from './reducer';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

export default function configureStore(initialState, client) {
  const rootReducer = configureRootReducer(client);
  return createStore(rootReducer, initialState, composeEnhancers(
    applyMiddleware(routerMiddleware(browserHistory)),
    applyMiddleware(client.middleware())
  ));
}
