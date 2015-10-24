import * as ActionTypes from '../actions';
import merge from 'lodash/object/merge';
import tags from './tags';
import dictionaries from './dictionaries';
import { routerStateReducer as router } from 'redux-router';
import { combineReducers } from 'redux';

const rootReducer = combineReducers({
  router,
  tags,
  dictionaries
});

export default rootReducer;
