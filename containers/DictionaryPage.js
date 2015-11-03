import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { Button, Glyphicon } from 'react-bootstrap'
import Dictionary from '../components/Dictionary'
import { fetchDetails } from '../actions'
import { goBack } from 'redux-router'

class DictionaryPage extends Component {
  constructor() {
    super()
    this.fname = null
  }
  componentWillMount() {
    const { location } = this.context
    this.fname = location.pathname.substring(
      location.pathname.lastIndexOf('/') + 1
    )
    this.getDetailsBasedOnProps(this.props)
  }
  componentWillReceiveProps(p) {
    this.getDetailsBasedOnProps(p)
  }
  getDetailsBasedOnProps(props) {
    const dictionary = props.dictionaries.list[this.fname]
    const details = props.details[this.fname]
    if (dictionary && !details) {
      this.props.fetchDetails(this.fname)
    }
  }
  render() {
    const { children, dictionaries, details, formats, tags } = this.props

    if (!dictionaries.list[this.fname]) {
      return (<p>Dictionary not found</p>)
    }
    return (
      <div>
        <Button href="#">
          <small>
            <Glyphicon glyph="chevron-left" />
          </small>
          {` Back to List`}
        </Button>
        <hr className="dictionary-page"/>
        <Dictionary dictionary={dictionaries.list[this.fname]}
                    details={details[this.fname]}
                    formats={formats}
                    tags={tags} />
      </div>
    )
  }
}

DictionaryPage.contextTypes = { location: PropTypes.object.isRequired }

function mapStateToProps(state) {
  return { dictionaries: state.dictionaries
         , details: state.details
         , formats: state.formats
         , tags: state.tags
         }
}

function mapDispatchToProps(dispatch) {
  return { fetchDetails: x => dispatch(fetchDetails(x)) }
}

export default connect(mapStateToProps, mapDispatchToProps)(DictionaryPage)
