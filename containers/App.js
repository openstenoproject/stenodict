import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { pushState } from 'redux-router';
import Dictionaries from '../components/Dictionaries'

class App extends Component {
  render() {
    const { children, dictionaries } = this.props;
    return (
      <div>
        <Dictionaries dictionaries={dictionaries} />
        {children}
      </div>
    );
  }
}

App.propTypes = {
  // Injected by React Redux
  pushState: PropTypes.func.isRequired,
  // Injected by React Router
  children: PropTypes.node
};

function mapStateToProps(state) {
  return { dictionaries: state.dictionaries };
}

export default connect(mapStateToProps, {
  pushState
})(App);
