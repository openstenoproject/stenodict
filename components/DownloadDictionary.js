import React, { Component, PropTypes } from 'react'
import { Button, Label, Glyphicon } from 'react-bootstrap'
import Markdown from './Markdown'

class DownloadDictionary extends Component {
  render() {
    const { dictFormats
          , formats
          , filename
          , name
          , version
          } = this.props
    const links = dictFormats.map(x => (
      <Button href={`dictionaries/${filename}.${formats[x]}`}
              bsStyle="primary" key={x} download={`${filename}_v${version}.${formats[x]}`}>
        <Glyphicon glyph="download" style={{ marginRight: 10 }}/>
        Download { name }
        <Label bsStyle="info" style={{ marginLeft: 10 }}>
        {formats[x].toUpperCase()}
        </Label>
    </Button>
    ))
    return (
      <div>
        { links }
      </div>
    )
  }
}

DownloadDictionary.propTypes = { formats: PropTypes.object.isRequired
                               , dictFormats: PropTypes.array.isRequired
                               , name: PropTypes.string.isRequired
                               , filename: PropTypes.string.isRequired
                               , version: PropTypes.number.isRequired
                               }

export default DownloadDictionary
