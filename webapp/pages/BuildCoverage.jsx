import React from 'react';
import PropTypes from 'prop-types';

import AsyncPage from '../components/AsyncPage';
import BuildCoverageComponent from '../components/BuildCoverage';

export default class BuildCoverageTree extends AsyncPage {
  static contextTypes = {
    ...AsyncPage.contextTypes,
    build: PropTypes.object.isRequired,
    repo: PropTypes.object.isRequired
  };

  getEndpoints() {
    let {repo} = this.context;
    let {buildNumber} = this.props.params;
    return [
      [
        'result',
        `/repos/${repo.full_name}/builds/${buildNumber}/file-coverage-tree`,
        {query: this.props.location.query}
      ]
    ];
  }

  renderBody() {
    return <BuildCoverageComponent result={this.state.result} {...this.props} />;
  }
}
