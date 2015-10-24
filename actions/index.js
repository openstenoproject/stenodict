import { fetchJSON } from '../util/load'

export const LOAD_DICTIONARIES = 'LOAD_DICTIONARIES'
export const FETCHING = 'FETCHING'
export const SUCCESS = 'SUCCESS'
export const FAILURE = 'FAILURE'

export function fetchDictionaries() {
  return dispatch => {
    dispatch({ type: LOAD_DICTIONARIES
             , status: FETCHING
             })
    fetchJSON('http://www.tedmor.in/stenodict/dictionaries.json')
      .then(({ tags, dictionaries }) => {
        dispatch({ type: LOAD_DICTIONARIES
                 , status: SUCCESS
                 , tags
                 , dictionaries
                 })
      })
      .catch(error => {
        dispatch({ type: LOAD_DICTIONARIES
                 , status: FAILURE
                 , error
                 })
      })
  }
}
