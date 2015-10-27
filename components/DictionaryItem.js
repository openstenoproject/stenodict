import React, { Component, PropTypes } from 'react'
import { Link } from 'react-router'
import Markdown from './Markdown'

class DictionaryItem extends Component {
  render() {
    const { dictionary } = this.props
    return (
      <li>
        <b>{ `${dictionary.name}: ` }</b>
        { `${dictionary.description.what} -- ` }
        <Link to={`dictionary/${dictionary.filename}`}>
          View
        </Link>
      </li>
    )
  }
}

DictionaryItem.propTypes = { dictionary: React.PropTypes.object.isRequired
                           }

export default DictionaryItem
