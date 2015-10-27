import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import Dictionaries from '../components/Dictionaries'

class DictionariesPage extends Component {
  render() {
    const { children, dictionaries } = this.props;
    return (
        <Dictionaries dictionaries={dictionaries} />
    );
  }
}

function mapStateToProps(state) {
  return { dictionaries: state.dictionaries };
}

export default connect(mapStateToProps, {})(DictionariesPage);
