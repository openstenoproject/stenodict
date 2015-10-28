import { fetchJSON } from '../util/load'

export const LOAD_DICTIONARIES = 'LOAD_DICTIONARIES'
export const GET_DETAILS = 'GET_DETAILS'
export const FETCHING = 'FETCHING'
export const SUCCESS = 'SUCCESS'
export const FAILURE = 'FAILURE'

export function fetchDictionaries() {
  return dispatch => {
    dispatch({ type: LOAD_DICTIONARIES
             , status: FETCHING
             })
    fetchJSON('dictionaries.json')
      .then(({ tags, dictionaries, formats }) => {
        dispatch({ type: LOAD_DICTIONARIES
                 , status: SUCCESS
                 , tags
                 , formats
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

export function fetchDetails(filename: string) {
  return dispatch => {
    dispatch({ type: GET_DETAILS
             , status: FETCHING
             , filename
             })
    fetchJSON(`dictionaries/${filename}_info.json`)
     .then(({ why, how }) => {
       dispatch({ type: GET_DETAILS
                , status: SUCCESS
                , why
                , how
                , filename
                })
     })
     .catch(error => {
       dispatch({ type: GET_DETAILS
                , status: FAILURE
                , error
                , filename
                })
     })
  }
}
