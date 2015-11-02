import React, { Component, PropTypes } from 'react'
import { Button, Label } from 'react-bootstrap'
import Markdown from './Markdown'

class DownloadDictionary extends Component {
  render() {
    const { dictFormats, formats, filename, name } = this.props
    const links = dictFormats.map(x => (
      <Button href={`dictionaries/${filename}.${formats[x]}`} bsStyle="primary" key={x}>
        Download {`${name}  `}<Label bsStyle="info">{formats[x].toUpperCase()}</Label>
    </Button>
    ))
    return (
      <div>
        { links }
      </div>
    )
  }
}

DownloadDictionary.propTypes = { formats: PropTypes.object
                               , dictFormats: PropTypes.array
                               , name: PropTypes.string
                               , filename: PropTypes.string
                               }

export default DownloadDictionary
