var path = require('path');
var webpack = require('webpack');

module.exports = {
  entry: [
    './index'
  ],
  output: {
    path: path.join(__dirname, '../gh-pages/javascripts'),
    filename: 'stenodict.js',
    publicPath: '/javascripts/'
  },
  plugins: [
    new webpack.optimize.DedupePlugin(),
    new webpack.optimize.OccurenceOrderPlugin(),
    new webpack.optimize.UglifyJsPlugin(),
    new webpack.DefinePlugin({
      'process.env': {
        'NODE_ENV': '"production"'
      }
    })
  ],
  module: {
    loaders: [{
      test: /\.js$/,
      loaders: ['babel'],
      exclude: /node_modules/,
      include: __dirname
    }]
  }
};
