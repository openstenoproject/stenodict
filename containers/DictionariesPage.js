import React, { Component, PropTypes } from 'react';
import { Row, Col, Panel } from 'react-bootstrap'
import { connect } from 'react-redux';
import Dictionaries from '../components/Dictionaries'

class DictionariesPage extends Component {
  render() {
    const { children, dictionaries } = this.props;
    return (
      <Row>
        <Col mdPush={10} md={2}>
          <Panel>
            [Pretend that I'm a set of filters. Pew, pew!]
          </Panel>
        </Col>
        <Col mdPull={2} md={10}>
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
