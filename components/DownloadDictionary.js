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
    const downloadGlyph =
      <Glyphicon glyph="download" style={{ marginRight: 10 }}/>
    const links = dictFormats.map((x, i) => (
      <Button href={`dictionaries/${filename}.${formats[x]}`}
              style={{marginLeft: i ? 5 : 0}}
              bsStyle="primary" key={x} download={`${filename}_v${version}.${formats[x]}`}>
        { !i ? <span>{downloadGlyph}Download {name}</span> : '' }
        <Label bsStyle="info" style={{ marginLeft: !i ? 10 : 0 }}>
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
