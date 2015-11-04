import React, { Component, PropTypes } from 'react';
import { Row, Col, Panel } from 'react-bootstrap'
import { connect } from 'react-redux';
import Dictionaries from '../components/Dictionaries'
import FilterWidget from '../components/FilterWidget'
import { toggleFilter, clearFilters } from '../actions'

class DictionariesPage extends Component {
  render() {
    const { children
          , dictionaries
          , tags
          , toggleFilter
          , filtered
          , clearFilters
          } = this.props;
    return (
      <Row>
        <Col md={3}>
          <h4>Filter</h4>
          <FilterWidget dictionaries={dictionaries}
                        tags={tags}
                        toggleFilter={toggleFilter}
                        clearFilters={clearFilters}/>
        </Col>
        <Col md={9}>
          <h4>Dictionaries</h4>
          <Dictionaries dictionaries={dictionaries}
                        filtered={filtered}/>
        </Col>
      </Row>
    )
  }
}

function mapStateToProps(state) {
  return { dictionaries: state.dictionaries
         , tags: state.tags
         , filtered: state.filtered
         }
}

function mapDispatchToProps(dispatch) {
  return { toggleFilter: x => dispatch(toggleFilter(x))
         , clearFilters: () => dispatch(clearFilters())
         }
}

export default connect(mapStateToProps, mapDispatchToProps)(DictionariesPage);
