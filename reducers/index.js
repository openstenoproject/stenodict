import * as ActionTypes from '../actions';
import merge from 'lodash/object/merge';
import tags from './tags';
import dictionaries from './dictionaries';
import details from './details';
import formats from './formats';
import { routerStateReducer as router } from 'redux-router';
import { combineReducers } from 'redux';

const rootReducer = combineReducers({
  router,
  tags,
  formats,
  details,
  dictionaries
});

export default rootReducer;
