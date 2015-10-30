import React, { Component, PropTypes } from 'react';
import { Row } from 'react-bootstrap'
import { connect } from 'react-redux';
import { pushState } from 'redux-router';

class App extends Component {
  render() {
    const { children, dictionaries } = this.props;
    return (
      <div>
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
