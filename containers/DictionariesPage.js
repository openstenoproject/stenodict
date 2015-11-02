import React, { Component, PropTypes } from 'react';
import { Row, Col, Panel } from 'react-bootstrap'
import { connect } from 'react-redux';
import Dictionaries from '../components/Dictionaries'

class DictionariesPage extends Component {
  render() {
    const { children, dictionaries } = this.props;
    return (
      <Row>
        <Col md={3}>
          <h4>Filter</h4>
          <p>
            There will be filters here, soon!
          </p>
        </Col>
        <Col md={9}>
          <h4>Dictionaries</h4>
          <Dictionaries dictionaries={dictionaries} />
        </Col>
      </Row>
    );
  }
}

function mapStateToProps(state) {
  return { dictionaries: state.dictionaries };
}

export default connect(mapStateToProps, {})(DictionariesPage);
