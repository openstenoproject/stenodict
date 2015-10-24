import { LOAD_DICTIONARIES, FETCHING, SUCCESS, FAILURE } from '../actions'

export default function dictionaries(state = { fetching: false
                                             , list: []
                                             , error: null
                                             }
                                    , action
                                    ) {
  switch (action.type) {
  case LOAD_DICTIONARIES:
    switch (action.status) {
      case FETCHING:
        return { ...state
               , fetching: true
               , error: null
               }
      case SUCCESS:
        return { ...state
               , fetching: false
               , list: action.dictionaries
               }
      case FAILURE:
        return { ...state
               , fetching: false
               , error: action.error
               }
    }
  	return state
  default:
    return state
  }
}
