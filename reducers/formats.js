import { LOAD_DICTIONARIES, SUCCESS } from '../actions';

export default function formats(state = {}, action) {
  switch (action.type) {
  case LOAD_DICTIONARIES:
    switch (action.status) {
    case SUCCESS:
      return { ...action.formats }
    }
  default:
    return state;
  }
}
