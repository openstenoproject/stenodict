import React, { Component, PropTypes } from 'react'
import Markdown from './Markdown'
import DownloadDictionary from './DownloadDictionary'

class Dictionary extends Component {
  render() {
    const { dictionary, details, formats, tags } = this.props
    let dictDetails = (<h3>Loading details...</h3>)
    if (details && !details.isLoading) {
      if (!details.why && !details.how) {
        dictDetails = (
          <h3>
            Sorry, can't find details on this dictionary!
          </h3>
        )
      } else {
        dictDetails = (
          <div>
          <h2>Why</h2>
          <Markdown>{details.why}</Markdown>
          <h2>How</h2>
          <Markdown paragraphs={details.how}/>
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
        <h3>{ dictionary.what}</h3>
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
