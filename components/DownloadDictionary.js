import React, { Component, PropTypes } from 'react'
import Markdown from './Markdown'

class DownloadDictionary extends Component {
  render() {
    const { dictFormats, formats, filename, name } = this.props
    const links = dictFormats.map(x => (
      <li key={x}>
      <a href={`dictionaries/${filename}.${formats[x]}`}>
        Download {name} [{formats[x].toUpperCase()}]
      </a>
      </li>
    ))
    return (
      <ul>
        { links }
      </ul>
    )
  }
}

DownloadDictionary.propTypes = { formats: PropTypes.object
                               , dictFormats: PropTypes.array
                               , name: PropTypes.string
                               , filename: PropTypes.string
                               }

export default DownloadDictionary
