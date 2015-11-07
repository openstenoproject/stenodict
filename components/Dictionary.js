import React, { Component, PropTypes } from 'react'
import { Glyphicon, Button, Row, Col } from 'react-bootstrap'
import Markdown from './Markdown'
import DownloadDictionary from './DownloadDictionary'

class Dictionary extends Component {
  render() {
    const { dictionary, details, formats, tags } = this.props
    let dictDetails = (<h4>Loading details...</h4>)
    let downloadButton = null
    let versionTag = null
    if (details && details.version) {
      versionTag = (<small style={{ color: "#aaa" }}>
        {`v${details.version}`}
        </small>)
    }
    if (details && !details.isLoading) {
      if (!details.why && !details.how) {
        dictDetails = (
          <h4>
            Sorry, can't find details on this dictionary!
          </h4>
        )
      } else {
        downloadButton = (<DownloadDictionary name={dictionary.name}
            filename={dictionary.filename}
            version={details.version}
            formats={formats}
            dictFormats={dictionary.formats} />)
        dictDetails = (
          <div>
          <h3>Why</h3>
          <Markdown>{details.why}</Markdown>
          <h3>How</h3>
          <Markdown paragraphs={details.how}/>
          <h3>Where</h3>
          <p>Get the dictionary file for {dictionary.name}:</p>
          { downloadButton }
          </div>
        )
      }
    }
    return (
      <div>
        <Row>
          <Col md={3} sm={2} xs={12}>
            <Button href="#">
            <small>
              <Glyphicon glyph="chevron-left" />
            </small>
            {` Back to List`}
            </Button>
          </Col>
          <Col md={9} sm={10} xs={12} className="text-right">
            { downloadButton }
          </Col>
        </Row>

        <hr className="dictionary-page"/>

        <h1 className="dictionary-title">
          { dictionary.name + ' ' }
          { versionTag }
        </h1>
        <p className="author">By { dictionary.author }</p>
        <h4>{ dictionary.what}</h4>
        { dictDetails }
      </div>
    )
  }
}

Dictionary.propTypes = { dictionary: PropTypes.object
                       , details: PropTypes.object
                       , formats: PropTypes.object
                       , tags: PropTypes.object
                       }

export default Dictionary
