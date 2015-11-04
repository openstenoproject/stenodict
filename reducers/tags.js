import { LOAD_DICTIONARIES
       , SUCCESS
       , TOGGLE_FILTER
       , CLEAR_FILTERS
       } from '../actions';

export default function tags(state = {}, action) {
  switch (action.type) {
  case LOAD_DICTIONARIES:
    switch (action.status) {
    case SUCCESS:
      const { tags, dictionaries } = action
      const filtered = Object.keys(tags).map(key => {
        // Count how many dictionaries have each tag
        let count = Object.keys(dictionaries).reduce((prev, next) => {
          let tags = dictionaries[next].tags
          let nKey = parseInt(key, 10)
          if (tags.includes(nKey)) {
            return prev + 1
          }
          return prev
        }, 0)
        return { key, count, label: tags[key], selected: false }
      })
      // Forget about tags that aren't used
      .filter(x => x.count > 0)
      // Turn back into an object
      .reduce((p, n) => {
        p[n.key] = n
        return p
      }, {})
      return { ...filtered }
    }
  case TOGGLE_FILTER:
    const { tag } = action
    if (tag === null || tag === undefined) {
      return state
    }
    return { ...state
           , [tag]: { ...state[tag]
                    , selected: !state[tag].selected
                    }
           }
  case CLEAR_FILTERS:
    let newState = { ...state }
    newState = Object.keys(newState)
      .reduce((p, n) => {
        p[n] = newState[n]
        p[n].selected = false
        return p
      }, {})
    return newState
  default:
    return state;
  }
}
