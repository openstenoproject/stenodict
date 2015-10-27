import React, { Component, PropTypes } from 'react'
import Markdown from './Markdown'

class Dictionary extends Component {
  render() {
    const { dictionary } = this.props
    console.log(dictionary)
    return (
      <div>
        <h1>{ dictionary.name }</h1>
        <h3>{ dictionary.description.what}</h3>
        <h2>Why</h2>
        <Markdown>{dictionary.description.why}</Markdown>
        <h2>How</h2>
        <Markdown paragraphs={dictionary.description.how}/>
        <h3><a href={`dictionaries/${dictionary.filename}`}>
          Download
        </a></h3>
      </div>
    )
  }
}

Dictionary.propTypes = { dictionary: PropTypes.object }

export default Dictionary
