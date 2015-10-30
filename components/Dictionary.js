import React, { Component, PropTypes } from 'react'
import Markdown from './Markdown'
import DownloadDictionary from './DownloadDictionary'

class Dictionary extends Component {
  render() {
    const { dictionary, details, formats, tags } = this.props
    let dictDetails = (<h4>Loading details...</h4>)
    if (details && !details.isLoading) {
      if (!details.why && !details.how) {
        dictDetails = (
          <h4>
            Sorry, can't find details on this dictionary!
          </h4>
        )
      } else {
        dictDetails = (
          <div>
          <h3>Why</h3>
          <Markdown>{details.why}</Markdown>
          <h3>How</h3>
          <Markdown paragraphs={details.how}/>
          <h3>Where</h3>
          <p>Get the dictionary file for {dictionary.name}:</p>
          <DownloadDictionary name={dictionary.name}
                              filename={dictionary.filename}
                              formats={formats}
                              dictFormats={dictionary.formats} />
          </div>
        )
      }
    }
    return (
      <div>
        <h1>{ dictionary.name }</h1>
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
