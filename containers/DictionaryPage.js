import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import Dictionary from '../components/Dictionary'

class DictionaryPage extends Component {
  render() {
    const { children, dictionaries } = this.props
    const { location } = this.context
    let fname = location.pathname.substring(
      location.pathname.lastIndexOf('/') + 1
    )
    if (!dictionaries.list[fname]) {
      return (<p>Dictionary not found</p>)
    }
    return (
        <Dictionary dictionary={dictionaries.list[fname]}/>
    );
  }
}

DictionaryPage.contextTypes = { location: PropTypes.object.isRequired }

function mapStateToProps(state) {
  return { dictionaries: state.dictionaries };
}

export default connect(mapStateToProps, {})(DictionaryPage);
