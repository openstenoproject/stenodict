import { APPLY_FILTERS
       , TOGGLE_FILTER
       , CLEAR_FILTERS
       } from '../actions'

export default function filtered(state = []
                                    , action
                                    ) {
  switch (action.type) {
  case APPLY_FILTERS:
    const { tags, formats, dictionaries } = action
    const { list } = dictionaries
    let selectedTags = Object.keys(tags)
      .filter(x => tags[x].selected)
    let filtered = Object.keys(list)
    if (selectedTags.length !== 0) {
      filtered = filtered
        .filter(x =>
          selectedTags.every(y =>
            list[x].tags.includes(parseInt(y, 10))
          )
        )
    }
    filtered = filtered.sort((a, b) =>
      list[a].name
        .localeCompare(list[b].name)
    )
    return filtered
  default:
    return state
  }
}
