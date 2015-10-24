import { LOAD_DICTIONARIES, STATUS } from '../actions';

export default function tags(state = 0, action) {
  switch (action.type) {
  case LOAD_DICTIONARIES:
  	return state;
  default:
    return state;
  }
}
