import React, { Component, PropTypes } from 'react'
import { Button } from 'react-bootstrap'

class FilterWidget extends Component {
  toggleBy(x) {
    return () => {
      this.props.toggleFilter(x)
    }
  }
  render() {
    const { tags, dictionaries, toggleFilter, clearFilters } = this.props
    return (
        <div className="filters">
        <h5>Tags</h5>
        <Button bsStyle="link" onClick={clearFilters}>Clear</Button>
        { Object.keys(tags).map(x => (
            <Button bsStyle={ tags[x].selected ? 'primary' : 'default' }
              onClick={this.toggleBy({ tag: x })} key={x}>{tags[x].label}</Button>
        )) }
        </div>
        )
      }
    }

FilterWidget.PropTypes = { tags: PropTypes.object
                         , formats: PropTypes.object
                         , toggleFilter: PropTypes.func.isRequired
                         , clearFilters: PropTypes.func.isRequired
                         }

export default FilterWidget
