import { fetchJSON } from '../util/load'

export const LOAD_DICTIONARIES = 'LOAD_DICTIONARIES'
export const GET_DETAILS = 'GET_DETAILS'
export const FETCHING = 'FETCHING'
export const SUCCESS = 'SUCCESS'
export const FAILURE = 'FAILURE'
export const APPLY_FILTERS = 'APPLY_FILTERS'
export const CLEAR_FILTERS = 'CLEAR_FILTERS'
export const TOGGLE_FILTER = 'TOGGLE_FILTER'

export function fetchDictionaries() {
  return dispatch => {
    dispatch({ type: LOAD_DICTIONARIES
             , status: FETCHING
             })
    fetchJSON(`dictionaries.json`)
      .then(({ tags, dictionaries, formats }) => {
        dispatch({ type: LOAD_DICTIONARIES
                 , status: SUCCESS
                 , tags
                 , formats
                 , dictionaries
                 })
        dispatch(applyFilters())
      })
      .catch(error => {
        dispatch({ type: LOAD_DICTIONARIES
                 , status: FAILURE
                 , error
                 })
      })
  }
}

export function toggleFilter({ tag = null, format = null }) {
  return dispatch => {
    dispatch(
      { type: TOGGLE_FILTER
      , tag
      , format
      }
    )
    dispatch(applyFilters())
  }
  }

export function clearFilters() {
  return (dispatch, getState) => {
    const { tags, formats, dictionaries } = getState()
    dispatch({ type: CLEAR_FILTERS
             , tags
             , formats
             , dictionaries
             })
    dispatch(applyFilters())
  }}

export function applyFilters() {
  return (dispatch, getState) => {
    const { tags, formats, dictionaries } = getState()
    dispatch({ type: APPLY_FILTERS
             , tags
             , formats
             , dictionaries
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
