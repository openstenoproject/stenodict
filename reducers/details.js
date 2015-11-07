import { FETCHING
       , SUCCESS
       , FAILURE
       , GET_DETAILS
       } from '../actions'

export default function details(state = {}, action) {
  switch (action.type) {
  case GET_DETAILS:
    let { filename } = action
    switch (action.status) {
    case FETCHING:
      return { ...state
             , [filename]: { isLoading: true }
             }
    case SUCCESS:
      let { why, how, version = 1 } = action
      return { ...state
             , [filename]: { why, how, version, isLoading: false }
             }
    case FAILURE:
      let { error } = action
      return { ...state
             , [filename]: { isLoading: false, error }
             }
    }
  default:
    return state
  }
}
