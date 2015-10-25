import React, { Component, PropTypes } from 'react'
import marked from 'marked'

class Markdown extends Component {

  parseMarkdown(md: string) {
    // marked is sanitized by default.
    return { __html: marked(md) }
  }

  render() {
    let { paragraphs = null, children } = this.props
    if (paragraphs) {
      paragraphs = paragraphs.join('\n\n')
    }
    if (children) {
      paragraphs = paragraphs ? children + '\n\n' + paragraphs : children
    }
    if (!paragraphs && !children) {
      return null
    }
    return (
      <span dangerouslySetInnerHTML={this.parseMarkdown(paragraphs)}>
      </span>
    )
  }
}

Markdown.propTypes = { paragraphs: React.PropTypes.array
                     }

export default Markdown
