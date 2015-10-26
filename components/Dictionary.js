import React, { Component, PropTypes } from 'react'
import Markdown from './Markdown'

class Dictionary extends Component {
  render() {
    const { dictionary } = this.props
    return (
      <li>
        <b>{ `${dictionary.name}: ` }</b>
        { `${dictionary.description.what} -- ` }
        <a href={`dictionaries/${dictionary.filename}`}>
          Download
        </a>
        <Markdown paragraphs={dictionary.description.how}></Markdown>
      </li>
    )
  }
}

Dictionary.propTypes = { dictionary: React.PropTypes.object.isRequired
                       }

export default Dictionary
