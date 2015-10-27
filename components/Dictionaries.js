import React, { Component, PropTypes } from 'react'
import DictionaryItem from './DictionaryItem'

class Dictionaries extends Component {
  render() {
    const { dictionaries } = this.props
    let list = dictionaries.list
    return (
      <ul>
        { Object.keys(list).map(x =>
          (<DictionaryItem key={x} dictionary={list[x]} />)) }
      </ul>
    )
  }
}

Dictionaries.propTypes = { dictionaries: React.PropTypes.object.isRequired
                         }

export default Dictionaries
