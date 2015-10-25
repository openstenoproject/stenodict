import React, { Component, PropTypes } from 'react'
import Markdown from './Markdown'

class Dictionary extends Component {
  render() {
    const { dictionary } = this.props
    console.log(dictionary)
    return (
      <li>
        <b>{ `${dictionary.name}: ` }</b>
        { `${dictionary.description.what} -- ` }
        <a href={`http://tedmor.in/stenodict/dictionaries/${dictionary.filename}`} download>
          Download
        </a>
      </li>
    )
  }
}

Dictionary.propTypes = { dictionary: React.PropTypes.object.isRequired
                       }

export default Dictionary
