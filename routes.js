import React from 'react';
import { Route, IndexRoute } from 'react-router';
import App from './containers/App';
import DictionaryPage from './containers/DictionaryPage'
import DictionariesPage from './containers/DictionariesPage'

export default (
  <Route path="/" component={App}>
    <IndexRoute component={DictionariesPage} />
    <Route path="main" component={DictionariesPage} />
    <Route path="dictionary/:dictionary" component={DictionaryPage} />
  </Route>
);
